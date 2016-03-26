from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Usuario
from .models import Periodo

class UsuariosViews(object):
	def inicio(self, request):
		template = loader.get_template('index.html')
		usuarios = Usuario.objects.all()
		context = {
			'titulo': 'Bienvenido',
			'usuarios': usuarios
		}
		return HttpResponse(template.render(context, request))
		
	def agenda(self, request, slug):
		template = loader.get_template('agenda.html')
		usuario = get_object_or_404(Usuario, us_slug=slug)
		periodos = Periodo.objects.order_by('prd_inicio').filter(id_us=usuario.id_us)
		context = {
			'titulo': 'agenda',
			'nombre': usuario.us_nombre + " " + usuario.us_apat + " " + usuario.us_amat,
			'periodos': periodos
		}
		return HttpResponse(template.render(context, request))

	def query(self, request):
		return HttpResponse("respuesta")