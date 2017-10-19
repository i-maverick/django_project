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
]
