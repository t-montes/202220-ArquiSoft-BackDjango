from django.db import models
from usuarios.models import Usuario

class Empresa(models.Model):
    nit = models.CharField(max_length=20, blank=False, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "Empresa %s" % (self.usuario.nombre)
