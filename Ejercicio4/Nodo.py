class Nodo(object):
    info, sig = None, None
""""    
aux = Nodo()
aux.info = "Primer nodo"
palabra = input("Ingrese una palabra: ")
naux = aux
while (palabra != ""):
    nodo = Nodo()
    nodo.info = palabra
    naux.sig = nodo
    naux = nodo
    palabra = input("Ingrese una palabra: ")
    while (aux is not None):
        print(aux.info)
        aux = aux.sig
""" 