# Reto_11

## Punto 1 
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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

```

# Punto 2
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
def ingresar_matriz(filas, columnas):#Esta función pide al usuario los elementos de una matriz de tamaño 'filas x columnas'.
    print(f"Ingrese los elementos de la matriz de {filas}x{columnas}:")
    matriz = []
    for fila in range(filas):#A traves de dos ciclo for se le va pidiendo al usuario elemento por elemento la primera matriz.
        matriz.append([]) 
        for columna in range(columnas):
            x = int(input(f"Por favor ingrese un numero entero de la primera matriz en la posicion {[fila, columna]}: "))
            matriz[fila].append(x)
    return matriz  # Devuelve la matriz completa.

def mostrar_matriz(matriz):# Esta función muestra la matriz en un formato legible.
    for fila in matriz:  
        print("[", end=" ")  
        for elemento in fila:  
            print(elemento, end=" ")  
        print("]")  

def multiplicar_matrices(matriz1, matriz2):# Esta función multiplica dos matrices y devuelve la matriz resultante.
    filas_m1 = len(matriz1)  # Obtiene el número de filas y columnas de la primera matriz y el numero de columnas de la segunda matriz.
    columnas_m1 = len(matriz1[0])  
    columnas_m2 = len(matriz2[0])  

    
    resultado = [[0 for i in range(columnas_m2)] for j in range(filas_m1)]# Crear la matriz resultante de tamaño adecuado

    
    for i in range(filas_m1):  # Realizar la multiplicación de matrices
        for j in range(columnas_m2): 
            for k in range(columnas_m1):  
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]  # Acumula el producto de los elementos correspondientes.

    return resultado  # Devuelve la matriz resultante.

# Solicitar dimensiones de la primera matriz
filas_m1 = int(input("Ingrese el número de filas de la primera matriz: "))
columnas_m1 = int(input("Ingrese el número de columnas de la primera matriz: "))

# Solicitar dimensiones de la segunda matriz
filas_m2 = int(input("Ingrese el número de filas de la segunda matriz: "))
columnas_m2 = int(input("Ingrese el número de columnas de la segunda matriz: "))

# Verificar que las matrices se pueden multiplicar
if columnas_m1 != filas_m2:
    print("Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
else:
    
    matriz1 = ingresar_matriz(filas_m1, columnas_m1)# Ingresar las matrices  
    matriz2 = ingresar_matriz(filas_m2, columnas_m2)  

    
    resultado = multiplicar_matrices(matriz1, matriz2) # Multiplicar las matrices 

    
    print("\nPrimera matriz:")# Mostrar las matrices y el resultado
    mostrar_matriz(matriz1)  

    print("\nSegunda matriz:")
    mostrar_matriz(matriz2)  

    print("\nResultado de la multiplicación:")
    mostrar_matriz(resultado) 

```

# Punto 3 
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

# Punto 4

Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
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
    for fila in range(filas): 
        suma += matriz[fila][x] #Le suma a la variable suma todos los elementos en la columna que el usuario indico.
    print(f"La suma de los elementos de esa columnna es {suma}")

if __name__ == "__main__":
    x = int(input("Ingrese el numero de la columna cuyos elementos quiere sumar: "))#Se le pide al usuario el numero de la columna cuyos elementos quiere sumar
    crearMatriz()#Se llaman a las funciones.
    sumarElementos(x)
```

# Punto 5 
Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
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
```
