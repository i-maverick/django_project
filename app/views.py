from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Author, Book


def index(request):
    return render(request, 'app/index.html')


@login_required
def private(request):
    return render(request, 'app/private.html')


class AuthorList(LoginRequiredMixin, ListView):
    model = Author


class BookList(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'


class AuthorBookList(LoginRequiredMixin, ListView):
    template_name = 'app/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(authors=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(AuthorBookList, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['author'] = Author.objects.get(id=self.kwargs['id'])
        return context


class CreateAuthorView(CreateView):
    model = Author
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('app:author_list')

    def form_valid(self, form):
        return super(CreateAuthorView, self).form_valid(form)


class CreateBookView(CreateView):
    model = Book
    fields = ['title', 'authors', 'publication_year']
    success_url = reverse_lazy('app:book_list')

    def form_valid(self, form):
        return super(CreateBookView, self).form_valid(form)
