from django.shortcuts import render
from .src.Funciones.Cifrado_decifrado import RSA


# Create your views here.
def index(request):
    return render(request, "index.html", {"User": request.user})


def about(request):
    return render(request, "about.html")


def dec_cif(request):
    if request.method == "GET":
        return render(request, "dec_cif.html")
    elif request.method == "POST":
        rsa = RSA()
        llave_publica, llave_privada = [235457, 82949], [235457, 154829]
        mensaje = request.POST["input_dec_cif"]
        if request.POST["select_dec_cif"] == "1":
            mensaje_cifrado = rsa.cifrar(mensaje, llave_publica)
            return render(request, "dec_cif.html", {"mensaje": mensaje_cifrado})
        elif request.POST["select_dec_cif"] == "2":
            mensaje_descifrado = rsa.descifrar(mensaje, llave_privada)
            return render(request, "dec_cif.html", {"mensaje": mensaje_descifrado})
