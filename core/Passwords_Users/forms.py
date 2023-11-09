from django import forms

from .models import Passwords_users
from ..Users_EncrytedPage.models import Users_EncrytedPage


class PasswordsUsersForm(forms.ModelForm):
    class Meta:
        model = Passwords_users
        fields = [
            "password_name",
            "password_username",
            "password_email",
            "password_origin",
            "password",
        ]
        widgets = {
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "type": "password",
                    "placeholder": "Contraseña",
                    "required": "true",
                    "id": "floatingInputPassword",
                }
            ),
            "password_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre",
                    "required": "true",
                    "id": "floatingInputName",
                    "type": "text",
                }
            ),
            "password_username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Usuario",
                    "type": "text",
                    "required": "true",
                    "id": "floatingInputUsername",
                }
            ),
            "password_email": forms.EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "id": "floatingInputEmail",
                    "required": "true",
                    "placeholder": "",
                }
            ),
            "password_origin": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Origen",
                    "type": "text",
                    "required": "true",
                    "id": "floatingInputOrigin",
                }
            ),
        }

    # Desactiva el autocompletado de los campos del formulario
    def __init__(self, *args, **kwargs):
        super(PasswordsUsersForm, self).__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({"autocomplete": "off"})
        self.fields["password_name"].widget.attrs.update({"autocomplete": "off"})
        self.fields["password_origin"].widget.attrs.update({"autocomplete": "off"})


class MasterKeyForm(forms.ModelForm):
    class Meta:
        model = Users_EncrytedPage
        fields = [
            "master_key",
        ]
        widgets = {
            "master_key": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "",
                    "aria-label": "Pin",
                    "aria-describedby": "addon-wrapping",
                    "required": True,
                    "maxlength": "8",
                    "onkeypress": "return (event.charCode >= 48 && event.charCode <= 57)",
                    "minlength": "8",
                    "autocomplete": "off",
                }
            )
        }
