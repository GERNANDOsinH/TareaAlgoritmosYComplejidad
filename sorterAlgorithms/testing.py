import struct
import cProfile

from selectionSort import selectionSort
from quickSort import quickSort
from mergeSort import merge_sort


def leer_listas_binario(ruta_archivo, num_elementos_por_lista=100):
    listas = []
    
    with open(ruta_archivo, 'rb') as archivo:
        while True:
            datos = archivo.read(num_elementos_por_lista * 4)  # Lee 100 enteros (4 bytes cada uno)
            if not datos:
                break
            lista = list(struct.unpack(f'{num_elementos_por_lista}i', datos))
            listas.append(lista)
    
    return listas

listas = leer_listas_binario('sorterAlgorithms/testSorter.bin')

for lista in listas:
    # Funcion Sorting implementada en la biblioteca estandar de python.
    cProfile.run('sorted(lista)')

    # Mis funciones de ordenamiento
    cProfile.run('selectionSort(lista)')
    cProfile.run('quickSort(lista)')
    cProfile.run('merge_sort(lista)')