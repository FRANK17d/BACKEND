from django.contrib import admin
from .models import Categoria, Curso

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'creado_en', 'actualizado_en']
    list_filter = ['creado_en']
    search_fields = ['nombre', 'descripcion']
    readonly_fields = ['creado_en', 'actualizado_en']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'instructor', 'precio', 'duracion', 'nivel', 'categoria', 'activo', 'creado_en']
    list_filter = ['nivel', 'categoria', 'activo', 'creado_en']
    search_fields = ['nombre', 'instructor', 'descripcion']
    readonly_fields = ['creado_en', 'actualizado_en']
    list_editable = ['activo']
