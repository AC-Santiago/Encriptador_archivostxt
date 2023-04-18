from pymongo import MongoClient
import pymongo




Client = pymongo.MongoClient("mongodb+srv://SantiagoA:IrRfBA8kgyiuIIxJ@proyecte.cbmd2qp.mongodb.net/?retryWrites=true&w=majority")
db = Client.Encriptador_proyect


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
try:
    Client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)