from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Categoria, Curso
from .serializers import CategoriaSerializer, CursoSerializer, CursoDetailSerializer

# CRUD para Categorías
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# CRUD para Cursos
class CursoListCreate(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoDetailSerializer

# Vista adicional para obtener cursos por categoría
@api_view(['GET'])
def cursos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    cursos = Curso.objects.filter(categoria=categoria, activo=True)
    serializer = CursoDetailSerializer(cursos, many=True, context={'request': request})
    return Response(serializer.data)
