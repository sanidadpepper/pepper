# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from CaninoApp.apps.base.models import *

class Command(BaseCommand):

	def handle(self, *args, **options):

		Barrio.objects.create(nombre_barrio = "La esperanza")
		print("Barrios creados")
		OcupacionCanino.objects.create(nombre_ocupacion = "Cuidandero")
		print("Ocupaciones creados")
		Raza.objects.create(nombre_raza = "Pitbull")
		print("Razas creados")
		Rol.objects.create(nombre_rol = "Normal", prefijo_rol = "NM")
		print("Roles creados")