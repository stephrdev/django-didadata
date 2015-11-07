from .exceptions import InvalidValueException, MetricNotFoundException
from .models import Metric


def record(name, value):
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

    return metric.record_set.create(value=value)
