# Curso Básico de Django
En este primer curso de la saga de Django analizarás los conceptos iniciales para desarrollar el backend de tu aplicación web con este framework. Aprenderás sobre la estructura de un proyecto, sus archivos más importantes y cómo desarrollar en cada uno, de la mano de tu profesor Facundo García Martoni.

- Dar los primeros pasos en el desarrollo backend con Python
- Crear, desde cero, tu primer aplicación web
- Aprender a estructurar un proyecto en este framework
- Conocer a Django y ubicarlo en el ecosistema de Python

Lo que verás a continuación son mis notas del curso 🚀
Si ves algún error o punto a mejorar no dudes en hacer tu aporte 💚

## Starting

Instalar Django: \
`pip install django` \
Empezar un proyecto en Django: \
`django-admin startproject premiosplatziapp` \
\
Django crea distintos archivos:
- `manage.py` : Muestra los diferentes comando disponibles para hacer que el proyecto funcione.

- `_init_.py` : Indica que la carpeta es un paquete que contiene los archivos de la aplicación web.

- `asgi.py` / `wsgi.py` : Sirven para hacer el despliegue de la aplicación.

- `settings.py` : Contiene toda la información de la configuración del proyecto como el lenguaje, la zona horaria, las bases de datos, etc.

- `urls.py` : Donde se trbajan las direcciones con las que nos podemos mover a través del proyecto como la ruta admin o user.

## El servidor de desarrollo

Nunca se toca el código que está en producción, siempre se desarrolla en local y se hace deploy.
Django facilita el proceso brindando infraestructura para ver el proyecto sin necesidad de enviarlo al servidor.
Podemos correr el servidor:
```zsh
python3 manage.py runserver
```
La salida del anterior comando nos va a decir si hay errores o advertencias.
Se imprime la fecha, la versión de django, el archivo de configuraciones que se está usando, la dirección donde está corriendo el server (será localhost), por último una instrucción para poder cerrar el server (ctrl+c).

Tendremos una salida de este estilo:


# Helpful tips

## Crear un entorno virtual

```zsh
python3 -m venv venv
source ./venv/bin/activate
```



## Crear carpetas anidadas

```zsh
mkdir -p CarpetaGeneral/{carpeta1,carpeta2/{subdirectorio1,subdirectorio2},carpeta3,carpeta4}
```

# Helpful Links

- [.gitignore](https://www.toptal.com/developers/gitignore)

- [Django documentation](https://docs.djangoproject.com/en/3.2/)