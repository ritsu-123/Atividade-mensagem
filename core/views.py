from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from .models import Categoria, Tag, Noticia
from .forms import CategoriaForm, TagForm, NoticiaForm
# Create your views here.



def projeto_lista(request):
    projetos = Projeto.objects.all()

    return render(
        request,
        'core/projeto_lista.html',
        {'projetos': projetos}
    )


def projeto_criar(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('core:projeto_lista')
    else:
        form = ProjetoForm()

    return render(
        request,
        'core/projeto_form.html',
        {'form': form}
    )


def projeto_editar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('core:projeto_lista')

    else:
        form = ProjetoForm(instance=projeto)

    return render(
        request,
        'core/projeto_form.html',
        {
            'form': form,
            'projeto': projeto
        }
    )


def projeto_excluir(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('core:projeto_lista')

    return render(
        request,
        'core/projeto_confirmar_exclusao.html',
        {'projeto': projeto}
    )


def tarefa_lista(request):
    tarefas = Tarefa.objects.select_related('projeto').all().order_by('concluido', 'prioridade', 'titulo')

    return render(request, 'core/tarefa_lista.html',{'tarefas': tarefas})

def tarefa_criar(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('core:tarefa_lista')
    else:
        form = TarefaForm()

    return render(request, 'core/tarefa_form.html', {'form': form})


def tarefa_editar(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('core:tarefa_lista')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'core/tarefa_form.html', {'form': form, 'tarefa': tarefa})

def tarefa_excluir(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('core:tarefa_lista')

    return render(request, 'core/tarefa_confirmar_exclusao.html', {'tarefa': tarefa})
   



# Gerenciamento de categorias
def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(request, "core/categoria_lista.html", {"categorias": categorias})


def categoria_criar(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria cadastrada com sucesso!")
            return redirect("core:categoria_lista")
    else:
        form = CategoriaForm()
    return render(request, "core/categoria_form.html", {"form": form})


def categoria_editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria atualizada com sucesso!")
            return redirect("core:categoria_lista")
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, "core/categoria_form.html", {"form": form, "categoria": categoria})


def categoria_excluir(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        try:
            categoria.delete()
            messages.success(request, "Categoria excluída com sucesso!")
        except ProtectedError:
            messages.error(request, "Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.")
        return redirect("core:categoria_lista")
    return render(request, "core/categoria_confirmar_exclusao.html", {"categoria": categoria})


# Gerenciamento de tags
def tag_lista(request):
    tags = Tag.objects.all()
    return render(request, "core/tag_lista.html", {"tags": tags})


def tag_criar(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag cadastrada com sucesso!")
            return redirect("core:tag_lista")
    else:
        form = TagForm()
    return render(request, "core/tag_form.html", {"form": form})


def tag_editar(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag atualizada com sucesso!")
            return redirect("core:tag_lista")
    else:
        form = TagForm(instance=tag)
    return render(request, "core/tag_form.html", {"form": form, "tag": tag})


def tag_excluir(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        messages.success(request, "Tag excluída com sucesso!")
        return redirect("core:tag_lista")
    return render(request, "core/tag_confirmar_exclusao.html", {"tag": tag})


# Notícias para testar os relacionamentos entre categorias, tags e notícias.
def noticia_lista(request):
    noticias = Noticia.objects.select_related("categoria").prefetch_related("tags")
    return render(request, "core/noticia_lista.html", {"noticias": noticias})


def noticia_criar(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Notícia cadastrada com sucesso!")
            return redirect("core:noticia_lista")
    else:
        form = NoticiaForm()
    return render(request, "core/noticia_form.html", {"form": form})
