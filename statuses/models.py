from django.db import models
from django.utils.translation import gettext as _


# Create your models.py here.
class Status(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("=Status=")
        verbose_name_plural = _("=Statuses=")
        ordering = ['-created_at']
