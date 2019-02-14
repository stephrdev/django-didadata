from django.contrib import admin

from .models import Metric, Record


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('metric', 'timestamp', 'value')
    list_filter = ('metric',)
    date_hierarchy = 'timestamp'
