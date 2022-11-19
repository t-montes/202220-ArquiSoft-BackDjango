from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from avanzo.auth0backend import getRole
from .logic.credito_logic import update_credit, create_credit, get_creditos, get_credito
from .forms import CreditoCreateForm, CreditoUpdateForm
from .models import Credito
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
def credito_update(request, id):
    role = getRole(request)
    if role in ["ADMIN", "ANALISTA"]:
        credito = Credito.objects.get(id=id)
        if request.method == 'POST':
            form = CreditoUpdateForm(request.POST, instance=credito)
            if form.is_valid():
                update_credit(form)
                messages.add_message(request, messages.SUCCESS, 'Crédito actualizado correctamente')
                return HttpResponseRedirect('/creditos/')
            else:
                print(form.errors)
        elif request.method == 'GET':
            form = CreditoUpdateForm(instance=credito)
        else:
            return render(request, '404.html')
        
        context = {
            'form': form,
            'credito': credito,
            # 'role': role
        }
        return render(request, 'credito_update.html', context)

    else:
        return render(request, 'unauthorized.html')

@login_required
@csrf_exempt
def credito_create(request):
    role = getRole(request)
    print("\tRole:",role)
    if role in ["ADMIN", "ANALISTA", "EMPLEADO"]:
        if request.method == 'POST':
            if request.POST:
                print("create from FORM")
                form = CreditoCreateForm(request.POST)
            else:
                print("create from Connection Recovery")
                form = CreditoCreateForm()
                body = json.loads(request.body)
                form.instance.monto = float(body['monto'])
                form.instance.cuotas = int(body['cuotas'])
                form.instance.csrfmiddlewaretoken = body['csrfmiddlewaretoken']
                form.clean()

            print("FORM",form)
            print("dir-form",dir(form))
            print("form.instance",form.instance)
            if form.is_valid():
                print("[VIEWS] form valid")
                create_credit(form)
                messages.add_message(request, messages.SUCCESS, 'Credito creado correctamente')
                return HttpResponseRedirect('/creditos/')
            else:
                print("form invalid")
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

