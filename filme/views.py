from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView


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
    # object_list


