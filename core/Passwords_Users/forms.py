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

    #! Desactiva el aoutocompletado de los campos del formulario
    def __init__(self, *args, **kwargs):
        super(PasswordsUsersform, self).__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({"autocomplete": "off"})
        self.fields["password_name"].widget.attrs.update({"autocomplete": "off"})
        self.fields["password_origin"].widget.attrs.update({"autocomplete": "off"})
