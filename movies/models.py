from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title +' - '+ self.director

class user(models.Model):
        username = models.CharField(max_length=150) 
        password = models.CharField(max_length=128)
        email = models.EmailField(max_length=254)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=150)

        def __str__(self):
            return self.username +' - '+ self.email
        
    

class Meta:
        permissions = [
            ("can_add_movie", "Can add movie"),
            ("can_add_usuario", "Can add usuario"),
        ]
