from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from avanzo.auth0backend import getRole
from .logic.credito_logic import update_credit, create_credit, get_creditos, get_credito
from .forms import CreditoForm
import json

def creditos_list(request):
    # role = getRole(request)
    if request.method == 'GET':
        creditos = get_creditos()
        context = {
            'creditos': creditos,
            # 'role': role
        }
        return render(request, 'Credito/creditos_list.html', context)
    else:
        return HttpResponse("Not allowed method", status=400)

# @login_required
def credito_detail(request, id=0):
    # role = getRole(request)
    print("parte1")
    if request.method == 'GET':
        credito = get_credito(id)
        context = {
            'credito': credito,
            # 'role': role
        }
        print("parte2", credito)
        return render(request, 'creditos/credito_detail.html', context)
    else:
        return HttpResponse("Not allowed method", status=400)

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
        return HttpResponse("Not allowed method", status=400)

# @login_required
def credito_create(request):
    # role = getRole(request)
    if request.method == 'POST':
        # print("request BODY", request.body)
        # request.body to dict
        body = request.body.decode('utf-8')
        body = json.loads(body)
        create_credit(body)
        messages.add_message(request, messages.SUCCESS, 'Credito creado correctamente')
        return HttpResponse(status=200)
    elif request.method == 'GET':
        form = CreditoForm()
        context = {
            'form': form,
        }
        return render(request, 'Credito/credito_create.html', context)
    else:
        return HttpResponse("Not allowed method", status=400)

