from django import forms
from .models import Documento

class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = "__all__"