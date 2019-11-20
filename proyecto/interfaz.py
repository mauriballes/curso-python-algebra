import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from .matriz import Matriz
from .utils import llenar_tabla_con_matriz

class Interfaz(QtWidgets.QMainWindow):
    """
    Constructor
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("proyecto/ui_window.ui", self)

        # Declarando Objetos
        self.matriz_a = None
        self.matriz_b = None
        self.matriz_resultado = None

    """
    Configurando Interfaz
    """
    def setup_ui(self):
        # self.label.setText("Hola a todos a los chicos de Python")
        # Acciones Click
        self.boton_a.clicked.connect(self._generar_matriz_a)
        self.boton_b.clicked.connect(self._generar_matriz_b)

    """
    Acciones
    """
    def _generar_matriz_a(self):
        edit_filas = self.edit_fila_a.text()
        edit_columnas = self.edit_columna_a.text()

        filas = int(edit_filas) if edit_filas.isdigit() else Matriz.DEFAULT_FILAS
        columnas = int(edit_columnas) if edit_columnas.isdigit() else Matriz.DEFAULT_COLUMNAS

        self.matriz_a = Matriz(filas, columnas)
        llenar_tabla_con_matriz(self.tabla_matriz_a, self.matriz_a)

    def _generar_matriz_b(self):
        edit_filas = self.edit_fila_b.text()
        edit_columnas = self.edit_columna_b.text()

        filas = int(edit_filas) if edit_filas.isdigit() else Matriz.DEFAULT_FILAS
        columnas = int(edit_columnas) if edit_columnas.isdigit() else Matriz.DEFAULT_COLUMNAS

        self.matriz_b = Matriz(filas, columnas)
        llenar_tabla_con_matriz(self.tabla_matriz_b, self.matriz_b)
        