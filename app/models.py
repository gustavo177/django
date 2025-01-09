from django.db import models
from django.db.models.signals import post_delete, pre_save
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

# Señal para eliminar el archivo anterior antes de actualizar
@receiver(pre_save, sender=FileArchivo)
def actualizar_archivo(sender, instance, **kwargs):
    if not instance.pk:  # Si es una nueva instancia, no hace nada
        return

    try:
        # Obtener la instancia previa antes de actualizar
        old_instance = FileArchivo.objects.get(pk=instance.pk)
        # Si el archivo anterior es diferente al nuevo, eliminar el anterior
        if old_instance.archivo and old_instance.archivo != instance.archivo:
            old_instance.archivo.delete(save=False)  # Elimina el archivo anterior
    except FileArchivo.DoesNotExist:
        pass  # Si no existe la instancia previa, no hay nada que eliminar