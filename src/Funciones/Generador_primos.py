from Manipulador_json import manage_json


#! Verifica que los numeros sean primos
def primo_check(a):
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


def Gene_pri():
    path = "../Archivos.json"
    Archivo = manage_json(path)
    lista = list()
    for i in range(100, 1000):
        if primo_check(i):
            lista.append(i)
    Archivo.create_json(
        path, "Numeros_primos.json", '{"Numeros_primos": ' + str(lista) + "}"
    )


if __name__ == "__main__":
    Gene_pri()
