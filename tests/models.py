from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.name


class Dump(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)
    device_name = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return "{} {}".format(self.name, self.device_name)


class TestDump(models.Model):
    test_id = models.ForeignKey(Test)
    dump_id = models.ForeignKey(Dump)
    dump_number = models.IntegerField()

    def __str__(self):
        return "test_id: {}, dump_id: {}".format(self.test_id, self.dump_id)
