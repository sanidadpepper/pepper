# -*- encoding: utf-8 -*-
from django.db import models

class Barrio(models.Model):
	nombre_barrio = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre_barrio

	def __unicode__(self):
		return self.nombre_barrio

class OcupacionCanino(models.Model):
	nombre_ocupacion = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre_ocupacion

	def __unicode__(self):
		return self.nombre_ocupacion

class Raza(models.Model):
	nombre_raza = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre_raza

	def __unicode__(self):
		return self.nombre_raza

class Rol(models.Model):
	nombre_rol = models.CharField(max_length = 40)
	prefijo_rol = models.CharField(max_length = 2)

	def __str__(self):
		return self.nombre_rol

	def __unicode__(self):
		return self.nombre_rol