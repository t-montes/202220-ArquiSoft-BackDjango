from django.db import models

from documentos.models import Documento

class Nomina(models.Model):
    fecha_expedicion = models.DateField()
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return 'Nómina #%s' % (self.documento.num_documento)
    
