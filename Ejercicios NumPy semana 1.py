import numpy as np

# Ejercicio 1: Array de 10 ceros
ej1 = np.zeros(10)

# Ejercicio 2: Números del 1 al 20
ej2 = np.arange(1, 21)

# Ejercicio 3: Números pares del 2 al 50
ej3 = np.arange(2, 51, 2)

# Ejercicio 5: Matriz 4x4 con valores aleatorios entre 0 y 1
ej5 = np.random.rand(4,4)

# Ejercicio 6: Suma elemento a elemento
a = np.array([1,2,3])
b = np.array([4,5,6])
ej6 = a + b

# Ejercicio 7: Multiplicación de dos matrices 3x3
m1 = np.random.randint(1, 11, (3,3))
m2 = np.random.randint(1, 11, (3,3))
ej7 = np.dot(m1, m2)

# Ejercicio 8: Array de 15 valores aleatorios entre 1 y 100
ej8 = np.random.randint(1, 101, 15)
max_val, min_val, prom = ej8.max(), ej8.min(), ej8.mean()

# Ejercicio 9: Matriz 5x5 y su diagonal
ej9 = np.arange(1, 26).reshape(5,5)
diag = np.diag(ej9)

# Ejercicio 10: Suma de filas y columnas
ej10 = np.random.randint(1, 21, (5,5))
suma_filas = ej10.sum(axis=1)
suma_columnas = ej10.sum(axis=0)
