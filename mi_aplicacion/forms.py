from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Ingrese un correo válido',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de Usuario'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar Contraseña'
            }),
        }
        labels = {
            'username': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
