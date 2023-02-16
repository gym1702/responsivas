from keyword import kwlist
from urllib import request
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.contrib import messages
import datetime
from django.utils import timezone
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from applications.catalogos.views import EmpleadoListar
from applications.catalogos.forms import EmpleadoForm

from .models import Detalle, Responsiva, ResponsivaBackup, DetalleBackup
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

    def get_queryset(self):
        return Responsiva.objects.filter(activo='Si')


#
@login_required(login_url='/login/')
@permission_required('responsivas.change_responsiva', login_url='home_app:sin_privilegios')
def responsivas(request, responsiva_id=None):
    template_name =  'responsivas/responsiva.html'
    equipo = Equipo.objects.filter(status='Libre', activo='Si')

    form_resp = {}
    contexto = {}

    if request.method == 'GET':
        form_resp = ResponsivaForm()
        enc = Responsiva.objects.filter(pk=responsiva_id).first()
        emp = Empleado.objects.filter(tiene_responsiva='No')
        #
        #enc2 = ResponsivaBackup.objects.filter(pk=responsiva_id).first()

        if enc:
            det = Detalle.objects.filter(responsiva=enc)
            fecha_entrega = datetime.date.isoformat(enc.fecha_entrega)
            e = {
                'fecha_entrega': fecha_entrega,
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
                estado_entrega = estado_entrega,
                no_responsiva = no_responsiva,
                empleado = emp,
                observaciones = observaciones,
                recibe_devolucion = recibe_devolucion,
                usuario_crea = request.user,
            )

            # 
            # encbackup = ResponsivaBackup(
            #     fecha_entrega = fecha_entrega,
            #     estado_entrega = estado_entrega,
            #     no_responsiva = no_responsiva,
            #     empleado = emp,
            #     observaciones = observaciones,
            #     recibe_devolucion = recibe_devolucion,
            #     usuario_crea = request.user,
            # )

            if enc:
                enc.save()
                #encbackup.save()
                responsiva_id = enc.id
                
        else:
            #EDITA ENCABEZADO
            enc = Responsiva.objects.filter(pk=responsiva_id).first()
            #encbackup = ResponsivaBackup.objects.filter(pk=responsiva_id).first()

            emp = Empleado.objects.get(pk=empleado)
            if enc:
                enc.fecha_entrega = fecha_entrega
                enc.no_responsiva = no_responsiva
                enc.observaciones = observaciones
                enc.recibe_devolucion = recibe_devolucion
                enc.empleado = emp
                enc.usuario_modifica = request.user.email
                enc.save()

                #encbackup.fecha_entrega = fecha_entrega
                #encbackup.no_responsiva = no_responsiva
                #encbackup.observaciones = observaciones
                #encbackup.recibe_devolucion = recibe_devolucion
                #encbackup.empleado = emp
                #encbackup.usuario_modifica = request.user.email
                #encbackup.save()
            
            
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
        
        #
        detbackup = DetalleBackup(
            responsiva = enc,
            equipo = equi,
            cantidad = cantidad,
            usuario_crea = request.user,
            categoria_id = equi.categoria_id,
        )

        if det:
            det.save()
            detbackup.save()

        return redirect("responsivas_app:responsiva_editar", responsiva_id=responsiva_id)  

    return render(request, template_name, contexto)



#
class BorrarDetalle(SinPrivilegios, generic.DeleteView):
    permission_required = 'responsivas.delete_detalle'
    model = Detalle
    template_name = 'responsivas/eliminar_detalle.html'
    context_object_name = 'obj'

    def get_success_url(self):
        responsiva_id = self.kwargs['responsiva_id']
        return reverse_lazy('responsivas_app:responsiva_editar', kwargs={'responsiva_id': responsiva_id})


# class BorrarDetalleBackup(SinPrivilegios, generic.DeleteView):
#     permission_required = 'responsivas.delete_detalle'
#     model = DetalleBackup
#     template_name = 'responsivas/eliminar_detalle.html'
#     context_object_name = 'obj'

#     def get_success_url(self):
#         responsiva_id = self.kwargs['responsiva_id']
#         return reverse_lazy('responsivas_app:responsiva_editar', kwargs={'responsiva_id': responsiva_id})



#
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


#
# class ResponsivaEliminar(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
#     permission_required = 'responsivas.delete_responsiva'
#     model = Responsiva
#     template_name = 'responsivas/eliminar.html'
#     context_object_name = 'obj'
#     success_url = reverse_lazy('responsivas_app:responsiva_listar')
#     success_message = "Responsiva eliminada correctamente"



@login_required(login_url='/login/')
@permission_required('responsivas.change_responsiva', login_url='home_app:sin_privilegios')
def eliminar_responsiva(request, pk):
    resp = Responsiva.objects.filter(id=pk).first()
    if request.method == 'POST':
        resp.activo = 'No'
        resp.save()
    
        return redirect('responsivas_app:responsiva_listar')
    
    return render(request, 'responsivas/eliminar.html', {'resp':resp})



class ResponsivaEliminar(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required = 'responsivas.change_responsiva'
    model = Responsiva
    template_name = 'responsivas/eliminar.html'
    context_object_name = 'obj'
    #form_class = ResponsivaForm
    fields = ['activo',]
    success_url = reverse_lazy('responsivas_app:responsiva_listar')
    success_message = "Responsiva eliminada correctamente"

    #OPCIONAL PARA GUARDAR DESPUES DEL GUARDADO
    def form_valid(self, form):
        form.instance.activo = 'No'
        return super().form_valid(form)



class VerDetalleResponsiva(generic.TemplateView):
    permission_required = 'responsivas.view_responsiva'
    #model = Responsiva
    template_name = 'responsivas/detalle.html'
    #context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(VerDetalleResponsiva, self).get_context_data(**kwargs)

        context["obj"] = Responsiva.objects.filter(pk = self.kwargs['pk']).first()

        context['det'] = DetalleBackup.objects.filter(responsiva_id = self.kwargs['pk'])
        return context





