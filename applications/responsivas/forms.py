from django import forms

from applications.catalogos.models import Empleado
from .models import Responsiva

#****************************************
#       FORMULARIO PARA RESPONSIVA 
#****************************************
class ResponsivaForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(
        queryset = Empleado.objects.filter(activo='Si') #tiene_responsiva='No'
    )



    class Meta:
        model = Responsiva
        fields = ('no_responsiva', 'fecha_entrega', 'fecha_devolucion', 'estado_entrega', 'empleado', 'observaciones')
       
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['estado_entrega'].widget.attrs['readonly'] = True
