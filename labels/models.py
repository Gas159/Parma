from django.db import models
from django.utils.translation import gettext_lazy as _



class Labels(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_('Label name'))
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("=Label=")
        verbose_name_plural = _("=Labels=")
        # ordering = ['created_at']