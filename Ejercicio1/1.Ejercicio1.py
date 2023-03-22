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
# Hacemos un bucle para que la aguja 1 tenga 74 datos apilados
n = 74
for dato in range(n):
    Pila.apilar(aguja1, dato)

print(Pila.pila_vacia(aguja1))
print(Pila.en_cima(aguja1))
print(Pila.Tamaño(aguja1))