from django.contrib import admin
from django.urls import path, include
from anuncio.views import *

urlpatterns = [
    path('', ListarAnuncio.as_view(), name="listar-anuncio"),
    path('novo/', CriarAnuncio.as_view(), name="criar-anuncio"),
    path('fotos/<str:arquivo>/', FotoAnuncio.as_view(), name="foto-anuncio"),
    #Em str:arquivo, str pode ser substituido por id, por maior segurança
    path('<int:pk>/', EditarAnuncio.as_view(), name="editar-anuncio"),
    path('deletar/<int:pk>/', DeletarAnuncio.as_view(), name="deletar-anuncio"),
]