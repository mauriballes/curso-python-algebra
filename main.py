import sys

from PyQt5 import QtWidgets

from proyecto.interfaz import Interfaz
from proyecto.matriz import Matriz

if __name__ == "__main__":
    # Init Interfaz
    app = QtWidgets.QApplication(sys.argv)
    window = Interfaz()
    window.setup_ui()
    window.show()
    app.exec_()
    
    """
    matriz = Matriz(4, 8)
    print(matriz.cantidad_filas())
    print(matriz.cantidad_columnas())
    print(matriz[1][1])
    print(matriz)
    matriz[1][1] = 15
    print(matriz)
    """
