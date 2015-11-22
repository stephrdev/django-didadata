from rest_framework import serializers

from .models import Metric, Record


class MetricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metric


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('metric', 'timestamp', 'value')
