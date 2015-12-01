from rest_framework import serializers

from .models import Metric, Record


class MetricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metric


class MinimalRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('timestamp', 'value')


class RecordSerializer(serializers.ModelSerializer):
    metric = serializers.SlugRelatedField(
        queryset=Metric.objects.all(), slug_field='name')

    class Meta:
        model = Record
        fields = ('metric', 'timestamp', 'value')
