from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('analizarDocumentos/', csrf_exempt(views.analizar_documentos), name='analizarDocumentos')
]