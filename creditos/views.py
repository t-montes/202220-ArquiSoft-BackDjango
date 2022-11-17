from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from avanzo.auth0backend import getRole
from .logic.credito_logic import update_credit
from .forms import CreditoForm
import json

# @login_required
def credito_update(request):
    # role = getRole(request)
    if request.method == 'PUT':
        print("request BODY", request.body)
        # request.body to dict
        body = request.body.decode('utf-8')
        body = json.loads(body)
        update_credit(body)
        messages.add_message(request, messages.SUCCESS, 'Credito actualizado correctamente')
        return HttpResponse(status=200)
    else:
        return HttpResponse("BAD REQUEST", status=400)
def esta_funcionando_papi(request):
    return HttpResponse("Esta funcionando papi")
# Create your views here.
