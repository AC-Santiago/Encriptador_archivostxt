import json


class manage_json:
    def __init__(self, ruta):
        self.ruta = ruta
        self.tipo = int()  # 1 = lista y diccionario, 2 = diccionario
        self.lent = (
            int()
        )  # dice la cantidad de elementos que tiene el json si empiza por "[]" dira los elemntos pero si "{}" tambien pero si es un diccionario dira la cantidad de elementos que tiene el diccionario
        self.errorfoundfield = int(0)

    # Funcion que obtenga el json y la meta en una variable para poder manipularla
    def get_json(self):
        try:
            with open(self.ruta, "r") as contenido:
                Datos = json.load(contenido)
                if type(Datos) == list:  # Si es una lista y diccionario
                    # print("Es una lista y diccionario")
                    self.tipo = 1
                    self.lent = len(Datos)
                elif type(Datos) == dict:  # Si es un diccionario
                    # print("Es un diccionario")
                    self.tipo = 2
                    self.lent = len(Datos)
            return Datos
        except FileNotFoundError:
            print("No se encontro el archivo")
            self.errorfoundfield = 1

    # Funcion que pueda extraer un elemento de la lista y diccionario
    def get_element(self, elemento):
        if self.errorfoundfield == 0:
            if self.tipo == 1:
                lista_resultado = list()
                Datos = self.get_json()
                contador = 0
                for Dato in Datos:  # type:ignore
                    lista_resultado.append(Dato.get(elemento))
                    contador += 1
                # print(contador)
                return lista_resultado

            elif self.tipo == 2:
                resultado = list()
                Datos = self.get_json()
                resultado.append(Datos.get(elemento))  # type:ignore
                return resultado

    # Funcion que pueda editar valores del json y guardarlos en el archivo
    def edit_element(self, elemento, valor1, valor2):
        if self.errorfoundfield == 0:
            contador = 0
            if self.tipo == 1:
                with open(self.ruta, "r") as f:
                    data = json.load(f)

                for diccionario in data:
                    if diccionario[elemento] == valor1:
                        diccionario[elemento] = valor2
                        contador += 1

                # Guardar los cambios en el archivo JSON
                with open(self.ruta, "w") as f:
                    json.dump(data, f)

            elif self.tipo == 2:
                with open(self.ruta, "r") as f:
                    data = json.load(f)

                if data[elemento] == valor1:
                    data[elemento] = valor2
                    contador += 1

                # Guardar los cambios en el archivo JSON
                with open(self.ruta, "w") as f:
                    json.dump(data, f)

            if contador == 0:
                print("No se encontro el elemento")


if __name__ == "__main__":
    ruta = "./src/Archivos.json/Nombre_usuario.json"
    prueba = manage_json(ruta)
    print(prueba.get_json())
    prueba.edit_element("Nombre", "Santiago", "SantiagoA")
    print(prueba.get_json())
