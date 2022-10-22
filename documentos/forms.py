from django import forms
from .models import Documento

class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'nombre',
            'num_documento',
            'path_image'
        ]
        labels = {
            'nombre': 'Nombre',
            'num_documento': 'Num_documento',
            'path_image': 'Path_image'
        }