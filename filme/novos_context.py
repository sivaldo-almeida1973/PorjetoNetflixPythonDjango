from .models import Filme

#lista de filmes recentes
def lista_filmes_recentes(request):
     lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]
     return {"lista_filmes_recentes": lista_filmes}

#lista de filmes em alta:
def lista_filmes_emalta(request):
      lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
      return {"lista_filmes_emalta": lista_filmes}


#vai ser exibido na homefilmes.html
#precisa riar um gerenciador de contexto dentro (settings/hashflix), para conectar a outras pagina
