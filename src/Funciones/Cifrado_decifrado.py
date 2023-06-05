import time
import secrets

abecedario = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
}


# funcion que verifica si un numero es primo
def primo_check(a):
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


# funcion que muestra los maximos como un divisor de dos numeros
def maximo_comun_divisor(a, b):
    while b != 0:
        a, b = b, a % b  # funciona con el algoritmo de euclides
    return a


# funcion que hace una lista de los numeros que den como maximos como un divisor de 1
def lista_maximo_comun_divisor(a):
    lista = []
    for i in range(2, a):
        if maximo_comun_divisor(a, i) == 1:
            lista.append(i)
    return lista
