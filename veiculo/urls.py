from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculo.as_view(), name="listar-veiculo"),
    path('novo/', CriarVeiculo.as_view(), name="criar-veiculo"),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name="foto-veiculo"),
    #Em str:arquivo, str pode ser substituido por id, por maior segurança
    path('<int:pk>/', EditarVeiculos.as_view(), name="editar-veiculo"),
    path('api/', APIListarVeiculos.as_view(), name="api-listar-veiculo"),
    path('deletar/<int:pk>/', DeletarVeiculos.as_view(), name="deletar-veiculo"),
    path('api/deletar/<int:pk>', DeleteAPIVeiculo.as_view(), name="api-listar-anuncio"),
]