from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from avanzo.auth0backend import getRole
from .logic.credito_logic import update_credit, create_credit, get_creditos, get_credito
from .forms import CreditoCreateForm, CreditoUpdateForm
import json

@login_required
def creditos_list(request):
    role = getRole(request)
    if role in ["ADMIN", "ANALISTA"]:
        if request.method == 'GET':
            creditos = get_creditos()
            context = {
                'creditos': creditos,
                # 'role': role
            }
            return render(request, 'creditos_list.html', context)
        else:
            return render(request, '404.html')
    else:
        return render(request, 'unauthorized.html')

@login_required
def credito_detail(request, id=0):
    role = getRole(request)
    if role in ["ADMIN", "ANALISTA"]:
        if request.method == 'GET':
            credito = get_credito(id)
            context = {
                'credito': credito,
                # 'role': role
            }
            return render(request, 'credito_detail.html', context)
        else:
            return render(request, '404.html')
    else:
        return render(request, 'unauthorized.html')

@login_required
def credito_update(request):
    role = getRole(request)
    if role in ["ADMIN", "ANALISTA"]:
        if request.method == 'PUT':
            print("request BODY", request.body)
            # request.body to dict
            body = request.body.decode('utf-8')
            body = json.loads(body)
            update_credit(body)
            messages.add_message(request, messages.SUCCESS, 'Credito actualizado correctamente')
            return HttpResponse(status=200)
        else:
            return render(request, '404.html')
    else:
        return render(request, 'unauthorized.html')

@login_required
def credito_create(request):
    role = getRole(request)
    if role in ["ADMIN", "ANALISTA", "EMPLEADO"]:
        if request.method == 'POST':
            print("request POST", request.POST)
            form = CreditoCreateForm(request.POST)
            if form.is_valid():
                create_credit(form)
                messages.add_message(request, messages.SUCCESS, 'Credito creado correctamente')
                return HttpResponseRedirect('/creditos/')
            else:
                print(form.errors)
        elif request.method == 'GET':
            form = CreditoCreateForm()
        else:
            return render(request, '404.html')

        context = {
            'form': form,
        }
        return render(request, 'credito_create.html', context)

    else:
        return render(request, 'unauthorized.html')

