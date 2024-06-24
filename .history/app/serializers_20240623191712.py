from rest_framework import serializers
from .models import *

class ArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivos
        fields = ('archivoid','ticketid','archivonom','archivourl','archivouser','archivofechainsercion')
        read_only_fields = ('archivofechainsercion', )


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('regionid','regionnom')
        read_only_fields = ('regionid','regionnom')    
