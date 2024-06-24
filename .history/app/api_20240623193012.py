from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class ArchivosViewSet(viewsets.ModelViewSet):
    queryset = Archivos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArchivosSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = RegionSerializer    
    
class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProvinciaSerializer   
    
class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ComunaSerializer          