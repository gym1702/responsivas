from django.urls import path

from . import views


app_name = 'users_app'

urlpatterns = [
    path('usuario-crear/', views.UserRegisterView.as_view(), name='usuarios_crear'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('cambiar-pass/', views.CambiarPassword.as_view(), name='cambiar_pass'),
    path('usuario-verificacion/<pk>/', views.CodVerificacionView.as_view(), name='usuario_verificacion'),
]

