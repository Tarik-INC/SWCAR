from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Atividade, Usuario
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm



class AtividadeSelecionarForm(ModelForm):
    class Meta: 
        model = Atividade
        
        labels = {
            "justificativa": "Documento de justificativa"
        }

        fields = '__all__'


class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
      
        fields = ['nome', 'descricao', 'prazo', 'em_equipe', 'trofeu']
       # exclude = 'justificativa',

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        if(nome[0].isdigit()):
            raise ValidationError(
                'Nome de atividades não podem começar com letras')
        elif(nome.length <= 3):
            raise ValidationError(
                "Nome de atividade muito curto, utilize pelo menos 4 caracteres")

        return nome

    def clean_prazo(self):
        data_completa_prazo = self.cleaned_data['prazo']

        if (datetime.now() >= data_completa_prazo):
            raise ValidationError('Prazo inserido está incorreto')

        return data_completa_prazo


class CriarUsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
       

        fields = '__all__'
        exclude = 'password', 'is_active', 'is_admin', 'last_login'
