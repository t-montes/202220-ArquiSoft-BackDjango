from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from .models import Formato
from .logic.FormatosForm import FormatosForm
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = request.POST
        form = FormatosForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error'})
    else:
        formatos = Formato.objects.all()
        data = serializers.serialize('json', formatos)
        return HttpResponse(data, content_type='application/json')
