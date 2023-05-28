from django.shortcuts import render
from .models import Cliente, Filme, Locacao

def index(request):
    nomes = Cliente.objects.all()
    titulos_filmes = Filme.objects.all() 
    Context = {'nomes' : nomes, 'titulos' : titulos_filmes}
    return render(request, 'index.html',Context)

def locacaourl(request):
    lugares = Locacao.objects.all()
    
    Context2 = {'lugar' : lugares}
    return render(request, 'locacao.html',Context2)

def filmes_url(request): 
    context = {'filme' : Filme.objects.all() }
    return render(request, 'filmes.html', context)