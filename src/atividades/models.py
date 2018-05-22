from django.db import models

class Atividade(models.Model):
    nome = models.CharField(max_length = 30)
    descricao = models.TextField(max_length=200)
    prazo = models.DateTimeField()
    em_grupo = models.BooleanField(default =  False)
    object = models.Manager()

    escolha_trofeu = (
        (3, 'Bronze'),
        (5, 'Prata'),
        (7, 'Ouro'),
    )

    trofeu = models.IntegerField(choices =escolha_trofeu, default =1)

    def __str__(self):
        return f'Atividade: {self.nome}\n'

class Usuario(models.Model):
    nome = models.CharField(max_length = 30)
    cpf = models.CharField(max_length = 11)
    escolha_sexo = (
        ('masc', 'masculino'),
        ('fem', 'feminino'),
        ('open', 'não declarado')
    )

    sexo = models.CharField(max_length = 20, choices = escolha_sexo,default =  'open' )
    senha = models.CharField(max_length = 50)
    professor = models.BooleanField(default = False)
