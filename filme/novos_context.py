from .models import Filme

#lista de filmes recentes
def lista_filmes_recentes(request):
     lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]  #regula a qtde de filmes na secao filmes recentes
     if lista_filmes:
       filme_destaque = lista_filmes[0]
     else:
       filme_destaque = None
     return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}

#lista de filmes em alta:
def lista_filmes_emalta(request):
      lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8] #regula a qtde de filmes na secao filmes em alta
      return {"lista_filmes_emalta": lista_filmes}
#vai ser exibido na homefilmes.html
#criar um gerenc contexto (hashflix/settings/templates/context_proc), para conectar a outras pagina



#def filme_destaque(request):
   # lista_filmes = Filme.objects.order_by('-data_criacao')[0]
  #  return {"filme_destaque": lista_filmes, "filme_destaque": filme_destaque}
#vai ser exibido na homefilmes.html
#criar um gerenc contexto (hashflix/settings/templates/context_proc), para conectar a outras pagina
