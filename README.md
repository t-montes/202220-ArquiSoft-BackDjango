# Proyecto_Uno
'NAME': 'avanzo'
'USER': 'metateoremas'
'PASSWORD': 'arquisoft2022'


# HTTPS 
Instrucciones para garantizar HTTPS en GCP con un proyecto DJANGO.

## Ingredientes

- NGINX con UWSGI
    ![alt text](https://tonyteaches.tech/wp-content/uploads/2020/10/nginx-uwsgi-django-stack-1536x128.png) 
    >**NGINX**: Nginx es un servidor web que también puede ser usado como proxy inverso, balanceador de carga. 
    Su principal función es lograr una conexión con el socket de unix para conectar con los puertos adecuados para qué la petición que se envía redireccione al puerto adecuado, él maneja también los certificados del dominio para lograr HTTPS.

    >**uWSGI**: Servidor de aplicaciones que se encarga de recibir las peticiones que recibe NGINX y ejecutarlas en el entorno virtual de python sobre el proyecto Django asociado, este módulo es capaz de resolver las consultas y escalar de ser necesario para resolverlas a todas, también se puede usar Gunicorn en su defecto y el código no cambia, es decir, se comporta de forma modular con cualquier otro servidor de aplicaciones de python.
- Entorno virtual de Python 
    > Se necesita un entorno virtual para que el manejo de dependencias de un proyecto DJANGO sea independiente y no se instalen directamente en la máquina sino en un entorno donde se tiene completo control sobre los módulos importados, estos a su vez son usados por uWSGI para decidir en qué ambiente tiene que ejecutar la petición HTTP/HTTPS.
- Ejecución en un entorno de producción
    > El gran problema que tienen los servidores de aplicaciones que tienen implementados Django y otras tecnologías de backend, es que corren en modo de prueba y por lo tanto no es posible monitorear ciertos comportamientos que se desean en una app desplegada propiamente, el entorno de producción hace posible que la aplicación corra en segundo plano con sus capacidades al 100 %, esto incluye manejo de peticiones HTTPS, para aplicaciones web Python el modelo usado es NGINX conectado a uWSGI para el manejo de entornos de producción.
    
# Instrucciones

Ubiquese en la carpeta del proyecto Django que contenga el archivo manage.py

## Crear un entorno virtual con Virtual env

```
sudo apt-get update 
sudo apt-get install  python3-venv
mkdir ~/entornos_virtuales/env_avanzo
python3 -m vEnv ~/entornos_virtuales/env_avanzo
source ~/entornos/blog/bin/activate
```
>Le llamaremos vEnv al entorno virtual python y lo guardaremos en una carpeta llamada env_avanzo sobre una carpeta que nos guardará todos los entornos.

## Instalar dependencias
 > NOTA: asegurese de que el entorno virtual de python esté activo antes de incializar este proceso.



