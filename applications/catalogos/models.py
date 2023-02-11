from statistics import mode
from tabnanny import verbose
from django.db import models
from applications.home.models import Comun
from django.conf import settings

from model_utils.models import TimeStampedModel

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# MODELO CATEGORIA
class Categoria(Comun):
    nombre = models.CharField(max_length=100, help_text='Nombre', unique=True)
    descripcion = models.CharField(max_length=255, help_text='Descripcion', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

    # Metodo convertir todo a mayusculas
    # def save(self):  
    #     self.nombre = self.nombre.upper()
    #     super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


# MODELO MARCAS
class Marca(Comun):
    nombre = models.CharField(max_length=100, help_text='Nombre', unique=True)
    descripcion = models.CharField(max_length=255, help_text='Descripcion', blank=True, null=True)
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Marcas"



# MODELO PUESTOS
class Puesto(Comun):
    nombre = models.CharField(max_length=100, help_text='Nombre', unique=True)
    funcion = models.CharField(max_length=255, help_text='Funcion', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Puestos"



# MODELO DEPTOS
class Departamento(Comun):
    nombre = models.CharField(max_length=100, help_text='Nombre', unique=True)
    funcion = models.CharField(max_length=255, help_text='Funcion', blank=True, null=True)
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Departamentos"



# MODELO EMPLEADOS
class Empleado(Comun):

    SEX = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('No especifica', 'No especifica'),
    )
    nombre = models.CharField(max_length=100, unique=True, help_text='Nombre completo')
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    depto = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, help_text='Telefono', blank=True, null=True)
    email = models.CharField(max_length=100, help_text='Email', blank=True, null=True)
    sexo = models.CharField(choices=SEX, default='No especifica', max_length=20)
    foto = models.ImageField(upload_to="empleados/", blank=True, null=True, default="perfil-user.png")
    tiene_responsiva = models.CharField(max_length=10, default='No')
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Empleados"



# MODELO PROCESADOR
class Procesador(Comun):

    marca = (
        ('-', '-'),
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
    )

    marca = models.CharField(choices=marca, default='-', max_length=100)
    numero = models.CharField(max_length=30, unique=True)
    generacion = models.IntegerField(blank=True, null=True)
    velocidad = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    

    def __str__(self):
        return str(self.numero)

    class Meta:
        verbose_name_plural = "Procesadores"



# MODELO RAM
class Ram(Comun):
    tipo = models.CharField(max_length=30)
    velocidad = models.IntegerField(blank=True, null=True)
    frecuencia = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    

    
    def __str__(self):
        return str(self.tipo) +' - '+ str(self.velocidad)

    class Meta:
        verbose_name_plural = "Memorias Ram"



# MODELO DISCOS DUROS
class Disco(Comun):

    tipo = (
        ('-', '-'),
        ('Interno', 'Interno'),
        ('Externo', 'Externo'),
    )

    interfaz = (
        ('-', '-'),
        ('SCSI', 'SCSI'),
        ('IDE', 'IDE'),
        ('SATA', 'SATA'),
        ('SSD', 'SSD'),
        ('USB', 'USB'),
        ('M-SATA', 'M-SATA'),
        ('M.2', 'M.2')
    )

    tipo = models.CharField(choices=tipo, max_length=30, default='-')
    interfaz = models.CharField(choices=interfaz, max_length=30, default='SATA')
    capacidad = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.interfaz) +' - '+ str(self.capacidad)

    class Meta:
        verbose_name_plural = "Discos Duros"



# MODELO SO
class SistemaOperativo(Comun):
    arq = (
        ('-', '-'),
        ('x86', 'x86'),
        ('x64', 'x64'),
    )

    nombre = models.CharField(max_length=100)
    arquitectura = models.CharField(choices=arq, max_length=50, blank=True, null=True, default='-')
    

    def __str__(self):
        return self.nombre +' - '+ self.arquitectura

    class Meta:
        verbose_name_plural = "Sistemas Operativos"



# MODELO EQUIPOS
class Equipo(Comun):

    condicion = (
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
    )

    status =(
        ('Asignado', 'Asignado'),
        ('Libre', 'Libre'),
    )

    monitores = (
        ('-', '-'), 
        ('7"', '7"'),
        ('10.1"', '10.1"'),
        ('13"', '13"'),
        ('14"', '14"'),
        ('15.6"', '15.6"'),
        ('17"', '17"'),
        ('19"', '19"'),
        ('21.5"', '21.5"'),
        ('23"', '23"'),
        ('27"', '27"'),
        ('32"', '32"'),
        ('40"', '40"'),
        ('42"', '42"'),
        ('50"', '50"'),
        ('55"', '55"'),
        ('60"', '60"'),
        ('90"', '90"'),
    )

    insumo = models.PositiveIntegerField(unique=True, help_text='Insumo', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=30, help_text='Modelo')
    serie = models.CharField(max_length=30, help_text='Numero de serie')
    condiciones = models.CharField(choices=condicion, max_length=20, help_text='Condiciones')
    procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    so = models.ForeignKey(SistemaOperativo, on_delete=models.CASCADE)
    pantalla = models.CharField(choices=monitores, blank=True, null=True, default='-', max_length=20)
    caracteristicas = models.CharField(max_length=300, blank=True, null=True, help_text='Caracteristicas', default='-')
    depto = models.CharField(max_length=50, blank=True, null=True, default='-')
    usuario = models.CharField(max_length=100,  blank=True, null=True, default='-')
    imagen = models.ImageField(upload_to='equipos/', blank=True, null=True, default="otro-equipo.jpg")
    status = models.CharField(choices=status, blank=True, null=True, default='Libre', max_length=20, help_text='Status')
    observaciones = models.CharField(max_length=150, blank=True, null=True, default='-')
    descripcion = models.CharField(max_length=100,  blank=True, null=True, default='-')
    
    def __str__(self):
        return str(self.marca.nombre +' - '+ self.modelo +' - '+ self.serie)
    
    
    # def save(self):  
    #     if self.categoria == 1:
    #         self.imagen = 'media/default-pc.png'
    #     if self.categoria == 2:
    #         self.imagen = 'media/default-lap.png'
    #     if self.categoria == 3:
    #         self.imagen = 'media/default-imp.jpg'
    #     if self.categoria == 4:
    #         self.imagen = 'media/default-otro.png'
    #     super(Equipo, self).save()

    class Meta:
        verbose_name_plural = "Equipos"



@receiver(post_save, sender=Equipo)
def guardar_imagen_segun_categoria(sender, instance, **kwargs):
    id_equipo = instance.id
            
    equi = Equipo.objects.filter(pk=id_equipo).first()
    if equi:
        if equi.categoria == 2:
            equi.imagen = "..\media\default-lap.png"
            equi.save()