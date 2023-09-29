from django import forms
from .models import Chat

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)



class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['text']
