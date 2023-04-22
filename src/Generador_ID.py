import secrets


# funcion que genera el id
def Generar_id():
    id = secrets.token_hex(5)
    return id
