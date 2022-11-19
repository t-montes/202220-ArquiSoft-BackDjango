from django.contrib import admin
from .models import Documento
class DocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'path_image', 'num_documento', 'nombre', 'imagen')
    
admin.site.register(Documento, DocumentoAdmin)
