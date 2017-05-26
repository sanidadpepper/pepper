# -*- encoding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

template_dir = 'caninos/'

class CaninoTemplateView(TemplateView):
	template_name = template_dir+'panel.html'

	def get_context_data(self, **kwargs):
		context = super(CaninoTemplateView, self).get_context_data(**kwargs)
		context['title'] = 'Mis canino'
		return context

class CaninoDetailView(DetailView):
	model = Canino
	template_name = template_dir+'detail_canino.html'

	def get_context_data(self, **kwargs):
		context = super(CaninoDetailView, self).get_context_data(**kwargs)
		context['title'] = 'Detalle del canino'
		return context

class CaninoEditView(SuccessMessageMixin, UpdateView):
	model = Canino
	template_name = template_dir+'crear.html'
	success_message = 'Canino actualizada correctamente'
	form_class = CaninoForm

	def get_context_data(self, **kwargs):
		context = super(CaninoEditView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar canino'
		context['url'] = reverse('edit-canino', kwargs = {'pk': self.kwargs['pk']})
		return context

	def get_success_url(self):
		return reverse('panel')

class PanelUsuarioView(SuccessMessageMixin, CreateView):
	template_name = template_dir+'crear.html'
	success_message = 'Canino agregado correctamente'
	form_class = CaninoForm

	def get_context_data(self, **kwargs):
		context = super(PanelUsuarioView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar canino'
		context['url'] = reverse('crear-canino')
		return context

	def form_valid(self, form):
		form.instance.propietario_canino = self.request.user
		return super(PanelUsuarioView, self).form_valid(form)

	def get_success_url(self):
		return reverse('panel')

class CaninoDocumentoView(SuccessMessageMixin, FormView):
	template_name = template_dir+'documento_add.html'
	success_message = 'Documento agregado'
	form_class = DocumentoForm

	def get_context_data(self, **kwargs):
		context = super(CaninoDocumentoView, self).get_context_data(**kwargs)
		context['title'] = 'Documento'
		context['pk'] = self.kwargs['pk']
		return context

	def form_valid(self, form):
		form.save_data(self.kwargs['pk'])
		return super(CaninoDocumentoView, self).form_valid(form)

	def get_success_url(self):
		return reverse('detail-canino', kwargs = {'pk': self.kwargs['pk']})