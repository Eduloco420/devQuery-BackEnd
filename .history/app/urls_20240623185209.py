from rest_framework import routers
from .api import ArchivosViewSet

router = routers.DefaultRouter()

router.register('api/archivos', ArchivosViewSet, 'archivos')

urlpatterns = router.urls