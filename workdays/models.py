from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product
from statuses.models import Status
from users.models import Users


class WorkDay(models.Model):
    user_name = models.ForeignKey(Users, on_delete=models.DO_NOTHING, null=True, verbose_name=_('Worker name'))
    workplace_name = models.CharField(max_length=222, null=True, verbose_name=_('Workplace'))
    # user = models.(Users, on_delete=models.CASCADE,  verbose_name=_('Worker name'))
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name=_('Product name'))
    time = models.IntegerField(verbose_name=_('Time'))
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=' ', null=True,  verbose_name=_('Status1'))
    description = models.TextField(max_length=333, blank=True, verbose_name=_('Description'))
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
