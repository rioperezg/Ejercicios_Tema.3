"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma 
iterativa
"""
I = [[1,0,0],
     [0,1,0],
     [0,0,1]]
# Funcion para clacular det 3x3 con sarrus
# Primero de forma iterativa
def Iter_sarrus(matrix):
    # primera multiplicaicon diagonal
    for indice in enumerate(matrix):
        if indice == 1:
            suma1 = matrix[1]*matrix[5]*matrix[9]
        # segunda multiplicacion
        elif indice == 2:
            suma2 = matrix[2]*matrix[6]*matrix[7]
        # tercera multipicaicon
        elif indice == 3:
            suma3 = matrix[3]*matrix[4]*matrix[8]
        #   lo mismo pero al reves:primera multiplicacion
        elif indice == 4:
            resta1 = matrix[4]*matrix[2]*matrix[9]
        elif indice == 5:
            resta2 = matrix[5]*matrix[3]*matrix[7]
        elif indice == 6:
            resta3 = matrix[6]*matrix[1]*matrix[8]
        else:
            pass
    suma = suma1 + suma2 + suma3
    resta = resta1 + resta2 + resta3
    return suma - resta

    



matriz = [[1, 3, 4],[-1, -5, 4],[1, 0, -2]]
print(Iter_sarrus(I))

# Ahora de forma recursiva
# Como podemos hacer para crear una funcion que se llame asi misma constantemente para calcular el det de una matriz 3x3 mediante 
# sarrus, Lo haremos con condicionales: Podemos hacer que cada vez que una posicion se multiplique se cambie ese valor por 0 para
# asi meter la condicion de que todas las posiciones tienen valor 0 se deje de iterar

def recur_Sarrus(matrix):
    if matrix == [[0,0,0],
                    [0,0,0],
                    [0,0,0]]:
                  
        print("Se ha calculado el determinante")
    else:
        matrix[0]*matrix[4]*matrix[8]

   


# print(recur_Sarrus(I))

def Iter_sarrus(matrix):
    # primera multiplicaicon diagonal
    for indice, i in enumerate(matrix):
        for indice1, j in enumerate(matrix):
            if indice == 1 and indice1 == 1:
                suma1 = matrix[1][1]*matrix[5][5]*matrix[9][9]

    suma = suma1 + suma2 + suma3
    resta = resta1 + resta2 + resta3
    return suma - resta