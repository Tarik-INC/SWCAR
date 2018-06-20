from datetime import datetime, timedelta
from django.test import TestCase
from .models import Atividade
from .forms import AtividadeForm


class AtividadeFormTestes(TestCase):

    def setUp(self):
        self.NOME_CORRETO = 'Testes'
        self.NOME_INCORRETO_CURTO = 'es'
        self.NOME_INCORRETO_LETRA = '5Testes'
        self.DESCRICAO = 'Atividade utilizada em teste unitario'
        self.PRAZO_CORRETO = datetime.now() + timedelta(days=5)
        self.PRAZO_INCORRETO = datetime.now() + timedelta(days=-5)
        self.TROFEU = 3
        self.EM_EQUIPE = True

    def test_atividade_prazo_passado(self):
        """[Método responsável por testar se atividades cadastradas que
            possuem inconsistência no prazo(prazo devem ser uma data futura)
            são rejeitadas pelo sistema]
        """

        AtividadePrazoErrado = Atividade(nome=self.NOME_CORRETO, descricao=self.DESCRICAO,
                                         prazo=self.PRAZO_INCORRETO, em_equipe=self.EM_EQUIPE, trofeu=self.TROFEU)

        FormAtividadePrazoErrado = AtividadeForm(instance=AtividadePrazoErrado)
        self.assertEquals(FormAtividadePrazoErrado.is_valid(), False)

<<<<<<< HEAD:src/atividades/tests.py
    def test_atividade_nome_incorreto(self):
        """[Método responsável por testar se atividades cadastradas que 
            possuem nomes começando com letras são rejeitadas pelo sistema]
        """
       
        AtividadeNomeIncorreto = Atividade(nome=self.NOME_INCORRETO, descricao=self.DESCRICAO,
=======
    def test_atividade_nome_incorreto_letra_seguida_caractere(self):

        AtividadeNomeIncorreto = Atividade(nome=self.NOME_INCORRETO_LETRA, descricao=self.DESCRICAO,
>>>>>>> 5d2ea14243849cced06cf2ff58beb80bddcae1a0:src/atividades/tests_forms.py
                                           prazo=self.PRAZO_CORRETO, em_equipe=self.EM_EQUIPE, trofeu=self.TROFEU)

        FormAtividadeNomeIncorreto = AtividadeForm(
            instance=AtividadeNomeIncorreto)
        self.assertEquals(FormAtividadeNomeIncorreto.is_valid(), False)

<<<<<<< HEAD:src/atividades/tests.py
    def test_atividade_preenchida_corretamente(self):
        """[Método responsável por testar se atividades cadastradas são aceitas
            pelo sistema]
        """
=======
    def test_atividade_nome_incorreto_curto(self):
>>>>>>> 5d2ea14243849cced06cf2ff58beb80bddcae1a0:src/atividades/tests_forms.py

        AtividadeNomeCorreto = Atividade(nome=self.NOME_INCORRETO_CURTO, descricao=self.DESCRICAO,
                                         prazo=self.PRAZO_CORRETO, em_equipe=self.EM_EQUIPE, trofeu=self.TROFEU)

        FormAtividadeNomeCorreto = AtividadeForm(instance=AtividadeNomeCorreto)
<<<<<<< HEAD:src/atividades/tests.py
        self.assertTrue(FormAtividadeNomeCorreto.is_valid())
=======
        self.assertFalse(FormAtividadeNomeCorreto.is_valid())
>>>>>>> 5d2ea14243849cced06cf2ff58beb80bddcae1a0:src/atividades/tests_forms.py