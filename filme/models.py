from django.db import models
from django.utils import timezone

# Create your models here.

#tupla com tupla dentro=(categoria)
LISTA_CATEGORIAS = (
#inform q vai armazenar o banco dados - inform q vai aparecer para o usuario
    ("ANALISES","Análises"),
    ("PROGRAMACAO","Programação"),
    ("APRESENTACAO","Apresentação"),
    ("OUTROS","Outros"),
)

#criar tabela o filme no banco dados

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')#(thumb guarda imagem)
    descricao = models.TextField(max_length= 1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):#funcao que faz aparecer o titulo do filme
        return self.titulo



#criar episodios

#criar usuário
