from django.contrib import admin
from .models import Persona

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    # Mostrar columnas específicas en la lista
    list_display = ('id', 'nombre', 'apellido')
    
    # Agregar un buscador
    search_fields = ('nombre', 'apellido')
    
    # Filtrar por campos específicos
    list_filter = ('apellido',)
    
    # Configurar la vista de detalle (opcional)
    fields = ('nombre', 'apellido')
    
    # Opcional: ordenar por defecto por un campo
    ordering = ('apellido',)

# Registrar el modelo con la configuración personalizada
admin.site.register(Persona, PersonaAdmin)
