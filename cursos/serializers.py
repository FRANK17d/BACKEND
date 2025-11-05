from rest_framework import serializers
from .models import Categoria, Curso

class CategoriaSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()
    
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ['creado_en', 'actualizado_en']
    
    def get_imagen(self, obj):
        if obj.imagen:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.imagen.url)
            return obj.imagen.url
        return None

class CursoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    imagen = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = '__all__'
        read_only_fields = ['creado_en', 'actualizado_en']
    
    def get_imagen(self, obj):
        if obj.imagen:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.imagen.url)
            return obj.imagen.url
        return None

class CursoDetailSerializer(CursoSerializer):
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta(CursoSerializer.Meta):
        fields = '__all__'