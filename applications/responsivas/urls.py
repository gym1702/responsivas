from django.urls import path
from . import views
from .reportes import reporte_responsivas, imprimir_responsiva, imprimir_devolucion

app_name = 'responsivas_app'

urlpatterns =[
    #RESPONSIVAS
    path('responsivas/listar/', views.ResponsivaListar.as_view(), name='responsiva_listar'),
    path('responsivas/crear/', views.responsivas, name='responsiva_crear'),
    path('responsivas/editar/<int:responsiva_id>', views.responsivas, name='responsiva_editar'),
    path('responsivas/<responsiva_id>/eliminar/<pk>/', views.BorrarDetalle.as_view(), name='responsiva_del'),
    #path('responsivas/<responsiva_id>/eliminar/<pk>/', views.BorrarDetalle.as_view(), name='responsiva_del2'),
    #path('responsivas/<int:responsiva_id>/eliminar/<int:pk>/', views.borra_detalle, name='responsiva_del_det'),
    path('responsivas/devolver/<int:responsiva_id>', views.devolver_responsiva, name='responsiva_devolver'),
    path('responsivas/eliminar/<pk>', views.ResponsivaEliminar.as_view(), name='responsiva_eliminar'),
    #path('responsivas/eliminar/<pk>', views.eliminar_responsiva, name='responsiva_eliminar'),
    path('responsivas/detalle/<pk>', views.VerDetalleResponsiva.as_view(), name='responsiva_detalle'),


    path('responsivas/reporte', reporte_responsivas, name='responsivas_print_all'),
    path('responsivas/<int:resp_id>/imprimir/', imprimir_responsiva, name='responsivas_print_one'),
    path('responsivas/<int:resp_id>/devolucion/', imprimir_devolucion, name='responsivas_devolucion'),

    #ruta para mostrar empleado en combo al agregarlo en responsiva
    # path('responsivas/empleados/crear/', empleado_resp, name='empleado_resp_crear'),
    # path('responsivas/empleados/editar/<int:pk>', empleado_resp, name='empleado_resp_modificar'),


]