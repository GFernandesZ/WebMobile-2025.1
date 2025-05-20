from django.forms import ModelForm
from anuncio.models import Anuncio
from django.forms import ModelForm

class FormularioAnuncio(ModelForm):
    class Meta:
        model = Anuncio
        exclude = []