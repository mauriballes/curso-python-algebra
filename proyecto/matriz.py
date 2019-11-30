class Matriz:
    """
    Constantes
    """
    DEFAULT_FILAS = 3
    DEFAULT_COLUMNAS = 3
    MAX_RANDOM_VALUE = 10

    """
    Constructor
    """
    def __init__(self, filas=DEFAULT_FILAS, columnas=DEFAULT_COLUMNAS):
        self._filas = filas
        self._columnas = columnas

        self._elementos = self._construir_matriz()

    """
    Getters (Metodos para acceder a los atributos)
    """
    def cantidad_filas(self):
        return self._filas
    
    def cantidad_columnas(self):
        return self._columnas

    def get_elemento(self, fila, columna):
        if fila < 1 or fila > self._filas or columna < 1 or columna > self._columnas:
            return None
        return self._elementos[fila - 1][columna - 1]

    def set_elemento(self, fila, columna, valor):
        if fila < 1 or fila > self._filas or columna < 1 or columna > self._columnas:
            return
        self._elementos[fila - 1][columna - 1] = valor

    def get_fila(self, fila):
        if fila < 1 or fila > self._filas:
            return []
        
        # Obtener fila
        fil = []
        for columna in range(1, self._columnas + 1):
            elemento = self.get_elemento(fila, columna)
            fil.append(elemento)

        return fil

    def get_columna(self, columna):
        if columna < 1 or columna > self._columnas:
            return []
        
        # Obtener columna
        col = []
        for fila in range(1, self._filas + 1):
            elemento = self.get_elemento(fila, columna)
            col.append(elemento)

        return col

    """
    Metodos privados de Clase
    """
    def _construir_matriz(self):
        import random
        matriz = []

        for x in range(self._filas):
            fila = []
            for y in range(self._columnas):
                fila.append(random.randint(1, Matriz.MAX_RANDOM_VALUE))
            matriz.append(fila)

        return matriz

    """
    Metodo toString (Representacion en String de la Clase)
    """
    def __str__(self):
        matriz = ""

        for filas in self._elementos:
            for valor in filas:
                matriz = matriz + str(valor) + ","
            matriz = matriz + "\n"

        return matriz
    
    """
    * Momento de Diversion *

    Esto es super experimental, no necesitas prestarle mucha atencion.
    De todos modos, aqui lo tienes ;-)
    """
    def __getitem__(self, fila):
        if fila < 1 or fila > self._filas:
            raise Exception("Fuera del Rango de las filas")
        return Matriz.Fila(self, fila, self._columnas, self._elementos[fila - 1])

    class Fila:
        def __init__(self, matriz, posicion, columnas, elementos):
            self._columnas = columnas   # Cantidad de Columnas
            self._elementos = elementos # Elementos de la Fila
            self._matriz = matriz       # Matriz Padre
            self._posicion = posicion   # Nro de la Fila en la Matriz
        
        def __getitem__(self, columna):
            if columna < 1 or columna > self._columnas:
                raise Exception("Fuera del Rango de las columnas")
            return self._elementos[columna - 1]

        def __setitem__(self, columna, valor):
            if columna < 1 or columna > self._columnas:
                raise Exception("Fuera del Rango de las columnas")
            self._matriz.set_elemento(self._posicion, columna, valor)
