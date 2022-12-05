from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html",{
        "question": question
    } )


def results(request, question_id):
    return HttpResponse(f"Estás viendolos resultados de la pregunta número {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando por la pregunta número {question_id}")


