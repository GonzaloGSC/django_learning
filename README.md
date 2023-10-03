# <span style="color: #F5FF30; font-weight: bold;">Django Learning</span>
Repositorio enfocado a almacenar el conocimiento adquirido durante diversos cursos de Django.

Django es un framework de aplicaciones web de código abierto escrito en Python que se utiliza para el desarrollo rápido y eficiente de aplicaciones web. Fue creado en 2003 por Adrian Holovaty y Simon Willison, dos programadores de Python que querían crear un marco que les permitiera desarrollar aplicaciones web de manera rápida y sencilla.

Desde su creación, Django se ha convertido en uno de los frameworks de aplicaciones web más populares y ampliamente utilizados. Se caracteriza por su enfoque en la reutilización de componentes y en la separación del modelo, la vista y el controlador, lo que facilita el mantenimiento y el desarrollo de aplicaciones web.

En la actualidad, Django se utiliza en una amplia variedad de proyectos, desde pequeños sitios web hasta aplicaciones empresariales y plataformas en línea. Ha sido adoptado por una gran cantidad de empresas y organizaciones y es una de las opciones más populares entre los desarrolladores de Python para el desarrollo de aplicaciones web.
# <span style="color: #F5FF30; font-weight: bold;">Índice</span>
- [Django Learning](#django-learning)
- [Índice](#índice)
- [Utiles](#utiles)
  - [Virtualenv](#virtualenv)
    - [Crear](#crear)
    - [Activar](#activar)
    - [Desactivar](#desactivar)
  - [Instalaciones y librerías](#instalaciones-y-librerías)
    - [djangorestframework](#djangorestframework)
    - [django-filter](#django-filter)
    - [django-cors-headers](#django-cors-headers)
    - [django-extensions](#django-extensions)
    - [djangorestframework-simplejwt](#djangorestframework-simplejwt)
    - [whitenoise](#whitenoise)
    - [requests](#requests)
  - [Django y manage.py](#django-y-managepy)
    - [Start a project](#start-a-project)
    - [Start an app](#start-an-app)
    - [Create superuser](#create-superuser)
    - [Migrations](#migrations)
    - [Collectstatic](#collectstatic)
    - [Runserver](#runserver)
  - [Lecturas complementarias y recursos](#lecturas-complementarias-y-recursos)
    - [Para termino de produccion](#para-termino-de-produccion)
  - [Cursos](#cursos)
    - [Básico](#básico)
    - [Intermedio](#intermedio)
    - [Avanzado](#avanzado)
- [Testing](#testing)
- [Deploy](#deploy)
# <span style="color: #F5FF30; font-weight: bold;">Utiles</span>
## <span style="color: #D0D929; font-weight: bold;">Virtualenv</span>
### <span style="color: #6E7316; font-weight: bold;">Crear</span>
Crear entorno virtual ([Fuente](https://www.roelpeters.be/virtualenv-venv-choose-python-version/)):
```
virtualenv -p="path_python_executable" <virtual_environment_directory> 
```
[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Activar</span>
Activar entorno virtual en Windows:
```
source env/Scripts/activate
```
Activar entorno virtual en Linux:
```
source env/bin/activate
```
[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Desactivar</span>
Desactivar entorno virtual:
```
deactivate
```
[Volver al Índice 🔝](#índice)
## <span style="color: #D0D929; font-weight: bold;">Instalaciones y librerías</span>
Las librerías básicas y más utilizadas en un proyecto Django son las siguientes:
```
pip install django
pip install djangorestframework
pip install django-filter
pip install django-cors-headers
pip install django-extensions
pip install djangorestframework-simplejwt
pip install whitenoise
pip install requests
```
Para registrar las dependencias del proyecto, se utiliza el siguiente comando:
```
pip freeze > requirements.txt
```
Para instalar las dependencias del proyecto, se utiliza el siguiente comando:
```
pip install -r requirements.txt
```
Installed apps en settings.py:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'django_extensions',
]
```
[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">djangorestframework</span>
Django REST framework es una librería de Python que se utiliza para crear APIs (Application Programming Interfaces, o Interfaces de Programación de Aplicaciones) en aplicaciones web desarrolladas con Django. Una API es un conjunto de funcionalidades que se exponen a través de una interfaz de programación y que permiten que otras aplicaciones puedan interactuar con ellas de forma automatizada.

Django REST framework proporciona un conjunto de herramientas y características que facilitan la creación de APIs en Django. Algunas de estas características incluyen:

- Serialización de objetos de Django a formato JSON y viceversa.
- Soporte para autenticación y permisos.
- Integración con el sistema de plantillas de Django para la generación de respuestas en formato HTML.
- Soporte para la creación de documentación automatizada de la API

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">django-filter</span>
Django-filter es una librería de Python que se utiliza para filtrar consultas de bases de datos en aplicaciones web desarrolladas con Django. Se utiliza para crear formularios de búsqueda que permiten a los usuarios especificar diferentes criterios de búsqueda y recibir resultados que cumplen con esos criterios.

Por ejemplo, si tenemos una base de datos de libros y queremos permitir a los usuarios buscar libros por título, autor o año de publicación, podemos utilizar Django-filter para crear un formulario de búsqueda que permita a los usuarios especificar estos criterios de búsqueda y recibir resultados que cumplan con ellos.

Django-filter se integra con el sistema de consultas de Django y proporciona una forma sencilla de filtrar resultados sin tener que escribir código SQL manualmente.

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">django-cors-headers</span>
Django-cors-headers es una librería de Python que se utiliza para habilitar el uso de cabeceras CORS (Cross-Origin Resource Sharing, o Compartición de Recursos de Origen Cruzado) en aplicaciones web desarrolladas con Django.

Las cabeceras CORS son un conjunto de cabeceras HTTP que permiten que una aplicación web en un origen diferente al de una página web acceda a los recursos de esa página web. Por ejemplo, si tenemos una aplicación web en example.com que quiere acceder a los recursos de otra aplicación web en api.example.com, podemos utilizar cabeceras CORS para permitir que la aplicación de example.com acceda a los recursos de api.example.com.

Django-cors-headers se utiliza para habilitar el uso de cabeceras CORS en aplicaciones Django y permite configurar de forma sencilla qué aplicaciones pueden acceder a los recursos de nuestra aplicación.

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">django-extensions</span>
Django-extensions es una librería de Python que proporciona un conjunto de herramientas y extensiones para aplicaciones web desarrolladas con Django. Algunas de las características que proporciona esta librería son:

Un conjunto de scripts para el manejo de la base de datos, como la creación de diagramas de modelos o la generación de datos aleatorios.
Una extensión para el sistema de plantillas de Django que permite el uso de código Python directamente en las plantillas.
Una extensión para el panel de administración de Django que permite ver el tiempo de ejecución de las consultas realizadas a la base de datos.
Una extensión para el sistema de URLs de Django que permite ver las URLs de la aplicación en un formato gráfico.
En resumen, Django-extensions es una librería de Python que proporciona un conjunto de herramientas y extensiones para aplicaciones web desarrolladas con Django y que facilita tareas como el manejo de la base de datos, el uso de código Python en las plantillas o la visualización de las URLs de la aplicación.

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">djangorestframework-simplejwt</span>
Django REST framework-simplejwt es una librería de Python que proporciona un conjunto de herramientas para la autenticación y autorización de usuarios en aplicaciones web que utilizan Django REST framework. Esta librería proporciona una implementación de los tokens JWT (JSON Web Token, o Token Web JSON) para la autenticación y autorización de usuarios.

Los tokens JWT son una forma de transmitir información de forma segura entre diferentes sistemas. Se utilizan comúnmente en aplicaciones web para permitir que una aplicación de un origen confiable autentique a un usuario y le proporcione acceso a recursos protegidos sin necesidad de enviar la contraseña del usuario a través de la red.

Django REST framework-simplejwt proporciona una implementación fácil de usar de los tokens JWT para la autenticación y autorización de usuarios en aplicaciones web que utilizan Django REST framework.

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">whitenoise</span>
WhiteNoise es una librería de Python que se utiliza para servir archivos estáticos en aplicaciones web desarrolladas con Django. Los archivos estáticos son aquellos que se utilizan para dar estilo y diseño a una aplicación web, como imágenes, hojas de estilo CSS y archivos JavaScript.

WhiteNoise se utiliza para simplificar el proceso de servir estos archivos estáticos en Django. De forma predeterminada, Django utiliza un servidor de archivos estáticos separado para servir estos archivos, pero WhiteNoise permite que se integren en la misma aplicación web, lo que puede simplificar la configuración y el despliegue de la aplicación.

WhiteNoise Documentación: [Link](http://whitenoise.evans.io/en/stable/).

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">requests</span>
Requests es una librería de Python que se utiliza para enviar peticiones HTTP a servidores web. Con esta librería podemos realizar diferentes tipos de peticiones HTTP, como GET, POST, PUT, DELETE, entre otras, y procesar las respuestas que recibimos del servidor.

Requests proporciona una interfaz sencilla y fácil de usar para enviar peticiones HTTP y procesar las respuestas, y se utiliza comúnmente en aplicaciones web y scripts de Python para interactuar con servicios web y APIs.

[Volver al Índice 🔝](#índice)
## <span style="color: #D0D929; font-weight: bold;">Django y manage.py</span>
manage.py es un archivo que se encuentra en la raíz de un proyecto Django y que proporciona una serie de comandos para administrar la aplicación. Algunos de los comandos más comunes que se pueden realizar con este archivo son:

1) Crear una nueva aplicación dentro del proyecto: python manage.py startapp nombre_de_la_aplicación
2) Crear una nueva base de datos para el proyecto: python manage.py migrate
3) Crear un superusuario para el panel de administración: python manage.py createsuperuser
4) Iniciar el servidor de desarrollo: python manage.py runserver
5) Ver los comandos disponibles: python manage.py help
6) Ejecutar pruebas para una aplicación específica: python manage.py test nombre_de_la_aplicación
7) Ejecutar pruebas para todas las aplicaciones del proyecto: python manage.py test
8) Ver los modelos del proyecto en formato de diagrama: python manage.py graph_models
9) Generar datos aleatorios para los modelos del proyecto: python manage.py generate_fake_data
10) Ver el contenido de una base de datos en formato SQL: python manage.py sqlmigrate nombre_de_la_aplicación número_de_la_migración
11) Ver los cambios que se han realizado en las migraciones: python manage.py sqlmigrate nombre_de_la_aplicación número_de_la_migración --backwards

En resumen, manage.py es un archivo que proporciona una serie de comandos para administrar la aplicación Django y que se utiliza comúnmente para tareas como ejecutar pruebas, ver el contenido de la base de datos o generar datos aleatorios.

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Start a project</span>
Crear proyecto django:
```
django-admin startproject nombre_proyecto
```
[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Start an app</span>
Crear apps:
```
python manage.py startapp nombre_app
```
[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Create superuser</span>
Crear un superuser:
```
python manage.py createsuperuser
```
[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Migrations</span>
Crea la migración de cambios en los modelos y bdd:
```
python manage.py makemigrations
```
Realizar migración de cambios a los modelos y bdd:
```
python manage.py migrate
```
[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Collectstatic</span>
Colecta todos los archivos estaticos en la carpeta configurada en STATIC_ROOT:
```
python manage.py collectstatic
```
[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Runserver</span>
Correr servidor de proyecto django:
```
python manage.py runserver
```
[Volver al Índice 🔝](#índice)
## <span style="color: #D0D929; font-weight: bold;">Lecturas complementarias y recursos</span>
- Documentacion sobre administracion de archivos django: [Link](https://docs.djangoproject.com/en/3.1/topics/files/).
- Documentacion de generic-views: [Link](https://www.django-rest-framework.org/api-guide/generic-views/).
- Codigos de estado HTTP: [Link](https://www.django-rest-framework.org/api-guide/status-codes/).
- Autenticación y autorización basadas en roles con DjangoRestFramework y SimpleJWT: [Link](https://medium.com/python-in-plain-english/role-based-authentication-and-authorization-with-djangorestframework-and-simplejwt-d9614d79995c). Tiene errores que fueron corregidos en este proyecto: [Proyecto](https://github.com/GonzaloGSC/escuelasespeciales_backend/tree/main/src/apps/api).
- Cómo extraer la parte del nombre de host de una URL en JavaScript: [Link](https://stackoverflow.com/questions/1368264/how-to-extract-the-hostname-portion-of-a-url-in-javascript).
- Eliminacion de tildes, Ñs, Üs y demas similares: [Link](https://es.stackoverflow.com/questions/135707/c%C3%B3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l).
- Ejecucion continua de aplicacion django: [Link](https://medium.com/@kevin.michael.horan/scheduling-tasks-in-django-with-the-advanced-python-scheduler-663f17e868e6).

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Para termino de produccion</span> 
- ¿Cómo deshabilitar la interfaz navegable de estilo administrador de django-rest-framework?: [Link](https://stackoverflow.com/questions/11898065/how-to-disable-admin-style-browsable-interface-of-django-rest-framework).
- Tutorial de Django Parte 11: Desplegando Django a producción: [Link](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Deployment).
- ¿Por qué la configuración DEBUG=False hace que mi acceso a archivos estáticos de django falle?: [Link](https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail).
- How to run Django on cpanel (video): [Link](https://www.youtube.com/watch?v=EZSvsgemDJ0).
- WhiteNoise Documentación: [Link](http://whitenoise.evans.io/en/stable/).

[Volver al Índice 🔝](#índice)
## <span style="color: #D0D929; font-weight: bold;">Cursos</span>
### <span style="color: #6E7316; font-weight: bold;">Básico</span>
- Para dominar django, primero debes saber estos temas: [Link](https://www.youtube.com/watch?v=jjFRruzS4Yw).
- Conceptos básicos en Django 3 con Python 3: MVC y MTV 🐍: [Link](https://www.youtube.com/watch?v=c2hvf3TfplM).
- 🚀 Curso DJANGO paso a paso para PRINCIPIANTES: [Link](https://www.youtube.com/playlist?list=PL8ZnVqiE4oiY6fh6_vvNKwkxfutf3CiMY).
- Desarrollo Web con Django | Curso Completo: [Link](https://www.youtube.com/playlist?list=PLFRKQL-FSrHJuoNJdVd554Hg9awJw9w9P).

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Intermedio</span>
- Curso Django [Link](https://www.youtube.com/playlist?list=PLpOqH6AE0tNgL7Jg9Kx4SdfA5_oK6292j).
- Curso de Python con Django de 0 a Máster | Español [Link](https://www.youtube.com/playlist?list=PLxm9hnvxnn-j5ZDOgQS63UIBxQytPdCG7).

[Volver al Índice 🔝](#índice)
### <span style="color: #6E7316; font-weight: bold;">Avanzado</span>
- Django Tutorials: [Link](https://www.youtube.com/playlist?list=PLxm9hnvxnn-j5ZDOgQS63UIBxQytPdCG7).
- Curso de Python con Django Avanzado | Español: [Link](https://www.youtube.com/playlist?list=PLxm9hnvxnn-gvB0h0sEWjAf74ge4tkTOO).

[Volver al Índice 🔝](#índice)
# <span style="color: #F5FF30; font-weight: bold;">Testing</span>
[Volver al Índice 🔝](#índice)
# <span style="color: #F5FF30; font-weight: bold;">Deploy</span>

Utilizar idealmente AWS EC2 para crear maquina Ubuntu.

Comandos de preparación maquina:
```
sudo apt-get update
sudo apt-get install git python3.10 python3-pip virtualenv libpq-dev postgresql postgresql-contrib nginx net-tools -y
```
Comandos para preparación de BDD postgresql:
```
sudo su postgres
psql
CREATE DATABASE db_name;
CREATE USER user_name WITH PASSWORD 'password'; 
ALTER USER user_name WITH PASSWORD 'password';
ALTER ROLE user_name SET client_encoding TO 'utf8';
ALTER ROLE user_name SET default_transaction_isolation TO 'read committed';
ALTER ROLE user_name SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;
\q
exit
```
Comandos para proyecto:
```
git clone https://GonzaloGSC:TOKEN@github.com/GonzaloGSC/bet_detector_api.git
cd path/to/bet_detector_api
virtualenv env
source env/bin/activate
pip install -r requirements_prod.txt
```
Siguientes pasos:

- Colocar .env en carpeta backend o core del proyecto.
- Editar .env añadiendo la public_ip en ALLOWED_HOSTS.
- python manage.py migrate
- python manage.py collectstatic
- python manage.py runserver 0.0.0.0:8000  (ver con http://public_ip:8000/)
- press CTRL + C to stop testing.
- gunicorn --bind 0.0.0.0:8000 myproject.wsgi
- press CTRL + C to stop testing.

Comandos para gunicorn:

- sudo gpasswd -a nombreUsuario nombreGrupo (añadir usuario linux al grupo www-data, https://www.zeppelinux.es/como-agregar-un-usuario-a-un-grupo-en-linux/)
- sudo nano /etc/systemd/system/gunicorn.socket
  
Archivo gunicorn.socket:
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
- sudo nano /etc/systemd/system/gunicorn.service

Archivo gunicorn.service:
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=nombreUsuario
Group=www-data
WorkingDirectory=/home/ubuntu/carpeta_proyecto
EnvironmentFile=/home/ubuntu/carpeta_proyecto/backend/.env
ExecStart=/home/ubuntu/carpeta_proyecto/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          carpeta_proyecto_wsgi.wsgi:application

[Install]
WantedBy=multi-user.target
```
Cambiar propetario de archivos creados con chown USER:GROUP FILE:
```
chown ubuntu:www-data /etc/systemd/system/gunicorn.service
chown ubuntu:www-data /etc/systemd/system/gunicorn.socket
chown ubuntu:www-data -R /home/ubuntu/bet_detector_api/
```
Ahora puede iniciar y habilitar el zócalo Gunicorn. Esto creará el archivo de socket ahora /run/gunicorn.socky en el arranque. 
Cuando se realiza una conexión a ese socket, systemd iniciará automáticamente gunicorn.servicepara manejarlo:
```
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```
Verifique el estado del proceso para saber si se pudo iniciar:
```
sudo systemctl status gunicorn.socket
```
A continuación, verifique la existencia del gunicorn.sockarchivo dentro del /rundirectorio:
```
file /run/gunicorn.sock
```
Output
/run/gunicorn.sock: socket

Para probar el mecanismo de activación del socket, puede enviar una conexión al socket curlescribiendo:
```
curl --unix-socket /run/gunicorn.sock localhost
```
En caso de errores, vea las siguientes opciones: 
```
sudo journalctl -u gunicorn.socket
sudo journalctl -u gunicorn.service -b -e -n 50
sudo tail -f /var/log/gunicorn/access.log
```
Revise su /etc/systemd/system/gunicorn.service archivo en busca de problemas. 
Si realiza cambios en el /etc/systemd/system/gunicorn.servicearchivo, vuelva a cargar el demonio 
para volver a leer la definición del servicio y reinicie el proceso de Gunicorn escribiendo:
```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```
Comandos para Nginx:

Comience por crear y abrir un nuevo bloque de servidor en el sites-available directorio de Nginx:
```
sudo nano /etc/nginx/sites-available/nombre_archivo
```
Archivo bloque de servidor:
```
server {
    listen 80;
    listen [::]:80;
    server_name 15.228.235.226;

    location /favicon.ico {
        access_log off;
        log_not_found off;
    }

    location /static {
        alias /var/www/html/;
    }

    location /media {
        alias /home/ubuntu/carpeta_proyecto/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
        proxy_redirect off;
        add_header P3P 'CP="ALL DSP COR PSAa OUR NOR ONL UNI COM NAV"';
        add_header Access-Control-Allow-Origin *;
    }
}
```
Editar archivo proxy_params:
```
sudo nano /etc/nginx/proxy_params
```
Archivo proxy_params:
```
proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $server_name;
```
Ahora, puede habilitar el archivo vinculándolo al sites-enableddirectorio:
```
sudo ln -s /etc/nginx/sites-available/nombre_archivo /etc/nginx/sites-enabled
```
Pruebe su configuración de Nginx en busca de errores de sintaxis escribiendo:
```
sudo nginx -t
```
Si existen errores:
```
sudo tail -F /var/log/nginx/error.log
```
Si no se informan errores, continúe y reinicie Nginx escribiendo:
```
sudo systemctl restart nginx
```
Finalmente, debe abrir su firewall al tráfico normal en el puerto 80. Dado que ya no necesita acceso al servidor de desarrollo, también puede eliminar la regla para abrir el puerto 8000:
```
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
```
Ahora debería poder ir al dominio o dirección IP de su servidor para ver su aplicación.

Comados para full reset:
```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart gunicorn.socket gunicorn.service
sudo nginx -t && sudo systemctl restart nginx
```

Fuente: [Link](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04)

[Volver al Índice 🔝](#índice)
