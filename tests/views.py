from django.shortcuts import render
from .models import Test, Dump, TestDump


def index(request):
    q = TestDump.objects.all()\
        .select_related('test_id')\
        .select_related('dump_id')\
        .filter(test_id__name__icontains='Test')\
        .filter(dump_id__device_name__exact='ATM')

    tests = dict()
    for item in q:
        test_id = item.test_id.id
        device = item.dump_id.device_name
        if test_id not in tests:
            tests[test_id] = dict()
            tests[test_id]['test'] = item.test_id.name
            tests[test_id]['devices'] = [device]
        elif device not in tests[test_id]['devices']:
            tests[test_id]['devices'].append(device)

    return render(request, 'tests/index.html', {'tests': tests})
