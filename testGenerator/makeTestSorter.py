import random
import struct


with open('testSorter.bin', 'wb') as testSorter:
    # Caso constante, los elementos son iguales.
    for i in range(0,100):
        testSorter.write(struct.pack('i', 0))

    # Caso ascendente, los elementos estan ordenados de manera ascendente.
    for i in range(0,100):
        testSorter.write(struct.pack('i', (i + 1)))
    
    # Caso aleatorio, los elementos estan generados de manera aleatoria.
    for i in range(0,100):
        testSorter.write(struct.pack('i', random.randint(0,100)))