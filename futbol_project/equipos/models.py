from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fundacion = models.PositiveIntegerField()
    estadio = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)
    presidente = models.CharField(max_length=100, blank=True)
    colores = models.CharField(max_length=100, help_text="Colores del equipo separados por coma")
    titulos_liga = models.PositiveIntegerField(default=0)
    titulos_copa = models.PositiveIntegerField(default=0)
    titulos_internacionales = models.PositiveIntegerField(default=0)
    presupuesto_anual = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    sitio_web = models.URLField(blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Equipo de Fútbol"
        verbose_name_plural = "Equipos de Fútbol"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"

    def colores_lista(self):
        return [color.strip() for color in self.colores.split(',')]