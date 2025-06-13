from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from veiculo.models import *
from veiculo.forms import *
from datetime import datetime

class TesteModelVeiculo(TestCase):
    def setUp(self):
        self.instancia = Veiculo(
            marca=1,
            modelo='Fusca',
            ano=datetime.now().year,
            cor=2,
            combustivel=1
        )

    def test_is_new(self):
       self.assertTrue(self.instancia.veiculo_novo)
       self.instancia.ano = datetime.now().year - 5
       self.assertFalse(self.instancia.veiculo_novo)

    def test_year_use(self):
       self.instancia.ano = datetime.now().year - 10
       self.assertEqual(self.instancia.anos_de_uso(), 10)

class TestesViewListarVeiculos (TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('listar-veiculo')
        Veiculo(marca=1, modelo='Fusca', ano=2, cor=3, combustivel=1).save()
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('veiculo')), 1)

class TestesViewCriarVeiculo (TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculo')
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
    
    def test_post(self):
        data = {
            'marca': 1,
            'modelo': 'Fusca',
            'ano': datetime.now().year,
            'cor': 2,
            'combustivel': 1
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculo'))

        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'Fusca')

class TestesViewEditarVeiculo (TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.instancia = Veiculo(marca=1, modelo='Fusca', ano=datetime.now().year, cor=2, combustivel=1)
        self.instancia.save()
        self.url = reverse('editar-veiculo', kwargs={'pk': self.instancia.pk})
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)
        self.assertEqual(response.context.get('object').marca, 1)
    
    def test_post(self):
        data = {
            'marca': 2,
            'modelo': 'Combi',
            'ano': 4,
            'cor': 3,
            'combustivel': 1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculo'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 2)
        self.assertEqual(Veiculo.objects.first().modelo, 'Combi')
        self.assertEqual(Veiculo.objects.first().pk, self.instancia.pk)
    
class TestesViewDeletarVeiculo (TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.instancia = Veiculo(marca=1, modelo='Fusca', ano=datetime.now().year, cor=2, combustivel=1)
        self.instancia.save()
        self.url = reverse('deletar-veiculo', kwargs={'pk': self.instancia.pk})
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)

    def test_post(self):
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculo'))
        self.assertEqual(Veiculo.objects.count(), 0)