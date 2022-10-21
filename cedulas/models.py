from django.db import models
from documentos.models import Documento

class Cedula(models.Model):
    tipo_documento = models.CharField(max_length=50)
    lugar_expedicion = models.CharField(max_length=50)
    fecha_expedicion = models.DateField()
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return "Cédula %s de %s" % (self.documento.num_documento, self.lugar_expedicion)
