from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView , DetailView


# Create your views here.-----------------------------------
#def homepage(request):     #template
#  return render(request, "homepage.html")

#essa classe substitui a função acima------------------------------
class Homepage(TemplateView):
    template_name = "homepage.html"



#sempre que for criar uma view, estamos criando uma
# pagina nova para o site, entao temos que criar uma :
# url - view - html
#def homefilmes(request): #funcao homefilmes---------------------
  #  context = {}
 #   lista_filmes = Filme.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request, "homefilmes.html", context)

class Homefilmes(ListView):#vai exibir lista de filmes do banco dados
    template_name = "homefilmes.html"
    model = Filme
    # object_list ->lista de itens do modelo

#classe que vai mostrar os detalhes dos filmes
class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # objec -> 1 item do nosso modelo
