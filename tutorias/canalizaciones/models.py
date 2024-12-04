from django.db import models

# Modelo para representar a los alumnos
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre completo del alumno
    matricula = models.CharField(max_length=20, unique=True)  # Identificador único del alumno
    grupo = models.CharField(max_length=20, blank=True, null=True)  # Grupo al que pertenece
    email = models.EmailField(blank=True, null=True)  # Correo electrónico del alumno

    def __str__(self):
        return f"{self.nombre} ({self.matricula})"


# Modelo para representar las solicitudes de canalización
class Solicitud(models.Model):
    TIPOS_CANALIZACION = [
        ('becas', 'Becas'),
        ('asesorias', 'Asesorías'),
        ('psicologia', 'Atención Psicológica'),
        ('otros', 'Otros'),
    ]

    tipo_canalizacion = models.CharField(
        max_length=10,
        choices=TIPOS_CANALIZACION,
        default='otros',  # Valor por defecto
    )
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)  # Relación con el modelo Alumno
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_canalizacion.capitalize()} para {self.alumno.nombre}"

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"
