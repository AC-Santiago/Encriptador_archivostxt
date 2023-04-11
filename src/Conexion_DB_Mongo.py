from pymongo import MongoClient


MongoURI = "mongodb://localhost:27017/"

Client = MongoClient(MongoURI)

db = Client["Encriptador_proyect"] #Nombre de la base de datos
Colection = db["Users"] #Nombre de la coleccion

def Verificar_user(user,password):
    resultado = Colection.find_one({"Name":user,"Password":password})
    if resultado != None:
        return True
    else:
        return False
    
def Insertar_user(user,password):
    try:
        resultado = Colection.find_one({"Name":user,"Password":password})
        if resultado != None:
            return True
        else:
            Colection.insert_one({"Name":user,"Password":password})
            return False
    except:
        print("Error al registrar el usuario")
