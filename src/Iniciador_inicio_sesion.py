from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import sys
from Iniciador_Registro import Registro
from Conexion_DB_Mongo import Verificar_user


class Inicio_sesion(QMainWindow):
    def __init__(self):
        super(Inicio_sesion, self).__init__()
        loadUi("src/Archivos.ui/Inicio_sesion.ui", self)
        self.setWindowTitle("Inicio de sesión")

        # Funcion que se ejecuta al presionar el boton de iniciar sesion
        self.Button_inicio_sesion.clicked.connect(self.datos_user)
        self.Button_registrarse.clicked.connect(self.registrarse)

        # detecta cuando el checkbox de mantener sesion activa esta activado o desactivado
        # self.Mantener_sesion.connect(self.mantener_sesion)

    # Funcion que obtiene los datos del usuario
    def datos_user(self):
        self.user = self.Text_usuario.text()
        self.password = self.Text_password.text()
        if Verificar_user(self.user, self.password) == True:
            print("Bienvenido")
        else:
            print("Usuario o contraseña incorrecta")

    # Funcion que abre la ventana de registro y cierra la ventana de inicio de sesion
    def registrarse(self):
        self.registro = Registro()
        self.registro.show()
        self.close()
