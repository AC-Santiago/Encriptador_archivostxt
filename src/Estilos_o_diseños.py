class Estilos(object):
    #Estilo de Frame de fondo
    def Estilo_Frame_Fondo(self):
        Estilos_Frame_fondo = str("QFrame {\n"
                                "border-radius:10px;\n"
                                "background-image: url(src/imagenes/Fondo.svg);\n"
                                "background-repeat: no-repeat;\n"
                                "background-position: center;\n"" }")
        return Estilos_Frame_fondo

    #Estilo de Botones_inicio_sesion
    def Estilo_Boton_Inicio_Sesion(self):
        Estilos_Boton_Inicio_Sesion = str("QPushButton{\n"
                                        "\n"
                                        "  display: inline-block;\n"
                                        "  -webkit-box-sizing: content-box;\n"
                                        "  -moz-box-sizing: content-box;\n"
                                        "  box-sizing: content-box;\n"
                                        "  cursor: pointer;\n"
                                        "  padding: 10px 20px;\n"
                                        "  border: 1px solid rgba(90,90,90,1);\n"
                                        "  -webkit-border-radius: 12px;\n"
                                        "  border-radius: 12px;\n"
                                        "  font: normal 16px/normal Arial, Helvetica, sans-serif;\n"
                                        "  color: rgba(0,0,0,1);\n"
                                        "  -o-text-overflow: clip;\n"
                                        "  text-overflow: clip;\n"
                                        "  background: -webkit-linear-gradient(0deg, rgba(255,255,255,0) 0, rgba(255,255,255,1) 100%);\n"
                                        "  background: -moz-linear-gradient(90deg, rgba(255,255,255,0) 0, rgba(255,255,255,1) 100%);\n"
                                        "  background: linear-gradient(90deg, rgba(255,255,255,0) 0, rgba(255,255,255,1) 100%);\n"
                                        "  background-position: 50% 50%;\n"
                                        "  -webkit-background-origin: padding-box;\n"
                                        "  background-origin: padding-box;\n"
                                        "  -webkit-background-clip: border-box;\n"
                                        "  background-clip: border-box;\n"
                                        "  -webkit-background-size: auto auto;\n"
                                        "  background-size: auto auto;\n"
                                        "  -webkit-box-shadow: 2px 2px 2px 0 rgba(140,140,140,1) ;\n"
                                        "  box-shadow: 2px 2px 2px 0 rgba(140,140,140,1) ;\n"
                                        "  -webkit-transition: all 300ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                        "  -moz-transition: all 300ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                        "  -o-transition: all 300ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                        "  transition: all 300ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "   background-color: rgb(234, 236, 238);\n"
                                        "   cursor: pointer\n"
                                        "}\n")
        return Estilos_Boton_Inicio_Sesion
    
    # Estilo de los labeles
    def Estilo_Label(self):        
        Estilos_Label = str("QLabel{\n"
                        "  -webkit-box-sizing: content-box;\n"
                        "  -moz-box-sizing: content-box;\n"
                        "  box-sizing: content-box;\n"
                        "  border: none;\n"
                        "  font: normal 16px/1 Arial, Helvetica, sans-serif;\n"
                        "  background-color: none;\n"
                        "  -o-text-overflow: ellipsis;\n"
                        "  text-overflow: ellipsis;\n"
                        "}")
        return Estilos_Label
    
    # Estilo del textbox_usuario
    def Estilo_Textbox_Usuario(self):
        Estilos_Textbox_Usuario = str("QLineEdit{\n"
                                    "  display: inline-block;\n"
                                    "  -webkit-box-sizing: content-box;\n"
                                    "  -moz-box-sizing: content-box;\n"
                                    "  box-sizing: content-box;\n"
                                    "  padding: 10px 20px;\n"
                                    "  border: 1px solid #b7b7b7;\n"
                                    "  -webkit-border-radius: 12px;\n"
                                    "  border-radius: 12px;\n"
                                    "  font: normal 16px/normal Arial, Helvetica, sans-serif;\n"
                                    "  color: rgba(0,0,0,1);\n"
                                    "  -o-text-overflow: clip;\n"
                                    "  text-overflow: clip;\n"
                                    "  background: -webkit-linear-gradient(0deg, rgba(0,0,0,0) 0, rgba(224,224,224,1) 100%);\n"
                                    "  background: -moz-linear-gradient(90deg, rgba(0,0,0,0) 0, rgba(224,224,224,1) 100%);\n"
                                    "  background: linear-gradient(90deg, rgba(0,0,0,0) 0, rgba(224,224,224,1) 100%);\n"
                                    "  background-position: 50% 50%;\n"
                                    "  -webkit-background-origin: padding-box;\n"
                                    "  background-origin: padding-box;\n"
                                    "  -webkit-background-clip: border-box;\n"
                                    "  background-clip: border-box;\n"
                                    "  -webkit-background-size: auto auto;\n"
                                    "  background-size: auto auto;\n"
                                    "  -webkit-box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) inset;\n"
                                    "  box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) inset;\n"
                                    "  text-shadow: 1px 1px 0 rgba(255,255,255,0.66) ;\n"
                                    "  -webkit-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                    "  -moz-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                    "  -o-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                    "  transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                    "\n"
                                    "}")  
        return Estilos_Textbox_Usuario

    # Estilo del textbox_contraseña
    def Estilo_Textbox_Contraseña(self):
        Estilos_Textbox_Contraseña = str("QLineEdit{\n"
                                        "  display: inline-block;\n"
                                        "  -webkit-box-sizing: content-box;\n"
                                        "  -moz-box-sizing: content-box;\n"
                                        "  box-sizing: content-box;\n"
                                        "  padding: 10px 20px;\n"
                                        "  border: 1px solid #b7b7b7;\n"
                                        "  -webkit-border-radius: 12px;\n"
                                        "  border-radius: 12px;\n"
                                        "  font: normal 16px/normal Arial, Helvetica, sans-serif;\n"
                                        "  color: rgba(0,0,0,1);\n"
                                        "  -o-text-overflow: clip;\n"
                                        "  text-overflow: clip;\n"
                                        "  background: -webkit-linear-gradient(0deg, rgba(0,0,0,0) 0, rgba(224,224,224,1) 100%);\n"
                                        "  background: -moz-linear-gradient(90deg, rgba(0,0,0,0) 0, rgba(224,224,224,1) 100%);\n"
                                        "  background: linear-gradient(90deg, rgba(0,0,0,0) 0, rgba(224,224,224,1) 100%);\n"
                                        "  background-position: 50% 50%;\n"
                                        "  -webkit-background-origin: padding-box;\n"
                                        "  background-origin: padding-box;\n"
                                        "  -webkit-background-clip: border-box;\n"
                                        "  background-clip: border-box;\n"
                                        "  -webkit-background-size: auto auto;\n"
                                        "  background-size: auto auto;\n"
                                        "  -webkit-box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) inset;\n"
                                        "  box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) inset;\n"
                                        "  text-shadow: 1px 1px 0 rgba(255,255,255,0.66) ;\n"
                                        "  -webkit-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                        "  -moz-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                        "  -o-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                        "  transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);\n"
                                        "\n"
                                        "}")
        return Estilos_Textbox_Contraseña
    
    # Estilo del checkbox_manter_sesion
    def Estilo_Checkbox_Manter_Sesion(self):
        Estilos_Checkbox_Manter_Sesion = str("QCheckBox {\n"
                                        "  -webkit-box-sizing: content-box;\n"
                                        "  -moz-box-sizing: content-box;\n"
                                        "  box-sizing: content-box;\n"
                                        "  border: none;\n"
                                        "  font: normal 16px/1 Arial, Helvetica, sans-serif;\n"
                                        "  color: black;\n"
                                        "  -o-text-overflow: ellipsis;\n"
                                        "  text-overflow: ellipsis;\n"
                                        "}")
        return Estilos_Checkbox_Manter_Sesion