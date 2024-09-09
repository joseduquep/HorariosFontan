# estudiantes/forms.py
from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
 
 
        fields = ['nombre', 'apellido', 'cedula',  'nivel_autonomia', 'vacaciones_prolongadas', 'grado', 'taller', 'foto', 'email']

def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre estudiante'
        self.fields['nombre'].label = ''
        self.fields['nombre'].help_text = mark_safe('<span style="color:blue;" class="form-text text-muted"><small>Debe ser 20 caracteres o menos. Solo letras, números y @/./+/-/_</small></span>')

        self.fields['apellido'].widget.attrs['class'] = 'form-control'
        self.fields['apellido'].widget.attrs['placeholder'] = 'Apellido estudiante'
        self.fields['apellido'].label = ''
        self.fields['apellido'].help_text = mark_safe('')    

        self.fields['cedula'].widget.attrs['class'] = 'form-control'
        self.fields['cedula'].widget.attrs['placeholder'] = 'Cédula estudiante'
        self.fields['cedula'].label = ''
        self.fields['cedula'].help_text = mark_safe('')   

        self.fields['nivel_autonomia'].widget.attrs['class'] = 'form-control'
        self.fields['nivel_autonomia'].widget.attrs['placeholder'] = 'Nivel autonomia'
        self.fields['nivel_autonomia'].label = ''
        self.fields['nivel_autonomia'].help_text = mark_safe('')   

        self.fields['taller'].widget.attrs['class'] = 'form-control'
        self.fields['taller'].widget.attrs['placeholder'] = 'Taller Base'
        self.fields['taller'].label = ''
        self.fields['taller'].help_text = mark_safe('')   

        self.fields['grado'].widget.attrs['class'] = 'form-control'
        self.fields['grado'].widget.attrs['placeholder'] = 'Grado estudiante'
        self.fields['grado'].label = ''
        self.fields['grado'].help_text = mark_safe('')   

        self.fields['foto'].widget.attrs['class'] = 'form-control'
        self.fields['foto'].widget.attrs['placeholder'] = 'Grado estudiante'
        self.fields['foto'].label = ''
        self.fields['foto'].help_text = mark_safe('') 
        