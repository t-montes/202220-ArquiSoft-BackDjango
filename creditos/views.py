from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from avanzo.auth0backend import getRole
from .logic.credito_logic import update_credit, create_credit, get_creditos, get_credito
from .forms import CreditoForm
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
            return HttpResponse("Not allowed method", status=400)
    else:
        print("getAll-part1")
        response = render_to_response('unauthorized.html', {}, context_instance=RequestContext(request))
        response.status_code = 401
        print("getAll-part2", response)
        return response

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
            return HttpResponse("Not allowed method", status=400)
    else:
        return HttpResponse("Unauthorized", status=401)

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
            return HttpResponse("Not allowed method", status=400)
    else:
        return HttpResponse("Unauthorized", status=401)

@login_required
def credito_create(request):
    role = getRole(request)
    if role in ["ADMIN", "ANALISTA", "EMPLEADO"]:
        print("create-parte1")
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
            print("create-parte2; empty form", form)
            return render(request, 'credito_create.html', context)
        else:
            return HttpResponse("Not allowed method", status=400)
    else:
        return HttpResponse("Unauthorized", status=401)

