from rest_framework.routers import DefaultRouter

from .viewsets import MetricViewSet, RecordViewSet

router = DefaultRouter()
router.register(r'metrics', MetricViewSet)
router.register(r'records', RecordViewSet)
urlpatterns = router.urls
