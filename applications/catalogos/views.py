from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django .contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse
import json
from django.contrib import messages

from .models import Categoria, Marca, Procesador, Puesto, Departamento, Empleado, Equipo, Ram, Disco, SistemaOperativo

from .forms import CategoriaForm, MarcaForm, PuestoForm, DeptoForm, EmpleadoForm, EquipoForm, ProcesadorForm, RamForm, DiscoForm, SoForm

from applications.responsivas.models import Responsiva

from applications.home.views import SinPrivilegios

from .functions import generador_codigo



#Valida que no se duplique el registro
class MixinFormInvalid:

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self. request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(form.errors, status=400)
        else:
            return response


#****************************************
#         CLASES PARA CATEGORIA 
#****************************************
class CategoriaListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_categoria"
    model = Categoria
    template_name = 'catalogos/categorias/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Categoria.objects.filter(activo='Si')
    

class CategoriaCrear(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, CreateView):
    model = Categoria
    permission_required = 'catalogos.add_categoria'
    template_name = 'catalogos/categorias/formulario.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('catalogos_app:categoria_listar')
    success_message = "Categoría creada correctamente"
    
    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)
    
  
        

class CategoriaEditar(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, UpdateView):
    permission_required = 'catalogos.change_categoria'
    model = Categoria
    template_name = 'catalogos/categorias/formulario.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('catalogos_app:categoria_listar')
    success_message = ("Categoría actualizada correctamente")

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        return super().form_valid(form)



class CategoriaEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_categoria'
    model = Categoria
    template_name = 'catalogos/categorias/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:categoria_listar')
    success_message = "Proceso realizado con éxito"


# @login_required(login_url='/login/')
# @permission_required('catalogos:change_marca', login_url='bases:sin_privilegios')
# def categoria_activar(request, id):
#     categoria = Categoria.objects.filter(pk=id).first()
#     contexto = {}
#     template_name = 'categorias/eliminar.html'
    
#     if not categoria:
#         return redirect('catalogos:categoria_listar')

#     if request.method == 'GET':
#         contexto = {'obj': categoria}
    
#     if request.method == 'POST':
#         categoria.activo='Si'
#         categoria.save()
#         messages.success(request, 'Categoria eliminada correctamente')
#         return redirect('catalogos:categoria_listar')

#     return render(request, template_name, contexto)

    

#****************************************
#         CLASES PARA MARCA 
#****************************************
class MarcaListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_marca"
    model = Marca
    template_name = 'catalogos/marcas/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Marca.objects.filter(activo='Si')


class MarcaCrear(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, CreateView):
    permission_required = 'catalogos.add_marca'
    model = Marca
    template_name = 'catalogos/marcas/formulario.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('catalogos_app:marca_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class MarcaEditar(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, UpdateView):
    permission_required = 'catalogos.change_marca'
    model = Marca
    template_name = 'catalogos/marcas/formulario.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('catalogos_app:marca_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        return super().form_valid(form)



class MarcaEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_marca'
    model = Marca
    template_name = 'catalogos/marcas/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:marca_listar')
    success_message = "Proceso realizado con éxito"



#****************************************
#         CLASES PARA PUESTO 
#****************************************
class PuestoListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_puesto"
    model = Puesto
    template_name = 'catalogos/puestos/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Puesto.objects.filter(activo='Si')


