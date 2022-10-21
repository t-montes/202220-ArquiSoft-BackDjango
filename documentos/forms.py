from django import forms
from .models import Documento

class DocumentosForm(forms.ModelForm):
    class Meta:
        path_image = forms.CharField(max_length=100)
        num_documento = forms.CharField(max_length=100)
        nombre = forms.CharField(max_length=100)