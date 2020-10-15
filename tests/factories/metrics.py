from factory import Sequence, SubFactory
from factory.django import DjangoModelFactory

from didadata.models import Metric, Record


class MetricFactory(DjangoModelFactory):
    name = Sequence(lambda i: 'metric-{0}'.format(i))

    class Meta:
        model = Metric


class RecordFactory(DjangoModelFactory):
    metric = SubFactory(MetricFactory)
    value = 0

    class Meta:
        model = Record
