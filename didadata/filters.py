import django_filters
from django import forms
from django.db.models import Q
from django_filters.fields import IsoDateTimeField, RangeField

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


class MultipleCharFilter(django_filters.CharFilter):
    field_class = forms.CharField

    def filter(self, qs, value):
        value = value or ''

        if not value:
            return qs

        q = Q()
        for v in set(value.split(',')):
            q |= Q(**{self.field_name: v})

        return self.get_method(qs)(q)


class RecordFilter(django_filters.FilterSet):
    metric = MultipleCharFilter(field_name='metric__name')
    timestamp = IsoDateTimeRangeFilter()

    class Meta:
        model = Record
        fields = ('metric', 'timestamp')
