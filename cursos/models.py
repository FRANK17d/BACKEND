from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, default='')
    imagen = CloudinaryField('imagen', folder='categorias', blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

class Curso(models.Model):
    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(default='')
    duracion = models.IntegerField(help_text="Duración en horas", default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    instructor = models.CharField(max_length=100, default='')
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='basico')
    imagen = CloudinaryField('imagen', folder='cursos', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cursos')
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-creado_en']
