# import time
import secrets
from Manipulador_json import manage_json


# ? Tener en cuanta que el cifrado ARS necesita que n que es (p*q) sea mayor que el mensaje a cifrar
# ? ejemplo si el cuadro de referencia contempla 65 caracteres n no puede ser menor
# ? 0<=m<n donde m es la letra a cifrar y n es el cuadro de referencia
class RSA:
    def __init__(self):
        self.p = int()  ## numero primo
        self.q = int()  ## numero primo
        self.n = int()  ## n = p*q
        self.phi = int()  ## phi = (p-1)*(q-1)
        self.e = int()
        self.d = int()

        self.longitud_mensaje = int()
        self.mensaje_cifrado = str()
        self.letter = str()
        self.select = int()

        self.resultado_cifrado = list()
        self.resultado_decifrado = list()

        ## Abre el archivo json
        self.path = "src/Archivos.json/Abecedario.json"
        self.abecedario = manage_json(self.path)
        self.rules = list()
        self.rulesFinal = list()

    #! Verifica que los numeros sean primos
    def primo_check(self, a):
        contador = int(0)
        for i in range(1, a + 1):
            residuo = int(a % i)
            if residuo == 0:
                contador += 1
            elif contador > 2:
                break
        if contador == 2:
            return True
        else:
            return False

    #! Genera los numeros primos y los componentes esenciales del cifrado como n y phi(n)
    def generar_bases(self):
        path = "src/Archivos.json/Numeros_primos.json"
        Numero_primo = manage_json(path)
        while self.p == self.q:
            self.p = secrets.choice(
                Numero_primo.get_element("Numeros_primos")[0]  # type:ignore
            )

            self.q = secrets.choice(
                Numero_primo.get_element("Numeros_primos")[0]  # type:ignore
            )
        else:
            self.n = self.p * self.q
            self.phi = (self.p - 1) * (self.q - 1)
            return self.p, self.q, self.n, self.phi

    #! funcion que muestra los maximos como un divisor de dos numeros
    def maximo_comun_divisor(self, a, b):
        while b != 0:
            a, b = b, a % b  # * funciona con el algoritmo de euclides
        return a

    #! funcion que hace una lista de los numeros que den como maximos como un divisor de 1
    def lista_maximo_comun_divisor(self, a):
        lista = []
        for i in range(2, a):
            if self.maximo_comun_divisor(a, i) == 1:
                lista.append(i)
        return lista

    #! Genera los dos componentes escenciales para las clave publica y privada
    def generar_clave(self):
        self.generar_bases()
        self.e = int(secrets.choice(self.lista_maximo_comun_divisor(self.phi)))
        for i in range(1, self.phi):
            operacion_d1 = 1 + (i * self.phi)
            operacion_d2 = operacion_d1 / self.e
            if operacion_d2.is_integer():
                self.d = int(operacion_d2)
                # * evita que d sea igual a e
                if self.d != self.e:
                    break
        return [self.n, self.e], [self.n, self.d]

    #! Funcion que identifica que tipo de letra es la que se esta cifrando para dar un valor numerico más preciso
    def ident_letra(self):
        capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        special_symbol = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~¿¡°¬¨·çÇñÑ"  # type:ignore
        accent_letter = "áéíóúÁÉÍÓÚ"
        special_letter = "üÜàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛäëïöüÄËÏÖâêîôûÂÊÎÔÛãõÃÕåæÆœŒßþÞðÐøØµ€¥¢£§©®™°¹²³¼½¾±÷¬¦«»"  # type:ignore

        ## Verifica si la "letra" es mayuscula
        if self.letter in capital_letters:
            self.select = 1

        ## Verifica si la "letra" es minuscula
        elif self.letter in lower_letters:
            self.select = 2

        ## Verifica si la "letra" es un numero
        elif self.letter in numbers:
            self.select = 3

        ## Verifica si la "letra" es un simbolos especial
        elif self.letter in special_symbol:
            self.select = 4

        ## Verifica si la "letra" es un caracter con tilde
        elif self.letter in accent_letter:
            self.select = 5

        ## Verifica si la "letra" es un caracter especial
        elif self.letter in special_letter:
            self.select = 6

    def cifrar(self, mensaje, Llave_publica):
        self.longitud_mensaje = len(mensaje)
        self.mensaje_cifrado = str(mensaje)
        self.n = Llave_publica[0]
        self.e = Llave_publica[1]

        operacion = int()
        rule = int()  # *cantidad de cifras que tiene el numero de la letra cifrada

        opciones = {
            1: "Mayusculas",
            2: "Minusculas",
            3: "Numeros",
            4: "Simbolos_especiales",
            5: "Caracteres_tilde",
            6: "Caracteres_especiales",
        }
        #! Hace iteraciones por cada letra del mensaje
        for letra in self.mensaje_cifrado:
            self.letter = letra
            self.ident_letra()
            lista_letras = list(
                self.abecedario.get_element(opciones[self.select])  # type:ignore
            )
            dict_letras = lista_letras[0]
            dato = int(dict_letras.get(letra))
            operacion = (dato**self.e) % self.n
            self.resultado_cifrado.append(operacion)
            rule = len(str(operacion))
            self.rules.append(rule)
        contador = 1
        for i in range(len(self.rules) - 1):
            if self.rules[i] == self.rules[i + 1]:
                contador += 1
            else:
                self.rulesFinal.append(
                    int(
                        str(len(str(contador)))
                        + str(contador)
                        + str(len(str(self.rules[i])))
                        + str(self.rules[i])
                    )
                )
                contador = 1
        self.rulesFinal.append(
            int(
                str(len(str(contador)))
                + str(contador)
                + str(len(str(self.rules[-1])))
                + str(self.rules[-1])
            )
        )
        return self.resultado_cifrado

    def decifrar(self, mensaje_cifrado, Llave_privada):
        self.resultado_cifrado = mensaje_cifrado
        rango = len(self.resultado_cifrado)
        self.n = Llave_privada[0]
        self.d = Llave_privada[1]
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
            elif operacion <= 102:
                lista_simbolos = list(
                    self.abecedario.get_element("Simbolos_especiales")  # type:ignore
                )
                dict_simbolos = lista_simbolos[0]  # type:ignore

                # * Busca el simbolo que corresponde al numero
                for key, value in dict_simbolos.items():
                    if value == operacion:
                        self.resultado_decifrado.append(key)
            elif operacion <= 112:
                lista_tilde = list(
                    self.abecedario.get_element("Caracteres_tilde")  # type:ignore
                )
                dict_tilde = lista_tilde[0]

                # * Busca el caracter con tilde que corresponde al numero
                for key, value in dict_tilde.items():
                    if value == operacion:
                        self.resultado_decifrado.append(key)
            elif operacion <= 181:
                lista_especiales = list(
                    self.abecedario.get_element("Caracteres_especiales")  # type:ignore
                )
                dict_especiales = lista_especiales[0]

                # * Busca el caracter especial que corresponde al numero
                for key, value in dict_especiales.items():
                    if value == operacion:
                        self.resultado_decifrado.append(key)

        mesanje_decifrado = "".join(self.resultado_decifrado)
        return mesanje_decifrado

    def organizar_mensajeC(self):
        pass


if __name__ == "__main__":
    rsa = RSA()
    mensaje = "Hola, este es un mensaje de prueba para el cifrado RSA."
    rsa.cifrar(mensaje, [26123, 6731])
    print("Mensaje cifrado: ", rsa.resultado_cifrado)
    print("Mensaje decifrado: ", rsa.decifrar(rsa.resultado_cifrado, [26123, 3971]))
    # print(rsa.generar_clave())
