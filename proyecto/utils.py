from PyQt5.QtWidgets import QTableWidgetItem

def llenar_tabla_con_matriz(tabla, matriz):
    tabla.setRowCount(matriz.cantidad_filas())
    tabla.setColumnCount(matriz.cantidad_columnas())

    for i in range(matriz.cantidad_filas()):
        for j in range(matriz.cantidad_columnas()):
            valor = QTableWidgetItem(str(matriz.get_elemento(i + 1, j + 1)))
            tabla.setItem(i, j, valor)