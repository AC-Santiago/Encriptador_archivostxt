import time
import secrets
from Manipulador_json import manage_json


class RSA:
    def __init__(self, p, q):
        self.p = int(p)
        self.q = int(q)
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = int()
        self.d = int()
        self.resultado = list()

    def generar_clave(self):
        # global e
        # global d
        self.e = int(secrets.choice(self.lista_maximo_comun_divisor(self.phi)))
        for i in range(1, self.phi):
            operacion_d1 = 1 + (i * self.phi)
            operacion_d2 = operacion_d1 / self.e
            if operacion_d2.is_integer():
                self.d = int(operacion_d2)
                if self.d != self.e:  ## evita que d sea igual a e
                    break
        return self.e, self.d

    #! Verifica que los numeros sean primos
    def primo_check(self, a):
        star_time = time.time()
        contador = int(0)
        for i in range(1, a + 1):
            residuo = int(a % i)
            if residuo == 0:
                contador += 1
            elif contador > 2:
                break
        if contador == 2:
            end_time = time.time()
            print("Tiempo de ejecucion: ", end_time - star_time)
            return True
        else:
            end_time = time.time()
            print("Tiempo de ejecucion: ", end_time - star_time)
            return False

    #! funcion que muestra los maximos como un divisor de dos numeros
    def maximo_comun_divisor(self, a, b):
        while b != 0:
            a, b = b, a % b  # funciona con el algoritmo de euclides
        return a

    #! funcion que hace una lista de los numeros que den como maximos como un divisor de 1
    def lista_maximo_comun_divisor(self, a):
        lista = []
        for i in range(2, a):
            if self.maximo_comun_divisor(a, i) == 1:
                lista.append(i)
        return lista

    def cifrar(self, mensaje):
        capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"

        mensaje_cifrado = str(mensaje)

        #! Abre el archivo json
        path = "src/Archivos.json/Abecedario.json"
        abecedario = manage_json(path)
        operacion = int(0)
        #! Hace iteraciones por cada letra del mensaje
        for letra in mensaje_cifrado:
            ## Verifica si la "letra" es mayuscula
            if letra in capital_letters:
                lista_letras = list(abecedario.get_element("Mayusculas"))  # type:ignore
                dict_letras = lista_letras[0]  # type:ignore
                dato = int(dict_letras.get(letra))
                operacion = (dato**self.e) % self.n
                self.resultado.append(operacion)

            ## Verifica si la "letra" es minuscula
            elif letra in lower_letters:
                lista_letras = list(abecedario.get_element("Minusculas"))  # type:ignore
                dict_letras = lista_letras[0]
                dato = int(dict_letras.get(letra))
                operacion = (dato**self.e) % self.n
                self.resultado.append(operacion)

            ## Verifica si la "letra" es un numero
            elif letra in numbers:
                lista_letras = list(abecedario.get_element("Numeros"))  # type:ignore
                dict_letras = lista_letras[0]
                dato = int(dict_letras.get(letra))
                operacion = (dato**self.e) % self.n
                self.resultado.append(operacion)
        print("e: ", self.e)

    def decifrar(self):
        resultado_cifrado = self.resultado
        print(resultado_cifrado)
        print("d: ", self.d)


if __name__ == "__main__":
    p = 3
    q = 11
    rsa = RSA(p, q)
    e, d = rsa.generar_clave()
    mensaje = "Hola"
    rsa.cifrar(mensaje)
    rsa.decifrar()
