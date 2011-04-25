from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^admin/(.*)', admin.site.root),
  (r'^about/$', 'ctlgr.about.views.index'),
  (r'^$', 'ctlgr.catalogo.views.index'),
  (r'^catalogo/$', 'ctlgr.catalogo.views.index'),
  (r'^catalogo/livros/$', 'ctlgr.catalogo.views.livros'),
  (r'^catalogo/livro/(?P<livro_id>\d+)$', 'ctlgr.catalogo.views.livros_show'),
  (r'^catalogo/livros/search/$', 'ctlgr.catalogo.views.searchLivro'),
  (r'^catalogo/filmes/$', 'ctlgr.catalogo.views.filmes'),
  (r'^catalogo/filme/(?P<filme_id>\d+)$', 'ctlgr.catalogo.views.filmes_show'),
  (r'^catalogo/filmes/search/$', 'ctlgr.catalogo.views.searchFilme'),
  (r'^ctlgr-theme/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': '/home/mario/ctlgr/public'}), 
)
