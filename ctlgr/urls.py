from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

# admin url
admin_url = url(
	r'^admin/(.*)',
	admin.site.root,
	name='admin_url',
)

# about url
about_url = url(
	r'^about/$',
	'ctlgr.about.views.index',
	name='about_url',
)

# index
index_url = url(
	r'^$',
	'ctlgr.catalogo.views.index',
	name='index_url',
)

# books list
books_list_url = url(
	r'books/$',
	'ctlgr.catalogo.views.list',
	{'type': 'books'},
	name='books_list_url',
)

# books search
books_search_url = url(
	r'books/search',
	'ctlgr.catalogo.views.search',
	{'type': 'books'},
	name='books_search_url',
)

# books show
books_show_url = url(
	r'book/(?P<book_id>\d+)$',
	'ctlgr.catalogo.views.show',
	{'type': 'books'},
	name='books_show_url',
)

# movies list
movies_list_url = url(
	r'movies/$',
	'ctlgr.catalogo.views.list',
	{'type': 'movies'},
	name='movies_list_url',
)

# movies search
movies_search_url = url(
	r'movies/search',
	'ctlgr.catalogo.views.search',
	{'type': 'movies'},
	name='movies_search_url',
)

# movies show
movies_show_url = url(
	r'movie/(?P<movie_id>\d+)$',
	'ctlgr.catalogo.views.show',
	{'type': 'movies'},
	name='movies_show_url',
)

# theme url
theme_url = url(
	r'^ctlgr-theme/(?P<path>.*)$',
	'django.views.static.serve',
	{'document_root': '/home/mario/ctlgr/public'}
)

urlpatterns = patterns('',
	admin_url,
	about_url,
	index_url,
	books_list_url,
	books_search_url,
	books_show_url,
	movies_list_url,
	movies_search_url,
	movies_show_url,
)
