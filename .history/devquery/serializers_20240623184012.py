from rest_framework import serializers
from .models import Archivos

class ArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivos
        fields = ('archivoid','ticketid','archivonom','archivourl','archivouser','archivofechainsercion')
        read_only_fields = ('archivofechainsercion')
