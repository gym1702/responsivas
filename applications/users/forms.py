from django import forms
from django.contrib.auth import authenticate

from .models import User



class UserRegisterForm(forms.ModelForm):

    pass1 = forms.CharField(
        label= 'Contraseña',
        required= True,
        widget= forms.PasswordInput()        
    )

    pass2 = forms.CharField(
        label= 'Contraseña',
        required= True,
        widget= forms.PasswordInput()        
    )

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'ocupacion',
            'dia_nac',
            'genero',
        )  

        widgets = {
            'email': forms.EmailInput(),
            'dia_nac': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
        }      

    #Da estilos de bootstrap a todos los campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })    

    #Valida que la contraseña sea igual
    def clean_pass2(self):
        if self.cleaned_data['pass1'] != self.cleaned_data['pass2']:
            self.add_error('pass2', 'La contraseña no coincide')



class LoginForm(forms.Form):

    email = forms.CharField(
        label= 'Email',
        required= True,
        widget= forms.TextInput()        
    )

    password = forms.CharField(
        label= 'Contraseña',
        required= True,
        widget= forms.PasswordInput()        
    )

    #Valida si exixte el usuario y contraseña
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        
        return self.cleaned_data


    #Da estilos de bootstrap a todos los campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })



class CambiarPassForm(forms.Form):

    password1 = forms.CharField(
        label= 'Contraseña actual',
        required= True,
        widget= forms.PasswordInput()        
    )

    password2 = forms.CharField(
        label= 'Contraseña nueva',
        required= True,
        widget= forms.PasswordInput()        
    )

    password3 = forms.CharField(
        label= 'Confirmar contraseña',
        required= True,
        widget= forms.PasswordInput()        
    )


    #Valida que las nuevas contraseñas sean iguales
    def clean_password3(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password3']:
            self.add_error('password3', 'La contraseña no coincide')


    #Da estilos de bootstrap a todos los campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })



class VerificacionForm(forms.Form):
    codigo_registro = forms.CharField(required=True)

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificacionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


    #Valida que el codigo enviado sea correcto
    def clean_codigo_registro(self):
        codigo = self.cleaned_data['codigo_registro']

        if len(codigo) == 6:
            #verifica que el codigo y el id son validos
            activo = User.object.cod_validacion(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('El codigo no es valido')
        else:
            raise forms.ValidationError('El codigo no es valido')

