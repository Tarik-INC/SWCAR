from atividades.models import Usuario
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist


class MyAuthBackend(object):

    def authenticate(self, request, email, password):
        login_valid = (settings.ADMIN_LOGIN == email)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = Usuario.objects.get(email=email)
            except ObjectDoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = Usuario(email=email)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
