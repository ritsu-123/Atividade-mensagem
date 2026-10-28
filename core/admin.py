from django.contrib import admin
from .models import Projeto, Tarefa, Categoria, Tag, Noticia

# Register your models here.

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio')
    search_fields = ('nome',)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridade', 'concluido', 'projeto')
    list_filter = ('prioridade', 'concluido', 'projeto')
    search_fields = ('titulo',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "criada_em")
    list_filter = ("categoria", "tags")
    search_fields = ("titulo", "conteudo")
