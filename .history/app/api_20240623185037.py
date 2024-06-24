from .models import Archivos
from rest_framework import viewsets, permissions
from .serializers import ArchivosSerializer

class ArchivosViewSet(viewsets.ModelViewSet):
    queryset = Archivos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArchivosSerializer