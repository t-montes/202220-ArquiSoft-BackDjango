import time
import pika
from ..models import Documento

#Ip de la base de datos
rabbit_host = '10.128.0.12'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'analizando_documentos'
topic = 'DocumentosTopic'

def analizador_documentos(img):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    cuerpo = str(img)
    channel.basic_publish(exchange=exchange, routing_key=topic, body=cuerpo)
    connection.close()
    print('> Sending documents. To exit press CTRL+C')
    print(cuerpo)

def get_documentos ():
    queryset = Documento.objects.all()
    return (queryset)


def get_documento_by_num_documento (num_documento):
    try:
        documento = Documento.objects.get(num_documento=num_documento)
        return (documento)
    except:
        documento = None
        return (documento)