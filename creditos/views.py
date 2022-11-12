from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from avanzo.auth0backend import getRole
from .logic.credito_logic import update_credit
from .forms import CreditoForm

@login_required
def credito_update(request):
    role = getRole(request)
    if request.method == 'PUT':
        if role == "ANALIZADOR":
            form = CreditoForm(request.PUT)
            print("FORM [views]:", form)
            if form.is_valid():
                print("FORM IS VALID [views]")
                update_credit(form)
                print("FORM UPDATED [views]")
                messages.add_message(request, messages.SUCCESS, 'Credito actualizado correctamente')
                return HttpResponse(status=200)
            else:
                messages.add_message(request, messages.ERROR, 'Error al actualizar credito')
                return HttpResponse(status=200)
        else:
            return HttpResponse("Unauthorized User", status=401)
    else:
        return HttpResponse("BAD REQUEST", status=204)

# Create your views here.
