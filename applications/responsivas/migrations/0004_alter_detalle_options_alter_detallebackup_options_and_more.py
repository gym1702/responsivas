# Generated by Django 4.1.6 on 2023-02-16 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responsivas', '0003_alter_detallebackup_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalle',
            options={'permissions': [('supervisor_det', 'Permiso de supervisor en detalles')], 'verbose_name_plural': 'Detalles'},
        ),
        migrations.AlterModelOptions(
            name='detallebackup',
            options={'permissions': [('supervisor_det', 'Permiso de supervisor en detalles')], 'verbose_name_plural': 'Detalles backup'},
        ),
        migrations.AlterModelOptions(
            name='responsivabackup',
            options={'permissions': [('supervisor_responsivas', 'Permiso de supervisor en responsivas')], 'verbose_name_plural': 'Responsivas backup'},
        ),
    ]
