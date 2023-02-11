from datetime import datetime
from django.db import models
from applications.home.models import Comun
from django.db import models 
from applications.catalogos.models import Empleado, Equipo
from django.contrib.auth import authenticate

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Responsiva(Comun):

    estadoentrega = (
        ('Pendiente', 'Pendiente'),
        ('Equipo Entregado', 'Equipo Entregado'),
        ('Equipo Devuelto', 'Equipo Devuelto'),
        ('Sin Equipo', 'Sin Equipo'),
    )

    fecha_entrega = models.DateTimeField()
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    estado_entrega = models.CharField(max_length=20, default='Pendiente')
    no_responsiva = models.CharField(max_length=20, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    observaciones = models.TextField(max_length=150, blank=True)
    recibe_devolucion = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    # def save(self):
    #     self.no_responsiva = self.id

    #     super(Responsiva,self).save()
    
    class Meta:
        verbose_name_plural = "Responsivas"
        permissions = [
            ('supervisor_resp', 'Permiso de supervisor en responsivas')
        ]


class Detalle(Comun):
    responsiva = models.ForeignKey(Responsiva, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    categoria_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.equipo)
    

    class Meta:
        verbose_name_plural = "Detalles responsivas" 
        permissions = [
            ('supervisor_det', 'Permiso de supervisor en detalles')
        ]


#PARA AFECTAR EL CAMPO STATUS AL AGREGAR O BORRAR DE LA RESPONSIVA

@receiver(post_save, sender=Detalle)
def resp_detalle_borra(sender, instance, **kwargs):
    id_equipo = instance.equipo.id
    id_respon = instance.responsiva.id
            
    equi = Equipo.objects.filter(pk=id_equipo).first()
    resp = Responsiva.objects.filter(pk=id_respon).first()
    if equi:
        equi.status = 'Asignado'
        equi.usuario = str(resp.empleado)
        equi.depto = str(resp.empleado.depto)
        equi.save()

        resp.estado_entrega = 'Equipo Entregado'
        resp.save()

      

@receiver(post_delete, sender=Detalle)
def resp_detalle_borra(sender, instance, **kwargs):
    id_equipo = instance.equipo.id
    id_respon = instance.responsiva.id
    id_emp = instance.responsiva.empleado.id

    equi = Equipo.objects.filter(pk=id_equipo).first()
    resp = Responsiva.objects.filter(pk=id_respon).first()
    det = Detalle.objects.filter(responsiva_id=id_respon)
    emp = Empleado.objects.filter(pk=id_emp).first()
    
    if equi:
        equi.status = 'Libre'
        equi.usuario = '-'
        equi.depto = '-'
        equi.save()

        if not det:
            resp.estado_entrega = 'Equipo Devuelto'      
            resp.fecha_devolucion = datetime.now()
            #resp.recibe_devolucion = user.firts_name
            resp.save()

            equi.usuario = '-'
            equi.depto = '-'
            equi.status = 'Libre'
            equi.save()

            emp.tiene_responsiva = 'No'
            emp.save()



@receiver(post_save, sender=Responsiva)
def emp_tiene_resp(sender, instance, **kwargs):
    id_emp = instance.empleado.id

    emp = Empleado.objects.filter(pk=id_emp).first()
    if emp:
        emp.tiene_responsiva = 'Si'
        emp.save()



# @receiver(post_delete, sender=Responsiva)
# def emp_tiene_resp(sender, instance, **kwargs):
#     id_emp = instance.empleado.id

#     emp = Empleado.objects.filter(pk=id_emp).first()
#     if emp:
#         emp.tiene_responsiva = 0
#         emp.save()