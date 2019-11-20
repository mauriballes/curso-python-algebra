from PyQt5.QtWidgets import QTableWidgetItem

from .matriz import Matriz

def llenar_tabla_con_matriz(tabla, matriz):
    tabla.setRowCount(matriz.cantidad_filas())
    tabla.setColumnCount(matriz.cantidad_columnas())

    for i in range(matriz.cantidad_filas()):
        for j in range(matriz.cantidad_columnas()):
            valor = QTableWidgetItem(str(matriz.get_elemento(i + 1, j + 1)))
            tabla.setItem(i, j, valor)

def suma_matrices(matriz_a, matriz_b):
    return Matriz()

def resta_matrices(matriz_a, matriz_b):
    return Matriz()

def producto_matrices(matriz_a, matriz_b):
    return Matriz()

def producto_escalar_matrices(matriz_a, escalar):
    return Matriz()

def inversa_matrices(matriz_a):
    return Matriz()