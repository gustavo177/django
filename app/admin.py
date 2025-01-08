from django.contrib import admin
from .models import Persona, FileArchivo, Ciudad

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

@admin.register(FileArchivo)
class FileArchivoAdmin(admin.ModelAdmin):
    list_display = ('user', 'archivo', 'hora')  # Campos a mostrar en la lista
    list_filter = ('hora',)  # Filtros en la barra lateral
    search_fields = ('user__nombre',)  # Campos para búsqueda (ajusta según el modelo relacionado)
    
@admin.register(Ciudad)
class Ciudad(admin.ModelAdmin):
    list_display = ('user','nombre')  # Campos a mostrar en la lista
    search_fields = ('user__nombre',)  # Campos para búsqueda (ajusta según el modelo relacionado)
    