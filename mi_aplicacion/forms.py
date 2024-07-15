# mi_aplicacion/forms.py
from django import forms
from .models import MensajeContacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import ValidadorSoloLetras, ValidadorSoloLetrasNumeros

class FormularioRegistro(UserCreationForm):
    pnombre = forms.CharField(
        label='Nombre',
        max_length=255,
        help_text='Ingrese su primer nombre',
        validators=[ValidadorSoloLetras().validador],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu nombre...'
        })
    )
    appaterno = forms.CharField(
        label='Apellido',
        max_length=255,
        help_text='Ingrese su apellido paterno',
        validators=[ValidadorSoloLetras().validador],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu apellido...'
        })
    )
    email = forms.EmailField(
        label='Correo',
        max_length=254,
        help_text='Ingresa un correo válido',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico'
        })
    )

    username = forms.CharField(
        label='Nombre de Usuario',
        max_length=150,
        validators=[ValidadorSoloLetrasNumeros().validador],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu Nombre De Usuario...'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'pnombre', 'appaterno')
        widgets = {
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu contraseña...'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar Contraseña...'
            }),
        }

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'apellido', 'telefono', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }