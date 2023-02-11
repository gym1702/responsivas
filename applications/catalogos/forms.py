from django import forms
from .models import Categoria, Marca, Procesador, Puesto, Departamento, Empleado, Equipo, Ram, Disco, SistemaOperativo


#****************************************
#       FORMULARIO PARA CATEGORIA 
#****************************************
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'activo']
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    
    #Validad que no se duplique el registro
    def clean(self):
        try:
            nombre = Categoria.objects.get(nombre=self.cleaned_data['nombre'].upper())
            if not self.instance.pk:
                raise forms.ValidationError('El nombre ingresado ya existe')
            elif self.instance.pk!=nombre.pk:
                raise forms.ValidationError('El nombre coincide con el de otro registro')
        except Categoria.DoesNotExist:
            pass
        return self.cleaned_data

 

#****************************************
#       FORMULARIO PARA MARCA 
#****************************************
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre', 'descripcion', 'activo')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    

    #Validad que no se duplique el registro
    def clean(self):
        try:
            nombre = Marca.objects.get(nombre=self.cleaned_data['nombre'].upper())
            if not self.instance.pk:
                raise forms.ValidationError('El nombre ingresado ya existe')
            elif self.instance.pk!=nombre.pk:
                raise forms.ValidationError('El nombre coincide con el de otro registro')
        except Marca.DoesNotExist:
            pass
        return self.cleaned_data
        

#****************************************
#       FORMULARIO PARA PUESTOS 
#****************************************
class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = ('nombre', 'funcion', 'activo')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


    #Validad que no se duplique el registro
    def clean(self):
        try:
            nombre = Puesto.objects.get(nombre=self.cleaned_data['nombre'].upper())
            if not self.instance.pk:
                raise forms.ValidationError('El nombre ingresado ya existe')
            elif self.instance.pk!=nombre.pk:
                raise forms.ValidationError('El nombre coincide con el de otro registro')
        except Puesto.DoesNotExist:
            pass
        return self.cleaned_data

    
#****************************************
#       FORMULARIO PARA DEPTOS 
#****************************************
class DeptoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nombre', 'funcion', 'activo')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    
    #Validad que no se duplique el registro
    def clean(self):
        try:
            nombre = Departamento.objects.get(nombre=self.cleaned_data['nombre'].upper())
            if not self.instance.pk:
                raise forms.ValidationError('El nombre ingresado ya existe')
            elif self.instance.pk!=nombre.pk:
                raise forms.ValidationError('El nombre coincide con el de otro registro')
        except Departamento.DoesNotExist:
            pass
        return self.cleaned_data



#****************************************
#       FORMULARIO PARA EMPLEADOS 
#****************************************
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre', 'puesto', 'depto', 'telefono', 'email', 'sexo', 'foto', 'tiene_responsiva', 'activo')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['tiene_responsiva'].widget.attrs['readonly'] = True


    #Validad que no se duplique el registro
    def clean(self):
        try:
            nombre = Empleado.objects.get(nombre=self.cleaned_data['nombre'].upper())
            if not self.instance.pk:
                raise forms.ValidationError('El nombre del empleado ya existe')
            elif self.instance.pk!=nombre.pk:
                raise forms.ValidationError('El nombre del empleado coincide con el de otro registro')
        except Empleado.DoesNotExist:
            pass
        return self.cleaned_data



#****************************************
#       FORMULARIO PARA PROCESADORES 
#****************************************
class ProcesadorForm(forms.ModelForm):
    class Meta:
        model = Procesador
        fields = ('marca', 'numero', 'generacion', 'velocidad', 'activo',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
    
    #Validad que no se duplique el registro
    def clean(self):
        try:
            numero = Procesador.objects.get(numero=self.cleaned_data['numero'].upper())
            if not self.instance.pk:
                raise forms.ValidationError('El numero ingresado ya existe')
            elif self.instance.pk!=numero.pk:
                raise forms.ValidationError('El numero coincide con el de otro registro')
        except Procesador.DoesNotExist:
            pass
        return self.cleaned_data



#****************************************
#       FORMULARIO PARA RAMS 
#****************************************
class RamForm(forms.ModelForm):
    class Meta:
        model = Ram
        fields = ('tipo', 'velocidad', 'frecuencia', 'activo')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    #Validad que no se duplique el registro
    # def clean(self):
    #     try:
    #         tipo = Ram.objects.get(tipo=self.cleaned_data['tipo'].upper())
    #         if not self.instance.pk:
    #             raise forms.ValidationError('El tipo ingresado ya existe')
    #         elif self.instance.pk!=tipo.pk:
    #             raise forms.ValidationError('El tipo coincide con el de otro registro')
    #     except Ram.DoesNotExist:
    #         pass
    #     return self.cleaned_data
        


#****************************************
#       FORMULARIO PARA DISCOS 
#****************************************
class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ('tipo', 'interfaz', 'capacidad', 'activo')
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


#****************************************
#       FORMULARIO PARA Sistema Operativo 
#****************************************
class SoForm(forms.ModelForm):
    class Meta:
        model = SistemaOperativo
        fields = ('nombre', 'arquitectura', 'activo')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })



#****************************************
#       FORMULARIO PARA EQUIPO 
#****************************************
class EquipoForm(forms.ModelForm):
    marca = forms.ModelChoiceField(
        queryset = Marca.objects.filter(activo='Si')
    )

    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(activo='Si')
    )

    ram = forms.ModelChoiceField(
        queryset = Ram.objects.filter(activo='Si')
    )

    procesador = forms.ModelChoiceField(
        queryset = Procesador.objects.filter(activo='Si')
    )

    disco = forms.ModelChoiceField(
        queryset = Disco.objects.filter(activo='Si')
    )

    so = forms.ModelChoiceField(
        queryset = SistemaOperativo.objects.filter(activo='Si')
    )
    

    class Meta:
        model = Equipo
        fields = ('insumo', 'categoria', 'marca', 'modelo', 'serie', 'condiciones', 'procesador', 
                    'ram', 'disco', 'so', 'pantalla', 'depto', 'usuario', 'caracteristicas', 
                    'status', 'observaciones', 'descripcion', 'activo')
       
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
        self.fields['usuario'].widget.attrs['readonly'] = True
        self.fields['depto'].widget.attrs['readonly'] = True
        self.fields['insumo'].widget.attrs['number'] = True
        
        
    


    #Validad que no se duplique el registro y que insumo se numerico
    def clean(self):
        try:
            insumo = Equipo.objects.get(insumo=self.cleaned_data['insumo'])

            if not self.instance.pk:
                raise forms.ValidationError('El insumo ingresado ya existe')

            elif self.instance.pk!=insumo.pk:
                raise forms.ValidationError('El insumo coincide con el de otro registro')

            # elif self.instance.insumo:
            #     for i in self.instance.insumo:
            #         if i not in '0123456789':
            #             raise forms.ValidationError('El insumo debe ser numerico')

        except Equipo.DoesNotExist:
            pass
        return self.cleaned_data


    # def clean_insumo(self):
    #     insumo = self.cleaned_data['insumo']
    #     for i in insumo:
    #         if i not in '0123456789':
    #             raise forms.ValidationError('El insumo debe ser numerico')
    #     return insumo

