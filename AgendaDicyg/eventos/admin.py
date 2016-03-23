from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class AdminEvento(admin.ModelAdmin):
	list_display = ("id_event", "id_us", "id_per", "event_inicio", "event_fin", "event_descripcion")