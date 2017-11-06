from django.db import models


class Dump(models.Model):
    class Meta:
        db_table = 'TDump'

    name = models.CharField(max_length=32, null=False, blank=False)
    device_name = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return "{} {}".format(self.name, self.device_name)


class Test(models.Model):
    class Meta:
        db_table = 'TTest'

    name = models.CharField(max_length=32, null=False, blank=False)
    dumps = models.ManyToManyField(Dump, through='TestDump')

    def __str__(self):
        return self.name


class TestDump(models.Model):
    class Meta:
        db_table = 'TTestDump'

    test_id = models.ForeignKey(Test, name='test_id')
    dump_id = models.ForeignKey(Dump, name='dump_id')
    dump_number = models.IntegerField(null=False)

    def __str__(self):
        return "{} {}".format(self.test_id, self.dump_id)
