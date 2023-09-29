from django.db import models
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title +' - '+ self.director

class Usuario(models.Model):
        username = models.CharField(max_length=150) 
        password = models.CharField(max_length=128)
        email = models.EmailField(max_length=254)
        primer_nombre = models.CharField(max_length=30)
        segundo_nombre = models.CharField(max_length=150)

        def __str__(self):
            return self.username+' '+ self.email
        

class Forum(models.Model):
    title = models.CharField(max_length=200)


class Chat(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Meta:
        permissions = [
            ("can_add_movie", "Can add movie"),
            ("can_add_usuario", "Can add usuario"),
            ("can_add_forum", "Can add forum"),
            ("can_add_chat", "Can add chat"),
        ]



