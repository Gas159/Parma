from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("=Status=")
        verbose_name_plural = _("=Statuses=")
        ordering = ['-created_at']
