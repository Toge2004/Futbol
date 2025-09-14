from django.contrib import admin
from .models import EquipoFutbol

@admin.register(EquipoFutbol)
class EquipoFutbolAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'pais', 'fundacion', 'entrenador', 'activo']
    list_filter = ['pais', 'activo', 'fundacion']
    search_fields = ['nombre', 'ciudad', 'entrenador']
    list_editable = ['activo']