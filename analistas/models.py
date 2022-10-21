from django.db import models
from usuarios.models import Usuario

class Analista(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return 'Analista %s' % (self.usuario.nombre)
