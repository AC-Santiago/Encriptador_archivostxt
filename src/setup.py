from Iniciador_inicio_sesion import Inicio_sesion
from Funciones.Manipulador_json import manage_json
from Iniciador_Pagina_inicial import Pagina_inicial

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    import sys

    ruta = "src/Archivos.json/Nombre_usuario.json"
    manage = manage_json(ruta)

    #! Verifica si existe una sesion iniciada
    if (
        manage.get_element("estado_check") == 1
    ):  #! Si existe una sesion iniciada se abre la ventana de la pagina inicial
        app = QApplication(sys.argv)
        window = Pagina_inicial()
        window.show()
        sys.exit(app.exec_())
    else:  #! Si no existe una sesion iniciada se abre la ventana de inicio de sesion
        app = QApplication(sys.argv)
        window = Inicio_sesion()
        window.show()
        sys.exit(app.exec_())
