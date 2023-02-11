from keyword import kwlist
from urllib import request
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import json
from django.contrib import messages
import datetime
from django.utils import timezone
from django.contrib.auth import authenticate

from applications.catalogos.views import EmpleadoListar
from applications.catalogos.forms import EmpleadoForm

from .models import Detalle, Responsiva
from .forms import ResponsivaForm
from applications.catalogos.models import Empleado, Equipo

from applications.home.views import SinPrivilegios




#****************************************
#         CLASES PARA RESPONSIVAS 
#****************************************
class ResponsivaListar(SinPrivilegios, generic.ListView):
    permission_required = "responsivas.view_responsiva"
    model = Responsiva
    template_name = 'responsivas/listar.html'
    context_object_name = 'obj'

    # def get_context_data(self, **kwargs):
    #     context = super(ResponsivaListar, self).get_context_data(**kwargs)

    #     context["detalle"] = Detalle.
    #     return context



@login_required(login_url='/login/')
@permission_required('responsivas.change_responsiva', login_url='bases:sin_privilegios')
def responsivas(request, responsiva_id=None):
    template_name =  'responsivas/responsiva.html'
    equipo = Equipo.objects.filter(status='Libre', activo='Si')

    form_resp = {}
    contexto = {}

    if request.method == 'GET':
        form_resp = ResponsivaForm()
        enc = Responsiva.objects.filter(pk=responsiva_id).first()
        emp = Empleado.objects.filter(tiene_responsiva='No')

        if enc:
            det = Detalle.objects.filter(responsiva=enc)
            fecha_entrega = datetime.date.isoformat(enc.fecha_entrega)
            #fecha_entrega = datetime.today().strftime('%Y-%m-%d')
            #fecha_devolucion = datetime.date.isoformat(enc.fecha_devolucion)
            e = {
                'fecha_entrega': fecha_entrega,
                #'fecha_devolucion': enc.fecha_devolucion,
                'estado_entrega': enc.estado_entrega,
                'no_responsiva': enc.no_responsiva,
                'empleado': enc.empleado,
                'observaciones': enc.observaciones,
                'recibe_devolucion': enc.recibe_devolucion,
            }
            form_resp = ResponsivaForm(e)
        else:
            det = None
        
        contexto = {'equipos':equipo, 'encabezado':enc, 'detalle':det, 'form_enc':form_resp}


    if request.method == 'POST':
        fecha_entrega = request.POST.get("fecha_entrega")
        #fecha_devolucion  = request.POST.get("fecha_devolucion")
        estado_entrega = request.POST.get("estado_entrega")
        no_responsiva = request.POST.get("no_responsiva")
        empleado = request.POST.get("empleado")
        observaciones = request.POST.get("observaciones")
        recibe_devolucion = request.POST.get("recibe_devolucion")

        #CREA ENCABEZADO
        if not responsiva_id:
            emp = Empleado.objects.get(pk=empleado)

            enc = Responsiva(
                fecha_entrega = fecha_entrega,
                #fecha_devolucion = fecha_devolucion,
                estado_entrega = estado_entrega,
                no_responsiva = no_responsiva,
                empleado = emp,
                observaciones = observaciones,
                recibe_devolucion = recibe_devolucion,
                usuario_crea = request.user,
            )

            if enc:
                enc.save()
                responsiva_id = enc.id
                

        else:
            #EDITA ENCABEZADO
            enc = Responsiva.objects.filter(pk=responsiva_id).first()
            emp = Empleado.objects.get(pk=empleado)
            if enc:
                enc.fecha_entrega = fecha_entrega
                #enc.fecha_devolucion = fecha_devolucion
                #enc.estado_entrega = estado_entrega
                enc.no_responsiva = no_responsiva
                enc.observaciones = observaciones
                enc.recibe_devolucion = recibe_devolucion
                enc.empleado = emp
                usuario_modifica = request.user.email
                enc.save()
            
        if not responsiva_id:
            return redirect('responsivas_app:responsiva_listar')


        #CREA DETALLE
        equipo = request.POST.get("id_id_equipo")
        cantidad  = request.POST.get("id_cantidad_detalle")

        equi = Equipo.objects.get(pk=equipo)

        det = Detalle(
            responsiva = enc,
            equipo = equi,
            cantidad = cantidad,
            usuario_crea = request.user,
            categoria_id = equi.categoria_id,
        )

        if det:
            det.save()

        return redirect("responsivas_app:responsiva_editar", responsiva_id=responsiva_id)  

    return render(request, template_name, contexto)



class BorrarDetalle(SinPrivilegios, generic.DeleteView):
    permission_required = 'responsivas.delete_detalle'
    model = Detalle
    template_name = 'responsivas/eliminar_detalle.html'
    context_object_name = 'obj'

    def get_success_url(self):
        responsiva_id = self.kwargs['responsiva_id']
        return reverse_lazy('responsivas_app:responsiva_editar', kwargs={'responsiva_id': responsiva_id})



