from django import forms
from .models import Credito

class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = [
            'monto',
            'cuotas',
            'estado',
        ]
        labels = {
            'monto': 'Monto',
            'cuotas': 'Cuotas',
            'estado': 'Estado',
        }