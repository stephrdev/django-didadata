from datetime import timedelta

import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone

from didadata import api
from didadata.exceptions import InvalidValueException, MetricNotFoundException

from .factories.metrics import MetricFactory


@pytest.mark.django_db
class TestRecordApi:

    def test_invalid_metric(self):
        with pytest.raises(MetricNotFoundException):
            api.record('my-metric', 0)

    def test_invalid_value(self):
        MetricFactory.create(name='my-metric')
        with pytest.raises(InvalidValueException):
            api.record('my-metric', 'foo')

    def test_created(self):
        metric = MetricFactory.create(name='my-metric')
        obj = api.record('my-metric', 23)
        assert obj.pk is not None
        assert metric.record_set.count() == 1

    def test_created_with_timestamp(self):
        yesterday = timezone.now() - timedelta(days=1)
        metric = MetricFactory.create(name='my-metric')
        obj = api.record('my-metric', 23, timestamp=yesterday)
        assert obj.pk is not None
        assert metric.record_set.count() == 1
        assert obj.timestamp == yesterday

    def test_created_with_timestamp_invalid_format(self):
        yesterday = 'yesterday'
        MetricFactory.create(name='my-metric')

        with pytest.raises(ValidationError):
            api.record('my-metric', 23, timestamp=yesterday)
