from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Users


class OverTime(models.Model):
    user = models.OneToOneField(Users, on_delete=models.SET_NULL,
                                null=True, verbose_name=_('Worker name'))
    time = models.FloatField(help_text='Write you overtime.', verbose_name=_('Overtime'))
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    # def __str__(self):
    #     return self.user_name

    class Meta:
        verbose_name = 'Overtime'
        verbose_name_plural = _('-=Overtime=-')
        ordering = ['user']
