from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic import View
from veiculo.forms import FormularioVeiculo
from veiculo.models import Veiculo
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404


class ListarVeiculo(ListView):
    model = Veiculo
    context_object_name = 'veiculo'
    template_name = 'veiculo/listar.html'

class CriarVeiculo(CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculo')

class FotoVeiculo(View):

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculos/fotos/{}'.format(arquivo)),
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404('Fotos não encontradas ou acesso não autorizado')
        except Exception as exception:
            raise exception
        