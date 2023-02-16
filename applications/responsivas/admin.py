from django.contrib import admin
from .models import Responsiva, Detalle, ResponsivaBackup, DetalleBackup

class ResponsivaAdmin(admin.ModelAdmin):
    list_display = ('id', 'empleado', 'fecha_entrega', 'fecha_devolucion', 'estado_entrega', 'observaciones', 'activo')
    list_filter = ['estado_entrega', 'activo',]
    search_fields = ['no_responsiva', 'usuario',]

class DetalleAdmin(admin.ModelAdmin):
    list_display = ('responsiva', 'cantidad', 'equipo', 'id')
    search_fields = ['responsiva',]

# class ResponsivaBackupAdmin(admin.ModelAdmin):
#     list_display = ('no_responsiva', 'empleado', 'fecha_entrega', 'fecha_devolucion', 'estado_entrega', 'observaciones', 'id', 'activo')
#     list_filter = ['estado_entrega',]
#     search_fields = ['no_responsiva', 'usuario',]

class DetalleBackupAdmin(admin.ModelAdmin):
    list_display = ('responsiva', 'cantidad', 'equipo',  'en_responsiva', 'id')
    search_fields = ['responsiva',]


# Register your models here.
admin.site.register(Responsiva, ResponsivaAdmin)
admin.site.register(Detalle, DetalleAdmin)
#admin.site.register(ResponsivaBackup, ResponsivaBackupAdmin)
admin.site.register(DetalleBackup, DetalleBackupAdmin)
