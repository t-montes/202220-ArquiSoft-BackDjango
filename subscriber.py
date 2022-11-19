import json
import pika
from time import sleep
from sys import path
from os import environ
import django
from faker import Faker
import ast
import io
from PIL import Image
from io import BytesIO
from random import choice, randint

f = Faker()
rabbit_host = '10.128.0.12'
rabbit_user = 'avanzo_user'
rabbit_password = 'avanzo'
exchange = 'analizando_documentos'
topic = 'DocumentosTopic'

path.append('avanzo/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'avanzo.settings')
django.setup()

# from cedulas.logic.cedulas_logic import create_cedula_object
# from certificaciones_bancarias.logic.certificaciones_bancarias_logic import create_certificacion_bancaria_object
# from certificaciones_laborales.logic.certificaciones_laborales_logic import create_certificacion_laboral_object
# from comprobantes_de_pago.logic.comprobantes_de_pago_logic import create_comprobante_de_pago_object
# from nominas.logic.nominas_logic import create_nomina_object

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(
    exchange=exchange, queue=queue_name, routing_key=topic)

print('> Waiting measurements. To exit press CTRL+C')

def callback(ch, method, properties, body):
    payload = body
    image = io.BytesIO(body)
    make_post(image,"1","1","1")

    # print(f'> Received: {body}')
    payload['nombre'] = payload['nombre'].lower()
    if payload['nombre'] not in ['cedula', 'certificacion_bancaria', 'certificacion_laboral', 'comprobante_de_pago', 'nomina']:
        print(f'Tipo de documento {payload["nombre"]} no soportado')
        
    else:
        datos = analizar_documento(payload) # toda la magia del OCR
        # if payload['nombre'] == 'cedula':
        #     print(f'> Saving cedula 1: {datos}')
        #     create_cedula_object(*datos)
        # elif payload['nombre'] == 'certificacion_bancaria':
        #     create_certificacion_bancaria_object(*datos)
        # elif payload['nombre'] == 'certificacion_laboral':
        #     create_certificacion_laboral_object(*datos)
        # elif payload['nombre'] == 'comprobante_de_pago':
        #     create_comprobante_de_pago_object(*datos)
        # elif payload['nombre'] == 'nomina':
        #     create_nomina_object(*datos)
        # else:
        #     print(f'> Tipo de documento no reconocido: {payload["nombre"]}')

def make_post(imagen, nombre, num_documento,path_image):
    import requests
    url = 'http://34.172.157.154:8000/create/'
    data = {'nombre': '1',
            'num_documento': '1',
            'path_image': '1',
            'imagen': imagen}

    files ={'imagen': imagen}
    requests.post(url, data=files,files = files)

    
def analizar_documento(payload):
    # simular analisis de documento
    
    sleep(randint(5,10))
    # fake data for each type
    if payload['nombre'] == 'cedula':
        return [f.administrative_unit(), f.date(), f.date(), f.iana_id(), f.name()]
    elif payload['nombre'] == 'certificacion_bancaria':
        return [f.iana_id(), f.word(), choice(['Activa', 'Inactiva']), f.date(), f.name(), f.company(), f.iana_id(), f.company() + " Bank"]
    elif payload['nombre'] == 'certificacion_laboral':
        return [f.word(), 100+randint(0,100), f.company(), f.administrative_unit(), f.iana_id(), f.name()]
    elif payload['nombre'] == 'comprobante_de_pago':
        return [f.iana_id(), f.text(), f.iana_id(), f.iana_id(), 200+randint(0,200), f.iana_id(), f.iana_id(), f.name()]
    elif payload['nombre'] == 'nomina':
        return [f.date(), f.iana_id(), f.name()]


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
