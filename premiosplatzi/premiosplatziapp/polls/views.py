from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estás en la página principal de premios Platzi app")


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estás viendolos resultados de la pregunta número {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando por la pregunta número {question_id}")


