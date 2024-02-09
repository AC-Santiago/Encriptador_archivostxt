import pandas as pd
import numpy as np


def import_passwords(path: str, username: str, email: str):
    """
    funcion que trata los datos del csv, si no tiene el formato adecuado
    retorna un mensaje de error y si no tiene los datos necesarios
    retorna el dataframe con los datos por defecto.

    Args:
        path (str): ruta del archivo csv
        username (str): nombre de usuario por defecto
        email (str): email por defecto

    Returns:
        pd.DataFrame: dataframe con los datos tratados
    """
    error = _error_management(path)
    if error:
        return error
    else:
        df = pd.read_csv(path)
        df["email"] = df["username"]
        default_username = username
        default_email = email

        for index, row in df.iterrows():
            email = row["email"]
            if isinstance(email, (float, np.int64)) or (
                "@" not in email or "." not in email
            ):
                df.at[index, "email"] = default_email
            username = row["username"]
            if isinstance(username, (float, np.int64)) or len(username) < 3:
                df.at[index, "username"] = default_username
        return df


def _error_management(path: str):
    """
    funcion que maneja los errores de importacion, como no encontrar
    el archivo no tiene el formato adecuado o no tiene los datos necesarios
    """
    try:
        pd.read_csv(path)
    except FileNotFoundError:
        return "El archivo no se encuentra en la ruta especificada"
    except pd.errors.ParserError:
        return "El archivo no tiene el formato adecuado"
    except pd.errors.EmptyDataError:
        return "El archivo no tiene los datos necesarios"


if __name__ == "__main__":
    path = r"C:\Users\acost.DESKTOP-0EA6P9D\OneDrive\Escritorio\Carpetas de escritorio\Recursos de programacion\Proyectos de programación\Encrypt_txt\core\Passwords_Users\ArchivosTemporales\Contraseñas de Microsoft Edge personal.csv"
    print(import_passwords(path, "SantiagoA", "acostasantiago311124578@gmail.com"))
