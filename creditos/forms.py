from django import forms
from .models import Credito

class CreditoCreateForm(forms.ModelForm):
    class Meta:
        model = Credito
        exclude = ['estado']

class CreditoUpdateForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = '__all__'
