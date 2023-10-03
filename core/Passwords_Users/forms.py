from django.forms import ModelForm
from .models import Passwords_users


class PasswordsUsersform(ModelForm):
    class Meta:
        model = Passwords_users
        fields = [
            "password_name",
            "password_username",
            "password_email",
            "password_origin",
            "password",
        ]
