from django.shortcuts import render
from .models import Filme


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

#sempre que for criar uma view, estamos criando uma
# pagina nova para o site, entao temos que criar uma :
# url - view - html
def homefilmes(request):
    context = {}
    lista_filmes = Filme.objects.all()
    context['lista_filmes'] = lista_filmes
    return render(request, "homefilmes.html", context)

