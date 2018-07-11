from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
"""
class Trofeu(models.Model):
    nome = models.CharField(max_length=30)
    pontuacao = models.IntegerField(primary_key=True)
    icone = models.ImageField(upload_to=f'trofeus/{nome}', blank = True, null = True)

    def __str__(self):

        if(self.pontuacao > 1):
            return f"{self.nome}-{self.pontuacao} pontos"
        else:
            return f"{self.nome}-{self.pontuacao} ponto"
"""

TROFEU_DEFAULT_ID = 1

class Atividade(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=200)
    prazo = models.DateTimeField()
    em_equipe = models.BooleanField(default=True)
    object = models.Manager()

    escolha_trofeu = (
        (3, 'Bronze'),
        (5, 'Prata'),
        (7, 'Ouro'),
    )


    trofeu = models.IntegerField(choices = escolha_trofeu, default =1)

    def __str__(self):
        return f'Atividade: {self.nome}, trofeu: {self.trofeu}\n'

'''
        trofeu1 = models.ForeignKey(
        Trofeu, related_name='trofeu1', on_delete=models.PROTECT, default = TROFEU_DEFAULT_ID)

    trofeu2 = models.ForeignKey(
        Trofeu, related_name='trofeu2', on_delete=models.PROTECT, blank = True, null = True)

    trofeu3 = models.ForeignKey(
         Trofeu, related_name='trofeu3', on_delete=models.PROTECT, blank=True, null=True)
'''

class UsuarioManager(BaseUserManager):

    def create_user(self, email, cpf, sexo, professor, password=None):
        """
        Cria e salva um usuário com dado email, cpf, sexo,
        se ele é professor e senha opcional
        """
        if not email:
            raise ValueError('Usuários deverão possuir um email')

        user = self.model(
            email=self.normalize_email(email),
            cpf=cpf,
            sexo = sexo,
            professor = professor
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cpf, sexo, professor, password):
        """
        Cria e salva um super usuário com dado email, cpf, sexo, se ele
        é professor e senha obrigatória 
        """
        user = self.create_user(
            email,
            cpf=cpf,
            sexo = sexo,
            professor = professor,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, primary_key = True)
    email = models.EmailField(max_length = 120, default = 'exemplo@exemplo.com', unique =True)
    instituicao = models.CharField(max_length = 50, blank = True, null = True)
    escolha_sexo = (
        ('masc', 'masculino'),
        ('fem', 'feminino'),
        ('open', 'não declarado')
    )

    sexo = models.CharField(
        max_length=20, choices=escolha_sexo, default='open')
    professor = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    objects = UsuarioManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    def get_short_name(self):
        return self.nome
    
    @property
    def is_staff(self):
        return self.professor

    def has_module_perms(self, atividades):
        return True

    USERNAME_FIELD = 'email'

    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['nome', 'cpf', 'sexo',  'professor' ]


