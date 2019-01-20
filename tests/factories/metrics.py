import factory

from didadata.models import Metric, Record


class MetricFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda i: 'metric-{0}'.format(i))

    class Meta:
        model = Metric


class RecordFactory(factory.DjangoModelFactory):
    metric = factory.SubFactory(MetricFactory)
    value = 0

    class Meta:
        model = Record
