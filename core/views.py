from django.http import HttpResponse
from django.shortcuts import render
from tarefas.models import TarefaModel

def index_view(request):
    contexto = {
        "nome": "Ray",
        "tarefas": TarefaModel.objects.all()
    }
    return render(request, 'home.html', contexto)