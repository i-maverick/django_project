from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView

from dal import autocomplete

from .models import Author, Book, Genre
from .forms import BookForm, AuthorSelectForm, SearchForm

def index(request):
    return render(request, 'app/index.html')


@login_required
def private(request):
    return render(request, 'app/private.html')


class AuthorList(ListView):
    model = Author


class BookList(ListView):
    # model = Book
    context_object_name = 'books'
    queryset = Book.objects.order_by('title')

    # def get_queryset(self):
    #     return Book.objects.order_by('title')


class AuthorBookList(ListView):
    template_name = 'app/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(authors=self.kwargs['id']).order_by('publication_year')

    def get_context_data(self, **kwargs):
        context = super(AuthorBookList, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['author'] = Author.objects.get(id=self.kwargs['id'])
        return context


class CreateAuthorView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ('__all__')
    success_url = reverse_lazy('app:author_list')

    def form_valid(self, form):
        return super(CreateAuthorView, self).form_valid(form)


# class CreateBookView(LoginRequiredMixin, CreateView):
#     model = Book
#     fields = ('__all__')
#     success_url = reverse_lazy('app:book_list')
#
#     def form_valid(self, form):
#         return super(CreateBookView, self).form_valid(form)


class CreateBookView(LoginRequiredMixin, FormView):
    form_class = BookForm
    template_name = 'app/book_form.html'
    success_url = reverse_lazy('app:book_list')

    def form_valid(self, form):
        form.save()
        return super(CreateBookView, self).form_valid(form)


class CreateGenreView(LoginRequiredMixin, CreateView):
    model = Genre
    fields = ('__all__')
    success_url = reverse_lazy('app:genre_list')

    # def form_valid(self, form):
    #     return super(CreateGenreView, self).form_valid(form)


class AjaxableResponseMixin(object):

    def form_valid(self, form):
        print('AjaxableResponseMixin', self.request)
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            print('ajax', response)
            return JsonResponse(data)
        else:
            return response


class AuthorAutocomplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
        qs = Author.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class AuthorSelectView(FormView):
    form_class = AuthorSelectForm
    template_name = 'app/author_select.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            if 'author' in self.request.POST:
                author = request.POST['author']
                books = Book.objects.filter(authors=author)
                context['books'] = books
        return render(request, self.template_name, context)


class SearchView(FormView):
    form_class = SearchForm
    template_name = 'app/search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        print(context)
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {'form': form}
        print("=========== post", form)
        if form.is_valid():
            data = request.POST.get('search')
            books = Book.objects.filter(
                Q(title__icontains=data))
                # Q(authors__name__icontains=data) |
                # Q(publication_year__icontains=data) |
                # Q(isbn__icontains=data))
                # Q(genres__name__icontains=data))
            # form.fields['books'].choices = [(book.id, "{}, {}".format(
            #     book.title, book.publication_year)) for book in books]
            context['books'] = books
            if 'selected' in request.POST:
                selected_ids = request.POST.getlist('selected')
                print(selected_ids)
                selected_books = Book.objects.filter(id__in = selected_ids)
                print(selected_books)
                context['selected'] = selected_books
        return render(request, self.template_name, context)
