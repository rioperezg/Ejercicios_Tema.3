""""
class Disco:
    def _init_(self, nombre):
        self.nombre = nombre
        
class Torre:
    def _init_(self, nombre):
        self.nombre = nombre
        self.discos = []

    def agregar_disco(self, disco):
        if not self.discos or disco.nombre < self.discos[-1].nombre:
            self.discos.append(disco)
            return True
        else:
            return False

def mover_torres(n, torre1, torre3, torre2):
    if n == 0:
        print("No hay discos que mover.")
    elif n == 1:
        print(f"Mover disco {torre1.discos[-1].nombre} de torre {torre1.nombre} a torre {torre3.nombre}")
        torre3.agregar_disco(torre1.discos.pop())
    else:
        mover_torres(n - 1, torre1, torre2, torre3)
        print(f"Mover disco {torre1.discos[-1].nombre} de torre {torre1.nombre} a torre {torre3.nombre}")
        torre3.agregar_disco(torre1.discos.pop())
        mover_torres(n - 1, torre2, torre3, torre1)
        return True

torre1 = Torre("1")
torre2 = Torre("2")
torre3 = Torre("3")
n = 3

for i in range(n, 0, -1): # sirve para agregar los discos a la torre 1 en orden de mayor a menor (de 3 a 1) 
    torre1.agregar_disco(Disco(str(i))) # str(i) es para convertir el numero a string y poder agregarlo a la torre como nombre del disco 

mover_torres(n, torre1, torre3, torre2)
"""


from pila import Pila
# Creamos tres pilas que corresponden a las tres agujas
aguja1 = Pila()
aguja2 = Pila()
aguja3 = Pila()
# intentemos hacerlo de forma recursiva: si n = 0 return se han apilado los discos y si no es = 0 llamamos recursivamente a la funcion
# def hanoi(n-1) y vamos apilando el disco 
def hanoi(n):
    Dato = "Disco{}".format(n)
    if n == 0:
        print("Se han apilado los discos")
        return Pila.barrido(aguja1)
    else:
        Pila.apilar(aguja1, Dato)
        return hanoi(n-1)
print(hanoi(7))