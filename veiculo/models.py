from django.db import models
from datetime import datetime
from veiculo.consts import *

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.TextField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField()
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS) 

