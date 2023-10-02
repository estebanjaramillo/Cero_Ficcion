from django.shortcuts import render, redirect
from .models import Movie, Forum, Chat
from .forms import ChatForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout

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
