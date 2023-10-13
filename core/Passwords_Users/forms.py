from django import forms
from .models import Passwords_users


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

    # Desactiva el aoutocompletado de los campos del formulario
    def __init__(self, *args, **kwargs):
        super(PasswordsUsersForm, self).__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({"autocomplete": "off"})
        self.fields["password_name"].widget.attrs.update({"autocomplete": "off"})
        self.fields["password_origin"].widget.attrs.update({"autocomplete": "off"})
