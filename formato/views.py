from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from .models import Formato
import json

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        formato = Formato(nombre=data['nombre'], descripcion=data['descripcion'])
        formato.save()
        return JsonResponse({'status': 'ok'})
    else:
        return HttpResponse("Hello, world. You're at the formato index.")
