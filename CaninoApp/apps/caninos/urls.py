from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('CaninoApp.apps.caninos.views',
	url(r'^$', login_required(CaninoTemplateView.as_view()), name = 'panel'),
	url(r'^detalle/(?P<pk>\d+)/$', login_required(CaninoDetailView.as_view()), name = 'detail-canino'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(CaninoEditView.as_view()), name = 'edit-canino'),
	url(r'^crear/$', login_required(PanelUsuarioView.as_view()), name = 'crear-canino'),
	url(r'^documento/(?P<pk>\d+)/$', 'form_add_document_canino', name = 'add-documento'),
)