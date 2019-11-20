import sys

from PyQt5 import QtWidgets

from proyecto.interfaz import Interfaz

if __name__ == "__main__":
    # Init Interfaz
    app = QtWidgets.QApplication(sys.argv)
    window = Interfaz()
    window.setup_ui()
    window.show()
    app.exec_()

