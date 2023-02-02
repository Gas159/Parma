from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Users
from statuses.models import Status
from labels.models import Labels


class Task(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_('Task name'))
    description = models.TextField(max_length=300, blank=True, verbose_name=_('Description'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, verbose_name=_('Status'))
    executor = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name=_('Executor'))
    author = models.ForeignKey(Users, related_name='author', on_delete=models.PROTECT,
                               verbose_name=_('Author'), default='2')

    labels = models.ManyToManyField(Labels, through='TaskLabel', blank=True,
                                    verbose_name=_('Labels'))
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("=Task=")
        verbose_name_plural = _("=Tasks=")
        ordering = ['-created_at']


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    labels = models.ForeignKey(Labels, on_delete=models.PROTECT)
