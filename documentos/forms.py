from django import forms
from .models import Documento

class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'name',
            'path_image', 
            'num_document'
        ]
        labels = {
            'name': 'Name',
            'path_image': 'Path_image',
            'num_document': 'Num_document'
        }