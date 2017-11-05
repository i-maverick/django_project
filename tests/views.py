from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'tests/index.html', context)
