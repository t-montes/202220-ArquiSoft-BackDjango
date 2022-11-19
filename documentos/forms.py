from django import forms
from .models import Documento

class DocumentosForm(forms.ModelForm):
    docfile = forms.FileField(label='Seleccione el archivo')
    class Meta:
        model = Documento
        fields = "__all__"