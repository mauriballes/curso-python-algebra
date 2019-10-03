def mi_metodo(p1, p2, p3):
    a = p1
    b = p2
    c = p3
    suma = a + b + c
    return suma

#print(mi_metodo("asdasd", 5, 6))

"""
atributos y metodos: snake_case
clases: CamelCase
"""
class MiClase:
    # Valores Staticos
    numero2 = 13

    def __init__(self, numero=40):
        # Atributos
        self.numero = numero
        self.__numero3 = 16
    
    # Metodos
    def mensaje(self, msg="Hola", msg2="A", msg3="Todos"):
        print("Mensaje 1 = %s" % msg)
        print("Mensaje 2 = %s" % msg2)
        print("Mensaje 3 = %s" % msg3)


objeto = MiClase()
print("-----------------")
print(objeto.numero2)
print("-----------------")
print(objeto.numero)
print("-----------------")
print(objeto.mensaje(msg3="Los de Algebra"))


