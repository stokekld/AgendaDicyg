from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class AdminPersona(admin.ModelAdmin):
	list_display = ("per_id", "per_nombre", "per_apat", "per_amat", "per_email")