from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
UserModel = get_user_model()
from .models import User


class authPhoneBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('phone')
        try:
            user = User.objects.get(phone=username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user