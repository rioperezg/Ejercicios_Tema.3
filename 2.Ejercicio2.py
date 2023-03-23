"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma 
iterativa
"""
# Funcion para clacular det 3x3 con sarrus
# Primero de forma iterativa
def Iter_sarrus(matrix):
# primera multiplicaicon diagonal
    for i in matrix:
        if i == 1:
            suma1 = matrix[1]*matrix[5]*matrix[9]
# segunda multiplicacion
        elif i == 2:
            suma2 = matrix[2]*matrix[6]*matrix[7]
# tercera multipicaicon
        elif i == 3:
            suma3 = matrix[3]*matrix[4]*matrix[8]
#   lo mismo pero al reves:primera multiplicacion
        elif i == 4:
            resta1 = matrix[4]*matrix[2]*matrix[9]
        elif i == 5:
            resta2 = matrix[5]*matrix[3]*matrix[7]
        elif i == 6:    
            resta3 = matrix[6]*matrix[1]*matrix[8]
    return (suma1 + suma2 + suma3) - (resta1 + resta2 + resta3)


matriz = [
           [1, 3, 4]
          ,[-1, -5, 4]
          ,[9, 0, -2]
]
print(Iter_sarrus(matriz))