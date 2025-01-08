from django.shortcuts import render
from .models import Persona  

# Create your views here.
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Hola, mundo desde Django!")

def home(request):
    #  # Cargar todos los datos de la tabla Persona
    # personas = Persona.objects.all()
    
    # Cargar todos los datos de la tabla Persona junto con los archivos relacionados
    personas = Persona.objects.prefetch_related('filearchivo_set', 'ciudad_set').all()

    # Pasar los datos a la plantilla index.html
    return render(request, 'index.html', {'personas': personas})
