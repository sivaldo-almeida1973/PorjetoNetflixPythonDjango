from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView , DetailView


# Create your views here.-----------------------------------
class Homepage(TemplateView):
    template_name = "homepage.html"

class Homefilmes(ListView):#vai exibir lista de filmes do banco dados
    template_name = "homefilmes.html"
    model = Filme
    # object_list ->lista de itens do modelo

#classe que vai mostrar os detalhes dos filmes
class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # objec -> 1 item do nosso modelo

#funcao que faz a contagem de acessos
    def get(self,request, *args, **kwargs):
        #descobrir qual filme ele esta acessando
        filme = self.get_object()
        #somar +1 nas visualizacoes daquele filme
        filme.visualizacoes += 1
        #salvar
        filme.save()
        return super(Detalhesfilme, self).get(request, *args, **kwargs)#redireciona o usuario para a URL final


    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        #filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a do filme da página(object)
        # self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return  context

#pagina construida dentro de filme/templates
class Pesquisafilme(ListView):
    template_name = "pesquisa.html"
    model = Filme

#def homepage(request):     #template
#  return render(request, "homepage.html")


# url - view - html
#def homefilmes(request): #funcao homefilmes---------------------
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request, "homefilmes.html", context)
