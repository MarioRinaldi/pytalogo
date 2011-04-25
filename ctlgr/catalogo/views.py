from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from django.template import Context, loader
from ctlgr.catalogo.models import Livro, Filme


def index(request):
  latest_list_books = Livro.objects.all().order_by('name')[:5]
  template = loader.get_template('catalogo/index.html')
  context = Context({
 	'latest_list_books': latest_list_books,
  })
  return HttpResponse(template.render(context))
  
def livros(request):
  latest_list_books = Livro.objects.all().order_by('name')[:10]
  template = loader.get_template('catalogo/livros.html')
  if latest_list_books: 
    context = Context({'latest_list_books': latest_list_books,})
  else:
    context = Context({'error_message': "Nao existem livros cadastrados!!!",})
  return HttpResponse(template.render(context))

def searchLivro(request):
  if 'q' in request.GET:
    livro_name = request.GET['q'].capitalize()
    latest_list_books = get_list_or_404(Livro, name__contains=livro_name)
    context = Context({ 'latest_list_books': latest_list_books, })
  else:
    context = Context({'error_message': "para fazer uma pesquisa \
              voce deve informar um parametro!",})
  template = loader.get_template('catalogo/livroSearch.html')
  return HttpResponse(template.render(context))

def livros_show(request, livro_id):
  livro = get_object_or_404(Livro, pk=livro_id)
  context = {'livro': livro}
  return render_to_response('catalogo/livros_show.html', context)

    
def filmes(request):
  latest_list_movies = Filme.objects.all().order_by('name')[:10]
  template = loader.get_template('catalogo/filmes.html')
  if latest_list_movies: 
    context = Context({'latest_list_movies': latest_list_movies,})
  else:
    context = Context({'error_message': "Nao existem filmes cadastrados!!!",})
  return HttpResponse(template.render(context))

def searchFilme(request):
  if 'q' in request.GET:
    filme_name = request.GET['q'].capitalize()
    latest_list_movies = get_list_or_404(Filme, name__contains=filme_name)
    context = Context({'latest_list_movies': latest_list_movies,})
  else:
    context = Context({'error_message': "para fazer uma pesquisa \
              voce deve informar um parametro!",})
  template = loader.get_template('catalogo/filmeSearch.html')
  return HttpResponse(template.render(context))
    

def filmes_show(request, filme_id):
  filme = get_object_or_404(Filme, pk=filme_id)
  context = {'filme': filme}
  return render_to_response('catalogo/filmes.html', context)

