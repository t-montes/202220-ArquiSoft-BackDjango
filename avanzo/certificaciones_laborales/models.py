from django.db import models
from documentos.models import Documento

class CertificacionLaboral(models.Model):
    tipo_contrato = models.CharField(max_length=50)
    salario_mensual = models.FloatField()
    empresa_asociada = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return "Contrato laboral #%s de tipo %s" % (self.documento.num_documento, self.tipo_contrato)
