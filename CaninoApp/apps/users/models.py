# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from CaninoApp.apps.base.models import *
from django.db import models

class ProfileUser(models.Model):
	user = models.OneToOneField(User, primary_key = True)
	role = models.ForeignKey(Rol)
	numero_identificacion = models.CharField(max_length = 10)
	direccion_residencia = models.CharField(max_length = 80)
	barrio_residencia = models.ForeignKey(Barrio)
	numero_telefonico = models.CharField(max_length = 10, default = '-')

	def __str__(self):
		return str(self.user)