from django.contrib import admin
from.models import Filme, Episodio, Usuario
#importar tabela usuarios e tabela episodios
from django.contrib.auth.admin import UserAdmin
#gerencia usuarios

#só existe porque quero que no admin apareça o campo personalizado filmes_vistoss
campos = list(UserAdmin.fieldsets)
campos.append(
     ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)



# Register your models here.(faz aparecer o admin)
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)


