from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from datetime import datetime, date, time, timedelta

from .models import Usuario
from .models import Periodo
from .models import Bloque

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
			'slug': usuario.us_slug
		}
		return HttpResponse(template.render(context, request))

	def query(self, request):
		fecha = request.POST.get('fecha')
		tokensFecha = fecha.split("-")
		slug = request.POST.get('slug')
		usuario = get_object_or_404(Usuario, us_slug=slug)
		periodos = Periodo.objects.order_by('prd_inicio').filter(id_us=usuario.id_us)
		bloque = float(str(usuario.id_bloq))

		for periodo in periodos:

			prdInicio = periodo.prd_inicio
			prdFin = periodo.prd_fin

			horaIni = datetime( int(tokensFecha[0]),  int(tokensFecha[1]),  int(tokensFecha[2]), prdInicio.hour, prdInicio.minute, prdInicio.minute )
			print (horaIni + timedelta(hours=bloque))
		return HttpResponse()