from django.shortcuts import render
import time
import resource
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
        mensaje = input_dec_cif
        inicio_recursos = resource.getrusage(resource.RUSAGE_SELF)
        rsa = RSA()
        inicio_bases = time.time()
        rsa.generar_bases()
        rsa.generar_clave()
        fin_bases = time.time()
        print(f"Tiempo de generacion de bases: {fin_bases - inicio_bases} segundos")
        llave_publica, llave_privada = [235457, 82949], [235457, 154829]
        print(f"Llave publica: {llave_publica}")
        print(f"Llave privada {llave_privada}")
        inicio_cifrado = time.time()
        mensaje_cifrado = rsa.cifrar(mensaje, llave_publica)
        print(f"mensaje cifrado: {mensaje_cifrado}")
        fin_cifrado = time.time()

        inicio_descifrado = time.time()
        mensaje_descifrado = rsa.descifrar(mensaje_cifrado, llave_privada)
        print(f"mensaje descifrado: {mensaje_descifrado}")
        fin_descifrado = time.time()
        fin_recursos = resource.getrusage(resource.RUSAGE_SELF)
        # Tiempo de CPU
        tiempo_cpu = fin_recursos.ru_utime - inicio_recursos.ru_utime

        # Uso máximo de memoria
        memoria_max = fin_recursos.ru_maxrss - inicio_recursos.ru_maxrss
        print(f"Tiempo de cifrado: {fin_cifrado - inicio_cifrado} segundos")
        print(f"Tiempo de descifrado: {fin_descifrado - inicio_descifrado} segundos")

        print(f"Tiempo de uso del CPU: {tiempo_cpu} segundos")
        print(f"Uso máximo de la memoria: {memoria_max} KB")

        return render(request, "dec_cif.html", {"mensaje": mensaje_descifrado})
