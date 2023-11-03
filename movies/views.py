from django.http import FileResponse,Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie, Forum, Chat, Estudiante, Aula, Asistencia, Calificacion, Proyecto, Equipo, Archivo
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from .forms import ForumForm,AulaForm,EstudianteForm,ArchivoForm,ChatForm,EquipoForm,ProyectoForm
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta, datetime
from django.conf import settings
import os


def movie_list(request):
    movies = Movie.objects.all()  
    return render(request, 'index.html', {'movies': movies})

# Obtener el número de usuarios registrados y el utlimo usuario registrado

def get_last_registered_user():
    try:
        last_user = User.objects.latest('date_joined')
        return last_user
    except User.DoesNotExist:
        return None

def contar_proyectos(request):
    numero_proyectos = Proyecto.objects.count()
    
    return numero_proyectos

def get_users_registered_last_day():
    today = datetime.now()
    one_day_ago = today - timedelta(days=1)
    
    users_last_day = User.objects.filter(date_joined__gte=one_day_ago, date_joined__lte=today)
    return users_last_day

def get_users_registered_last_year():
    now = timezone.now()
    one_year_ago = now - timedelta(days=365)
    users_last_year = User.objects.filter(date_joined__gte=one_year_ago, date_joined__lt=now)
    return users_last_year

def dashboard_admin(request):
    num_users = User.objects.count()
    last_user = get_last_registered_user()
    users_last_day = get_users_registered_last_day()
    users_last_year = get_users_registered_last_year()
    numero_proyectos = contar_proyectos(request)


    return render(request, 'dashboard_admin.html', {'num_users': num_users,
                                                    'numero_proyectos': numero_proyectos,
                                                    'last_user': last_user,
                                                    'users_last_day': users_last_day,
                                                        'users_last_year': users_last_year,})


#vista para ir al chat por foros y login
def dashboard(request):
    movies = Movie.objects.all()  
    return render(request, 'dashboard.html', {'dashboard': movies})

def login(request):
    movies= Movie.objects.all()  
    return render(request, 'login.html', {'login': movies})

#vista de la base de los templates
def base(request):
    movies= Movie.objects.all()  
    return render(request, 'base.html', {'base': movies})
    

#logica de login

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')


#logica de logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de inicio de sesión
#definicion de vistas del foro

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum_list.html', {'forums': forums})

def chat_detail(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    chats = Chat.objects.filter(forum=forum)
    
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            new_chat = form.save(commit=False)
            new_chat.forum = forum
            new_chat.sender = request.user  # Establece el remitente como el usuario actual
            new_chat.save()
            return redirect('chat_detail', forum_id=forum.id)
    else:
        form = ChatForm()

    return render(request, 'chat_detail.html', {'forum': forum, 'chats': chats, 'form': form})

#definicion de vistas de asistencia y calificacion

def lista_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'aulas.html', {'aulas': aulas})

def lista_estudiantes(request, aula_id):
    aula = Aula.objects.get(pk=aula_id)
    estudiantes = Estudiante.objects.filter(aula=aula)
    return render(request, 'estudiantes.html', {'aula': aula, 'estudiantes': estudiantes})

def tomar_asistencia(request, estudiante_id):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    if request.method == 'POST':
        fecha = request.POST['fecha']
        presente = request.POST.get('presente', False)
        Asistencia.objects.create(estudiante=estudiante, fecha=fecha, presente=presente)
        return redirect('lista_estudiantes', aula_id=estudiante.aula.id)
    return render(request, 'tomar_asistencia.html', {'estudiante': estudiante})



def asistencia_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    asistencias = Asistencia.objects.filter(estudiante=estudiante)

    return render(request, 'asistencia_estudiante.html', {
        'estudiante': estudiante,
        'asistencias': asistencias
    })

def registrar_calificacion(request, estudiante_id):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    if request.method == 'POST':
        materia = request.POST['materia']
        nota = request.POST['nota']
        Calificacion.objects.create(estudiante=estudiante, materia=materia, nota=nota)
        return redirect('lista_estudiantes', aula_id=estudiante.aula.id)
    return render(request, 'registrar_calificacion.html', {'estudiante': estudiante})

#definicion de vista para ver las notas
def notas_estudiante_por_aula(request, aula_id, estudiante_id):
    aula = get_object_or_404(Aula, pk=aula_id)
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id, aula=aula)
    calificaciones = Calificacion.objects.filter(estudiante=estudiante)
    
    return render(request, 'notas_estudiante_por_aula.html', {'aula': aula, 'estudiante': estudiante, 'calificaciones': calificaciones})


