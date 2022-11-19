from django.db import models

class Documento(models.Model):
    path_image = models.CharField(max_length=100)
    num_documento = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='Proyecto_Uno/static/media')
