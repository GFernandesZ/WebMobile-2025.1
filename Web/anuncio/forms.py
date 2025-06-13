from django.forms import ModelForm
from anuncio.models import Anuncio
from django import forms
from veiculo.models import Veiculo

class FormularioAnuncio(ModelForm):
    class Meta:
        model = Anuncio
        fields = ['veiculo', 'titulo', 'descricao', 'preco', 'ativo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['veiculo'].label_from_instance = lambda obj: f"{obj.modelo} - {obj.ano}"