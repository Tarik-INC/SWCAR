from datetime import datetime, timedelta
from django.test import TestCase
from .models import Atividade
from .forms import AtividadeForm


class AtividadeFormTestes(TestCase):

   
       
        

    def test_Atividade_Prazo_Passado(self):
        NOME_CORRETO = 'Testes'
        NOME_INCORRETO = '5TESTES'
        DESCRICAO = 'Atividade utilizada em teste unitario'
        PRAZO_CORRETO = datetime.now() + timedelta(days=5)
        PRAZO_INCORRETO = datetime.now() + timedelta(days=-5)
        EM_EQUIPE = True
        TROFEU = 7
        AtividadePrazoErrado = Atividade(nome=NOME_CORRETO, descricao=DESCRICAO,
                                                        prazo=PRAZO_INCORRETO, em_equipe=EM_EQUIPE)
        
        FormAtividadePrazoErrado = AtividadeForm(instance = AtividadePrazoErrado)


        self.assertEquals(FormAtividadePrazoErrado.is_valid(), False)
