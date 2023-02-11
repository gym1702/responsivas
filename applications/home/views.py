import imp
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Sum, Count

from datetime import datetime

from applications.responsivas.models import Responsiva, Detalle
from applications.catalogos.models import Equipo


#CLASE SIN PRIVILEGIOS
class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


# VISTA HOME
class Home(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy('users_app:login')

    #DATOS PARA LLENADO DE GRAFICO DE BARRAS
    def get_grafico_desktop(self):
        data = []
        try:
            total = Equipo.objects.filter(categoria_id=1).aggregate(r=Count('categoria_id')).get('r')
            data.append(int(total))
        except:
            pass
        return data

    def get_grafico_laptop(self):
        data = []
        try:           
            total = Equipo.objects.filter(categoria_id=2).aggregate(r=Count('categoria_id')).get('r')
            data.append(int(total))
        except:
            pass
        return data

    def get_grafico_imp(self):
        data = []
        try:           
            total = Equipo.objects.filter(categoria_id=3).aggregate(r=Count('categoria_id')).get('r')
            data.append(int(total))
        except:
            pass
        return data
        
    def get_grafico_otros(self):
        data = []
        try:
            total = Equipo.objects.filter(categoria_id=4).aggregate(r=Count('categoria_id')).get('r')
            data.append(int(total))
        except:
            pass
        return data


    #DATOS PARA EQUIPOS ENTREGADOS
    def get_responsivas_desktop(self):
        try:
            total = Detalle.objects.filter(categoria_id=1).aggregate(r=Sum('cantidad')).get('r')
        except:
            pass
        return total

    def get_responsivas_laptop(self):
        try:
            total = Detalle.objects.filter(categoria_id=2).aggregate(r=Sum('cantidad')).get('r')
        except:
            pass
        return total
    
    def get_responsivas_imp(self):
        try:
            total = Detalle.objects.filter(categoria_id=3).aggregate(r=Sum('cantidad')).get('r')
        except:
            pass
        return total
    
    def get_responsivas_otros(self):
        try:
            total = Detalle.objects.filter(categoria_id=4).aggregate(r=Sum('cantidad')).get('r')
        except:
            pass
        return total


    #ENVIA LOS DATOS AL TEMPLATE
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grafico_desktop'] = self.get_grafico_desktop()
        context['grafico_laptop'] = self.get_grafico_laptop()
        context['grafico_imp'] = self.get_grafico_imp()
        context['grafico_otros'] = self.get_grafico_otros()

        context['desktop'] = self.get_responsivas_desktop()
        context['laptop'] = self.get_responsivas_laptop()
        context['imp'] = self.get_responsivas_imp()
        context['otros'] = self.get_responsivas_otros()
        return context
   


# VISTA HOME SIN PRIVILEGIOS
class HomeSinPrivilegios(LoginRequiredMixin, TemplateView):
    login_url = 'bases:login'
    template_name = 'bases/sin_privilegios.html'


