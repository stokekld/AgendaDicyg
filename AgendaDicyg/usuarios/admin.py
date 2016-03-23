from django.contrib import admin
from .models import Bloque, Usuario, Periodo

@admin.register(Bloque)
class AdminBloque(admin.ModelAdmin):
	list_display = ('id_bloq', 'bloq_tiempo')

@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
	list_display = ("us_nombre", "us_apat", "us_amat", "us_slug", "us_user")

@admin.register(Periodo)
class AdminPeriodo(admin.ModelAdmin):
	list_display = ("id_prd", "id_us", "prd_inicio", "prd_fin")