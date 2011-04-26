from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from django.template import Context, loader
from ctlgr.about.models import About

def index(request):
  items = About.objects.all().order_by('id')[:5]
  context = Context({
    'items': items,
  })
  return render_to_response('about/index.html', context)

