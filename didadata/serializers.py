from rest_framework import serializers

from .models import Metric, Record


class MetricSerializer(serializers.ModelSerializer):
    record_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Metric


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('metric', 'timestamp', 'value')
