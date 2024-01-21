from Manipulador_json import manage_json


#! Verifica que los numeros sean primos
def check_primo(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True


def Gene_pri():
    path = "../Archivos.json"
    Archivo = manage_json(path)
    primos = [elemento for elemento in range(2, 1000000) if check_primo(elemento)]
    Archivo.create_json(
        path, "Numeros_primos.json", '{"Numeros_primos": ' + str(primos) + "}"
    )


if __name__ == "__main__":
    Gene_pri()
