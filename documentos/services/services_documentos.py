from ..logic.documentos_logic import get_documento_by_num_documento

# this function return documento id. If the documento does not exist, then it is created


def get_documento(num_documento):
    documento = get_documento_by_num_documento(num_documento)
    if documento != None:
        return (documento)
    else: 
        return ("El documento no se pudo cargar, por favor intente de nuevo.")

