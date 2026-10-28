from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media')
    concluido = models.BooleanField(default=False)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="noticias"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="noticias")
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo
