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
            with open(self.ruta) as contenido:
                Datos = json.load(contenido)
                if type(Datos) == list:  # Si es una lista y diccionario
                    print("Es una lista y diccionario")
                    self.tipo = 1
                    self.lent = len(Datos)
                elif type(Datos) == dict:  # Si es un diccionario
                    print("Es un diccionario")
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
                print(contador)
                return lista_resultado

            elif self.tipo == 2:
                resultado = list()
                Datos = self.get_json()
                resultado.append(Datos.get(elemento))  # type:ignore


if __name__ == "__main__":
    ruta = "./src/Archivos.json/Nombre_usuario.json"
    prueba = manage_json(ruta)
    print(prueba.get_json())
    # print(prueba.tipo)
    # print(prueba.lent)
    resultado = prueba.get_element("Estado_check")
    print(resultado)
