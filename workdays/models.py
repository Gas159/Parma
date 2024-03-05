from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product


class WorkDay(models.Model):
    user = models.CharField(max_length=222, unique=True, verbose_name=_('Worker name'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product name'))
    time = models.IntegerField(verbose_name=_('Time'))
    description = models.TextField(max_length=333, verbose_name=_('Description'))
    # workplace = models.ForeignKey(Workplace, on_delete=models.PROTECT,
    #                               null=True, blank=True, verbose_name=_('Workplace'))
    # in_supply = models.CharField(max_length=222, null=True, blank=True, default='В наличии')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'WorkDay'
        verbose_name_plural = _('-=WorkDays=-')
        ordering = ['-created_at']
