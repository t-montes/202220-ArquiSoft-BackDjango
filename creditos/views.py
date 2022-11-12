from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from avanzo.auth0backend import getRole
from .logic.credito_logic import update_credit

@login_required
def credit_update(request):
    role = getRole(request)
    if request.method == 'PUT':
        if role == "ANALIZADOR":
            form = CreditForm(request.POST)
            if form.is_valid():
                update_credit(form)
                messages.add_message(request, messages.SUCCESS, 'Credito actualizado correctamente')
                form.save()
                return HttpResponseRedirect('/creditos')
        else:
            return HttpResponse("Unauthorized User", status=401)
    else:
        return HttpResponse("BAD REQUEST", status=204)

# Create your views here.
