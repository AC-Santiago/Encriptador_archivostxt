from django.forms import ModelForm
from django import forms
from .models import models

OPCIONES_DES_CIF = [(1, "Cifrar"), (2, "Descifrar")]


class Cifrado_Descifrado(forms.Form):
    option_select = forms.ChoiceField(
        label="Opcion",
        choices=OPCIONES_DES_CIF,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
