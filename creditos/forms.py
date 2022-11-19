from django import forms
from .models import Credito

class CreditoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.estado = 'PENDIENTE'
    
    class Meta:
        model = Credito
        exclude = ['estado']

class CreditoUpdateForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = '__all__'
