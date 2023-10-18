from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie, Forum, Chat, Estudiante, Aula, Asistencia, Calificacion
from .forms import ChatForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from .forms import ForumForm,AulaForm,EstudianteForm,AsistenciaForm


def movie_list(request):
    movies = Movie.objects.all()  
    return render(request, 'index.html', {'movies': movies})

def dashboard(request):
    movies = Movie.objects.all()  
    return render(request, 'dashboard.html', {'dashboard': movies})

def login(request):
    movies= Movie.objects.all()  
    return render(request, 'login.html', {'login': movies})

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

