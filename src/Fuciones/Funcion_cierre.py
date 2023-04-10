from PyQt5 import QtWidgets

#Funcion que cierre de la ventana Inicio_sesion y otra funcion que haga lo mismo pero con la ventana Registro
class Cierre_ventanas:
    def Cierre_ventana_Inicio_sesion(self):
        from Archivos_ui_en_py.Inicio_sesion import Inicio_sesion
        self.window = QtWidgets.QMainWindow()
        self.ui = Inicio_sesion()
        self.window.close()

    def Cierre_ventana_Registro(self):
        from Archivos_ui_en_py.Registro import Registro
        self.window = QtWidgets.QMainWindow()
        self.ui = Registro()
        self.window.close()
