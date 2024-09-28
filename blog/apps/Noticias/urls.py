
from django.urls import path
from . import views

app_name = 'Noticias'

urlpatterns = [
    path('listar/',views.ListarLibros, name = 'listar_libros'),
    path('listar_c', views.ListarLibros_clase.as_view(), name = 'listar_libros_clase'),

    path('detalle/<int:pk>',views.DetalleLibro, name = 'detalle_libro'),
    path('detalle_c/<int:pk>',views.DetalleLibro_clase.as_view(), name = 'detalle_libro_clase'),

]