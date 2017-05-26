from django.contrib.auth.models import User
from CaninoApp.apps.base.models import *
from django import forms
from .models import *

class SignupForm(forms.Form):
	first_name = forms.CharField(label = 'Nombres', widget = forms.TextInput(attrs = {'class': 'form-control','required': True,'maxlength': 20}))
	last_name = forms.CharField(label = 'Apellidos', widget = forms.TextInput(attrs = {'class': 'form-control','required': True,'maxlength': 20}))
	email = forms.CharField(label = 'Correo electrónico', widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True, 'type': 'email', 'maxlength': 45}))
	numero_identificacion = forms.CharField(label = 'Número de identificación', widget = forms.TextInput(attrs = {'maxlength': 10, 'class': 'form-control only-number','required': True,'maxlength':10}))
	barrio_residencia = forms.ModelChoiceField(Barrio.objects.all(), label = 'Barrio de residencia', widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))
	direccion_residencia = forms.CharField(label = 'Dirección de residencia', widget = forms.TextInput(attrs = {'class': 'form-control','required': True,'maxlength':80}))
	numero_telefonico = forms.CharField(label = 'Número telefónico', widget = forms.TextInput(attrs = {'class': 'form-control only-number', 'required': False,'maxlength':10}))

	def clean_numero_identificacion(self):
		numero_identificacion = self.cleaned_data.get('numero_identificacion').lower()
		if ProfileUser.objects.filter(numero_identificacion = numero_identificacion).exists():
			raise forms.ValidationError('El número de identificación ya se ecuentra en uso.')
		return numero_identificacion

	def signup(self):
		first_name = self.cleaned_data['first_name']
		last_name = self.cleaned_data['last_name']
		numero_identificacion = self.cleaned_data['numero_identificacion']
		direccion_residencia = self.cleaned_data['direccion_residencia']
		barrio_residencia = self.cleaned_data['barrio_residencia']
		username = self.cleaned_data['email'].lower()
		numero_telefonico = self.cleaned_data['numero_telefonico']
		user = User.objects.create_user(username, '', numero_identificacion)
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		profile_user = ProfileUser(user = user,
			numero_identificacion = numero_identificacion,
			direccion_residencia = direccion_residencia,
			barrio_residencia = barrio_residencia,
			numero_telefonico = numero_telefonico,
			role = Rol.objects.get(prefijo_rol = "NM")
		)
		profile_user.save()