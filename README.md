# djangoBasico
Curso Básico de Django de Platzi

# Starting

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