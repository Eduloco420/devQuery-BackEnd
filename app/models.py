# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archivos(models.Model):
    archivoid = models.AutoField(db_column='archivoId', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ticketId')  # Field name made lowercase.
    archivonom = models.CharField(db_column='archivoNom', max_length=255)  # Field name made lowercase.
    archivourl = models.CharField(db_column='archivoURL', max_length=255)  # Field name made lowercase.
    archivouser = models.CharField(db_column='archivoUser', max_length=255)  # Field name made lowercase.
    archivofechainsercion = models.DateTimeField(db_column='archivoFechaInsercion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'archivos'


class Area(models.Model):
    areaid = models.AutoField(db_column='areaId', primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='areaName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'area'


class Cliente(models.Model):
    clienteid = models.AutoField(db_column='clienteId', primary_key=True)  # Field name made lowercase.
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    clientedocid = models.CharField(db_column='clienteDocId', unique=True, max_length=255)  # Field name made lowercase.
    clientenombre = models.CharField(db_column='clienteNombre', max_length=255)  # Field name made lowercase.
    clienteappaterno = models.CharField(db_column='clienteApPaterno', max_length=255)  # Field name made lowercase.
    clienteapmaterno = models.CharField(db_column='clienteApMaterno', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientefecnac = models.DateField(db_column='clienteFecNac', blank=True, null=True)  # Field name made lowercase.
    clientemail = models.CharField(db_column='clienteMail', max_length=255)  # Field name made lowercase.
    clientefono = models.IntegerField(db_column='clienteFono', blank=True, null=True)  # Field name made lowercase.
    clienteempresadeptoid = models.ForeignKey('Deptoempresa', models.DO_NOTHING, db_column='clienteEmpresaDeptoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    comunaid = models.AutoField(db_column='comunaId', primary_key=True)  # Field name made lowercase.
    comunanom = models.CharField(db_column='comunaNom', max_length=255)  # Field name made lowercase.
    provinciaid = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='provinciaId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comuna'


class Depto(models.Model):
    deptoid = models.AutoField(db_column='deptoId', primary_key=True)  # Field name made lowercase.
    deptonom = models.CharField(db_column='deptoNom', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'depto'


class Deptoempresa(models.Model):
    deptoempid = models.AutoField(db_column='deptoEmpId', primary_key=True)  # Field name made lowercase.
    empresaid = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresaId')  # Field name made lowercase.
    deptoid = models.ForeignKey(Depto, models.DO_NOTHING, db_column='deptoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deptoEmpresa'


class Empresa(models.Model):
    empresaid = models.AutoField(db_column='empresaId', primary_key=True)  # Field name made lowercase.
    empresadocid = models.CharField(db_column='empresaDocID', unique=True, max_length=255)  # Field name made lowercase.
    empresanom = models.CharField(db_column='empresaNom', max_length=255)  # Field name made lowercase.
    empresadireccion = models.CharField(db_column='empresaDireccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    empresacomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='empresaComuna', blank=True, null=True)  # Field name made lowercase.
    empresamail = models.CharField(db_column='empresaMail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    empresafono = models.IntegerField(db_column='empresaFono', blank=True, null=True)  # Field name made lowercase.
    empresafecinsercion = models.DateTimeField(db_column='empresaFecInsercion', blank=True, null=True)  # Field name made lowercase.
    empresafecinicvig = models.DateTimeField(db_column='empresaFecInicVig')  # Field name made lowercase.
    empresafectermvig = models.DateTimeField(db_column='empresaFecTermVig')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class Estado(models.Model):
    estadoid = models.AutoField(db_column='estadoId', primary_key=True)  # Field name made lowercase.
    estadonom = models.CharField(db_column='estadoNom', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'


class Logestadoticket(models.Model):
    estadoticketid = models.AutoField(db_column='estadoTicketId', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ticketId')  # Field name made lowercase.
    estadoticket = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estadoTicket')  # Field name made lowercase.
    estadoticketfec = models.DateTimeField(db_column='estadoTicketFec')  # Field name made lowercase.
    estadoticketcomentario = models.CharField(db_column='estadoTicketComentario', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estadoticketuser = models.CharField(db_column='estadoTicketUser', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logEstadoTicket'


class Mensajes(models.Model):
    mensajeid = models.AutoField(db_column='mensajeId', primary_key=True)  # Field name made lowercase.
    mensajetexto = models.CharField(db_column='mensajeTexto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mensajeticket = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='mensajeTicket')  # Field name made lowercase.
    mensajeuser = models.CharField(db_column='mensajeUser', max_length=255)  # Field name made lowercase.
    mensajefecha = models.DateTimeField(db_column='mensajeFecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mensajes'


class Permisos(models.Model):
    permisoid = models.AutoField(db_column='permisoId', primary_key=True)  # Field name made lowercase.
    nompermiso = models.CharField(db_column='nomPermiso', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permisos'


class Prioridad(models.Model):
    prioridadid = models.AutoField(db_column='prioridadId', primary_key=True)  # Field name made lowercase.
    prioridadglosa = models.CharField(db_column='prioridadGlosa', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prioridad'


class Provincia(models.Model):
    provinciaid = models.AutoField(db_column='provinciaId', primary_key=True)  # Field name made lowercase.
    provincianom = models.CharField(db_column='provinciaNom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    regionid = models.AutoField(db_column='regionId', primary_key=True)  # Field name made lowercase.
    regionnom = models.CharField(db_column='regionNom', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Rol(models.Model):
    rolid = models.AutoField(db_column='rolId', primary_key=True)  # Field name made lowercase.
    nomrol = models.CharField(db_column='nomRol', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rol'


class Rolpermiso(models.Model):
    rolpermisoid = models.AutoField(db_column='rolPermisoId', primary_key=True)  # Field name made lowercase.
    rolid = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rolId')  # Field name made lowercase.
    permisoid = models.ForeignKey(Permisos, models.DO_NOTHING, db_column='permisoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rolPermiso'


class Tecticket(models.Model):
    tecticketid = models.AutoField(db_column='tecTicketId', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ticketId')  # Field name made lowercase.
    tecnicoid = models.ForeignKey('Tecnico', models.DO_NOTHING, db_column='tecnicoId')  # Field name made lowercase.
    fechaasigtecnico = models.DateTimeField(db_column='fechaAsigTecnico')  # Field name made lowercase.
    userasigtecnico = models.CharField(db_column='userAsigTecnico', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tecTicket'


class Tecnico(models.Model):
    tecid = models.AutoField(db_column='tecId', primary_key=True)  # Field name made lowercase.
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    tecdocid = models.CharField(db_column='tecDocId', unique=True, max_length=255)  # Field name made lowercase.
    tecnombre = models.CharField(db_column='tecNombre', max_length=255)  # Field name made lowercase.
    tecappaterno = models.CharField(db_column='tecApPaterno', max_length=255)  # Field name made lowercase.
    tecapmaterno = models.CharField(db_column='tecApMaterno', max_length=255)  # Field name made lowercase.
    tecfecnac = models.DateTimeField(db_column='tecFecNac')  # Field name made lowercase.
    tecmail = models.CharField(db_column='tecMail', max_length=255)  # Field name made lowercase.
    tecarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='tecArea')  # Field name made lowercase.
    teccargo = models.IntegerField(db_column='tecCargo')  # Field name made lowercase.
    tecsupervisor = models.ForeignKey('self', models.DO_NOTHING, db_column='tecSupervisor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tecnico'


class Ticket(models.Model):
    ticketid = models.AutoField(db_column='ticketId', primary_key=True)  # Field name made lowercase.
    ticketficid = models.CharField(db_column='ticketFicId', unique=True, max_length=255)  # Field name made lowercase.
    ticketfeccreacion = models.DateTimeField(db_column='ticketFecCreacion')  # Field name made lowercase.
    ticketcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ticketCliente')  # Field name made lowercase.
    tickettipo = models.ForeignKey('Tipoticket', models.DO_NOTHING, db_column='ticketTipo')  # Field name made lowercase.
    ticketprioridad = models.ForeignKey(Prioridad, models.DO_NOTHING, db_column='ticketPrioridad')  # Field name made lowercase.
    ticketname = models.CharField(db_column='ticketName', max_length=255)  # Field name made lowercase.
    ticketdesc = models.CharField(db_column='ticketDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket'


class Ticketarea(models.Model):
    ticketareaid = models.AutoField(db_column='ticketAreaId', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey(Ticket, models.DO_NOTHING, db_column='ticketId')  # Field name made lowercase.
    areaid = models.ForeignKey(Area, models.DO_NOTHING, db_column='areaId')  # Field name made lowercase.
    fechaasigarea = models.DateTimeField(db_column='fechaAsigArea')  # Field name made lowercase.
    userasigarea = models.CharField(db_column='userAsigArea', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticketArea'


class Tipoticket(models.Model):
    tipoticketid = models.AutoField(db_column='tipoTicketId', primary_key=True)  # Field name made lowercase.
    tipoticketnom = models.CharField(db_column='tipoTicketNom', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoTicket'


class User(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', unique=True, max_length=50)  # Field name made lowercase.
    userpfp = models.CharField(db_column='userPfP', max_length=255)  # Field name made lowercase.
    userpass = models.CharField(db_column='userPass', max_length=255)  # Field name made lowercase.
    roluser = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rolUser')  # Field name made lowercase.
    userfecinsercion = models.DateTimeField(db_column='userFecInsercion', blank=True, null=True)  # Field name made lowercase.
    userfecinivig = models.DateTimeField(db_column='userFecIniVig')  # Field name made lowercase.
    userfectervig = models.DateTimeField(db_column='userFecTerVig')  # Field name made lowercase.
    bloqueouser = models.IntegerField(db_column='BloqueoUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
