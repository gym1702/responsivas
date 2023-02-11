from django.contrib import admin
from .models import Categoria, Marca, Puesto, Departamento, Empleado, Equipo, Procesador, Ram, Disco, SistemaOperativo

class CartegoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ['activo']
    search_fields = ['nombre']


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ['activo']
    search_fields = ['nombre']


class PuestoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ['activo']
    search_fields = ['nombre']


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ['activo']
    search_fields = ['nombre']


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'foto', 'depto', 'telefono', 'email', 'tiene_responsiva', 'activo')
    list_filter = ['activo', 'depto', 'tiene_responsiva']
    search_fields = ['nombre', 'telefono', 'email']


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'id', 'insumo', 'marca', 'categoria', 'serie', 'status', 'depto', 'activo')
    list_filter = ['activo', 'marca', 'categoria', 'depto', 'procesador', 'ram', 'status']
    search_fields = ['insumo', 'serie', 'marca', 'modelo']



# Register your models here.
admin.site.register(Categoria, CartegoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Puesto, PuestoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Procesador)
admin.site.register(Ram)
admin.site.register(Disco)
admin.site.register(SistemaOperativo)