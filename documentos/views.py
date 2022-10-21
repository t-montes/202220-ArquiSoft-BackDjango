from django.shortcuts import render
from .logic.documentos_logic import analizador_documentos
from django.contrib import messages
from .forms import DocumentosForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def analizar_documentos(request):
    if request.method == 'POST':
        form = DocumentosForm(request.POST)
        if form.is_valid():
            analizador_documentos(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully analizing the document')
            return HttpResponseRedirect(reverse('documentAnalize'))
        else:
            print(form.errors)
    else:
        form = DocumentosForm()

    context = {
        'form': form,
    }


