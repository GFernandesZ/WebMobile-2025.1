from rest_framework import serializers
from veiculo.models import Veiculo

class SerializadorVeiculos(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        exclude = []

