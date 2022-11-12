from ..models import Credito

def update_credit(body:dict):
    print("BODY [logic]",body)
    credit = Credito.objects.get(id=body['id'])
    credit.monto = body['monto']
    credit.cuotas = body['cuotas']
    credit.estado = body['estado']
    credit.save()
    print("Actualizado con éxito [logic]")
    print("Crédito:",credit)
    return ()
