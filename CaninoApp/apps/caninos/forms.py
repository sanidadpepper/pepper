# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class CaninoForm(forms.ModelForm):

	class Meta:
		model = Canino
		fields = '__all__'
		exclude = ('propietario_canino',)
		widgets = {
			'nombre_canino': forms.TextInput(attrs = {'class': 'form-control','required': True}),
			'fecha_nacimiento': forms.TextInput(attrs = {'class': 'form-control date','required': True}),
			'color_canino': forms.TextInput(attrs = {'class': 'form-control','required': True}),
			'descripcion_canino': forms.Textarea(),
			'ocupaciones': forms.CheckboxSelectMultiple()
		}
		labels = {
			'nombre_canino': 'Nombre del canino',
			'raza_canino': 'Raza',
			'fecha_nacimiento': 'Fecha de nacimiento',
			'sexo_canino': 'Sexo',
			'color_canino': 'Color',
			'descripcion_canino': 'Descripción',
		}

	def __init__(self, *args, **kwargs):
		super(CaninoForm, self).__init__(*args, **kwargs)
		self.fields['raza_canino'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['sexo_canino'].widget.attrs.update({'required': True, 'class': 'form-control'})

class DocumentoForm(forms.Form):
	detalle = forms.CharField(label = 'Detalle', widget = forms.Textarea())