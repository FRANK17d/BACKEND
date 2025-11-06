from rest_framework import serializers
from .models import Categoria, Curso

class CategoriaSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'imagen', 'imagen_url', 'creado_en', 'actualizado_en']
        read_only_fields = ['creado_en', 'actualizado_en']
    
    def get_imagen_url(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None

class CursoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    imagen_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'descripcion', 'duracion', 'precio', 'instructor', 'nivel', 
                  'imagen', 'imagen_url', 'categoria', 'categoria_nombre', 'activo', 'creado_en', 'actualizado_en']
        read_only_fields = ['creado_en', 'actualizado_en']
    
    def get_imagen_url(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None

class CursoDetailSerializer(CursoSerializer):
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta(CursoSerializer.Meta):
        fields = '__all__'