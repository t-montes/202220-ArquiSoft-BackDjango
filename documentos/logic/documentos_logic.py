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


def analizador_documentos(form):
    cuerpo = "'nombre':{}, 'path_image':{}, 'num_documento':{}".format(form.cleaned_data['nombre'],form.cleaned_data['path_image'],form.cleaned_data['num_documento'])
    channel.basic_publish(exchange=exchange, routing_key=topic, body=cuerpo)
    connection.close()
    print('> Sending documents. To exit press CTRL+C')