from django.shortcuts import render
from .logic.documentos_logic import analizador_documentos
from django.contrib import messages
from .forms import DocumentosForm
from django.http import HttpResponse

def analizar_documentos(request):
    print (request)
    if request.method == 'POST':
        img = request.FILES['docfile']
        analizador_documentos(img.file)
        messages.success(request, 'Documento enviado a analizar')
    else:
        print("Método no existente")
        form = DocumentosForm()
    
    context = {
        'form': form
    }
    
    return HttpResponse('error no es post',status=404)