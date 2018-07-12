from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Atividade, Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import User
from datetime import datetime

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        labels = {
            "upload": "Documento de justificativa"
        }
        fields = ['nome', 'descricao', 'prazo', 'em_equipe', 'trofeu']
        

    def clean_nome(self):
        nome = self.cleaned_data['nome'] 

        if(nome[0].isdigit()):
            raise ValidationError('Nome de atividades não podem começar com letras')
        elif(nome.length <= 3 ):
            raise ValidationError("Nome de atividade muito curto, utilize pelo menos 4 caracteres")

        return nome
    
    def clean_prazo(self):
        data_completa_prazo = self.cleaned_data['prazo']

        if (datetime.now() >= data_completa_prazo):
            raise ValidationError('Prazo inserido está incorreto')
        
        return data_completa_prazo

class CriarUsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        labels = {
            "password": "Senha"
        }

        fields = '__all__'
        exclude = 'is_active', 'is_admin', 'last_login'

  