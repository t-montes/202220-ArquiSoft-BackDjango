from django.db import models
from usuarios.models import Usuario

class Empleado(models.Model):
    cc = models.CharField(max_length=10, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Empleado %s' % (self.usuario.nombre)
