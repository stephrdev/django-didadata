from rest_framework import exceptions, mixins, permissions, viewsets

from .models import Metric, Record
from .serializers import MetricSerializer, RecordSerializer


# We dont use the ModelViewSet because we don't want to allow delete or update.
class MetricViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class RecordViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (permissions.DjangoModelPermissions,)

    def get_queryset(self):
        """
        Restrict listing of records to a specific metric.
        """
        if 'metric' not in self.request.query_params:
            raise exceptions.ValidationError(
                {'metric': 'Please provide a metric ID to retreive records.'})

        try:
            metric_id = int(self.request.query_params['metric'])
        except ValueError:
            raise exceptions.ValidationError(
                {'metric': 'Provided value is not a valid metric ID.'})

        return super().get_queryset().filter(metric_id=metric_id)
