from django.shortcuts import render
from .logic.documentos_logic import analizador_documentos
from django.contrib import messages
from .forms import DocumentosForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse



def analizar_documentos(request):
    if request.method == 'POST':
        form = DocumentosForm(request.POST)
        if form.is_valid():
            print("El form si es valido")
            analizador_documentos(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully analizing the document')
            return HttpResponse('ok')
        else:
            print(form.errors)
    else:
        print("No es valido el form")
        form = DocumentosForm()

        context = {
        'form': form,
        }
        return HttpResponse('not ok')