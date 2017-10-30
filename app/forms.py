import re
from django import forms
from django.core.exceptions import ValidationError

from dal import autocomplete

from .models import Author, Book, Genre


class AuthorForm(forms.ModelForm):
    name = forms.CharField(max_length=64, help_text='Enter the full name')

    class Meta:
        model = Author
        fields = ('__all__')


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('__all__')

    author_list = [(a.id, a) for a in Author.objects.all().order_by('name')]
    authors = forms.MultipleChoiceField(choices=author_list)
    genre_list = [(g.id, g) for g in Genre.objects.all().order_by('name')]
    genres = forms.MultipleChoiceField(choices=genre_list)

    def clean_publication_year(self):
        year = self.cleaned_data['publication_year']
        if len(str(year)) != 4:
            raise ValidationError('Incorrect year format (it should be 4 digits)')
        return year

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        m = re.match(r'^(\d)+$', isbn)
        if not m or len(m.group(0)) != 13:
            raise ValidationError('Incorrect ISBN format (it should be 13 digits)')
        return isbn


class AuthorSelectForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=autocomplete.Select2(
            url='app:author_autocomplete',
            attrs={
                'onChange': 'form.submit()',
                'data-placeholder': 'Select author...',
            }
        )
    )

    class Meta:
        model = Author
        fields = ('author',)


class SearchForm(forms.Form):
    field = forms.CharField(
        max_length=32,
        required=False,
        widget=forms.TextInput(attrs={'data-placeholder': 'Enter text ...'}))
