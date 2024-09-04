filas = int(input("Por favor ingresa el numero de filas que van a tener las matrices: "))#Se le pide al usuario la cantidad de columnas y de filas que van a tener las matrices.
columnas = int(input("Por favor ingresa el numero de columnas que van a tener las filas: "))
matrizA = []
matrizB = []
matrizResultante:list = []

def crearMatriz(a:list, filas, columnas):
    for fila in range(filas):#A traves de dos ciclo for se le va pidiendo al usuario elemento por elemento la primera matriz.
        a.append([]) 
        for columna in range(columnas):
            x = int(input(f"Por favor ingrese un numero entero de la primera matriz en la posicion {[fila, columna]}: "))
            a[fila].append(x)

def crearMatrizResultante():#Esta funcion crea una matriz del tamaño adecuado donde todos sus elementos son cero.
        for fila in range(filas):
            matrizResultante.append([]) 
            for columna in range(columnas):
                matrizResultante[fila].append(0)

def sumar_restar():
    print("Si quieres sumar las dos matrices escribe sumar, de lo contrario se restaran.")
    y = str(input("Tu respuesta: "))#Se le pregunta al usuario si quiere sumar o restar las matrices.

    if y.lower() == "sumar":
        for fila in range(filas):#Si el usuario quiere sumar las matrices, se suman los elementos correspondientes de las matrices a traves de un ciclo for.
            for columna in range(columnas):
                matrizResultante[fila][columna] = matrizA[fila][columna] + matrizB[fila][columna]
    else: 
        for fila in range(filas):#Si el usuario quiere restar las matrices, se restan los elementos correspondientes de las matrices a traves de un ciclo for.
            for columna in range(columnas):
                matrizResultante[fila][columna] = matrizA[fila][columna] - matrizB[fila][columna]

crearMatriz(matrizA,filas,columnas)
crearMatriz(matrizB,filas,columnas)
crearMatrizResultante()
sumar_restar()

print("La matriz resultante es: ")#Se imprime la matriz resultante
for i in range(filas):
    print(matrizResultante[i])

