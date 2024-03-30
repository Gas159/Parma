from django.db import models
from django.utils.translation import gettext_lazy as _

from labels.models import Labels
from products.models import Product
from statuses.models import Status
from users.models import Users
from workplaces.models import Workplace


class WorkDay(models.Model):
    user_name = models.ForeignKey(Users, on_delete=models.SET_NULL,
                                  null=True, verbose_name=_('Worker name'))
    workplace = models.ForeignKey(Workplace, on_delete=models.SET_NULL,
                                  null=True, verbose_name=_('Workplace'))
    # user = models.(Users, on_delete=models.CASCADE,  verbose_name=_('Worker name'))
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                null=True, verbose_name=_('Product name'))
    time = models.FloatField(verbose_name=_('Time of create'))
    operation = models.ForeignKey(Labels, on_delete=models.SET_NULL, blank=True,
                                  null=True, verbose_name=_('Operation'))
    status = models.ForeignKey(Status, on_delete=models.SET_NULL,
                               null=True, verbose_name=_('Status'))
    amount = models.IntegerField(verbose_name=_('Amount'), null=True, blank=True)
    description = models.TextField(max_length=333, blank=True,
                                   verbose_name=_('Description'))
    # workplace = models.ForeignKey(Workplace, on_delete=models.PROTECT,
    #                               null=True, blank=True, verbose_name=_('Workplace'))
    # in_supply = models.CharField(max_length=222, null=True, blank=True, default='В наличии')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    update_at = models.DateTimeField(auto_now=True, null=True)

    # def __str__(self):
    #     return self.user_name

    class Meta:
        verbose_name = 'WorkDay'
        verbose_name_plural = _('-=WorkDays=-')
        ordering = ['-created_at']
