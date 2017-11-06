from django.contrib import admin
from .models import Test, Dump, TestDump

admin.site.register(Test)
admin.site.register(Dump)
admin.site.register(TestDump)
