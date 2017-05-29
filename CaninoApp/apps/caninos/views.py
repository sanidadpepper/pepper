# -*- encoding: utf-8 -*-
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext
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

@csrf_exempt
def form_add_document_canino(request, pk):
	data = {}

	class RequiredFormSet(BaseFormSet):
		def __init__(self, *args, **kwargs):
			super(RequiredFormSet, self).__init__(*args, **kwargs)
			for form in self.forms:
				form.empty_permitted = False

	RegistroCaninoDocumentoFormSet = formset_factory(RegistroCaninoDocumentoForm, max_num = 10, formset = RequiredFormSet)
	if request.method == 'POST':
		registro_canino_form = RegistroCaninoForm(request.POST)
		registro_canino_documento_form = RegistroCaninoDocumentoFormSet(request.POST, request.FILES or None)
		if registro_canino_form.is_valid():
			registro_canino = registro_canino_form.save(commit = False)
			registro_canino.canino = Canino.objects.get(pk = pk)
			registro_canino.save()
			for form in registro_canino_documento_form.forms:

				registro_canino_documento = form.save(commit = False)
				if registro_canino_documento.nombre_documento != '':
					registro_canino_documento.registro_canino = registro_canino
					registro_canino_documento.save()
		return HttpResponseRedirect(reverse('detail-canino', kwargs = {'pk': pk}))
	else:
		registro_canino_form = RegistroCaninoForm()
		registro_canino_documento_form = RegistroCaninoDocumentoFormSet()
	c = {
		'registro_canino_form': registro_canino_form,
		'registro_canino_documento_form': registro_canino_documento_form
	}
	c.update(csrf(request))
	data['pk'] = pk
	data['c'] = c
	return render_to_response(template_dir+'documento_add.html', data)