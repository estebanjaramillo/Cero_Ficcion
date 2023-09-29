from django.shortcuts import render, redirect
from .models import Movie, Forum, Chat
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import ChatForm
from django.contrib.auth.decorators import login_required  # Importa el decorador de autenticación





def movie_list(request):
    movies = Movie.objects.all()  
    return render(request, 'index.html', {'movies': movies})

def login(request):
    movies= Movie.objects.all()  
    return render(request, 'login.html', {'login': movies})

def base(request):
    movies= Movie.objects.all()  
    return render(request, 'base.html', {'base': movies})
    
#logica de login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error_message': 'Credenciales inválidas'})
        else:
            return JsonResponse({'success': False, 'error_message': 'Formulario inválido'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

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