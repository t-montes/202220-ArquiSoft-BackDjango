import time
import pika

#Ip de la base de datos
rabbit_host = '10.128.0.8'
rabbit_user = 'avanzo_user'
rabbit_password = 'avanzo'
exchange = 'analizando_documentos'
topic = 'DocumentosTopic'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='topic')


def analizador_documentos(request):
    channel.basic_publish(exchange=exchange, routing_key=topic, body=request)
    connection.close()
    print('> Sending documents. To exit press CTRL+C')