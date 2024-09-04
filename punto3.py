filas = int(input("Por favor ingresa la cantidad de filas que va a tener tu matriz: "))#Se le pide el numero de filas y columnas que va a tener a matriz.
columnas = int(input("Por favor ingresa la cantidad de columnas que va a tener tu matriz: "))
matriz = []#Se crean dos listas vacias que luego van a ser las matrices.
matrizTranspuesta = []

def crearMatriz():#Se le pide al usuario elemento por elemento de la matriz a traves de dos ciclos for.
    for fila in range(filas): 
        matriz.append([])
        for columna in range(columnas):
            numero = int(input(f"Por favor ingrese un numero entero de la primera matriz en la posicion {[fila, columna]}: "))
            matriz[fila].append(numero)

def crearMatrizTranspuesta():#Se crea una matriz donde su numero de columnas es el numero de filas de la primera matriz y viceversa.
    for columna in range(columnas): 
        matrizTranspuesta.append([])
        for fila in range(filas):
            matrizTranspuesta[columna].append(0)

def invertirMatriz():#Se le asignan los valores a la matriz transpuesta inviertiendo las filas y columnas en las que se encuentran los elementos de la primera matriz.
    for fila in range(filas):
        for columna in range(columnas):
            matrizTranspuesta[columna][fila] = matriz[fila][columna]

if __name__  ==  "__main__":
    crearMatriz()#Se llaman a todas las funciones
    crearMatrizTranspuesta()
    invertirMatriz()
    print("La matriz transpuesta es:")
    
    for i in range(columnas):#Se imprime el resultado
        print(matrizTranspuesta[i])