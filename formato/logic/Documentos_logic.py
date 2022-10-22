from formato.models import Formato


def getPK_formato_name(name):
    try:
        return Formato.objects.get(nombre=name).pk
    except:
        return None