# @login_required(login_url='/login/')
# @permission_required('resp.change_responsiva', login_url='bases:sin_privilegios')
# def devolver_responsiva(request, responsiva_id):
#     template_name =  'responsivas/devolver.html'
#     resp = Responsiva.objects.filter(pk=responsiva_id).first()
#     det = Detalle.objects.filter(responsiva_id=resp)
#     #equi = Equipo.objects.filter(pk=det.equipo.equipo_id)

#     if det:
#         context = {"det":det, "resp":resp}

    
#     if request.method == "POST":
#         usr = request.POST.get('usuario')
#         pas = request.POST.get('pass')

#         user = authenticate(username=usr, password=pas)

#         if not user:
#             return HttpResponse("Usuario o contraseña incorrecta")

#         if not user.is_active:
#           return HttpResponse("Usuario inactivo")  

#         if user.is_superuser or user.has_perm("resp.supervisor_det"):
#             det.delete()

#             return HttpResponse("ok")

#         return HttpResponse("Usuario no autorizado")  

#     return render(request, template_name, context)


@login_required(login_url='/login/')
@permission_required('responsivas.change_responsiva', login_url='home_app:sin_privilegios')
def devolver_responsiva(request, responsiva_id):
    template_name =  'responsivas/devolver.html'

    resp = Responsiva.objects.filter(pk=responsiva_id).first()
    det = Detalle.objects.filter(responsiva_id=resp)
    #equi = Equipo.objects.filter(pk=det.equipo.equipo_id)

    if det:
        context = {"det":det, "resp":resp}

    
    if request.method == "POST":
        usr = request.POST.get('email')
        pas = request.POST.get('pass')

        user = authenticate(email=usr, password=pas)

        if not user:
            return HttpResponse("Usuario o contraseña incorrecta")

        if not user.is_active:
          return HttpResponse("Usuario inactivo")  

        if user.is_superuser or user.has_perm("responsivas.supervisor_det"):
            resp.recibe_devolucion = user.full_name 
            resp.save()
            det.delete()

            return HttpResponse("ok")

        return HttpResponse("Usuario no autorizado")  

    return render(request, template_name, context)



class ResponsivaEliminar(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    permission_required = 'responsivas.delete_responsiva'
    model = Responsiva
    template_name = 'responsivas/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('responsivas_app:responsiva_listar')
    success_message = "Responsiva eliminada correctamente"



#CODIGO PARA ELIMINAR LA RESPONSIVA
# @login_required(login_url='/login/')
# @permission_required('responsivas.view_responsiva', login_url='home_app:sin_privilegios')
# def devolver_responsiva(request, responsiva_id=None):
#     template_name =  'catalogos/responsivas/listar.html'
#     resp = Responsiva.objects.filter(pk=responsiva_id).first()
#     det = Detalle.objects.filter(responsiva_id=resp)
#     if det:
#         det.activo = 'No'
#         det.update()

#         return redirect("responsivas_app:responsiva_listar")  

#     return render(request, 'responsivas/devolver.html',{'responsiva_id':responsiva_id})




#CODIGO PARA QUE QUEDE SELECCIONADO EL EMPLEADO AL AGREGARLO
# @login_required(login_url='/login/')
# @permission_required('resp.change_empleado', login_url='bases:sin_privilegios')
# def empleado_resp(request, pk=None):
#     template_name = "empleados/formulario.html"
#     context = {}

#     if request.method == 'GET':
#         context['t'] = 'fc'
#         if not pk:
#             form = EmpleadoForm()
#         else:
#             empleado = Empleado.objects.filter(id=pk).first()
#             form = EmpleadoForm(instance=empleado)
#             context['obj'] = empleado
#         context['form'] = form
#     else:
#         nombre = request.POST.get("nombre")
#         apellidos = request.POST.get("apellidos")
#         puesto = request.POST.get("puesto")
#         depto = request.POST.get("depto")
#         telefono = request.POST.get("telefono")
#         email = request.POST.get("email")
#         foto = request.POST.get("foto")
#         tiene_responsiva = request.POST.get("tiene_responsiva")
#         user = request.user

#         if not pk:
#             empleado = Empleado.objects.create(
#                 nombre = nombre,
#                 apellidos = apellidos,
#                 puesto = puesto,
#                 depto = depto,
#                 telefono = telefono,
#                 email = email,
#                 foto = foto,
#                 tiene_responsiva = tiene_responsiva,
#                 usuario_crea = user
#             )
#         else:
#             empleado = Empleado.objects.filter(id=pk).first()
#             empleado.nombre = nombre
#             empleado.apellidos = apellidos
#             empleado.puesto = puesto
#             empleado.depto = depto
#             empleado.telefono = telefono
#             empleado.email = email
#             empleado.foto = foto
#             empleado.tiene_responsiva = tiene_responsiva
#             empleado.usuario_edita = user.id

#         empleado.save()
#         if not empleado:
#             return HttpResponse("Error al guardar el registro")

#         id = empleado.id
#         return HttpResponse(id)

#     return render(request, template_name, context)
