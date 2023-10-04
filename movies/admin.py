from django.contrib import admin
from movies.models import Forum,Chat,Estudiante,Aula,Asistencia,Calificacion

admin.site.register(Estudiante)
admin.site.register(Aula)
admin.site.register(Asistencia)
admin.site.register(Calificacion)
admin.site.register(Forum)
admin.site.register(Chat)


