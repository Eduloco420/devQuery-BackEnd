from .models import *
from .views import create_logestadoticket, assign_tecnico
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
import smtplib
import ssl
from email.message import EmailMessage
from django.conf import settings
from datetime import datetime


class ArchivosViewSet(viewsets.ModelViewSet):
    queryset = Archivos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArchivosSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegionSerializer    
    
class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProvinciaSerializer   
    
class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ComunaSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AreaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class DeptoViewSet(viewsets.ModelViewSet):
    queryset = Depto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DeptoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpresaSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstadoSerializer

class LogestadoticketViewSet(viewsets.ModelViewSet):
    queryset = Logestadoticket.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LogestadoticketSerializer

class MensajesViewSet(viewsets.ModelViewSet):
    queryset = Mensajes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MensajesSerializer

class PermisosViewSet(viewsets.ModelViewSet):
    queryset = Permisos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PermisosSerializer  

class PrioridadViewSet(viewsets.ModelViewSet):
    queryset = Prioridad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PrioridadSerializer  

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RolSerializer 

class RolpermisoViewSet(viewsets.ModelViewSet):
    queryset = Rolpermiso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RolpermisoSerializer 

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TecnicoSerializer 

class TecticketViewSet(viewsets.ModelViewSet):
    queryset = Tecticket.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TecticketSerializer 

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        UserModel  = get_user_model()
        user = self.request.user
        user_id = None
        print(UserModel)
        if user.is_authenticated:
            user_instance = UserModel.objects.filter(email=user.email).first()
            print(user_instance)
            if user_instance:
                ticket = serializer.save()
                create_logestadoticket(sender=Ticket, instance=ticket, created=True, user_instance=user_instance)
                username = user_instance.username
                assign_tecnico(sender=Ticket, instance=ticket, created=True, user_instance=user_instance)
                cliente = ticket.ticketcliente
                fecha_form = ticket.ticketfeccreacion.strftime("%d-%m-%Y %H:%M:%S")


                # Preparar el correo electrónico
                subject = f'Nuevo ticket registrado: {ticket.ticketname}'
                message = f"""
                Se ha registrado un nuevo ticket.
                
                Detalles del Ticket:
                ID: {ticket.ticketficid}
                Nombre: {ticket.ticketname}
                Descripción: {ticket.ticketdesc}
                Fecha de Creación: {fecha_form}
                
                Detalles del Cliente:
                Nombre: {cliente.clientenombre} {cliente.clienteappaterno} {cliente.clienteapmaterno}
                Teléfono: {cliente.clientefono}
                Empresa: {cliente.clienteempresa.empresanom}
                """
                recipient = cliente.userid.email

                # Enviar el correo electrónico
                email = EmailMessage()
                email['From'] = settings.DEFAULT_FROM_EMAIL
                email['To'] = recipient
                email['Subject'] = subject
                email.set_content(message)

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=context) as server:
                    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    server.send_message(email)

                print(f'Correo enviado a: {recipient}')


class TicketareaViewSet(viewsets.ModelViewSet):
    queryset = Ticketarea.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketareaSerializer 

class TipoticketViewSet(viewsets.ModelViewSet):
    queryset = Tipoticket.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoticketSerializer 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer             