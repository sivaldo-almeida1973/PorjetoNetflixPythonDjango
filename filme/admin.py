from django.contrib import admin
#importar tabela usuarios e tabela episodios
from.models import Filme, Episodio

# Register your models here.(faz aparecer o admin)
admin.site.register(Filme)
admin.site.register(Episodio)
