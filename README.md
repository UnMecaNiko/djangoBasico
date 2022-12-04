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

![image](https://user-images.githubusercontent.com/86577488/205124270-7f0923da-9ed2-4e95-aacc-3d404804c03d.png)

en el archivo de configuraciones, la variables `DEBUG` debe siempre estar en `True` cuando se trabaja en local

Un proyecto en Django es un conjunto de aplicaciones, una aplicación se refiere a un paquete donde se guardan los modelos, vistas y demás funcionalidades que estén estrechamente relacionadas.

## Premios Platzi App

Crear una aplicación "polls"
```zsh
python3 manage.py startapp polls
```

dentro de la carpeta principal "premiosplatziapp" hay dos carpetas "premiosplatziapp" y "polls"
El proyecto principal es contenedor de distintas aplicaciones, por lo que cada aplicación tiene su archivo `urls.py`.
El archivo que está contenido en la carpeta del proyecto principal tiene que incluir los archivos de las demás aplicaciones
Así:
*En el archivo `urls.py` de la carpeta del proyecto*
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/" ,include("polls.urls"))
]
```

La nueva aplicación creada *polls* debe ser agregada al archivo de configuración del proyecto:

**En el archivo *settings.py* de la carpeta del proyecto:**
```py
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Models

### ORM - Object Relational Mapping

Es la forma de replicar la estructura de una base de datos relacional con programación orientada a objetos.

>> Utilizando un ORM podemos operar sobre la base de datos aprovechando las características propias de la orientación a objetos, como herencia y polimorfismo.

Las bases de datos se conforman por tablas y cada tablas obtiene los datos relacionados a cada entidad, es posible convertir estas bases de datos en un archivo python que contiene la representación en programación orientada a objetos.

Las tablas corresponden a modelos (los cuales se expresan como clases), las columans van a corresponder a atributos de esas clases y los tipos de datos de cada columna correponderán a clases ligadas a los atributos de los objetos.

#### Ventajas 

- Facilidad y velocidad de uso
- Abstracción de la base de datos
- Seguridad de la capa de acceso a datos contra ataques.
- Reutilización. Nos permite utilizar los métodos de un objeto de datos desde distintas zonas de la aplicación, incluso desde aplicaciones distintas.
- Mantenimiento del código.

Siguiendo el siguiente diagrama:

