from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages

from .forms import UserRegisterForm, LoginForm, CambiarPassForm, VerificacionForm
from .models import User
from .functions import generador_codigo





class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '.'
    #login_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        #generar codigo de registro
        codigo = generador_codigo()

        #crea usuario
        usuario = User.object.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['pass1'],
            full_name = form.cleaned_data['full_name'],
            ocupacion = form.cleaned_data['ocupacion'],
            genero =  form.cleaned_data['genero'],
            dia_nac = form.cleaned_data['dia_nac'],
            cod_registro = codigo
        )
        
        #enviar codigo a email de usuario
        asunto = 'Confirmacion de email'
        mensaje = 'El código de verificación para activar su cuenta es: ' + codigo
        email_remitente = 'rgrsistemas@gmail.com'
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        
        #redirigir a pantalla de validacion
        return HttpResponseRedirect(reverse('users_app:usuario_verificacion', kwargs={'pk': usuario.id}))

    #contexto para cargar imagenes y logos de footer y navbar
    def get_context_data(self, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)

        #context["home"] = Home.objects.en_home()
        return context



class Login(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        user = authenticate(
            email= form.cleaned_data['email'],
            password= form.cleaned_data['password']
        )
        login(self.request, user)

        return super(Login, self).form_valid(form)

    #contexto para cargar imagenes y logos de footer y navbar
    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)

        #context["home"] = Home.objects.en_home()
        return context



class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(reverse('users_app:login'))



class CambiarPassword(LoginRequiredMixin, FormView):
    template_name = 'users/cambiar_pass.html'
    form_class = CambiarPassForm
    success_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            email= usuario.email,
            password= form.cleaned_data['password1']
        )

        if user:
            new_pass = form.cleaned_data['password2']
            usuario.set_password(new_pass)
            usuario.save()

        logout(self.request)
        return super(CambiarPassword, self).form_valid(form)
    
    #contexto para cargar imagenes y logos de footer y navbar
    def get_context_data(self, **kwargs):
        context = super(CambiarPassword, self).get_context_data(**kwargs)

        #context["home"] = Home.objects.en_home()
        return context



class CodVerificacionView(FormView):
    template_name = 'users/verificacion.html'
    form_class = VerificacionForm
    success_url = reverse_lazy('users_app:login')

    def get_form_kwargs(self):
        kwargs = super(CodVerificacionView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        User.object.filter(id=self.kwargs['pk']).update(is_active=True)

        return super(CodVerificacionView, self).form_valid(form)
