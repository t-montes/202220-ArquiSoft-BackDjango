from django import forms
from .models import Documento

class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'nombre',
            'path_image', 
            'num_documento'
        ]
        labels = {
            'nombre': 'Nombre',
            'path_image': 'Path_image',
            'num_documento': 'Num_documento'
        }