![tablas_django_facundo-db4611e4-7fa6-4e3a-aeeb-e9d06ae65a23.png](https://static.platzi.com/media/user_upload/tablas_django_facundo-db4611e4-7fa6-4e3a-aeeb-e9d06ae65a23-97a81043-4060-402c-9668-38ef6b1bdc90.jpg)

Se van a crear las estructuras de datos para nuestra aplicación.

**En el archivo *models.py* de la carpeta polls:**

```py
# Create your models here.

# name´s models always singular
# cada vez que se haga un cambio se debe hacer migration
class Question(models.Model):

    # id - Django lo hace automáticamente
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Luego, en la consola (tenemos que tener el entorno virtual activo y estar ubicados en la carpeta padre)
```zsh
python3 manage.py makemigrations polls
python3 manage.py migrate
```
El concepto *migration* corresponde a cambiar la información o software desde un sistema a otro. En este caso transformamos los escrito en python a una base de datos relacional.

Se crea un archivo *0001_initial.py* en el que django describe toda la creación de las tablas en la base de datos, aquí es donde se hace uso del concepto ORM.

Django toma la programación que hicimos en el archivo *models.py* y lo convierte a tablas en la base de datos que estamos usando (en este caso sqlite3)

Cuando se agregan métodos a las clases no es necesario hacer migraciones.

## Interactive shell in django

Es de saber genera que con el comando `python3` podemos acceder a la consola de python, el problema es que esta vive en un entorno aislado, por lo que no podemos acceder a los archivos de nuestro proyecto. Para esta situación Django nos da una solución, interactive shell:
Para correr una shell en Django correcmos lo siguiente en la consola
```zsh
python3 manage.py shell
```
dentro de InteractiveConsole
```py
from polls.models import Choice,Question
```
podemos acceder a las distintas características de las tablas, como `Question.objects.all()`

Ahora, podemos probar agregando datos a mano, primero tenemos que traer un módulo adicional: `from django.utils import timezone` 

Podemos agregar una pregunta:
```py
q = Question(question_text="¿Cual es el mejor curso de platzi?", pub_date=timezone.now())
# y para guardar en la base de datos:
q.save()
```
Si volvemos a ejecutar `Question.objects.all()` podemos ver que ya no devuelve un objeto vacío

## El método __str__

En el archivo *models..py*:
```py
from django.db import models

# Create your models here.
# name´s models always singular
# cada vez que se haga un cambio se debe hacer migration

# python3 manage.py makemigrations polls
# python3 manage.py migrate
from django.db import models
from django.utils import timezone

class Question(models.Model):

    # id - Django lo hace automáticamente
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

Se sobreescriben los métodos *__str__* para mostrar la lista de preguntas y opciones de una forma más visual en consola cuando ejecutamos `Question.objects.all()`, además se agregán un método que nos permite saber si la pregunta se ha publicado recientemente.
Cuenado se agregan métodos no es necesario hacer migraciones, si hay un cambio de nombre o se agrega una nueva clase la migración es obligatoria.

### Filtrando los objetos creados desde la consola interactiva

Para traer un objeto en específicos de las clases ORM podemos usar `Question.object.get(pk=1)` (el comando get sólo devuelve un valor)

Para obtener múltiples respuestas podemos usar `Question.objects.filter(question_text__startswith="¿Cual")` este método devuelve un QuerySet
Otro ejemplo: `Question.objects.filter(pub_date__year=timezone.now().year)`

## Administrador de datos

para comenzar a usar el administrador se debe crear un usuario y contraseña:
`python3 manage.py createsuperuser`
Se debe tener mucho cuidado con la seguridad de estos datos, ya que si son expuestos pueden comprometer la aplicación completa.

Ahora, se deben hacer disponibles los modelos creados al administrador:
*En el archivo *admin.py* de la carpeta polls:*
```py
from .models import Question

admin.site.register(Question)
```

Usando la dirección http://127.0.0.1:8000/admin/ Se puede entrar al panel de administración.

## Views

### MTV | Model Template View

Siempre se crea un modelo que se muestra en un template que a su vez aparece en una vista (en este proyecto se tienen los modelos Question y Choice)

### Crear vistas

en el archivo `views.py` de mi aplicacion yo puedo crear distintas vistas como se ven a continuación:
```py
def index(request):
    return HttpResponse("Estás en la página principal de premios Platzi app")


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estás viendolos resultados de la pregunta número {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando por la pregunta número {question_id}")
```
Luego estas vistas son ligadas a una url, esto se programa en el archivo `urls.py`:
```py
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="index"),
    path("<int:question_id>/results/", views.results, name="index"),
    path("<int:question_id>/vote/", views.vote, name="index"),
]
```
Como las urls están configuradas desde una aplicación, siempre van a tener el nombre de la aplicación antes de cualquier url.
Nótese como "<>" se usa para enviar parámetros a las vistas, esto permite tener múltiples urls con respuestas únicas.

### Crear Templates

Generalmente el desarrollador backend se encargaría de crear las vistas y el desarrollador front de los templates, usando distintos frameworks distintos a Django. Para este curso vamos a crear ambos de una manera sencilla.

Ubicados en la carpeta de la aplicación ejecutamos en consola:
`mkdir -p templates/polls`
Para crear una carpeta donde vamos a crear las templates.
Ahora creamos un archivo html para comenzar a crear la página.
`touch templates/polls/index.html`





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

## Tener sugerencias de autocompletado html en archivos ligados a Django
(Para vsCode) 

Instala la extensión Django en tu editor.
Presiona F1 y escribe "settings.json", selecciona la opción open user settings. Al archivo Json debes agregar estas líneas.
```py
"emmet.includeLanguages": {
        "django-html": "html"
    }
```
Puedes reiniciar la extensión si no te sale aún el autocompletado.

# Helpful Links

- [.gitignore](https://www.toptal.com/developers/gitignore)

- [Basic writing and formatting syntax](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

- [Django documentation](https://docs.djangoproject.com/en/3.2/)

- [Writing your first Django app, part 1](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)

- [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

- [Making queries | Django documentation](https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro)

