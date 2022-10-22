from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

from celda.logic.CeldaForm import CeldaForm
from celda.models import Celda



@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = request.POST
        celda = CeldaForm(data, request.FILES)
        if celda.is_valid():
            celda.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error'})
        



