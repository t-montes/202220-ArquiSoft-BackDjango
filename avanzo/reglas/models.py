from django.db import models

class Regla(models.Model):
    nombre = models.CharField(max_length=100)
    condiciones = models.TextField()

    def __str__(self):
        return self.nombre
