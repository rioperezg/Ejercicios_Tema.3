"""
En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una plataforma de bronce sobre la cual había 
tres agujas de diamante. En la primera aguja estaban apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que 
estaba debajo. A los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera, con dos condiciones, 
solo puede moverse un disco a la vez, y ningún disco podrá ponerse en- cima de otro más pequeño. Se dijo a los sacerdotes que, cuando 
hubieran terminado de mover los discos, llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.
"""
from pila import Pila
# Creamos tres pilas que corresponden a las tres agujas
aguja1 = Pila()
aguja2 = Pila()
aguja3 = Pila()
# intentemos hacerlo de forma recursiva: si n = 0 return se han apilado los discos y si no es = 0 llamamos recursivamente a la funcion
# def hanoi(n-1) y vamos apilando el disco
for i in range(74): 
    dato = i
    Pila.apilar(aguja1, dato)
Pila.barrido(aguja1)

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        # Mover el disco de la cima de origen a destino
        disco = origen.desapilar()
        destino.apilar(disco)
        print("Mover", disco, "de", origen, "a", destino)
    else:
        # 1. Mover n-1 discos de origen a auxiliar, usando destino como apoyo
        hanoi(n-1, origen, auxiliar, destino)
        # 2. Mover el disco n de origen a destino
        disco = origen.desapilar()
        destino.apilar(disco)
        print("Mover", disco, "de", origen, "a", destino)
        # 3. Mover n-1 discos de auxiliar a destino, usando origen como apoyo
        hanoi(n-1, auxiliar, destino, origen)

print(hanoi(74, aguja1, aguja2, aguja3))




