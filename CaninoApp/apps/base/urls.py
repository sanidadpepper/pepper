from django.contrib.auth.decorators import user_passes_test
from django.conf.urls import patterns, url, include
from .views import *

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/panel/')

urlpatterns = patterns('CaninoApp.apps.home.views',
	url(r'^$', login_forbidden(InicioTemplateView.as_view()), name = 'inicio'),
)