from django import forms
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory, modelform_factory, modelformset_factory
from django.forms import *
from .models import *


class FormUc(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets ={
            'nombre': TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
        }

class FormDocente(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets ={
            'nombre': TextInput(attrs={'class': 'form-control text-capitalize', 'autocomplete':'off'}),
            'apellido': TextInput(attrs={'class': 'form-control text-capitalize', 'autocomplete':'off'}),
            'ci': Select(attrs={'class': 'form-select text-center'}),          
            'num_ci': TextInput(attrs={'class': 'form-control', 'autocomplete':'off', 'placeholder':'00000000'}),
        }

class FormHorario(ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
        widgets ={
            'uc': Select(attrs={'class': 'form-select'}),
            'seccion': NumberInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'docente': Select(attrs={'class': 'form-select'}),
            'dia': Select(attrs={'class': 'form-select'}),          
            'entrada': TextInput(attrs={'class': 'form-control', 'autocomplete':'off', 'placeholder':'0:00 - 23:59'}),
            'salida':TextInput(attrs={'class': 'form-control', 'autocomplete':'off', 'placeholder':'0:00 - 23:59'}),
        }

class FormUc(ModelForm):    
    class Meta:
        model = Uc
        fields = '__all__'
        widgets ={'nombre': TextInput(attrs={'class': 'form-control', 'autocomplete':'off'})}

class FormAsistencia(ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        localized_fields=('fecha',)
        widgets ={
            'fecha': DateInput(attrs={'class':'form-control text-center', 'autocomplete':'off', 'placeholder':'DD/MM/AAAA'}),
            'docente': Select(attrs={'class': 'form-select'}),
            'asistencia': CheckboxInput(attrs={'class': 'form-check-input justify-content-center'}),
        }