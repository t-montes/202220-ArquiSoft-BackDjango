import time
import pika
from ..models import Documento
import io 
#Ip de la base de datos
rabbit_host = '10.128.0.12'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'analizando_documentos'
topic = 'DocumentosTopic'

def analizador_documentos(img):

    getvalue = img.getvalue()
    # print("get_value",getvalue)
    # print("get_value type",type(getvalue))

    # read = img.read()
    # print("read",read)
    # print("read type",type(read))

    print("IMG",img)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    cuerpo = getvalue
    channel.basic_publish(exchange=exchange, routing_key=topic, body=cuerpo)
    connection.close()
    print('> Sending documents. To exit press CTRL+C')
    print(cuerpo)

def get_documentos ():
    queryset = Documento.objects.all()
    return (queryset)
def get_documento (id):
    documento = Documento.objects.get(pk=id)
    return (documento)

def delete_documento(id):
    documento = Documento.objects.get(pk=id)
    documento.delete()

def get_documento_by_num_documento (num_documento):
    try:
        documento = Documento.objects.get(num_documento=num_documento)
        return (documento)
    except:
        documento = None
        return (documento)