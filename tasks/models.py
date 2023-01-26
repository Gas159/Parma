from django.db import models
from django.utils.translation import gettext as _

from users.models import Users
from statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_('Task name'))
    description = models.TextField(max_length=300, blank=True, verbose_name=_('Description'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    executor = models.ForeignKey(Users, on_delete=models.PROTECT, )
    author = models.ForeignKey(Users, related_name='author', on_delete=models.PROTECT,
                               verbose_name=_('Author'), default='2')

    # labels = models.ManyToManyField(
    #     Labels,
    #     related_name='label',
    #     through='TaskRelationLabel',
    #     blank=True,
    #     verbose_name=_('Label')
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("=Task=")
        verbose_name_plural = _("=Tasks=")
        ordering = ['-created_at']

from django.db import models

