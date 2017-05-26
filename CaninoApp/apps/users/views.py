from django.shortcuts import render
from django.views.generic import *

template_dir = 'caninos/'

class PanelUsuarioView(TemplateView):
	template_name = template_dir+'panel.html'

	def get_context_data(self, **kwargs):
		context = super(PanelUsuarioView, self).get_context_data(**kwargs)
		context['title'] = 'Bienvenido'
		return context