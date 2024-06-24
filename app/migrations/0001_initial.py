# Generated by Django 5.0.6 on 2024-06-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('archivoid', models.AutoField(db_column='archivoId', primary_key=True, serialize=False)),
                ('archivonom', models.CharField(db_column='archivoNom', max_length=255)),
                ('archivourl', models.CharField(db_column='archivoURL', max_length=255)),
                ('archivouser', models.CharField(db_column='archivoUser', max_length=255)),
                ('archivofechainsercion', models.DateTimeField(blank=True, db_column='archivoFechaInsercion', null=True)),
            ],
            options={
                'db_table': 'archivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('areaid', models.AutoField(db_column='areaId', primary_key=True, serialize=False)),
                ('areaname', models.CharField(db_column='areaName', max_length=255)),
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('clienteid', models.AutoField(db_column='clienteId', primary_key=True, serialize=False)),
                ('clientedocid', models.CharField(db_column='clienteDocId', max_length=255, unique=True)),
                ('clientenombre', models.CharField(db_column='clienteNombre', max_length=255)),
                ('clienteappaterno', models.CharField(db_column='clienteApPaterno', max_length=255)),
                ('clienteapmaterno', models.CharField(blank=True, db_column='clienteApMaterno', max_length=255, null=True)),
                ('clientefecnac', models.DateField(blank=True, db_column='clienteFecNac', null=True)),
                ('clientemail', models.CharField(db_column='clienteMail', max_length=255)),
                ('clientefono', models.IntegerField(blank=True, db_column='clienteFono', null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('comunaid', models.AutoField(db_column='comunaId', primary_key=True, serialize=False)),
                ('comunanom', models.CharField(db_column='comunaNom', max_length=255)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Depto',
            fields=[
                ('deptoid', models.AutoField(db_column='deptoId', primary_key=True, serialize=False)),
                ('deptonom', models.CharField(db_column='deptoNom', max_length=255)),
            ],
            options={
                'db_table': 'depto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deptoempresa',
            fields=[
                ('deptoempid', models.AutoField(db_column='deptoEmpId', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'deptoempresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresaid', models.AutoField(db_column='empresaId', primary_key=True, serialize=False)),
                ('empresadocid', models.CharField(db_column='empresaDocID', max_length=255, unique=True)),
                ('empresanom', models.CharField(db_column='empresaNom', max_length=255)),
                ('empresadireccion', models.CharField(blank=True, db_column='empresaDireccion', max_length=255, null=True)),
                ('empresamail', models.CharField(blank=True, db_column='empresaMail', max_length=255, null=True)),
                ('empresafono', models.IntegerField(blank=True, db_column='empresaFono', null=True)),
                ('empresafecinsercion', models.DateTimeField(blank=True, db_column='empresaFecInsercion', null=True)),
                ('empresafecinicvig', models.DateTimeField(db_column='empresaFecInicVig')),
                ('empresafectermvig', models.DateTimeField(db_column='empresaFecTermVig')),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('estadoid', models.AutoField(db_column='estadoId', primary_key=True, serialize=False)),
                ('estadonom', models.CharField(db_column='estadoNom', max_length=255)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logestadoticket',
            fields=[
                ('estadoticketid', models.AutoField(db_column='estadoTicketId', primary_key=True, serialize=False)),
                ('estadoticketfec', models.DateTimeField(db_column='estadoTicketFec')),
                ('estadoticketcomentario', models.CharField(blank=True, db_column='estadoTicketComentario', max_length=255, null=True)),
                ('estadoticketuser', models.CharField(db_column='estadoTicketUser', max_length=255)),
            ],
            options={
                'db_table': 'logestadoticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('mensajeid', models.AutoField(db_column='mensajeId', primary_key=True, serialize=False)),
                ('mensajetexto', models.CharField(blank=True, db_column='mensajeTexto', max_length=100, null=True)),
                ('mensajeuser', models.CharField(db_column='mensajeUser', max_length=255)),
                ('mensajefecha', models.DateTimeField(blank=True, db_column='mensajeFecha', null=True)),
            ],
            options={
                'db_table': 'mensajes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('permisoid', models.AutoField(db_column='permisoId', primary_key=True, serialize=False)),
                ('nompermiso', models.CharField(db_column='nomPermiso', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'permisos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('prioridadid', models.AutoField(db_column='prioridadId', primary_key=True, serialize=False)),
                ('prioridadglosa', models.CharField(db_column='prioridadGlosa', max_length=255)),
            ],
            options={
                'db_table': 'prioridad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('provinciaid', models.AutoField(db_column='provinciaId', primary_key=True, serialize=False)),
                ('provincianom', models.CharField(blank=True, db_column='provinciaNom', max_length=255, null=True)),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('regionid', models.AutoField(db_column='regionId', primary_key=True, serialize=False)),
                ('regionnom', models.CharField(db_column='regionNom', max_length=255)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rolid', models.AutoField(db_column='rolId', primary_key=True, serialize=False)),
                ('nomrol', models.CharField(db_column='nomRol', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rolpermiso',
            fields=[
                ('rolpermisoid', models.AutoField(db_column='rolPermisoId', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'rolpermiso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('tecid', models.AutoField(db_column='tecId', primary_key=True, serialize=False)),
                ('tecdocid', models.CharField(db_column='tecDocId', max_length=255, unique=True)),
                ('tecnombre', models.CharField(db_column='tecNombre', max_length=255)),
                ('tecappaterno', models.CharField(db_column='tecApPaterno', max_length=255)),
                ('tecapmaterno', models.CharField(db_column='tecApMaterno', max_length=255)),
                ('tecfecnac', models.DateTimeField(db_column='tecFecNac')),
                ('tecmail', models.CharField(db_column='tecMail', max_length=255)),
                ('teccargo', models.IntegerField(db_column='tecCargo')),
            ],
            options={
                'db_table': 'tecnico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tecticket',
            fields=[
                ('tecticketid', models.AutoField(db_column='tecTicketId', primary_key=True, serialize=False)),
                ('fechaasigtecnico', models.DateTimeField(db_column='fechaAsigTecnico')),
                ('userasigtecnico', models.CharField(db_column='userAsigTecnico', max_length=255)),
            ],
            options={
                'db_table': 'tecticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketid', models.AutoField(db_column='ticketId', primary_key=True, serialize=False)),
                ('ticketficid', models.CharField(db_column='ticketFicId', max_length=255, unique=True)),
                ('ticketfeccreacion', models.DateTimeField(db_column='ticketFecCreacion')),
                ('ticketname', models.CharField(db_column='ticketName', max_length=255)),
                ('ticketdesc', models.CharField(blank=True, db_column='ticketDesc', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticketarea',
            fields=[
                ('ticketareaid', models.AutoField(db_column='ticketAreaId', primary_key=True, serialize=False)),
                ('fechaasigarea', models.DateTimeField(db_column='fechaAsigArea')),
                ('userasigarea', models.CharField(db_column='userAsigArea', max_length=255)),
            ],
            options={
                'db_table': 'ticketarea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipoticket',
            fields=[
                ('tipoticketid', models.AutoField(db_column='tipoTicketId', primary_key=True, serialize=False)),
                ('tipoticketnom', models.CharField(db_column='tipoTicketNom', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'tipoticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='userId', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='userName', max_length=50, unique=True)),
                ('userpfp', models.CharField(db_column='userPfP', max_length=255)),
                ('userpass', models.CharField(db_column='userPass', max_length=255)),
                ('userfecinsercion', models.DateTimeField(blank=True, db_column='userFecInsercion', null=True)),
                ('userfecinivig', models.DateTimeField(db_column='userFecIniVig')),
                ('userfectervig', models.DateTimeField(db_column='userFecTerVig')),
                ('bloqueouser', models.IntegerField(db_column='BloqueoUser')),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
