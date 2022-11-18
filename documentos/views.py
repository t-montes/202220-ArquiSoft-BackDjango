from django.shortcuts import render
from .logic.documentos_logic import analizador_documentos
from django.contrib import messages
from .forms import DocumentosForm
from django.http import HttpResponse
import io
from PIL import Image

def analizar_documentos(request):
    print (request)
    if request.method == 'POST':
        img = request.FILES['docfile']
        print("tipo", type(img.file))
        aux_im = Image.open(io.BytesIO((img.file).content))
        print("tipo", type(aux_im))
        analizador_documentos(img)
        messages.success(request, 'Documento enviado a analizar')
    else:
        print("Método no existente")
        form = DocumentosForm()
    
    context = {
        'form': form
    }
    
    return HttpResponse('error no es post',status=404)