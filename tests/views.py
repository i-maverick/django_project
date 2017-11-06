from django.shortcuts import render
from .models import Test, Dump, TestDump


def index(request):
    q = TestDump.objects.all().select_related('test_id').select_related('dump_id')
    print(q)

    context = {'tests': q}
    return render(request, 'tests/index.html', context)
