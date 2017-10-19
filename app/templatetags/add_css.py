# From http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/#comment-1193609278

from django import template
register = template.Library()


@register.filter(name='css')
def add_css(field, css):
    return field.as_widget(attrs={"class": css})
