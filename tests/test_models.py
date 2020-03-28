import pytest

from .factories.metrics import MetricFactory, RecordFactory


@pytest.mark.django_db
class TestMetricModel:
    def test_repr(self):
        obj = MetricFactory.create(name="my-metric")
        assert str(obj) == "my-metric"


@pytest.mark.django_db
class TestRecordModel:
    def test_repr(self):
        obj = RecordFactory.create(value=23)
        assert str(obj).startswith("{0}/".format(obj.metric_id))
        assert "/{0:%s}/".format(obj.timestamp) in str(obj)
        assert str(obj).endswith("/23")
