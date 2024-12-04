from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Solicitud
from .forms import SolicitudForm
from rest_framework.viewsets import ModelViewSet
from .serializers import SolicitudSerializer
from django.shortcuts import render, redirect
from .forms import AlumnoForm
from .models import Alumno

def listar_alumnos(request):
    alumnos = Alumno.objects.all()  # Obtiene todos los alumnos registrados
    return render(request, 'canalizaciones/listar_alumnos.html', {'alumnos': alumnos})

def registrar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo alumno en la base de datos
            return redirect('listar_alumnos')  # Redirige a la lista de alumnos (deberás crear esta vista)
    else:
        form = AlumnoForm()
    return render(request, 'canalizaciones/registrar_alumno.html', {'form': form})


class SolicitudListView(ListView):
    model = Solicitud
    template_name = 'canalizaciones/solicitudes.html'
    context_object_name = 'solicitudes'  # Nombre para usar en el template


class SolicitudCreateView(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'canalizaciones/crear_solicitud.html'
    success_url = reverse_lazy('listar_solicitudes')  # Redirige al listado después de crear

class SolicitudViewSet(ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
