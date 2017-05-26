from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
	url(r'^dashboard/', admin.site.urls),
	url(r'^', include('CaninoApp.apps.base.urls')),
	url(r'^panel/', include('CaninoApp.apps.caninos.urls')),
	url(r'^usuario/', include('CaninoApp.apps.users.urls')),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]