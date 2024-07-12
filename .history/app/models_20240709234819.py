# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils import timezone


class Archivos(models.Model):
    archivoid = models.AutoField(db_column='archivoId', primary_key=True)
    ticketid = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ticketId')
    archivonom = models.CharField(db_column='archivoNom', max_length=255)
    archivourl = models.CharField(db_column='archivoURL', max_length=255)
    archivouser = models.CharField(db_column='archivoUser', max_length=255)
    archivofechainsercion = models.DateTimeField(db_column='archivoFechaInsercion', blank=True, null=True)

class Area(models.Model):
    areaid = models.AutoField(db_column='areaId', primary_key=True)
    areaname = models.CharField(db_column='areaName', max_length=255)

class Cliente(models.Model):
    clienteid = models.AutoField(db_column='clienteId', primary_key=True)
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='userId')
    clientedocid = models.CharField(db_column='clienteDocId', unique=True, max_length=255)
    clientenombre = models.CharField(db_column='clienteNombre', max_length=255)
    clienteappaterno = models.CharField(db_column='clienteApPaterno', max_length=255)
    clienteapmaterno = models.CharField(db_column='clienteApMaterno', max_length=255, blank=True, null=True)
    clientefecnac = models.DateField(db_column='clienteFecNac', blank=True, null=True)
    clientemail = models.CharField(db_column='clienteMail', max_length=255)
    clientefono = models.IntegerField(db_column='clienteFono', blank=True, null=True)
    clienteempresadeptoid = models.ForeignKey('Deptoempresa', models.DO_NOTHING, db_column='clienteEmpresaDeptoId')

class Comuna(models.Model):
    comunaid = models.AutoField(db_column='comunaId', primary_key=True)
    comunanom = models.CharField(db_column='comunaNom', max_length=255)
    provinciaid = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='provinciaId')

class Depto(models.Model):
    deptoid = models.AutoField(db_column='deptoId', primary_key=True)
    deptonom = models.CharField(db_column='deptoNom', max_length=255)

class Deptoempresa(models.Model):
    deptoempid = models.AutoField(db_column='deptoEmpId', primary_key=True)
    empresaid = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresaId')
    deptoid = models.ForeignKey(Depto, models.DO_NOTHING, db_column='deptoId')

class Empresa(models.Model):
    empresaid = models.AutoField(db_column='empresaId', primary_key=True)
    empresadocid = models.CharField(db_column='empresaDocID', unique=True, max_length=255)
    empresanom = models.CharField(db_column='empresaNom', max_length=255)
    empresadireccion = models.CharField(db_column='empresaDireccion', max_length=255, blank=True, null=True)
    empresacomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='empresaComuna', blank=True, null=True)
    empresamail = models.CharField(db_column='empresaMail', max_length=255, blank=True, null=True)
    empresafono = models.IntegerField(db_column='empresaFono', blank=True, null=True)
    empresafecinsercion = models.DateTimeField(db_column='empresaFecInsercion', blank=True, null=True)
    empresafecinicvig = models.DateTimeField(db_column='empresaFecInicVig')
    empresafectermvig = models.DateTimeField(db_column='empresaFecTermVig')

class Estado(models.Model):
    estadoid = models.AutoField(db_column='estadoId', primary_key=True)
    estadonom = models.CharField(db_column='estadoNom', max_length=255)

class Logestadoticket(models.Model):
    estadoticketid = models.AutoField(db_column='estadoTicketId', primary_key=True)
    ticketid = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ticketId')
    estadoticket = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estadoTicket')
    estadoticketfec = models.DateTimeField(db_column='estadoTicketFec')
    estadoticketcomentario = models.CharField(db_column='estadoTicketComentario', max_length=255, blank=True, null=True)
    estadoticketuser = models.CharField(db_column='estadoTicketUser', max_length=255)

class Mensajes(models.Model):
    mensajeid = models.AutoField(db_column='mensajeId', primary_key=True)
    mensajetexto = models.CharField(db_column='mensajeTexto', max_length=100, blank=True, null=True)
    mensajeticket = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='mensajeTicket')
    mensajeuser = models.CharField(db_column='mensajeUser', max_length=255)
    mensajefecha = models.DateTimeField(db_column='mensajeFecha', blank=True, null=True)

