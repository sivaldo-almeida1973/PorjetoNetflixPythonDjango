from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#importar tabela usuarios e tabela episodios
from.models import Filme, Episodio, Usuario

# Register your models here.(faz aparecer o admin)
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
