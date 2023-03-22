"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma 
iterativa
"""
# Funcion para clacular det 3x3 con sarrus
# Primero de forma iterativa
def Iter_sarrus(matrix):
# primera multiplicaicon diagonal
    for i, pos in matrix:
        if i == 1:
            suma1 = pos[1]*pos[5]*pos[9]
# segunda multiplicacion
        elif i == 2:
            pos[2]*pos[6]*pos[7]
# tercera multipicaicon
        elif i == 3:
            pos1 = pos
            for j, pos in matrix:
                if j == 4:
                    pos2 = pos
                    for k, pos in matrix:
                        if k == 8:
                            pos3 = pos
                            suma3 = pos1*pos2*pos3
                        else:
                            continue
                else:
                   continue
#   lo mismo pero al reves:primera multiplicacion
        elif i == 4:
            pos1 = pos
            for j, pos in matrix:
                if j == 2:
                    pos2 = pos
                    for k, pos in matrix:
                        if k == 9:
                            pos3 = pos
                            resta1 = pos1*pos2*pos3
                        else:
                            continue
                else:
                   continue     
        elif i == 5:
            pos1 = pos
            for j, pos in matrix:
                if j == 3:
                    pos2 = pos
                    for k, pos in matrix:
                        if k == 7:
                            pos3 = pos
                            resta2 = pos1*pos2*pos3
                        else:
                            continue
                else:
                   continue
        elif i == 6:    
            pos1 = pos
            for j, pos in matrix:
                if j == 1:
                    pos2 = pos
                    for k, pos in matrix:
                        if k == 8:
                            pos3 = pos
                            resta3 = pos1*pos2*pos3
                        else:
                            continue
                else:
                   continue
    return (suma1 + suma2 + suma3) - (resta1 + resta2 + resta3)
matriz = [1, 3, 4, -1, -5, 4, 9, 0, -2]
print(Iter_sarrus(matriz))