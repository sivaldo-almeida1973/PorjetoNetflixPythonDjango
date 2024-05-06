from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
#vai permitir criar os usuarios

# Create your models here.

#tupla com tupla dentro=(categoria)
LISTA_CATEGORIAS = (
#inform q vai armazenar no banco dados - inform q vai aparecer para o usuario
    ("ANALISES","Análises"),
    ("PROGRAMACAO","Programação"),
    ("APRESENTACAO","Apresentação"),
    ("OUTROS","Outros"),
)

#criar tabela o filme no banco dados(tabela)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')#(thumb guarda imagem)
    descricao = models.TextField(max_length= 1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):#faz aparecer o titulo do filme NO ADMIN
        return self.titulo

#um filme pode ter varios episodios
#um episodio poder ter apenas 1 filme

#criar episodios(tebela)---------------------------
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    def __str__(self):#faz aparecer o titulo do EPISODIO NO ADMIN
        return self.filme.titulo + "/ " + self.titulo

#criar classe usuário-----------------------------
class Usuario(AbstractUser): #relacao muitos pra muitos-
    filmes_vistos = models.ManyToManyField("Filme")
    #filmes_vistos sao itens da classe Filme

#sempre que criar uma nova classe , adicionar no admin.py
