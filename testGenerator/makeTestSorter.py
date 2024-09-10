import numpy as np


# Caso ascendente, los elementos estan ordenados de manera ascendente.
arreglos = []
array = np.arange(1,101)
arreglos.append(array)

# Caso aleatorio, los elementos estan generados de manera aleatoria.
array = np.random.randint(0,101,100)
arreglos.append(array)

with open('testSorterStatic.bin', 'wb') as file:
    for array in arreglos:
        np.save(file, array)

arreglos = []

# Variación de tamaño de los arreglos
for i in range(10):
    array = np.random.randint(0,101,2**i)
    arreglos.append(array)

with open('testSorter.bin', 'wb') as file:
    for array in arreglos:
        np.save(file, array)