class PuestoCrear(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, CreateView):
    permission_required = 'catalogos.add_puesto'
    model = Puesto
    template_name = 'catalogos/puestos/formulario.html'
    context_object_name = 'obj'
    form_class = PuestoForm
    success_url = reverse_lazy('catalogos_app:puesto_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class PuestoEditar(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, UpdateView):
    permission_required = 'catalogos.change_puesto'
    model = Puesto
    template_name = 'catalogos/puestos/formulario.html'
    context_object_name = 'obj'
    form_class = PuestoForm
    success_url = reverse_lazy('catalogos_app:puesto_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        return super().form_valid(form)



class PuestoEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_puesto'
    model = Puesto
    template_name = 'catalogos/puestos/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:puesto_listar')
    success_message = "Proceso realizado con éxito"



#****************************************
#         CLASES PARA DEPARTAMENTOS 
#****************************************
class DeptoListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_departamento"
    model = Departamento
    template_name = 'catalogos/deptos/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Departamento.objects.filter(activo='Si')


class DeptoCrear(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, CreateView):
    permission_required = "catalogos.add_departamento"
    model = Departamento
    template_name = 'catalogos/deptos/formulario.html'
    context_object_name = 'obj'
    form_class = DeptoForm
    success_url = reverse_lazy('catalogos_app:depto_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class DeptoEditar(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, UpdateView):
    permission_required = "catalogos.change_departamento"
    model = Departamento
    template_name = 'catalogos/deptos/formulario.html'
    context_object_name = 'obj'
    form_class = DeptoForm
    success_url = reverse_lazy('catalogos_app:depto_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        return super().form_valid(form)



class DeptoEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_departamento'
    model = Departamento
    template_name = 'catalogos/deptos/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:depto_listar')
    success_message = "Proceso realizado con éxito"



#****************************************
#         CLASES PARA EMPLEADOS 
#****************************************
class EmpleadoListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_empleado"
    model = Empleado
    template_name = 'catalogos/empleados/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Empleado.objects.filter(activo='Si')
        

class EmpleadoCrear(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, CreateView):
    permission_required = "catalogos.add_empleado"
    model = Empleado
    template_name = 'catalogos/empleados/formulario.html'
    context_object_name = 'obj'
    form_class = EmpleadoForm
    success_url = reverse_lazy('catalogos_app:empleado_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        form.instance.activo='Si'
        if form.instance.sexo == 'Masculino':
            form.instance.foto = '/male-user.png'
        elif form.instance.sexo == 'Femenino':
            form.instance.foto = '/female-user.png'

        return super().form_valid(form)

    #Para crear empleado desde la responsiva
    def get(self, request, *args, **kwargs):
        try:
            t = request.GET["t"]
        except:
            t = None
        
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 't':t})


class EmpleadoEditar(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, UpdateView):
    permission_required = "catalogos.change_empleado"
    model = Empleado
    template_name = 'catalogos/empleados/formulario.html'
    context_object_name = 'obj'
    form_class = EmpleadoForm
    success_url = reverse_lazy('catalogos_app:empleado_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        if form.instance.sexo == 'Masculino':
            form.instance.foto = '/male-user.png'
        elif form.instance.sexo == 'Femenino':
            form.instance.foto = '/female-user.png'
        elif form.instance.sexo == 'No especifica':
            form.instance.foto = '/perfil-user.png'

        return super().form_valid(form)

    
    #Para editar empleado desde la responsiva
    def get(self, request, *args, **kwargs):
        try:
            t = request.GET["t"]
        except:
            t = None
        
        self.object = self.get_object()
        form_class =  self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form, t=t)
        return self.render_to_response(context)



class EmpleadoEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_empleado'
    model = Empleado
    template_name = 'catalogos/empleados/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:empleado_listar')
    success_message = "Proceso realizado con éxito"



#****************************************
#         CLASES PARA PROCESADORES 
#****************************************
class ProcesadorListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_procesador"
    model = Procesador
    template_name = 'catalogos/procesadores/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Procesador.objects.filter(activo='Si')


