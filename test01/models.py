from django.db import models


# Create your models here.
# class Resource(models.Model):
#     url = models.CharField(max_length=100, null=False, blank=False, verbose_name='门户地址')
#
#     class Mata:
#         db_table = 'other'
# permissions = (('can_visit_res', 'Can visit this host'),)


class Resource(models.Model):
    codename = models.CharField(max_length=100, default='example', null=False, blank=False,
                                verbose_name='门户代码')
    name = models.CharField(max_length=100, default='http://www.example.com', null=False, blank=False,
                            verbose_name='门户地址')

    class Meta:
        db_table = 'resource'
        permissions = (('can_visit_res', 'Can visit this host'),)

    def __str__(self):
        return self.name
