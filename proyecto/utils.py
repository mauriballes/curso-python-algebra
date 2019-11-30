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
    # A(mxn) + B(mxn) = C(mxn)
    matriz_c = Matriz(matriz_a.cantidad_filas(), matriz_a.cantidad_columnas())
    for i in range(1, matriz_a.cantidad_filas() + 1):
        for j in range(1, matriz_a.cantidad_columnas() + 1):
            matriz_c[i][j] = matriz_a[i][j] + matriz_b[i][j]
            # valor = matriz_a.get_elemento(i,j) + matriz_b.get_elemento(i,j)
            # matriz_c.set_elemento(i,j, valor)
    """
    i = 3
    j = 3

    [[1,2,3],   [[1,2,3],     [[ 2, 4, 6], 
    [4,5,6]]     [5, 7,8]],   [ 9, 12, 14]]
    """

    return matriz_c

def resta_matrices(matriz_a, matriz_b):
    # A(mxn) - B(mxn) = C(mxn)
    matriz_c = Matriz(matriz_a.cantidad_filas(), matriz_a.cantidad_columnas())
    for i in range(1, matriz_a.cantidad_filas() + 1):
        for j in range(1, matriz_a.cantidad_columnas() + 1):
            matriz_c[i][j] = matriz_a[i][j] - matriz_b[i][j]
            # valor = matriz_a.get_elemento(i,j) - matriz_b.get_elemento(i,j)
            # matriz_c.set_elemento(i,j, valor)
    """
    i = 3
    j = 3

    [[1,2,3],   [[1,2,3],     [[ 2, 4, 6], 
    [4,5,6]]     [5, 7,8]],   [ 9, 12, 14]]
    """

    return matriz_c

def producto_matrices(matriz_a: Matriz, matriz_b: Matriz):
    matriz_r = Matriz(matriz_a.cantidad_filas(), matriz_b.cantidad_columnas())
    
    if matriz_a.cantidad_columnas() != matriz_b.cantidad_filas():
        raise Exception("Nel Perro!!!")

    i = 1
    j = 1

    for fila in range(1, matriz_a.cantidad_filas() + 1):
        j = 1
        for columna in range(1, matriz_b.cantidad_columnas() + 1):
            fil = matriz_a.get_fila(fila)
            col = matriz_b.get_columna(columna)
            valor = 0
            
            for k in range(len(fil)):
                valor = valor + fil[k] * col[k]
            
            matriz_r[i][j] = valor
            j = j + 1
        i = i + 1

    return matriz_r

def producto_escalar_matrices(matriz_a, escalar):
    matriz_c = Matriz(matriz_a.cantidad_filas(), matriz_a.cantidad_columnas())
    for i in range(1, matriz_a.cantidad_filas() + 1):
        for j in range(1, matriz_a.cantidad_columnas() + 1):
            matriz_c[i][j] = matriz_a[i][j] * escalar
            # valor = matriz_a.get_elemento(i,j) + matriz_b.get_elemento(i,j)
            # matriz_c.set_elemento(i,j, valor)
    """
    i = 3
    j = 3

    [[1,2,3],   [[1,2,3],     [[ 2, 4, 6], 
    [4,5,6]]     [5, 7,8]],   [ 9, 12, 14]]
    """

    return matriz_c

def inversa_matrices(matriz_a):
    return Matriz()