from django.contrib.messages.views import SuccessMessageMixin
from CaninoApp.apps.users.forms import SignupForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import *
from .models import *

template_dir = 'home/'

class InicioTemplateView(SuccessMessageMixin, FormView):
	template_name = template_dir+'home.html'
	success_message = 'Registro exitoso'
	form_class = SignupForm

	def get_context_data(self, **kwargs):
		context = super(InicioTemplateView, self).get_context_data(**kwargs)
		context['title'] = 'Bienvenido'
		return context

	def form_valid(self, form):
		form.signup()
		return super(InicioTemplateView, self).form_valid(form)

	def get_success_url(self):
		return reverse('login')