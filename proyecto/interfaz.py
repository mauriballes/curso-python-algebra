import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from .matriz import Matriz


class Interfaz(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("proyecto/ui_window.ui", self)

        self.matriz = Matriz(7, 7)

    def setup_ui(self):
        self.label.setText("Hola a todos a los chicos de Python")
        self.cargar_boton.clicked.connect(self._push_button_clicked)

    def _push_button_clicked(self):
        self.matriz = Matriz(7,7)
        self.label.setText(str(self.matriz))
        