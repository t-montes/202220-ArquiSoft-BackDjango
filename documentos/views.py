from django.shortcuts import render
from .logic.documentos_logic import analizador_documentos
from django.contrib import messages
from .forms import DocumentosForm
from django.http import HttpResponse

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
    documento = documento.objects.get(pk=id)

    if documento is None:
        return HttpResponse('Documento no encontrado',status=404)
    else :
        return render(request, 'documento.html', {'documento': documento})