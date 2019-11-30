import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from .matriz import Matriz
from .utils import (llenar_tabla_con_matriz, 
                    suma_matrices, 
                    resta_matrices, 
                    producto_matrices,
                    producto_escalar_matrices,
                    inversa_matrices)

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
        self.boton_editar_a.clicked.connect(self._editar_matriz_a)
        self.accion_suma_matrices.triggered.connect(self._suma_matrices)
        self.accion_resta_matrices.triggered.connect(self._resta_matrices)
        self.accion_producto_matrices.triggered.connect(self._producto_matrices)
        self.accion_producto_escalar_matrices.triggered.connect(self._producto_escalar_matrices)
        self.accion_inversa_matrices.triggered.connect(self._inversa_matrices)

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

    def _editar_matriz_a(self):
        for fila in range(self.tabla_matriz_a.rowCount()):
            for columna in range(self.tabla_matriz_a.columnCount()):
                self.matriz_a[fila + 1][columna + 1] = int(self.tabla_matriz_a.item(fila, columna).text())

    def _suma_matrices(self):
        self.matriz_resultado = suma_matrices(self.matriz_a, self.matriz_b)
        llenar_tabla_con_matriz(self.tabla_matriz_resultado, self.matriz_resultado)

    def _resta_matrices(self):
        self.matriz_resultado = resta_matrices(self.matriz_a, self.matriz_b)
        llenar_tabla_con_matriz(self.tabla_matriz_resultado, self.matriz_resultado)

    def _producto_matrices(self):
        self.matriz_resultado = producto_matrices(self.matriz_a, self.matriz_b)
        llenar_tabla_con_matriz(self.tabla_matriz_resultado, self.matriz_resultado)

    def _producto_escalar_matrices(self):
        edit_escalar = self.edit_escalar.text()
        escalar = int(edit_escalar) if edit_escalar.isdigit() else 1

        self.matriz_resultado = producto_escalar_matrices(self.matriz_a, escalar)
        llenar_tabla_con_matriz(self.tabla_matriz_resultado, self.matriz_resultado)

    def _inversa_matrices(self):
        self.matriz_resultado = inversa_matrices(self.matriz_a)
        llenar_tabla_con_matriz(self.tabla_matriz_resultado, self.matriz_resultado)
        