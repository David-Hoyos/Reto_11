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
