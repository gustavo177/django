from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Hola, mundo desde Django!")

def home(request):
    return render(request, 'index.html')
