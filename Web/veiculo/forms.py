from django.forms import ModelForm
from veiculo.models import Veiculo
from django.forms import ModelForm

class FormularioVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        exclude = []