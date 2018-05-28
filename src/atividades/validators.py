from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class CadastroAtividade(object):
   def __init__(self, word_1='python', word_2='password'):
       self.word_1 = word_1
       self.word_2 = word_2

   def validate(self, password, user=None):
       if self.word_1 in password or self.word_2 in password:
           raise ValidationError(
               _("You cannot include '%s' or '%s' in your password." %
                 (self.word_1, self.word_2)),
               code='Invalid password',
           )

   def get_help_text(self):
       return _("You cannot include '%s' or '%s' in your password." % (self.word_1, self.word_2))
