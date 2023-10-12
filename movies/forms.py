from django import forms
from .models import Chat, Forum, Aula,Estudiante,Asistencia
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
        




