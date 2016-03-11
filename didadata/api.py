from .exceptions import InvalidValueException, MetricNotFoundException
from .models import Metric


def record(name, value, timestamp=None):
    """
    This api method expects a name of an existing metric and a float convertable value.
    The value is stored and a new record object is returned.
    """
    try:
        metric = Metric.objects.get(name=name)
    except Metric.DoesNotExist:
        raise MetricNotFoundException(name)

    try:
        value = float(value)
    except ValueError:
        raise InvalidValueException(str(value))

    kwargs = dict(value=value)
    if timestamp:
        kwargs.update({'timestamp': timestamp})

    return metric.record_set.create(**kwargs)
