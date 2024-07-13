from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import smtplib
import ssl
from email.message import EmailMessage
from django.conf import settings
from datetime import datetime


# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)

        return Response({'token': token.key, 'user':serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):

    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Contraseña Incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@receiver(post_save, sender=Ticket)
def assign_tecnico(sender, instance, created, **kwargs):
    if created:
        last_assigned, created = LastAssignedTechnician.objects.get_or_create(pk=1)
        tecnicos = list(Tecnico.objects.all())
        if tecnicos:
            tecnico = tecnicos[last_assigned.last_assigned_index % len(tecnicos)]
            Tecticket.objects.create(
                ticketid=instance,
                tecnicoid=tecnico,
                fechaasigtecnico=timezone.now(),
                userasigtecnico='system'
            )
            last_assigned.last_assigned_index = (last_assigned.last_assigned_index + 1) % len(tecnicos)
            last_assigned.save()

def create_logestadoticket(sender, instance, created, user_instance ,**kwargs):
    if created:
        print(user_instance)
        Logestadoticket.objects.create(
            ticketid=instance,
            estadoticket_id=1,
            estadoticketfec=timezone.now(),
            estadoticketcomentario="Creación de Ticket",
            estadoticketuser=user_instance
        )

@api_view(['GET'])
def tecTicketAsig(request, ticket_id):
    try:
        tecticket = Tecticket.objects.filter(ticketid=ticket_id).order_by('-fechaasigtecnico').first()
        if tecticket:
            serializer = TecticketSerializer(tecticket)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No se encontraron registros para este ticket."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def estadoTicketAct(request, ticket_id):
    try:
        ticketest = Logestadoticket.objects.filter(ticketid=ticket_id).order_by('-estadoticketfec').first()
        if ticketest:
            serializer = LogestadoticketSerializer(ticketest)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No se encontraron registros para este ticket."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@receiver(post_save, sender=Logestadoticket)
def send_logestadoticket_email(sender, instance, created, **kwargs):
    if created:
        fecha_formateada = instance.estadoticketfec.strftime("%d-%m-%Y %H:%M:%S")
        subject = "Estado de Ticket Actualizado"
        body = (f"El estado del ticket con ID {instance.ticketid.ticketficid} ha sido actualizado.\n"
                f"Nuevo estado: {instance.estadoticket.estadonom}\n"
                f"Fecha de actualización: {fecha_formateada}\n"
                f"Comentario: {instance.estadoticketcomentario}\n")

        email = EmailMessage()
        email['From'] = settings.DEFAULT_FROM_EMAIL
        email['To'] = instance.ticketid.ticketcliente.userid.email  # Ajustar esto según tu modelo de cliente
        email['Subject'] = subject
        email.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=context) as server:
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.send_message(email)


