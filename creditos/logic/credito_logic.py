from ..models import Credito

def get_creditos():
    creditos = Credito.objects.all()
    # print("Creditos:",creditos)
    return (creditos)

def get_credito(id):
    credit = Credito.objects.get(id=id)
    # print("Crédito:",credit)
    return (credit)

def update_credit(form):
    print("FORM [logic] (update)",form)
    credit = form.save()
    credit.save()
    return ()

def create_credit(form):
    print("FORM [logic] (create)",form)
    credit = form.save()
    credit.save()
    return ()
