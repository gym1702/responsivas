from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# MODELO COMUN
estado = (
        ('Si', 'Si'),
        ('No', 'No'),
    )

class Comun(models.Model):
    activo = models.CharField(choices=estado, max_length=2, default='Si', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)
    usuario_crea = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario crea')
    usuario_edita = models.CharField(max_length=50, blank=True, null=True)
    #Especificamos que este modelo no lo tome en cuanta al crara una migracion
    class Meta:
        abstract = True

