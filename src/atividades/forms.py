from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Atividade
from datetime import datetime

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = ['nome', 'descricao', 'prazo', 'em_equipe', 'trofeu']

    def clean_nome(self):
        nome = self.cleaned_data['nome'] 

        if(nome[0].isdigit()):
            raise ValidationError('Nome de atividades não podem começar com letras')
        elif(nome.length <= 3 ):
            raise ValidationError("Nome de atividade muito curto, utiliza pelo menos 4 caracteres")

        return nome
    
    def clean_prazo(self):
        data_completa_prazo = self.cleaned_data['prazo']

        if (datetime.now() >= data_completa_prazo):
            raise ValidationError('Prazo inserido está no passado, logo ele é incoerente')
        
        return data_completa_prazo