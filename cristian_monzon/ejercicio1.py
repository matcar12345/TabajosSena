# Primero vamos a establecer las columnas y filas por cada matriz

#antes de todo, pediremos los espacios y las columnas para las dos matrices
filas = int(input("Ingrese las filas para ambas matrices : "))
columnas = int(input("Ingrese las columnas por cada fila de ambas matrices : "))

matriz1 = []
matriz2 = []

#ahora vamos a crear los espacios en ambas matrices con tres ciclos,
#  uno para recorrer las matrices
#  otro para recorrer las filas
#  otro para recorrer las columnas de la fila

cont_matriz = 1


#Recorremos las matrices
while cont_matriz <= 2:
    #Ciclo para recorrer las filas
    fila_turno = 0
    # Matriz la cual, llenaremos con lso espacios, se le dara
    # el valor a la matriz1 o matriz2 dependiendo del turno o "cont_matriz"
    matriz_turno = []

    while fila_turno != filas:
        fila_matriz = []
        columna_turno = 0
        #ciclo para recorrer lascolumnas
        while columna_turno!= columnas:
            fila_matriz.append(0)
            columna_turno+=1
        fila_turno +=1
        matriz_turno.append(fila_matriz)


    # Este if asigna la matriz con espacion dependiendo
    # del numero
    if cont_matriz ==1 :
        matriz1 = matriz_turno
    elif cont_matriz == 2:
        matriz2 = matriz_turno
    # Aumentamos el numero y cambiamos la matriz
    cont_matriz+=1

#AHORA vamos a llenaR las matrices vacias:

#volveremos a usar en cont_matriz, asi que lo resetearemos:
cont_matriz = 0
#print(matriz1)
#print(matriz2)


print("Iniciamos con el proceso de recoleccion de numeros en las matrices: ")
#Vamos a recorrerlo de igual manera a como lo hicimos arriba

while fila_turno < filas:

    print(f"llenando la fila de turno {fila_turno}:")

    #ciclo para ingresar los numeros de cada fila

    #variable para ir recorriendo las columnas
    columna_turno = 0
    while columna_turno<columnas:
        #Solicita al usuario 
        num1 = int(input(f"Numero para a fila:{fila_turno} columna :{columna_turno} en la matriz 1 :"))
        num2 = int(input(f"Numero para a fila:{fila_turno} columna :{columna_turno} en la matriz 2 :"))
        matriz1[fila_turno][columna_turno] = num1
        matriz2[fila_turno][columna_turno] = num2
        columna_turno += 1

    #apenas termine de recorrer las columnas, avanza con la siguiente fila
    fila_turno += 1


#confirmamos que los numeros se agregaron correctamente
print("matriz 1")
print(matriz1)
print("matriz 2")
print(matriz2)




# APARTADO DE SUMAS
# Matriz para almacenar los resultados:
# y le asignamos todos los espacios vacios paraalmacenar las sumas
#matriz_suma = matriz1