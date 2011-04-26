from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from django.template import Context, loader
from ctlgr.catalogo.models import Book, Movie


def index(request):
    latest_list_books = Book.objects.all().order_by('name')[:5]
    template = loader.get_template('catalogo/index.html')
    context = Context({
        'latest_list_books': latest_list_books,
    })
    return HttpResponse(template.render(context))
  
def list(request, templateName=None, type=None):
    if type == 'books'
        items = Book.objects.all().order_by('name')[:10]
    if type == 'movies'
        items = Movie.objects.all().order_by('name')[:10]
    templateName = templateName or 'list'
    template = loader.get_template('catalogo/' + templateName + '.html')
    
    if list: 
        context = Context({
            'items': items,
            'type': type,
        })

    return HttpResponse(template.render(context))
    
def search(request, type=None):
    if 'q' in request.GET:
        name = request.GET['q'].capitalize()
        items = get_list_or_404(type, name__contains=name)
        context = Context({
            'items': items,
            'type': type,
            'search': True,
        })

    templateName = templateName or 'list'
    template = loader.get_template('catalogo/' + templateName + '.html')
    return HttpResponse(template.render(context))

def show(request, item_id, type=None):
    if item_id:
        item = get_object_or_404(type, pk=item_id)
        context = context({
            'item': item,
            'type': type,
        })

    templateName = templateName or 'show'
    template = loader.get_template('catalogo/' + templateName + '.html')
    return HttpResponse(template.render(context))