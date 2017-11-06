from django.shortcuts import render
from .models import Test, Dump, TestDump


def index(request):
    q = TestDump.objects.all().select_related('test_id').select_related('dump_id')
    tests = dict()
    for item in q:
        test_id = item.test_id.id
        device = item.dump_id.device_name
        if test_id not in tests:
            tests[test_id] = dict()
            tests[test_id]['test'] = item.test_id.name
            tests[test_id]['devices'] = [device]

        if device not in tests[test_id]['devices']:
            tests[test_id]['devices'].append(device)
        print(tests)

    return render(request, 'tests/index.html', {'tests': tests})
