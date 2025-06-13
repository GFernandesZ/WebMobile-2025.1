from django.db import models
from datetime import datetime
from anuncio.consts import *
from veiculo.models import Veiculo

class Anuncio(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)