from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculo.as_view(), name="listar-veiculo"),
    path('novo/', CriarVeiculo.as_view(), name="criar-veiculo"),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name="foto-veiculo"),
    #Em  str:arquivo, str pode ser substituido por id, por maior segurança
]