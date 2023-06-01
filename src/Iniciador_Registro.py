from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import sys

from Funciones.Conexion_DB_Mongo import Insertar_user


class Registro(QMainWindow):
    def __init__(self):
        super(Registro, self).__init__()
        loadUi("src/Archivos.ui/Registro.ui", self)
        self.setWindowTitle("Registro")
        self.Button_cancelar.clicked.connect(
            self.cancelar
        )  # cuando oprime el boton de cancelar se cierra la ventana y se abre la de inicio de sesion
        self.Button_registro.clicked.connect(
            self.Registrar_usuario
        )  # cuando oprime el boton de registrar se registra el usuario
        self.Button_registro.clicked.connect(
            self.vaciar_textbox
        )  # cuando oprime el boton de registrar se vacian los textbox

    # Funcion que registra el usuario
    def Registrar_usuario(self):
        self.user = self.Textbox_usuario.text()
        self.password = self.Textbox_password.text()
        estado = Insertar_user(self.user, self.password)
        if estado != True:
            print("El usuario se registro correctamente el usuario")
        else:
            print("El usuario ya existe")

    def vaciar_textbox(self):
        self.Textbox_usuario.setText("")
        self.Textbox_password.setText("")
        self.Textbox_usuario.setFocus()

    # Funcion que abre la ventana de inicio de sesion y cierra la ventana de registro
    def cancelar(self):
        from Iniciador_inicio_sesion import Inicio_sesion

        self.inicio_sesion = Inicio_sesion()
        self.inicio_sesion.show()
        self.close()
