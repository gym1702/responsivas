# Generated by Django 4.1.6 on 2023-02-09 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='disco',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='procesador',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sistemaoperativo',
            name='usuario_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]