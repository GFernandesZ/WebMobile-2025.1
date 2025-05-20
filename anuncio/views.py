from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import View
from anuncio.models import Anuncio
from anuncio.forms import FormularioAnuncio
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin


class ListarAnuncio(ListView, LoginRequiredMixin):
    model = Anuncio
    context_object_name = 'anuncio'
    template_name = 'anuncio/listar.html'


class CriarAnuncio(CreateView, LoginRequiredMixin):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncio')

class FotoAnuncio(View):

    def get(self, request, arquivo):
        try:
            anuncio = Anuncio.objects.filter(foto='Anuncio/fotos/{}'.format(arquivo)).first()
            # veiculo = veiculo.first()

            print(anuncio)

            return FileResponse(anuncio.foto)
        except ObjectDoesNotExist:
            raise Http404('Fotos não encontradas ou acesso não autorizado')
        except Exception as exception:
            raise exception
    
class EditarAnuncio(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-anuncio')


class DeletarAnuncio(LoginRequiredMixin, DeleteView):
    
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncio')