from django.contrib import admin
from .models import Categoria,Cliente,Filme,Locacao
admin.site.register(Locacao)
class locacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data']


admin.site.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome',]
admin.site.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome','email']
admin.site.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ['valor', 'titulo']
