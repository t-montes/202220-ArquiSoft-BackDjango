from django.shortcuts import render
from .logic.documentos_logic import analizador_documentos
from django.contrib import messages
from .forms import DocumentosForm
from django.http import HttpResponse
from .logic.documentos_logic import get_documento
from .logic.documentos_logic import delete_documento

def analizar_documentos(request):
    print (request)
    if request.method == 'POST':
        print("DOC FILE",request.FILES['docfile'])
        img = request.FILES['docfile']
        print(type(img))
        print("DOC FILE . file",img)

        analizador_documentos(img.file)
        messages.success(request, 'Documento enviado a analizar')
    else:
        print("Método no existente")
        form = DocumentosForm()
    
    context = {
        'form': form
    }
    
    return HttpResponse('error no es post',status=404)

def documento(request,id):
    documento = get_documento(id)
    print("DOCUMENTO",documento)
    if documento is None:
        return HttpResponse('Documento no encontrado',status=404)
    else :
        print("hola")
        return render(request, 'documento.html', {'documento': documento})
def delete(request,id):
    documento = delete_documento(id)
    if documento is None:
        return HttpResponse('Documento no encontrado',status=404)
    else :
        return HttpResponse('Documento eliminado',status=200)
def create(request):
    if request.method == 'POST':
        form = DocumentosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Documento creado',status=200)
    else:
        form = DocumentosForm()
    return render(request, 'create.html', {'form': form})