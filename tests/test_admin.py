import pytest
from django.contrib import admin

from didadata.admin import MetricAdmin, RecordAdmin
from didadata.models import Metric, Record


@pytest.mark.django_db
class TestMetricAdmin:

    def test_list_display(self, rf):
        modeladmin = MetricAdmin(Metric, admin.site)
        assert modeladmin.list_display == ('name',)


@pytest.mark.django_db
class TestRecordAdmin:

    def test_list_display(self, rf):
        modeladmin = RecordAdmin(Record, admin.site)
        assert modeladmin.list_display == ('metric', 'timestamp', 'value')

    def test_list_filter(self, rf):
        modeladmin = RecordAdmin(Record, admin.site)
        assert modeladmin.list_filter == ('metric',)

    def test_date_hierarchy(self, rf):
        modeladmin = RecordAdmin(Record, admin.site)
        assert modeladmin.date_hierarchy == 'timestamp'
