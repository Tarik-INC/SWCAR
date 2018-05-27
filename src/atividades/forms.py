from django.forms import ModelForm
from .models import Atividade

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = ['nome', 'descricao', 'prazo', 'em_equipe', 'trofeu1', 'trofeu2']