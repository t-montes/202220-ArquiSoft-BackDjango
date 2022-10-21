from django.db import models

class Credito(models.Model):
    monto = models.FloatField()
    cuotas = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return 'Crédito de %f a %d' % (self.monto, self.cuotas)
