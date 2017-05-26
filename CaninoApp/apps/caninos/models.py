from django.contrib.auth.models import User
from CaninoApp.apps.base.models import *
from django.db import models

SEXO_CHOICES = (
	('M', 'Masculino'),
	('F', 'Femenino'),
)

class Canino(models.Model):
	propietario_canino = models.ForeignKey(User)
	nombre_canino = models.CharField(max_length = 45)
	raza_canino = models.ForeignKey(Raza)
	fecha_nacimiento = models.DateField()
	sexo_canino = models.CharField(max_length = 1, choices = SEXO_CHOICES)
	color_canino = models.CharField(max_length = 15)
	descripcion_canino = models.CharField(max_length = 200)
	ocupaciones = models.ManyToManyField(OcupacionCanino, blank = True, null = True)

	def __str__(self):
		return str(self.nombre_canino)

class RegistroCanino(models.Model):
	fecha_registro = models.DateField(auto_now = True)
	canino = models.ForeignKey(Canino)
	detalle_registro = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.fecha_registro)

class RegistroCaninoDocumento(models.Model):
	registro_canino = models.ForeignKey(RegistroCanino)
	nombre_documento = models.CharField(max_length = 40)
	documento = models.FileField(upload_to = 'files')

	def __str__(self):
		return self.nombre_documento