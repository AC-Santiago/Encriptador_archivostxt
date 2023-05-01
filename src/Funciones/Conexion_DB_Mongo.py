from pymongo import MongoClient
from pymongo.server_api import ServerApi
from Funciones.Generador_ID import Generar_id

Uri = "mongodb+srv://SantiagoA:IrRfBA8kgyiuIIxJ@proyecte.cbmd2qp.mongodb.net/?retryWrites=true&w=majority"
Client = MongoClient(Uri, server_api=ServerApi("1"))
db = Client.Encriptador_proyect


db = Client["Encriptador_proyect"]  # Nombre de la base de datos
Colection = db["Users"]  # Nombre de la coleccion


# Funcion que verifica si el usuario existe
def Verificar_user(user, password):
    resultado = Colection.find_one({"Name": user, "Password": password})
    if resultado != None:
        return True
    else:
        return False


# Funcion que inserta un usuario en la base de datos
def Insertar_user(user, password):
    try:
        resultado = Colection.find_one({"Name": user, "Password": password})
        if resultado != None:
            return True
        else:
            _id = Generar_id()
            resultado_1 = Colection.find_one(
                {"_id": _id}
            )  # Verifica que el id no exista
            while resultado_1 != None:
                _id = Generar_id()
                resultado_1 = Colection.find_one({"_id": _id})
            if resultado_1 == None:
                Colection.insert_one({"_id": _id, "Name": user, "Password": password})
                return False
    except:
        print("Error al registrar el usuario")


# Verica que se tenga conexion con la base de datos
try:
    Client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
