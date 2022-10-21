from django.db import models
from documentos.models import Documento

class CertificacionBancaria(models.Model):
    num_cuenta = models.BigIntegerField()
    tipo_cuenta = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    gerente_banco = models.CharField(max_length=50)
    nombre_empresa = models.CharField(max_length=50)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return 'La certificación bancaria %s está en estado %s' % (self.documento.num_documento, self.estado)