class Permisos(models.Model):
    permisoid = models.AutoField(db_column='permisoId', primary_key=True)
    nompermiso = models.CharField(db_column='nomPermiso', unique=True, max_length=255)

class Prioridad(models.Model):
    prioridadid = models.AutoField(db_column='prioridadId', primary_key=True)
    prioridadglosa = models.CharField(db_column='prioridadGlosa', max_length=255)


class Provincia(models.Model):
    provinciaid = models.AutoField(db_column='provinciaId', primary_key=True)
    provincianom = models.CharField(db_column='provinciaNom', max_length=255, blank=True, null=True)
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionId', blank=True, null=True)

class Region(models.Model):
    regionid = models.AutoField(db_column='regionId', primary_key=True)
    regionnom = models.CharField(db_column='regionNom', max_length=255)

class Rol(models.Model):
    rolid = models.AutoField(db_column='rolId', primary_key=True)
    nomrol = models.CharField(db_column='nomRol', unique=True, max_length=255)

class Rolpermiso(models.Model):
    rolpermisoid = models.AutoField(db_column='rolPermisoId', primary_key=True)
    rolid = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rolId')
    permisoid = models.ForeignKey(Permisos, models.DO_NOTHING, db_column='permisoId')

class Tecticket(models.Model):
    tecticketid = models.AutoField(db_column='tecTicketId', primary_key=True)
    ticketid = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ticketId')
    tecnicoid = models.ForeignKey('Tecnico', models.DO_NOTHING, db_column='tecnicoId')
    fechaasigtecnico = models.DateTimeField(db_column='fechaAsigTecnico')
    userasigtecnico = models.CharField(db_column='userAsigTecnico', max_length=255)

class Tecnico(models.Model):
    tecid = models.AutoField(db_column='tecId', primary_key=True)
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='userId')
    tecdocid = models.CharField(db_column='tecDocId', unique=True, max_length=255)
    tecnombre = models.CharField(db_column='tecNombre', max_length=255)
    tecappaterno = models.CharField(db_column='tecApPaterno', max_length=255)
    tecapmaterno = models.CharField(db_column='tecApMaterno', max_length=255)
    tecfecnac = models.DateTimeField(db_column='tecFecNac')
    tecmail = models.CharField(db_column='tecMail', max_length=255)
    tecarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='tecArea')
    teccargo = models.IntegerField(db_column='tecCargo')
    tecsupervisor = models.ForeignKey('self', models.DO_NOTHING, db_column='tecSupervisor', blank=True, null=True)

class Ticket(models.Model):
    ticketid = models.AutoField(db_column='ticketId', primary_key=True)
    ticketficid = models.CharField(db_column='ticketFicId', unique=True, max_length=255)
    ticketfeccreacion = models.DateTimeField(db_column='ticketFecCreacion')
    ticketcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ticketCliente')
    tickettipo = models.ForeignKey('Tipoticket', models.DO_NOTHING, db_column='ticketTipo')
    ticketprioridad = models.ForeignKey(Prioridad, models.DO_NOTHING, db_column='ticketPrioridad')
    ticketname = models.CharField(db_column='ticketName', max_length=255)
    ticketdesc = models.CharField(db_column='ticketDesc', max_length=255, blank=True, null=True)

class Ticketarea(models.Model):
    ticketareaid = models.AutoField(db_column='ticketAreaId', primary_key=True)
    ticketid = models.ForeignKey(Ticket, models.DO_NOTHING, db_column='ticketId')
    areaid = models.ForeignKey(Area, models.DO_NOTHING, db_column='areaId')
    fechaasigarea = models.DateTimeField(db_column='fechaAsigArea')
    userasigarea = models.CharField(db_column='userAsigArea', max_length=255)

class Tipoticket(models.Model):
    tipoticketid = models.AutoField(db_column='tipoTicketId', primary_key=True)
    tipoticketnom = models.CharField(db_column='tipoTicketNom', unique=True, max_length=255)

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("favor ingresa un e-mail valido")
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)

class User(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)
    username = models.CharField(db_column='userName', unique=True, max_length=50)
    email = models.EmailField(default='', unique = True)
    userpfp = models.CharField(db_column='userPfP', max_length=255)
    password = models.CharField(db_column='password', max_length=255)
    roluser = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rolUser')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username     

    def get_short_name(self):    
        return self.username or self.email.split('@')[0]
