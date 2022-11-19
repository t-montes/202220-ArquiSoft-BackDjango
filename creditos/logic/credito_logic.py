from ..models import Credito

def get_creditos():
    creditos = Credito.objects.all()
    # print("Creditos:",creditos)
    return (creditos)

def get_credito(id):
    credit = Credito.objects.get(id=id)
    # print("Crédito:",credit)
    return (credit)

def update_credit(body:dict):
    # print("BODY update [logic]",body)
    credit = Credito.objects.get(id=body['id'])
    credit.monto = body['monto']
    credit.cuotas = body['cuotas']
    credit.estado = body['estado']
    credit.save()
    # print("Actualizado con éxito [logic]")
    # print("Crédito:",credit)
    return ()

def create_credit(form):
    print("FORM [logic]",form)
    credit = form.save()
    credit.save()
    return ()
