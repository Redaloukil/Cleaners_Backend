from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError
from users.models import User

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(phone_number=username)
        except UserModel.DoesNotExist:
            raise ValidationError("Le numéro de télephone/email ou le mot de passe n'est pas valide")
        else:
            if user.check_password(password):
                return user
        raise ValidationError("Le numéro de télephone/email ou le mot de passe n'est pas valide")
