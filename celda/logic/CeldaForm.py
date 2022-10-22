"""
class Celda(models.Model):
    x = models.FloatField(blank=False, null=False)
    y = models.FloatField(blank=False, null=False)
    lenghX= models.FloatField(blank=False, null=False)
    lenghY= models.FloatField(blank=False, null=False)
    campo= models.CharField(max_length=50, blank=False, null=False)
    formato= models.ForeignKey(Formato, on_delete=models.CASCADE)
    def __str__(self):
        return "Celda %s" % (self.campo)

"""

# Compare this snippet from formato/logic/FormatosForm.py:

from django import forms
from celda.models import Celda

class CeldaForm(forms.ModelForm):
    class Meta:
        model = Celda
        fields = ('x', 'y', 'lenghX', 'lenghY', 'campo', 'formato')


