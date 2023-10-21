from django import forms
from .models import Chat, Forum, Aula,Estudiante,Asistencia,Archivo,Proyecto,Equipo
from django import forms

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'

        
class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['text']

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['nombre', 'archivo']
        
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'equipo']


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre']

