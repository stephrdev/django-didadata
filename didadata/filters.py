import django_filters
from django_filters.fields import RangeField, IsoDateTimeField

from .models import Record


class IsoDateTimeRangeField(RangeField):

    def __init__(self, *args, **kwargs):
        fields = (IsoDateTimeField(), IsoDateTimeField())
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            start_datetime, stop_datetime = data_list
            return slice(start_datetime, stop_datetime)

        return None


class IsoDateTimeRangeFilter(django_filters.RangeFilter):
    field_class = IsoDateTimeRangeField


class RecordFilter(django_filters.FilterSet):
    metric = django_filters.CharFilter(name='metric__name')
    timestamp = IsoDateTimeRangeFilter()

    class Meta:
        model = Record
        fields = ('metric', 'timestamp')
