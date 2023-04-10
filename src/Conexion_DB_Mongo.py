from pymongo import MongoClient


MongoURI = "mongodb://localhost:27017/"

mongo_client = MongoClient(MongoURI)

# Crear una colección en la base de datos "Encriptador_proyect" llamada "Usuarios"

db = mongo_client.Encriptador_proyect

collection_users = db.Users

