from django.forms import ModelForm
from app.models import Paciente
from django import forms
   
class MyCommentForm(forms.ModelForm):
    class Meta(object):
        model = Paciente
        fields = ['prontuario', 'name', 'dn', 'cpf', 'message']
        widgets = {
            'prontuario': forms.TextInput(
            attrs={
            'class': 'form-control',
            'type': 'int'
            }
            ),
            'name': forms.TextInput(
            attrs={
            'class': 'form-control'
            }
            ),
            'dn': forms.DateTimeInput(
            attrs={
            'class': 'form-control',
            'type': 'date'
            }
            ),
            'cpf': forms.TextInput(
            attrs={
            'class': 'form-control',
            'type': 'int'
            }
            ),
            'message': forms.Textarea(
            attrs={
            'class': 'form-control'
            }
            ),
   }