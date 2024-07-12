# Generated by Django 5.0.6 on 2024-07-11 04:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_tecnico_tecfecnac'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastAssignedTechnician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_assigned_index', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='tecticket',
            name='fechaasigtecnico',
            field=models.DateTimeField(db_column='fechaAsigTecnico', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketfeccreacion',
            field=models.DateTimeField(db_column='ticketFecCreacion', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ticketarea',
            name='fechaasigarea',
            field=models.DateTimeField(db_column='fechaAsigArea', default=django.utils.timezone.now),
        ),
    ]
