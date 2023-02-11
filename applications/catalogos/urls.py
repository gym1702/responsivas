from django.urls import path

from . import views

from .reportes import reporte_equipos

app_name = 'catalogos_app'


urlpatterns =[
    #CATEGORIAS
    path('categorias/listar/', views.CategoriaListar.as_view(), name='categoria_listar'),
    path('categorias/crear/', views.CategoriaCrear.as_view(), name='categoria_crear'),
    path('categorias/editar/<int:pk>', views.CategoriaEditar.as_view(), name='categoria_editar'),
    path('categorias/eliminar/<int:pk>', views.CategoriaEliminar.as_view(), name='categoria_eliminar'),
    #path('categorias/eliminar/<int:id>', views.categoria_eliminar, name='categorias_eliminar'),

    #MARCAS
    path('marcas/listar/', views.MarcaListar.as_view(), name='marca_listar'),
    path('marcas/crear/', views.MarcaCrear.as_view(), name='marca_crear'),
    path('marcas/editar/<int:pk>', views.MarcaEditar.as_view(), name='marca_editar'),
    path('marcas/eliminar/<int:pk>', views.MarcaEliminar.as_view(), name='marca_eliminar'),
    #path('marcas/eliminar/<int:id>', views.marca_eliminar, name='marca_eliminar'),

    #PUESTOS
    path('puesto/listar/', views.PuestoListar.as_view(), name='puesto_listar'),
    path('puesto/crear/', views.PuestoCrear.as_view(), name='puesto_crear'),
    path('puesto/editar/<int:pk>', views.PuestoEditar.as_view(), name='puesto_editar'),
    path('puesto/eliminar/<int:pk>', views.PuestoEliminar.as_view(), name='puesto_eliminar'),

    #DEPARTAMENTOS
    path('depto/listar/', views.DeptoListar.as_view(), name='depto_listar'),
    path('depto/crear/', views.DeptoCrear.as_view(), name='depto_crear'),
    path('depto/editar/<int:pk>', views.DeptoEditar.as_view(), name='depto_editar'),
    path('depto/eliminar/<int:pk>', views.DeptoEliminar.as_view(), name='depto_eliminar'),

    #EMPLAEDOS
    path('empleado/listar/', views.EmpleadoListar.as_view(), name='empleado_listar'),
    path('empleado/crear/', views.EmpleadoCrear.as_view(), name='empleado_crear'),
    path('empleado/editar/<int:pk>', views.EmpleadoEditar.as_view(), name='empleado_editar'),
    path('empleado/eliminar/<int:pk>', views.EmpleadoEliminar.as_view(), name='empleado_eliminar'),

    #EQUIPOS
    path('equipo/listar/', views.EquipoListar.as_view(), name='equipo_listar'),
    path('equipo/crear/', views.EquipoCrear.as_view(), name='equipo_crear'),
    path('equipo/editar/<int:pk>/', views.EquipoEditar.as_view(), name='equipo_editar'),
    path('equipo/eliminar/<int:pk>/', views.EquipoEliminar.as_view(), name='equipo_eliminar'),
    path('equipo/detalle/<int:pk>/', views.EquipoDetalle.as_view(), name='equipo_detalle'),

    #PROCESADORES
    path('procesador/listar/', views.ProcesadorListar.as_view(), name='procesador_listar'),
    path('procesador/crear/', views.ProcesadorCrear.as_view(), name='procesador_crear'),
    path('procesador/editar/<int:pk>', views.ProcesadorEditar.as_view(), name='procesador_editar'),
    path('procesador/eliminar/<int:pk>', views.ProcesadorEliminar.as_view(), name='procesador_eliminar'),

    #RAMS
    path('ram/listar/', views.RamListar.as_view(), name='ram_listar'),
    path('ram/crear/', views.RamCrear.as_view(), name='ram_crear'),
    path('ram/editar/<int:pk>', views.RamEditar.as_view(), name='ram_editar'),
    path('ram/eliminar/<int:pk>', views.RamEliminar.as_view(), name='ram_eliminar'),

    #DISCOS DUROS
    path('disco/listar/', views.DiscoListar.as_view(), name='disco_listar'),
    path('disco/crear/', views.DiscoCrear.as_view(), name='disco_crear'),
    path('disco/editar/<int:pk>', views.DiscoEditar.as_view(), name='disco_editar'),
    path('disco/eliminar/<int:pk>', views.DiscoEliminar.as_view(), name='disco_eliminar'),

    #SO
    path('so/listar/', views.SoListar.as_view(), name='so_listar'),
    path('so/crear/', views.SoCrear.as_view(), name='so_crear'),
    path('so/editar/<int:pk>', views.SoEditar.as_view(), name='so_editar'),
    path('so/eliminar/<int:pk>', views.SoEliminar.as_view(), name='so_eliminar'),


    path('equipo/reporte', reporte_equipos, name='equipos_print_all'),
    #path('responsivas/<int:resp_id>/imprimir/', imprimir_responsiva, name='responsivas_print_one'),

]