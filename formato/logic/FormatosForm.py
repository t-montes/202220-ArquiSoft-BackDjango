from django import forms
from formato.models import Formato

class FormatosForm(forms.ModelForm):
    class Meta:
        model = Formato
        fields = [
            'nombre',
            'descripcion'
        ]
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion'
        }


