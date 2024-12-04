from django import forms
from .models import Solicitud
from .models import Alumno


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['alumno', 'tipo_canalizacion', 'descripcion']  # Campos que se mostrarán en el formulario
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe la solicitud'}),
        }  
    alumno = forms.ModelChoiceField(queryset=Alumno.objects.all(), empty_label="Selecciona un alumno", label="Alumno")

    tipo_canalizacion = forms.ChoiceField(
        choices=Solicitud.TIPOS_CANALIZACION,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'matricula', 'grupo', 'email']
