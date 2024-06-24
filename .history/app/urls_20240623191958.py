from rest_framework import routers
from .api import ArchivosViewSet

router = routers.DefaultRouter()

router.register('api/archivos', ArchivosViewSet, 'archivos')
router.register('api/region', RegionViewSet, 'region')

urlpatterns = router.urls