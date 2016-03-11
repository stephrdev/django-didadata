from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Metric(models.Model):
    name = models.SlugField(_('Metric name'), max_length=40, unique=True)

    class Meta:
        verbose_name = _('Metric')
        verbose_name_plural = _('Metrics')

    def __str__(self):
        return self.name


class Record(models.Model):
    metric = models.ForeignKey(Metric, verbose_name=_('Metric'))
    timestamp = models.DateTimeField(
        _('Timestamp'), db_index=True, default=timezone.now, editable=False)
    value = models.FloatField(_('Value'))

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = _('Record')
        verbose_name_plural = _('Records')

    def __str__(self):
        return '{0}/{1:%s}/{2}'.format(self.metric_id, self.timestamp, self.value)