#definicion de funciones de CRUD para el foro
def forum_create(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_list')
    else:
        form = ForumForm()
    return render(request, 'forum_create.html', {'form': form})

def forum_update(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    
    if request.method == 'POST':
        form = ForumForm(request.POST, instance=forum)
        if form.is_valid():
            form.save()
            return redirect('forum_list')
    else:
        form = ForumForm(instance=forum)
    
    return render(request, 'forum_form.html', {'form': form})

def forum_delete(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    if request.method == 'POST':
        forum.delete()
        return redirect('forum_list')
    
    return render(request, 'forum_confirm_delete.html', {'forum': forum})

#definicion de funciones de CRUD para el Aulas
def aula_create(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/aulas')
    else:
        form = AulaForm()
    return render(request, 'aula_create.html', {'form': form})

def aula_update(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    
    if request.method == 'POST':
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect('/aulas')
    else:
        form = AulaForm(instance=aula)
    
    return render(request, 'aula_form.html', {'form': form})

def aula_delete(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    if request.method == 'POST':
        aula.delete()
        return redirect('/aulas')
    
    return render(request, 'aula_confirm_delete.html', {'aula': aula})

#definicion de funciones de CRUD para el Estudiantes
def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save()
            return redirect('/aulas/'+str(estudiante.aula.id)+'/estudiantes/')
    else:
        form = EstudianteForm()
    return render(request, 'estudiante_create.html', {'form': form})

def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('/aulas/'+str(estudiante.aula.id)+'/estudiantes/')
    else:
        form = EstudianteForm(instance=estudiante)
    
    return render(request, 'estudiante_form.html', {'form': form})

def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('/aulas/'+str(estudiante.aula.id)+'/estudiantes/')
    
    return render(request, 'estudiante_confirm_delete.html', {'estudiante': estudiante})

#Sistema de proyectos de clase


def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'lista_equipos.html', {'equipos': equipos})


def lista_proyectos(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    proyectos = Proyecto.objects.filter(equipo=equipo)
    return render(request, 'lista_proyectos.html', {'equipo': equipo, 'proyectos': proyectos})

def proyecto_create(request, equipo_id):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.equipo_id = equipo_id  # Asigna el equipo_id al proyecto
            proyecto.save()
            return redirect('lista_proyectos', equipo_id=equipo_id)
    else:
        form = ProyectoForm()

    return render(request, 'proyecto_create.html', {'form': form, 'equipo_id': equipo_id})

def proyecto_update(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos', equipo_id=proyecto.equipo_id)
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'proyecto_form.html', {'form': form, 'proyecto': proyecto})


def proyecto_delete(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    equipo_id = proyecto.equipo_id  # Guarda el equipo_id antes de eliminar el proyecto

    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos', equipo_id=equipo_id)

    return render(request, 'proyecto_delete.html', {'proyecto': proyecto})

def equipo_create(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('lista_equipos')

    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()

    return render(request, 'equipo_create.html', {'form': form})

def actualizar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)

    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('lista_equipos')

    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm(instance=equipo)

    return render(request, 'equipo_form.html', {'form': form, 'equipo': equipo})

def eliminar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)

    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('lista_equipos')

    if request.method == 'POST':
        equipo.delete()
        return redirect('lista_equipos')

    return render(request, 'equipo_confirm_delete.html', {'equipo': equipo})




def lista_archivos(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    archivos = Archivo.objects.filter(proyecto=proyecto)
    equipo = proyecto.equipo  # Asegúrate de que proyecto tenga una relación con un equipo
    return render(request, 'lista_archivos.html', {'proyecto': proyecto, 'archivos': archivos, 'equipo': equipo})


def cargar_archivo(request, proyecto_id):
    # Obtén el objeto Proyecto asociado al proyecto_id
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    
    if request.method == "POST":
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            # Asigna el proyecto al archivo antes de guardarlo
            archivo = form.save(commit=False)
            archivo.proyecto = proyecto
            archivo.uploader = request.user
            archivo.save()
            return redirect('lista_archivos', proyecto_id=proyecto_id)
    else:
        form = ArchivoForm()

    return render(request, 'cargar_archivo.html', {'form': form, 'proyecto': proyecto})

def descargar_archivo(request, archivo_id):
    archivo = get_object_or_404(Archivo, id=archivo_id)
    file_path = archivo.archivo.path
    file_name = archivo.nombre

    # Agregar un mensaje de alerta
    messages.warning(request, f"¿Estás seguro de que deseas descargar '{file_name}'?")

    # Preparar la respuesta para la descarga
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response


def descargar_confirmado(request, archivo_id):
    archivo = get_object_or_404(Archivo, pk=archivo_id)

    if request.method == "POST":
        file_path = os.path.join(settings.MEDIA_ROOT, str(archivo.archivo))
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response

    return render(request, 'confirmar_descarga.html', {'archivo': archivo})


def archivo_update(request, pk):
    archivo = get_object_or_404(Archivo, pk=pk)
    proyecto_id = archivo.proyecto_id

    if request.method == 'POST':
        # Obtener el archivo anterior antes de la actualización
        archivo_anterior = archivo.archivo

        # Actualizar el archivo con el nuevo archivo cargado por el usuario
        form = ArchivoForm(request.POST, request.FILES, instance=archivo)
        if form.is_valid():
            archivo = form.save()

            # Eliminar el archivo anterior de la carpeta de medios
            if archivo_anterior and archivo.archivo != archivo_anterior:
                file_path = os.path.join(settings.MEDIA_ROOT, str(archivo_anterior))
                if os.path.exists(file_path):
                    os.remove(file_path)

            return redirect('lista_archivos', proyecto_id=proyecto_id)

    else:
        form = ArchivoForm(instance=archivo)

    return render(request, 'archivo_form.html', {'form': form, 'archivo': archivo})

def archivo_delete(request, pk):
    archivo = get_object_or_404(Archivo, pk=pk)
    proyecto_id = archivo.proyecto_id

    if request.method == 'POST':
        # Eliminar el archivo de la base de datos
        archivo.delete()

        # Eliminar el archivo físico de la carpeta de archivos
        file_path = os.path.join(settings.MEDIA_ROOT, str(archivo.archivo))
        if os.path.exists(file_path):
            os.remove(file_path)

        return redirect('lista_archivos', proyecto_id=proyecto_id)

    return render(request, 'archivo_delete.html', {'archivo': archivo})