from django.urls import path
from . import views

urlpatterns = [
    # URLs para Categorías
    path('categorias/', views.CategoriaListCreate.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    
    # URLs para Cursos
    path('cursos/', views.CursoListCreate.as_view(), name='curso-list-create'),
    path('cursos/<int:pk>/', views.CursoDetail.as_view(), name='curso-detail'),
    
    # URLs adicionales
    path('cursos/categoria/<int:categoria_id>/', views.cursos_por_categoria, name='cursos-por-categoria'),
]