from django.contrib import admin
from .models import Documento
class DocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('id')

admin.site.register(Documento, DocumentoAdmin)
