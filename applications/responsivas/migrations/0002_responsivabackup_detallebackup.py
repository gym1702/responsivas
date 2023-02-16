# Generated by Django 4.1.6 on 2023-02-11 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0008_alter_equipo_insumo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('responsivas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsivaBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=2, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_edicion', models.DateTimeField(auto_now=True)),
                ('usuario_edita', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_entrega', models.DateTimeField()),
                ('fecha_devolucion', models.DateTimeField(blank=True, null=True)),
                ('estado_entrega', models.CharField(default='Pendiente', max_length=20)),
                ('no_responsiva', models.CharField(blank=True, max_length=20, null=True)),
                ('observaciones', models.TextField(blank=True, max_length=150)),
                ('recibe_devolucion', models.TextField(blank=True, max_length=150, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.empleado')),
                ('usuario_crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario crea')),
            ],
            options={
                'verbose_name_plural': 'Responsivas',
                'permissions': [('supervisor_resp', 'Permiso de supervisor en responsivas')],
            },
        ),
        migrations.CreateModel(
            name='DetalleBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=2, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_edicion', models.DateTimeField(auto_now=True)),
                ('usuario_edita', models.CharField(blank=True, max_length=50, null=True)),
                ('cantidad', models.IntegerField(default=1)),
                ('categoria_id', models.IntegerField(blank=True, null=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.equipo')),
                ('responsiva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='responsivas.responsiva')),
                ('usuario_crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario crea')),
            ],
            options={
                'verbose_name_plural': 'Detalles responsivas',
                'permissions': [('supervisor_det', 'Permiso de supervisor en detalles')],
            },
        ),
    ]
