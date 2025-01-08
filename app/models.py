from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class FileArchivo(models.Model):
    user = models.ForeignKey(Persona, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/')  # La ruta en el contenedor de Azure
    hora = models.DateTimeField(auto_now_add=True)

class Ciudad(models.Model):
    user = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)


# Señal para eliminar el archivo del almacenamiento al eliminar la instancia
@receiver(post_delete, sender=FileArchivo)
def eliminar_archivo(sender, instance, **kwargs):
    if instance.archivo:
        instance.archivo.delete(False)  # False evita guardar el modelo nuevamente
