from django.test import TestCase, client
from django.urls import reverse
from .models import Atividade
from datetime import datetime, timedelta
from django.utils import timezone

def criar_atividade(nome, descricao, prazo, em_equipe, trofeu ):
    """
    [Função auxiliar aos metódos de teste, utilizada para criar objetos de atividdade]

    Args:
        nome ([string]): [nome de uma atividade]
        descricao ([string]): [descricao de uma atividade]
        prazo ([datetime]): [prazo em objeto datetime python de uma atividade]
        em_equipe ([bool]): [se uma atividade é em equipe( true = sim)]
        trofeu ([int]): [número que descreve um tipo de trofeu ( bronze = 3, prata = 5, ouro = 7)]

    Returns:
        [Atividade]: [retorna um objeto atividade ]
    """

    return Atividade.object.create(nome= nome, descricao = descricao, prazo = prazo, em_equipe = em_equipe, trofeu = trofeu)


class AtividadeViewTestes(TestCase):


    def test_listar_atividades_vazia(self):

        response = self.client.get(reverse('playlist'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['atividades'], [])

    def test_listar_duas_atividades(self):

        criar_atividade('AtividadeTeste01', 'Atividade01 utilizada em teste unitário', 
        datetime.now() + timedelta(days=1), True,3)

        criar_atividade('AtividadeTeste02', 'Atividade02 utilizada em teste unitário',
        datetime.now() + timedelta(days=2), True,5)

        response = self.client.get(reverse('playlist'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['atividades'], ['<Atividade: Atividade: AtividadeTeste01, trofeu: 3\n>', '<Atividade: Atividade: AtividadeTeste02, trofeu: 5\n>'])

    def test_get_deletar_atividade(self):

        atividade1= criar_atividade('AtividadeTeste01', 'Atividade01 utilizada em teste unitário', 
        datetime.now() + timedelta(days=1), True,3)
        
        response = self.client.get(reverse('deletar_atividade', args = [atividade1.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tem certeza que deseja deletar a atividade abaixo?' )

        response = self.client.get(reverse('playlist'))
        self.assertQuerysetEqual(response.context['atividades'], ['<Atividade: Atividade: AtividadeTeste01, trofeu: 3\n>'])

    def test_post_deletar_atividade(self):

        atividade1= criar_atividade('AtividadeTeste01', 'Atividade01 utilizada em teste unitário', 
        datetime.now() + timedelta(days=1), True,3)
        
        post_response = self.client.post(reverse('deletar_atividade', args = [atividade1.id]))
        self.assertRedirects(post_response, reverse('playlist'), status_code = 302)





    