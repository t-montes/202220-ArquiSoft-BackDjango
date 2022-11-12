from ..models import Credito

def update_credit(form):
    credit = Credito.objects.get(id=form.cleaned_data['id'])
    credit.monto = form.cleaned_data['monto']
    credit.cuotas = form.cleaned_data['cuotas']
    credit.estado = form.cleaned_data['estado']
    credit.save()
    return ()
