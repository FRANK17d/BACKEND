from rest_framework import serializers
from .models import Categoria, Curso
import os

class CategoriaSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'imagen', 'imagen_url', 'creado_en', 'actualizado_en']
        read_only_fields = ['creado_en', 'actualizado_en']
    
    def get_imagen_url(self, obj):
        if obj.imagen:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.imagen.url)
            return obj.imagen.url
        return None
    
    def update(self, instance, validated_data):
        # Si hay una nueva imagen, eliminar la antigua
        if 'imagen' in validated_data and validated_data['imagen']:
            if instance.imagen:
                # Eliminar archivo antiguo si existe
                if os.path.isfile(instance.imagen.path):
                    os.remove(instance.imagen.path)
        return super().update(instance, validated_data)

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
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.imagen.url)
            return obj.imagen.url
        return None
    
    def update(self, instance, validated_data):
        # Si hay una nueva imagen, eliminar la antigua
        if 'imagen' in validated_data and validated_data['imagen']:
            if instance.imagen:
                # Eliminar archivo antiguo si existe
                if os.path.isfile(instance.imagen.path):
                    os.remove(instance.imagen.path)
        return super().update(instance, validated_data)

class CursoDetailSerializer(CursoSerializer):
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta(CursoSerializer.Meta):
        fields = '__all__'