class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas

        self.elementos = self.construir_matriz()

    def construir_matriz(self):
        return [ self.crear_filas() for y in range(self.filas) ]

    def crear_filas(self):
        import random
        return [ random.randint(1, 100) for x in range(self.columnas) ]

    def __str__(self):
        matriz = ""
        for filas in self.elementos:
            for valor in filas:
                matriz = matriz + str(valor) + ","
            matriz = matriz + "\n"
        return matriz
            
