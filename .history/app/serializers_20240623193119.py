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

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('provinciaid','provincianom','regionid')
        read_only_fields = ('provinciaid','provincianom','regionid')
        
class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('comunaid','comunanom','provinciaid')
        read_only_fields = ('comunaid','comunanom','provinciaid')   

