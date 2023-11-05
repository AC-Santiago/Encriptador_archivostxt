import secrets
import numpy as np
from .Manipulador_json import manage_json


# ? Tener en cuanta que el cifrado ARS necesita que n que es (p*q) sea mayor que el mensaje rsa cifrar
# ? Ejemplo si el cuadro de referencia contempla 65 caracteres n no puede ser menor
# ? 0≤m<n donde m es la letra rsa cifrar y n es el cuadro de referencia
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
        self.resultado_cifrado_final = str()
        self.resultado_descifrado = list()

        ## Abre el archivo json
        self.path = "../Archivos.json/Abecedario.json"
        # self.path = "core/Dec_Cif/src/Archivos.json/Abecedario.json"
        # self.path = "src/Archivos.json/Abecedario.json"

        self.abecedario = manage_json(self.path)
        self.rules = np.array([], dtype=int)
        self.rules_Final = list()

    # ! Verifica que los numeros sean primos
    def primo_check(self, a: int):
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

    # ! Genera los numeros primos y los componentes esenciales del cifrado como n y phi(n)
    def generar_bases(self):
        # path = "../Archivos.json/Numeros_primos.json"
        path = "core/Dec_Cif/src/Archivos.json/Numeros_primos.json"
        # path = "src/Archivos.json/Numeros_primos.json"
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

    # ! funcion que muestra los maximos como un divisor de dos numeros
    def maximo_comun_divisor(self, a: int, b: int):
        while b != 0:
            a, b = b, a % b  # * funciona con el algoritmo de euclides
        return a

    # ! funcion que hace una lista de los numeros que den como maximos como un divisor de 1
    def lista_maximo_comun_divisor(self, a: int):
        lista = list()
        for i in range(2, a):
            if self.maximo_comun_divisor(a, i) == 1:
                lista.append(i)
        return lista

    # ! Genera los dos componentes esenciales para las clave publica y privada
    def generar_clave(self):
        self.generar_bases()
        self.e = int(secrets.choice(self.lista_maximo_comun_divisor(self.phi)))
        for i in range(1, self.phi):
            operacion_d1 = 1 + (i * self.phi)
            operacion_d2 = operacion_d1 / self.e
            if operacion_d2.is_integer():
                self.d = int(operacion_d2)
                # * evita que d sea igual rsa e
                if self.d != self.e:
                    break
        return [self.n, self.e], [self.n, self.d]

    def cifrar(self, mensaje: str, Llave_publica: list):
        self.longitud_mensaje = len(mensaje)
        self.mensaje_cifrado = str(mensaje)
        self.n = Llave_publica[0]
        self.e = Llave_publica[1]

        operacion = int()
        rule = int()
        for letra in self.mensaje_cifrado:
            dato = int(ord(letra))
            operacion = (dato ** self.e) % self.n
            self.resultado_cifrado.append(operacion)
            rule = len(str(operacion))
            self.rules = np.append(self.rules, rule)
        return self.create_rule()

    def create_rule(self):
        contador = 1
        for i in range(len(self.rules) - 1):
            if self.rules[i] == self.rules[i + 1]:
                contador += 1
            else:
                self.rules_Final.append(
                    int(
                        str(len(str(contador)))
                        + str(contador)
                        + str(len(str(self.rules[i])))
                        + str(self.rules[i])
                    )
                )
                contador = 1
        self.rules_Final.append(
            int(
                str(len(str(contador)))
                + str(contador)
                + str(len(str(self.rules[-1])))
                + str(self.rules[-1])
            )
        )
        element = str(self.rules_Final[0]) + str(self.resultado_cifrado[0])
        self.resultado_cifrado[0] = int(element)

        component_A = int(0)
        component_B = int(0)
        if len(self.rules_Final) == 1:
            component_A = int(str(self.rules_Final[0])[0:1])
            component_B += int(str(self.rules_Final[0])[1: component_A + 1])
            self.resultado_cifrado_final = "".join(
                    str(e) for e in self.resultado_cifrado
                )
            return self.resultado_cifrado_final
        else:
            for i in range(1, len(self.rules_Final)):
                component_A = int(str(self.rules_Final[i - 1])[0:1])
                component_B += int(str(self.rules_Final[i - 1])[1: component_A + 1])
                element = str(self.rules_Final[i]) + str(
                    self.resultado_cifrado[component_B]
                )
                self.resultado_cifrado[component_B] = int(element)
                self.resultado_cifrado_final = "".join(
                    str(e) for e in self.resultado_cifrado
                )

            return self.resultado_cifrado_final

    def descifrar(self, mensaje_cifrado, Llave_privada: list):
        self.lista_cifrado = self.organizar_mensajeC(mensaje_cifrado)
        rango = len(self.lista_cifrado)
        self.n = Llave_privada[0]
        self.d = Llave_privada[1]
        for i in range(rango):
            letra_cifrado = int(self.lista_cifrado[i])
            operacion = (letra_cifrado ** self.d) % self.n
            self.resultado_descifrado.append(chr(operacion))
        mesanje_descifrado = "".join(self.resultado_descifrado)
        return mesanje_descifrado

    def organizar_mensajeC(self, mensaje_cifrado: str):
        resultado_cifrado = str(mensaje_cifrado)
        cifrado = []

        component_A = int(str(resultado_cifrado[0:1]))
        component_B = int(str(resultado_cifrado[1: component_A + 1]))
        component_C = int(str(resultado_cifrado[component_A + 1: component_A + 2]))
        component_D = int(
            str(resultado_cifrado[component_A + 2: component_A + 2 + component_C])
        )

        cifrado.append(
            int(
                resultado_cifrado[
                len(
                    str(component_A)
                    + str(component_B)
                    + str(component_C)
                    + str(component_D)
                ): len(
                    str(component_A)
                    + str(component_B)
                    + str(component_C)
                    + str(component_D)
                )
                   + component_D
                ]
            )
        )

        indice = int(
            len(
                str(component_A)
                + str(component_B)
                + str(component_C)
                + str(component_D)
            )
            + component_D
        )
        repeat = int(1)
        ciclo_repeat = int(0)
        contador = int(0)
        first_time = True
        for i in range(1, len(resultado_cifrado)):
            try:
                contador += 1
                if contador == component_B and first_time == True:
                    ciclo_repeat = component_B
                    first_time = False
                if repeat == component_B and ciclo_repeat >= 0:
                    component_A = int(resultado_cifrado[indice: indice + 1])
                    component_B = int(
                        resultado_cifrado[indice + 1: indice + 1 + component_A]
                    )
                    component_C = int(
                        resultado_cifrado[
                        indice + 1 + component_A: indice + 2 + component_A
                        ]
                    )
                    component_D = int(
                        resultado_cifrado[
                        indice
                        + 2
                        + component_A: indice
                                       + 2
                                       + component_A
                                       + component_C
                        ]
                    )
                    rule = len(
                        str(component_A)
                        + str(component_B)
                        + str(component_C)
                        + str(component_D)
                    )
                    cifrado.append(
                        int(
                            resultado_cifrado[
                            indice + rule: indice + rule + component_D
                            ]
                        )
                    )
                    indice += rule + component_D
                    ciclo_repeat = component_B
                    repeat = 1

                else:
                    cifrado.append(
                        int(resultado_cifrado[indice: indice + component_D])
                    )
                    indice += component_D
                    repeat += 1
                    ciclo_repeat -= 1

            except:
                break
        return cifrado
