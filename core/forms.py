from django import forms
from .models import Projeto
from django import forms
from .models import Projeto, Tarefa

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto

        fields = ['nome', 'descricao', 'data_inicio']

        widgets = { 'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome do projeto'
                }),

            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descrição do projeto',
                    'rows': 5
                }),

            'data_inicio': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
        }


class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa

        fields = [
            'titulo',
            'prioridade',
            'concluido',
            'projeto'
        ]

        labels = {
            'titulo': 'Título da tarefa',
            'prioridade': 'Prioridade',
            'concluido': 'Tarefa concluída',
            'projeto': 'Projeto',
        }

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Título da tarefa',
                    'maxlength': 200
                }
            ),

            'prioridade': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'concluido': forms.CheckboxInput(
                attrs={
                    'class': 'form-checkbox'
                }
            ),

            'projeto': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

from .models import Categoria, Tag, Noticia


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]
        labels = {"nome": "Nome da categoria"}
        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Digite o nome da categoria",
            })
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["nome"]
        labels = {"nome": "Nome da tag"}
        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Digite o nome da tag",
            })
        }


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "conteudo", "categoria", "tags"]
        labels = {
            "titulo": "Título",
            "conteudo": "Conteúdo",
            "categoria": "Categoria",
            "tags": "Tags",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "conteudo": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
