from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('analizarDocumentos/', csrf_exempt(views.analizar_documentos), name='analizarDocumentos'),
    path('documento/<int:id>', views.documento, name='documento'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('create/', csrf_exempt(views.create), name='create'),
]