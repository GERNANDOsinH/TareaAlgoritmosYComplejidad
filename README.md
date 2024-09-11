En este repositorio podra encontrar las funciones implementadas durante el desarrollo de la tarea "Dividir y Conquistar"
junto a los codigos que se utilizaron para generar las entradas y evaluar los distintos algoritmos.
Descripción de uso:
En las carpetas matrixAlgoritms y sorterAlgorithms podra encontrar los algoritmos de multiplicación de
matrices y ordenamiento junto a los respectivos datos de entrada en cada carpeta, los cuales pueden ser ejecutados en el
respectivo archivo testing.py alojado en cada carpeta que ejecutara los algoritmos con los distintos datos de entrada que
se encuentren en la misma carpetay arrojara graficas para que pueda analizar.
En la carpeta testGenerator podra encontrar los codigos que utilice para genere los datos de entrada, una vez eston son
ejecutados se generara un archivo .bin que debera mover a la carpeta matrixAlgoritms o sorterAlgorithms según corresponda.
Los codigos en la carpeta testGenerator no proporciona la capacidad de elegir la cantidad de datos generados ni como estaran
distribuidos, sin embargo puede generar sus propios datos de entrada teniendo en cuenta las siguientes consideraciones:
1) Las matrices deben ser estrictamente cuadradas y con tamaña 2**n.
2) Las matrices deben venir a pares de mismo tamaño para su multiplicación.
3) Los 2 primeros arreglos de entrada se supondran los arreglos descritos en el informe.
4) Tanto las matrices como los arreglos deben estar generados con la libreria numpy.
5) Los datos deben ser guardados en los datos de entrada mediante la función np.save(file,input)
