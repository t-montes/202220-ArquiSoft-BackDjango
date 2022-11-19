from django import forms
from .models import Credito

class CreditoCreateForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = [
            'monto',
            'cuotas',
        ]
        labels = {
            'monto': 'Monto',
            'cuotas': 'Cuotas',
        }

class CreditoUpdateForm(forms.ModelForm):
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