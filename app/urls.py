from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^private/$', views.private, name='private'),
    url(r'^authors/$', views.AuthorList.as_view(), name='author_list'),
    url(r'^authors/(?P<id>\d+)/$', views.AuthorBookList.as_view(), name='author_book_list'),
    url(r'^authors/create/$', views.CreateAuthorView.as_view(), name='create_author'),
    url(r'^books/$', views.BookList.as_view(), name='book_list'),
    url(r'^books/create/$', views.CreateBookView.as_view(), name='create_book'),
    url(r'^author_select/$', views.AuthorSelectView.as_view(), name='author_select'),
    url(r'^author_autocomplete/$', views.AuthorAutocomplete.as_view(), name='author_autocomplete'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^select_books/$', views.select_books, name='select_books'),
    url(r'^run_tests/$', views.run_tests, name='run_tests'),
]
