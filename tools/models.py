from django.db import models
from django.utils.translation import gettext_lazy as _

from workplaces.models import Workplace


class Tool(models.Model):
    type = models.CharField(max_length=222, null=True, blank=True, verbose_name=_('Type tool'))
    dm = models.FloatField('d, mm', null=True, blank=True)
    D = models.FloatField('D, mm', null=True, blank=True, )
    L = models.FloatField('L, mm', null=True, blank=True, )
    Lc = models.FloatField('Lc, mm', null=True, blank=True, )
    Z = models.FloatField('Z, amount', null=True, blank=True, )
    R = models.FloatField('R', null=True, blank=True, )
    departure = models.FloatField('Depart, mm', null=True, blank=True, )
    monolith = models.BooleanField('Monolith', null=True, blank=True, )
    plate = models.CharField('Plate', max_length=222, null=True, blank=True, )
    plate_name = models.CharField('Name of plate', max_length=222, null=True, blank=True, )
    company = models.CharField('Company', max_length=222, null=True, blank=True, )
    price = models.FloatField('Price, Rub', null=True, blank=True, )
    delivery_time = models.FloatField('Delivery time, days', null=True, blank=True, )

    workplace = models.ForeignKey(Workplace, on_delete=models.SET_NULL,
                                  null=True, blank=True, verbose_name=_('Workplace'))
    in_supply = models.CharField(max_length=222, null=True, blank=True, default='В наличии')
    description = models.TextField(max_length=333, verbose_name=_('Description'))

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tool'
        verbose_name_plural = _('-=Tools=-')
        ordering = ['-created_at']
