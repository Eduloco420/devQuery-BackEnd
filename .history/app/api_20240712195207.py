from .models import *
from .views import create_logestadoticket
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


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

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = AreaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class DeptoViewSet(viewsets.ModelViewSet):
    queryset = Depto.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = DeptoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = EmpresaSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = EstadoSerializer

class LogestadoticketViewSet(viewsets.ModelViewSet):
    queryset = Logestadoticket.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = LogestadoticketSerializer

class MensajesViewSet(viewsets.ModelViewSet):
    queryset = Mensajes.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = MensajesSerializer

class PermisosViewSet(viewsets.ModelViewSet):
    queryset = Permisos.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = PermisosSerializer  

class PrioridadViewSet(viewsets.ModelViewSet):
    queryset = Prioridad.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = PrioridadSerializer  

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = RolSerializer 

class RolpermisoViewSet(viewsets.ModelViewSet):
    queryset = Rolpermiso.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = RolpermisoSerializer 

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TecnicoSerializer 

class TecticketViewSet(viewsets.ModelViewSet):
    queryset = Tecticket.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TecticketSerializer 

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer 

    def perform_create(self, serializer):
        ticket = serializer.save()
        # Pasar el usuario a la señal post_save
        print(self.request.User)
        create_logestadoticket(ticket, self.request.User)

class TicketareaViewSet(viewsets.ModelViewSet):
    queryset = Ticketarea.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TicketareaSerializer 

class TipoticketViewSet(viewsets.ModelViewSet):
    queryset = Tipoticket.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TipoticketSerializer 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserSerializer             