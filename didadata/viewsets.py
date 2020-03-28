from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, viewsets

from .filters import RecordFilter
from .models import Metric, Record
from .serializers import MetricSerializer, MinimalRecordSerializer, RecordSerializer


# We dont use the ModelViewSet because we don't want to allow delete or update.
class MetricViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    permission_classes = (permissions.DjangoModelPermissions,)


class RecordViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Record.objects.all()
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = RecordFilter

    def get_queryset(self):
        qset = super().get_queryset()

        if 'minimal' in self.request.query_params:
            # Minimal response doesn't include metric name, no select_related
            # needed.
            return qset

        return qset.select_related('metric')

    def get_serializer_class(self):
        # Use reduced serializer (no metric name per record) if we filter based
        # on a metric.
        if 'minimal' in self.request.query_params:
            return MinimalRecordSerializer

        return RecordSerializer
