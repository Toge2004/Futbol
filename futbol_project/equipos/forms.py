# equipos/forms.py
from django import forms
from .models import EquipoFutbol
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EquipoFutbolForm(forms.ModelForm):
    class Meta:
        model = EquipoFutbol
        fields = [
            'nombre', 'ciudad', 'pais', 'fundacion', 'estadio', 
            'entrenador', 'presidente', 'colores', 'titulos_liga',
            'titulos_copa', 'titulos_internacionales', 'presupuesto_anual',
            'sitio_web', 'activo'
        ]
        widgets = {
            'fundacion': forms.NumberInput(attrs={'min': 1800, 'max': 2023}),
            'presupuesto_anual': forms.NumberInput(attrs={'step': '0.01'}),
            'colores': forms.TextInput(attrs={'placeholder': 'Ej: Rojo, Blanco, Azul'}),
        }
    
    def clean_fundacion(self):
        fundacion = self.cleaned_data.get('fundacion')
        if fundacion < 1800 or fundacion > 2023:
            raise forms.ValidationError("El año de fundación debe ser entre 1800 y 2023")
        return fundacion