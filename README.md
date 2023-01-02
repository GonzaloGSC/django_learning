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
