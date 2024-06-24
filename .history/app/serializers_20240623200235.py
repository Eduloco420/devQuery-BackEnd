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
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('Areaid','areaname')
        read_only_fields = ('Areaid','areaname')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('Areaid','areaname')
        read_only_fields = ('Areaid','areaname')
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('clienteid','userid','clientedocid','clientenombre','clienteappaterno','clienteapmaterno','clientefecnac','clientemail','clientefono','clienteempresadeptoid')

class DeptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depto
        fields = ('deptoid','deptonom') 

class DeptoempresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deptoempresa
        fields = ('deptoempid','empresaid','deptoid')    

class Empresa(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('empresaid','empresadocid','empresanom','empresadireccion','empresacomuna','empresamail','empresafono','empresafecinsercion','empresafecinicvig','empresafectermvig')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deptoempresa
        fields = ('estadoid','estadonom')    
        read_only_fields = ('estadoid','estadonom')

class LogestadoticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logestadoticket
        fields = ('estadoticketid','ticketid','estadoticket','estadoticketfec','estadoticketcomentario','estadoticketuser')    

class Mensajes(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
        fields = ('mensajeid','mensajetexto','mensajeticket','mensajeuser','mensajefecha')

class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permisos
        fields = ('permisoid','nompermiso')

class PrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridad
        fields = ('prioridadid','prioridadglosa')

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('rolid','nomrol')
        read_only_fields = ('rolid','nomrol')

class RolpermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rolpermiso
        fields = ('rolpermisoid','rolid','permisoid')
        read_only_fields = ('rolpermisoid','rolid','permisoid')

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('tecid','userid','tecdocid','tecnombre','tecappaterno','tecapmaterno','tecfecnac','tecmail','tecarea','teccargo','tecsupervisor')    

class TecticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rolpermiso
        fields = ('tecticketid','ticketid','tecnicoid','fechaasigtecnico','userasigtecnico')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('ticketid','ticketficid','ticketfeccreacion','ticketcliente','tickettipo','ticketprioridad','ticketname','ticketdesc')
        
class TicketareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticketarea
        fields = ('ticketareaid','ticketid','areaid','fechaasigarea','userasigarea')

class TipoticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipoticket
        fields = ('tipoticketid','tipoticketnom')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipoticket
        fields = ('userid','username','userpfp','userpass','roluser','userfecinsercion','userfecinivig','userfectervig','bloqueouser')        