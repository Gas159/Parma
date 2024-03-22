from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _

from statuses.models import Status
from workplaces.models import Workplace


class Product(models.Model):
    # unique = True
    name = models.CharField(max_length=222, verbose_name=_('Product name'))
    number = models.IntegerField(verbose_name=_('Product number'))
    specification = models.IntegerField('Specification', null=True, blank=True)

    description = models.TextField(max_length=333, blank=True, verbose_name=_('Description'))
    # step_1 = models.BooleanField(blank=True, default=False, verbose_name=_('Step_1'))
    # step_1 = models.CharField(max_length=222, blank=True, verbose_name=_('Step_1'))
    # step_2 = models.BooleanField(default='', verbose_name=_('Step_2'))
    clear_turning_first = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='status1', verbose_name=_('status1'))
    clear_turning_second = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True,
                                             related_name='status2', verbose_name=_('status2'))
    clear_turning_third = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='status3', verbose_name=_('status3'))
    # workplace = models.ForeignKey(Workplace, on_delete=models.PROTECT,
    #                               null=True, blank=True, verbose_name=_('Workplace'))
    # in_supply = models.CharField(max_length=222, null=True, blank=True, default='В наличии')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name + '  №' + str(self.number)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = _('-=Products=-')
        ordering = ['-created_at']
