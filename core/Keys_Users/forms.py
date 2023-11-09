from django import forms

from core.Users_EncrytedPage.models import Users_EncrytedPage
from .models import Keys_users


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


class Keys_users_form(forms.ModelForm):
    class Meta:
        model = Keys_users
        fields = [
            "key_name",
            "key_public",
            "key_private",
        ]
        widgets = {
            "key_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre",
                    "required": "true",
                    "id": "floatingInputKeyName",
                    "type": "text",
                }
            ),
            "key_public": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Clave pública",
                    "type": "text",
                    "id": "floatingInputKeyPublic",
                    "disabled": "true",
                }
            ),
            "key_private": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Clave privada",
                    "type": "text",
                    "id": "floatingInputKeyPrivate",
                    "disabled": "true",
                }
            ),
        }
