from django.db import models

# Create your models here.

class Formato(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    def __str__(self):
        return "Formato %s" % (self.nombre)
