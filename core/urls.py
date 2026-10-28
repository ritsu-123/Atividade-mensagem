from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("projetos/", views.projeto_lista, name="projeto_lista"),
    path("", views.projeto_lista, name="projeto_lista"),
    path("projetos/novo/", views.projeto_criar, name="projeto_criar"),
    path("projetos/<int:pk>/editar/", views.projeto_editar, name="projeto_editar"),
    path("projetos/<int:pk>/excluir/", views.projeto_excluir, name="projeto_excluir"),
    path("tarefas/", views.tarefa_lista, name="tarefa_lista"),
    path("tarefas/nova/", views.tarefa_criar, name="tarefa_criar"),
    path("tarefas/<int:pk>/editar/", views.tarefa_editar, name="tarefa_editar"),
    path("tarefas/<int:pk>/excluir/", views.tarefa_excluir, name="tarefa_excluir"),
    path("categorias/", views.categoria_lista, name="categoria_lista"),
    path("categorias/nova/", views.categoria_criar, name="categoria_criar"),
    path("categorias/<int:pk>/editar/", views.categoria_editar, name="categoria_editar"),
    path("categorias/<int:pk>/excluir/", views.categoria_excluir, name="categoria_excluir"),
    path("tags/", views.tag_lista, name="tag_lista"),
    path("tags/nova/", views.tag_criar, name="tag_criar"),
    path("tags/<int:pk>/editar/", views.tag_editar, name="tag_editar"),
    path("tags/<int:pk>/excluir/", views.tag_excluir, name="tag_excluir"),
    path("noticias/", views.noticia_lista, name="noticia_lista"),
    path("noticias/nova/", views.noticia_criar, name="noticia_criar"),
]