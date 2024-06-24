from rest_framework import routers
from .api import ArchivosViewSet

router = routers.DefaultRouter()

router.register('api/projects', ArchivosViewSet, 'projects')

urlpatterns = router.urls