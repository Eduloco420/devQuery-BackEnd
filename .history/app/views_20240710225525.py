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
                userasigtecnico='system'  # o el nombre del usuario que asigna
            )
            last_assigned.last_assigned_index = (last_assigned.last_assigned_index + 1) % len(tecnicos)
            last_assigned.save()
