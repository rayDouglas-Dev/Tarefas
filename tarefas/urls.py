from django.urls import path
from .views import deletar_view, editar_view, tarefas_view, adicionar_view

app_name = 'tarefas'

urlpatterns = [
    path('', tarefas_view, name='tarefas'),
    path('adicionar/', adicionar_view, name='adicionar'),
    path('deletar/<int:tarefa_id>/', deletar_view, name='deletar'),
    path('editar/<int:tarefa_id>/', editar_view, name='editar'),

]