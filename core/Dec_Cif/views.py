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
        input_dec_cif = request.POST["input_dec_cif"]
        print(input_dec_cif)
        for i in range(len(input_dec_cif)):
            print(
                f"el codigo ascii de {chr(ord(input_dec_cif[i]))} es: {ord(input_dec_cif[i])}"
            )
        mensaje = input_dec_cif
        # rsa = RSA()
        # llave_publica = [190237, 94057]
        # llave_privada = [190237, 188793]
        # try:
        #     mensaje_cifrado = rsa.cifrar(input_dec_cif, llave_publica)
        #     print(f"Mensaje cifrado: {mensaje_cifrado}")
        #
        #     mensaje_descifrado = rsa.descifrar(mensaje_cifrado, llave_privada)
        #     print(f"Mensaje descifrado: {mensaje_descifrado}")
        #     return render(request, "dec_cif.html", {"mensaje": mensaje_descifrado})
        # except ValueError:
        #     return render(
        #         request,
        #         "dec_cif.html",
        #         {"mensaje": "No se pudo cifrar el mensaje, intente de nuevo"},
        #     )
        return render(request, "dec_cif.html", {"mensaje": mensaje})
