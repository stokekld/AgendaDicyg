from django.conf.urls import url
from .views import UsuariosViews

views = UsuariosViews()

urlpatterns = [
	url(r'^$', views.inicio, name='inicio'),
	url(r'^agenda/(?P<slug>[a-z]+)/$', views.agenda, name='agenda'),
	url(r'^query/$', views.query, name='query'),
]