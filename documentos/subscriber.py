import json
import pika
from sys import path
from os import environ
import django

rabbit_host = '10.128.0.12'
rabbit_user = 'avanzo_user'
rabbit_password = 'avanzo'
exchange = 'analizando_documentos'
topic = 'DocumentosTopic'

path.append('avanzo/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'avanzo.settings')
django.setup()

from documentos.logic.documentos_logic import analizador_documentos

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

print('> Waiting measurements. To exit press CTRL+C')

def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    print(payload)
    topic = method.routing_key.split('.')
    variable = analizador_documentos(topic)
    print("Documento :%r" % (str(variable)))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()