from django.contrib import admin
from anuncio.models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'preco', 'ativo']
    search_fields = ['modelo']

admin.site.register(Anuncio, AnuncioAdmin)
