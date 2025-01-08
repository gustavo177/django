from django.urls import path
from . import views


urlpatterns = [
    path('hola/', views.hola_mundo, name='hola_mundo'),
    path('home/', views.home, name='home'),

]  

