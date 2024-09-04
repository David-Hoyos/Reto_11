filas = int(input("Por favor ingresa la cantidad de filas que va a tener tu matriz: "))#Se le pide el numero de filas y columnas que va a tener a matriz.
columnas = int(input("Por favor ingresa la cantidad de columnas que va a tener tu matriz: "))
matriz = []#Se crean una lista vacia que luego va a ser las matriz.

def crearMatriz():#Se le pide al usuario elemento por elemento de la matriz a traves de dos ciclos for.
    for fila in range(filas): 
        matriz.append([])
        for columna in range(columnas):
            numero = int(input(f"Por favor ingrese un numero entero de la primera matriz en la posicion {[fila, columna]}: "))
            matriz[fila].append(numero)

def sumarElementos(x:int):#Se crea una funcion que a traves de un ciclo for suma todos los elementos de una columna. 
    x -=1
    suma = 0
    for columna in range(columnas): 
        suma += matriz[x][columna] #Le suma a la variable suma todos los elementos en la fila que el usuario indico.
    print(f"La suma de los elementos de esa fila es {suma}")

if __name__ == "__main__":
    x = int(input("Ingrese el numero de la fila cuyos elementos quiere sumar: "))#Se le pide al usuario el numero de la fila cuyos elementos quiere sumar
    crearMatriz()#Se llaman a las funciones.
    sumarElementos(x)