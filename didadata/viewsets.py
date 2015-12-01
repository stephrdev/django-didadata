from rest_framework import filters, mixins, permissions, viewsets

from .filters import RecordFilter
from .models import Metric, Record
from .serializers import MetricSerializer, MinimalRecordSerializer, RecordSerializer


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
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RecordFilter

    def get_serializer_class(self):
        # Use reduced serializer (no metric name per record) if we filter based
        # on a metric.
        if 'metric' in self.request.query_params:
            return MinimalRecordSerializer

        return RecordSerializer
