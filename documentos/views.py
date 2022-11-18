from django.shortcuts import render
from .logic.documentos_logic import analizador_documentos
from django.contrib import messages
from .forms import DocumentosForm
from django.http import HttpResponse



def analizar_documentos(request):
    if request.method == 'POST':
        analizador_documentos(request.FILES['docfile'])
        messages.add_message(request, messages.SUCCESS, 'Successfully analizing the document', )
        return HttpResponse('ok',status=200)
    else:
        print("Método no existente")
        form = DocumentosForm()
    
    context = {
        'form': form
    }
    
    return HttpResponse('error no es post',status=404)