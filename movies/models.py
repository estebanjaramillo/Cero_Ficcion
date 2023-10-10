from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title + ' - ' + self.director
    class Meta:
        permissions = [
            ("can_add_movie", "Can add movie"),
        ]

class Forum(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_add_forum", "Can add forum"),
        ]

class Chat(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_add_chat", "Can add chat"),
        ]

class Aula(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("can_add_aula", "Can add aula"),
        ]

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("can_add_estudiante", "Can add estudiante"),
        ]

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_add_asistencia", "Can add asistencia"),
        ]

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.materia}"
    class Meta:
        permissions = [
            ("can_add_calificacion", "Can add calificacion"),
        ]
