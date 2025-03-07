#SQUARES
squares1=[x**2 for x in range(1,11)]
# 1x1=1 -> x variable del range
# 2X2=4
numbers=[1,2,3,4,5,6,7,8,9,10,11]
squares2=[x**3 for x in numbers]
# 1x1x1=1 -> x variable del range
# 2X2x2=8
print(squares2)

#CONVERT CELSIUS TO FARENHEIT
#°F=(9/5*°C)+32
celsius=[0,10,20,30,40]
fahrenheit=[(temp*9/5)*32 for temp in celsius]
# (10*9/5)*32=576
# (20*9/5)*32=1152
print("Temperatura en F:", fahrenheit)

#Numeros pares 
evens=[x for x in range(1,21) if x%2==0]
print("Numeros pares:",evens)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
transposed=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
#EXPLICACIÓN DEL CODIGO.
#parte1: Esta expresión obtiene la cantidad de columnas de la matriz original.
#numbers_columns=len(matrix[0])
#matrix[0] es [1, 2, 3] (la primera fila).
#len(matrix[0]) es 3 (porque hay 3 elementos en esa fila).
#print("Len columns of matrix:",numbers_columns)
#parte2: range(len(matrix[0])) Genera una secuencia de índices para recorrer las columnas
#Esto significa que el bucle recorrera los indices 0,1,2 para acceder a cada columna de la matriz.
#parte3 [row[i] for row in matrix] -> Esta es la parte interna de la lista por comprension.
#Cada valor de i (que representa el numero de columna), recoge los elementos de esa columna para todas las filas.
#Ejemplo con i=0 
#[row[0] for in matrix]
#Proceso:
#Para row = [1, 2, 3] → row[0] es 1.
#Para row = [4, 5, 6] → row[0] es 4.
#Para row = [7, 8, 9] → row[0] es 7.
#resultado:
#[row[0] for row in matrix]  # ➞ [1, 4, 7]
#*********************************************#
#Ejemplo con i=1
#[row[1] for in matrix]
#Proceso:
#Para row = [1, 2, 3] → row[1] es 2.
#Para row = [4, 5, 6] → row[1] es 5.
#Para row = [7, 8, 9] → row[1] es 8.
#resultado:
#[row[1] for row in matrix]  # ➞ [2, 5, 8]
#*********************************************#
#Ejemplo con i=2
#[row[2] for in matrix]
#Proceso:
#Para row = [1, 2, 3] → row[2] es 3.
#Para row = [4, 5, 6] → row[2] es 6.
#Para row = [7, 8, 9] → row[2] es 9.
#resultado:
#[row[2] for row in matrix]  # ➞ [3, 6, 9]

# transposed=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print("The Matrix original:",matrix)
# print("The transposed of matrix:",transposed)
