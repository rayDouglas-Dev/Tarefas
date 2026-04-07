from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
from django.http import HttpResponse


# Create your views here.

def tarefas_view(request):
    contexto = {
        "nome":"Ray",
        "tarefas":TarefaModel.objects.all()
    }
    return render(request, 'home.html', contexto)

def adicionar_view(request):
    if request.method == 'POST':
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:tarefas')
    contexto = {
        "form": TarefaForm()
    }
    return render(request, 'adicionar.html', context=contexto)

def editar_view(request, tarefa_id):

    tarefa = get_object_or_404(TarefaModel, id=tarefa_id)
    
    if request.method == 'POST':
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:tarefas')
    formulario = TarefaForm(instance=tarefa)
    contexto = {
        "form": formulario
    }
    return render(request, 'editar.html', contexto)


def deletar_view(request, tarefa_id):
    tarefa = get_object_or_404(TarefaModel, id=tarefa_id) 
    tarefa.delete()
    return redirect('tarefas:tarefas')