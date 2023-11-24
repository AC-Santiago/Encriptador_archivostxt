import json

from django.shortcuts import render

from .src.Funciones.Cifrado_decifrado import RSA
from ..Keys_Users.models import Keys_users


# Create your views here.


# -------------------------HOME PAGE-------------------------#
def index(request):
    return render(request, "index.html", {"User": request.user})


# -------------------------HOME PAGE-------------------------#

# -------------------------ABOUT PAGE-------------------------#


def about(request):
    return render(request, "about.html")


# -------------------------ABOUT PAGE-------------------------#


# -------------------------ENCRYPTION AND DECRYPTION-------------------------#
def dec_cif(request):
    keys = Keys_users.objects.filter(user=request.user)
    if request.method == "GET":
        return render(request, "dec_cif.html", {"keys": keys})
    elif request.method == "POST":
        rsa = RSA()
        llave = Keys_users.objects.get(key_name=request.POST["Keys"])
        print(llave.key_public, llave.key_private)
        llave_publica, llave_privada = json.loads(llave.key_public), json.loads(llave.key_private)
        mensaje = request.POST["input_dec_cif"]
        if request.POST["select_dec_cif"] == "1":
            mensaje_cifrado = rsa.cifrar(mensaje, llave_publica)
            return render(request, "dec_cif.html", {"mensaje": mensaje_cifrado, "keys": keys})
        elif request.POST["select_dec_cif"] == "2":
            mensaje_descifrado = rsa.descifrar(mensaje, llave_privada)
            return render(request, "dec_cif.html", {"mensaje": mensaje_descifrado, "keys": keys})

# -------------------------ENCRYPTION AND DECRYPTION-------------------------#
