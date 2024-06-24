from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/archivos', ArchivosViewSet, 'archivos')
router.register('api/region', RegionViewSet, 'region')
router.register('api/provincia', ProvinciaViewSet, 'provincia')
router.register('api/comuna', ComunaViewSet, 'comuna')


urlpatterns = router.urls