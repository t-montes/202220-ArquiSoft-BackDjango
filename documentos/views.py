from django.shortcuts import render
from .logic.documentos_logic import analizador_documentos
from django.contrib import messages
from .forms import DocumentosForm
from django.http import HttpResponse



def analizar_documentos(request):
    if request.method == 'POST':
        form = DocumentosForm(request.POST)
        if form.is_valid():
            print("El form si es valido")
            analizador_documentos(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully analizing the document')
            return HttpResponse('ok',status=200)
        else:
            print("El form no es valido")
            messages.add_message(request, messages.ERROR, 'Error analizing the document')
            return HttpResponse('error',status=412)
    else:
        print("Método no existente")
        return HttpResponse('error no es post',status=404)