class ProcesadorCrear(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, CreateView):
    permission_required = "catalogos.add_procesador"
    model = Procesador
    template_name = 'catalogos/procesadores/formulario.html'
    context_object_name = 'obj'
    form_class = ProcesadorForm
    success_url = reverse_lazy('catalogos_app:procesador_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)



class ProcesadorEditar(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, UpdateView):
    permission_required = "catalogos.change_procesador"
    model = Procesador
    template_name = 'catalogos/procesadores/formulario.html'
    context_object_name = 'obj'
    form_class = ProcesadorForm
    success_url = reverse_lazy('catalogos_app:procesador_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        return super().form_valid(form)


class ProcesadorEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_procesador'
    model = Procesador
    template_name = 'catalogos/procesadores/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:procesador_listar')
    success_message = "Proceso realizado con éxito"



#****************************************
#         CLASES PARA RAMS 
#****************************************
class RamListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_ram"
    model = Ram
    template_name = 'catalogos/rams/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Empleado.objects.filter(activo='Si')


class RamCrear(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "catalogos.add_ram"
    model = Ram
    template_name = 'catalogos/rams/formulario.html'
    context_object_name = 'obj'
    form_class = RamForm
    success_url = reverse_lazy('catalogos_app:ram_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class RamEditar(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = "catalogos.change_ram"
    model = Ram
    template_name = 'catalogos/rams/formulario.html'
    context_object_name = 'obj'
    form_class = RamForm
    success_url = reverse_lazy('catalogos_app:ram_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        return super().form_valid(form)



class RamEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_ram'
    model = Ram
    template_name = 'catalogos/rams/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:ram_listar')
    success_message = "Proceso realizado con éxito"



#****************************************
#         CLASES PARA DISCOS 
#****************************************
class DiscoListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_disco"
    model = Disco
    template_name = 'catalogos/discos/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Empleado.objects.filter(activo='Si')


class DiscoCrear(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "catalogos.add_disco"
    model = Disco
    template_name = 'catalogos/discos/formulario.html'
    context_object_name = 'obj'
    form_class = DiscoForm
    success_url = reverse_lazy('catalogos_app:disco_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class DiscoEditar(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = "catalogos.change_disco"
    model = Disco
    template_name = 'catalogos/discos/formulario.html'
    context_object_name = 'obj'
    form_class = DiscoForm
    success_url = reverse_lazy('catalogos_app:disco_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        return super().form_valid(form)



class DiscoEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_disco'
    model = Disco
    template_name = 'catalogos/discos/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:disco_listar')
    success_message = "Proceso realizado con éxito"



#****************************************
#         CLASES PARA SO
#****************************************
class SoListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_sistemaoperativo"
    model = SistemaOperativo
    template_name = 'catalogos/so/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Empleado.objects.filter(activo='Si')


class SoCrear(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "catalogos.add_sistemaoperativo"
    model = SistemaOperativo
    template_name = 'catalogos/so/formulario.html'
    context_object_name = 'obj'
    form_class = SoForm
    success_url = reverse_lazy('catalogos_app:so_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class SoEditar(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = "catalogos.change_sistemaoperativo"
    model = SistemaOperativo
    template_name = 'catalogos/so/formulario.html'
    context_object_name = 'obj'
    form_class = SoForm
    success_url = reverse_lazy('catalogos_app:so_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        return super().form_valid(form)



class SoEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_sistemaoperativo'
    model = SistemaOperativo
    template_name = 'catalogos/so/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:so_listar')
    success_message = "Proceso realizado con éxito"




#****************************************
#         CLASES PARA EQUIPOS 
#****************************************
class EquipoListar(SinPrivilegios, ListView):
    permission_required = "catalogos.view_equipo"
    model = Equipo
    template_name = 'catalogos/equipos/listar.html'
    context_object_name = 'obj'

    # def get_queryset(self):
    #     return Empleado.objects.filter(activo='Si')


class EquipoCrear(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, CreateView):
    permission_required = "catalogos.add_equipo"
    model = Equipo
    template_name = 'catalogos/equipos/formulario.html'
    context_object_name = 'obj'
    form_class = EquipoForm
    success_url = reverse_lazy('catalogos_app:equipo_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        #
        if form.instance.categoria.nombre == 'Desktops':
            form.instance.imagen = '/default-pc.png'
        elif form.instance.categoria.nombre == 'Laptops':
            form.instance.imagen = '/default-lap.png'
        elif form.instance.categoria.nombre == 'Impresoras':
            form.instance.imagen = '/default-imp.jpg'
        #
        if form.instance.insumo == None:
            form.instance.insumo = generador_codigo()
        else:
            form.instance.insumo = form.instance.insumo        

        return super().form_valid(form)



class EquipoEditar(SuccessMessageMixin, MixinFormInvalid, SinPrivilegios, UpdateView):
    permission_required = "catalogos.change_equipo"
    model = Equipo
    template_name = 'catalogos/equipos/formulario.html'
    context_object_name = 'obj'
    form_class = EquipoForm
    success_url = reverse_lazy('catalogos_app:equipo_listar')
    success_message = "Proceso realizado con éxito"

    def form_valid(self, form):
        form.instance.usuario_edita = self.request.user.email
        if form.instance.categoria.nombre == 'Desktops':
            form.instance.imagen = '/default-pc.png'
        elif form.instance.categoria.nombre == 'Laptops':
            form.instance.imagen = '/default-lap.png'
        elif form.instance.categoria.nombre == 'Impresoras':
            form.instance.imagen = '/default-imp.jpg'

        return super().form_valid(form)



class EquipoEliminar(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = 'catalogos.delete_equipo'
    model = Equipo
    template_name = 'catalogos/equipos/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('catalogos_app:equipo_listar')
    success_message = "Proceso realizado con éxito"


class EquipoDetalle(SuccessMessageMixin, SinPrivilegios, DetailView):
    permission_required = 'catalogos.view_equipo'
    model = Equipo
    template_name = 'catalogos/equipos/detalle.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(EquipoDetalle, self).get_context_data(**kwargs)
        return context