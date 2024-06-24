from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class ArchivosViewSet(viewsets.ModelViewSet):
    queryset = Archivos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArchivosSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = region.objects.all():
    permissions_classes = [permissions.AllowAny]
    serializer_class = RegionSerializer    