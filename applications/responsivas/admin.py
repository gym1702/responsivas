from django.contrib import admin
from .models import Responsiva, Detalle

class ResponsivaAdmin(admin.ModelAdmin):
    list_display = ('id', 'empleado', 'fecha_entrega', 'fecha_devolucion', 'estado_entrega', 'observaciones',)
    list_filter = ['estado_entrega',]
    search_fields = ['no_responsiva', 'usuario',]

class DetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'responsiva', 'cantidad', 'equipo')
    search_fields = ['responsiva',]


# Register your models here.
admin.site.register(Responsiva, ResponsivaAdmin)
admin.site.register(Detalle, DetalleAdmin)
