import time
import secrets
from Manipulador_json import manage_json


# ? Tener en cuanta que el cifrado ARS necesita que n que es (p*q) sea mayor que el mensaje a cifrar
# ? ejemplo si el cuadro de referencia contempla 65 caracteres n no puede ser menor
# ? 0<=m<n donde m es la letra a cifrar y n es el cuadro de referencia
class RSA:
    def __init__(self, p, q):
        self.p = int(p)
        self.q = int(q)
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = int()
        self.d = int()
        self.resultado_cifrado = list()
        self.resultado_decifrado = list()

        ## Abre el archivo json
        self.path = "src/Archivos.json/Abecedario.json"
        self.abecedario = manage_json(self.path)

    def generar_clave(self):
        # global e
        # global d
        self.e = int(secrets.choice(self.lista_maximo_comun_divisor(self.phi)))
        for i in range(1, self.phi):
            operacion_d1 = 1 + (i * self.phi)
            operacion_d2 = operacion_d1 / self.e
            if operacion_d2.is_integer():
                self.d = int(operacion_d2)
                # * evita que d sea igual a e
                if self.d != self.e:
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
        special_characters = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        mensaje_cifrado = str(mensaje)

        operacion = int()
        #! Hace iteraciones por cada letra del mensaje
        for letra in mensaje_cifrado:
            ## Verifica si la "letra" es mayuscula
            if letra in capital_letters:
                lista_letras = list(
                    self.abecedario.get_element("Mayusculas")  # type:ignore
                )
                dict_letras = lista_letras[0]  # type:ignore
                dato = int(dict_letras.get(letra))
                operacion = (dato**self.e) % self.n
                self.resultado_cifrado.append(operacion)

            ## Verifica si la "letra" es minuscula
            elif letra in lower_letters:
                lista_letras = list(
                    self.abecedario.get_element("Minusculas")  # type:ignore
                )
                dict_letras = lista_letras[0]
                dato = int(dict_letras.get(letra))
                operacion = (dato**self.e) % self.n
                self.resultado_cifrado.append(operacion)

            ## Verifica si la "letra" es un numero
            elif letra in numbers:
                lista_letras = list(
                    self.abecedario.get_element("Numeros")  # type:ignore
                )
                dict_letras = lista_letras[0]
                dato = int(dict_letras.get(letra))
                operacion = (dato**self.e) % self.n
                self.resultado_cifrado.append(operacion)

            ## Verifica si la "letra" es un caracter especial
            elif letra in special_characters:
                lista_letras = list(
                    self.abecedario.get_element("Simbolos_especiales")  # type:ignore
                )
                dict_letras = lista_letras[0]
                dato = int(dict_letras.get(letra))
                operacion = (dato**self.e) % self.n
                self.resultado_cifrado.append(operacion)

        mensaje_cifrado_final = "".join(map(str, self.resultado_cifrado))
        print("Mensaje cifrado: ", mensaje_cifrado_final)

    def decifrar(self):
        rango = len(self.resultado_cifrado)
        # print("rango: ", rango)
        # print(self.resultado_cifrado)
        for i in range(rango):
            letra_cifrado = int(self.resultado_cifrado[i])
            operacion = (letra_cifrado**self.d) % self.n
            if operacion <= 26:
                lista_letras = list(
                    self.abecedario.get_element("Mayusculas")  # type:ignore
                )
                dict_letras = lista_letras[0]  # type:ignore

                # * Busca la letra que corresponde al numero
                for key, value in dict_letras.items():
                    if value == operacion:
                        self.resultado_decifrado.append(key)
            elif operacion <= 52:
                lista_letras = list(
                    self.abecedario.get_element("Minusculas")  # type:ignore
                )
                dict_letras = lista_letras[0]  # type:ignore

                # * Busca la letra que corresponde al numero
                for key, value in dict_letras.items():
                    if value == operacion:
                        self.resultado_decifrado.append(key)
            elif operacion <= 62:
                lista_numeros = list(
                    self.abecedario.get_element("Numeros")  # type:ignore
                )
                dict_numeros = lista_numeros[0]  # type:ignore

                # * Busca el numero que corresponde al numero
                for key, value in dict_numeros.items():
                    if value == operacion:
                        self.resultado_decifrado.append(key)
            elif operacion <= 94:
                lista_simbolos = list(
                    self.abecedario.get_element("Simbolos_especiales")  # type:ignore
                )
                dict_simbolos = lista_simbolos[0]  # type:ignore

                # * Busca el simbolo que corresponde al numero
                for key, value in dict_simbolos.items():
                    if value == operacion:
                        self.resultado_decifrado.append(key)
        # print(self.resultado_decifrado)
        mesanje_decifrado = "".join(self.resultado_decifrado)
        print("Mensaje decifrado", mesanje_decifrado)


if __name__ == "__main__":
    p = 101
    q = 103
    rsa = RSA(p, q)
    e, d = rsa.generar_clave()
    mensaje = "Hola como esta mundo () acostasantiago@gmail.com"
    rsa.cifrar(mensaje)
    rsa.decifrar()
