import json
import os


class manage_json:
    def __init__(self, ruta):
        self.ruta = ruta
        self.tipo = int()  ## 1 = lista y diccionario, 2 = diccionario
        self.lent = (
            int()
        )  # * dice la cantidad de elementos que tiene el json si empiza por "[]" dira los elemntos pero si "{}" tambien pero si es un diccionario dira la cantidad de elementos que tiene el diccionario
        self.errorfoundfield = int(0)

    #! Funcion que verifique si el archivo existe
    def verify_file(self):
        if os.path.isfile(self.ruta):
            self.errorfoundfield = 0
            return True
        else:
            self.errorfoundfield = 1
            return False

    #! Funcion que obtenga el json y la meta en una variable para poder manipularla
    def get_json(self):
        self.verify_file()
        if self.errorfoundfield == 0:
            with open(self.ruta, "r") as contenido:
                Datos = json.load(contenido)
                if type(Datos) == list:  ## Si es una lista y diccionario
                    self.tipo = 1
                    self.lent = len(Datos)
                elif type(Datos) == dict:  ## Si es un diccionario
                    self.tipo = 2
                    self.lent = len(Datos)
            return Datos
        elif self.errorfoundfield == 1:
            print("El archivo no existe")

    #!Funcion que pueda extraer un elemento de la lista y diccionario
    def get_element(self, elemento):
        self.verify_file()
        self.get_json()
        if self.errorfoundfield == 0:
            if self.tipo == 1:
                lista_resultado = list()
                Datos = self.get_json()
                contador = 0
                for Dato in Datos:  # type:ignore
                    lista_resultado.append(Dato.get(elemento))
                    contador += 1
                if contador == 1:
                    return lista_resultado[0]
                else:
                    return lista_resultado

            elif self.tipo == 2:
                resultado = list()
                Datos = self.get_json()
                resultado.append(Datos.get(elemento))  # type:ignore
                return resultado
        elif self.errorfoundfield == 1:
            print("El archivo no existe")

    #! Funcion que pueda editar valores del json y guardarlos en el archivo
    def edit_element(self, elemento, valor1, valor2):
        self.verify_file()
        self.get_json()
        if self.errorfoundfield == 0:
            contador = 0
            if self.tipo == 1:
                with open(self.ruta, "r") as f:
                    data = json.load(f)

                for diccionario in data:
                    if diccionario[elemento] == valor1:
                        diccionario[elemento] = valor2
                        contador += 1

                # * Guardar los cambios en el archivo JSON
                with open(self.ruta, "w") as f:
                    json.dump(data, f)

            elif self.tipo == 2:
                with open(self.ruta, "r") as f:
                    data = json.load(f)

                if data[elemento] == valor1:
                    data[elemento] = valor2
                    contador += 1

                # * Guardar los cambios en el archivo JSON
                with open(self.ruta, "w") as f:
                    json.dump(data, f)

            if contador == 0:
                print("No se encontro el elemento")

        elif self.errorfoundfield == 1:
            print("El archivo no existe")

    #! Funcion que pueda crear un archivo json
    def create_json(self, ruta, name_json, contenido):
        # * Verifica que la ruta que se usa exista sino existe la crea
        if not os.path.exists(ruta):
            os.makedirs(ruta)

        # * Otra forma de saber si el archivo existe
        if os.path.isfile(os.path.join(ruta, name_json)):
            pass  # * Si existe no hace nada
        else:
            with open(os.path.join(ruta, name_json), "w") as file:
                file.write(contenido)

    #! Funcion que pueda eliminar un elemento del json
    def delete_element(self, elemento, valor):
        self.verify_file()
        self.get_json()
        if self.errorfoundfield == 0:
            if self.tipo == 1:
                with open(self.ruta, "r") as f:
                    data = json.load(f)

                for diccionario in data:
                    if diccionario[elemento] == valor:
                        data.remove(diccionario)

                # * Guardar los cambios en el archivo JSON
                with open(self.ruta, "w") as f:
                    json.dump(data, f)

            elif self.tipo == 2:
                with open(self.ruta, "r") as f:
                    data = json.load(f)

                if data[elemento] == valor:
                    data.remove(data[elemento])

                # * Guardar los cambios en el archivo JSON
                with open(self.ruta, "w") as f:
                    json.dump(data, f)

        elif self.errorfoundfield == 1:
            print("El archivo no existe")

    #! Funcion que pueda agregar un elemento al json
    def add_element(self, elemento, valor):
        self.verify_file()
        self.get_json()
        if self.errorfoundfield == 0:
            if self.tipo == 1:
                with open(self.ruta, "r") as f:
                    data = json.load(f)

                data.append({elemento: valor})

                # * Guardar los cambios en el archivo JSON
                with open(self.ruta, "w") as f:
                    json.dump(data, f)

            elif self.tipo == 2:
                with open(self.ruta, "r") as f:
                    data = json.load(f)

                data[elemento] = valor

                # * Guardar los cambios en el archivo JSON
                with open(self.ruta, "w") as f:
                    json.dump(data, f)

        elif self.errorfoundfield == 1:
            print("El archivo no existe")
