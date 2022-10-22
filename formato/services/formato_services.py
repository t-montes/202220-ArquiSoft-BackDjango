from formato.models import Formato 
import formato.logic.Documentos_logic as lg

def getPK_formato_name(name):
    try:
        return lg.getPK_formato_name(name)
    except:
        return None