from Manipulador_json import manage_json

import json
import os


#! Verifica que los numeros sean primos
def check_primo(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True


def Gene_pri():
    path = r"core\Dec_Cif\src\Archivos.json"
    primos = [elemento for elemento in range(1000, 5000) if check_primo(elemento)]
    new_file_path = os.path.join(path, "Numeros_primos.json")
    with open(new_file_path, "w") as file:
        json.dump({"Numeros_primos": primos}, file)


if __name__ == "__main__":
    Gene_pri()
