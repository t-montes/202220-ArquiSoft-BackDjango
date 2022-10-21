from django.db import models
from documentos.models import Documento

class ComprobanteDePago(models.Model):
    num_factura = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    numero_referencia = models.IntegerField()
    numero_comprobante = models.IntegerField()
    valor_pagado = models.FloatField()
    num_cuenta = models.IntegerField()
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return 'Comprobante de pago #%s de valor %f' % (self.documento.num_documento, self.valor_pagado)
