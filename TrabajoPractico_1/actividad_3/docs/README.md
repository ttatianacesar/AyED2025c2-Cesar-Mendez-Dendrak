# 📝Documentación del proyecto
En esta actividad  se implementaron y compararon  los algoritmos de ordenamiento Bubble Sort, QuickSort, RadixSort, que luego fueron comparados con la función Sorted de Python, el objetivo es corroborar que funcionen correctamente con listas de números aleatorios de cinco dígitos generados aleatoriamente, medir los tiempos de ejecución de los métodos con listas y graficar en una misma figura los tiempos obtenidos. 

**BUBBLE SORT:**
compara pares de elementos adyacentes y los intercambia si están desordenados, se repite el proceso hasta que no haya más cambios.

análisis de complejidad: 
mejor caso: O(n) → si la lista ya está ordenada.
Peor caso y promedio: O(n²) → el tiempo crece cuadráticamente, lento en listas grandes, porque compara cada elemento con los demás.

pseudocodigo descriptivo:
" " "
Repetir tantas veces como elementos tenga la lista:
    Recorrer la lista comparando cada par de elementos consecutivos.
    Si un elemento es mayor que el siguiente, intercambiarlos.
Al final de cada pasada, el elemento más grande “sube” al final de la lista.
Repetir el proceso hasta que la lista quede completamente ordenada.
" " "
**QUICKSORT:**
elige un elemento de referencia, divide la lista en menores iguales y mayores y se aplica recursión a cada parte.

análisis de complejidad: 
caso promedio: O(n log n) →rápido, más eficiente que cuadrático, porque divide la lista en partes cada vez más chicas y ordena cada parte.
peor caso: O(n²) → caso cuadrático, si se elige mal el elemento de referencia y divide de manera despareja.

pseudocódigo descriptivo: 
Si la lista tiene cero o un elemento, ya está ordenada.
Elegir un elemento de referencia dentro de la lista.
Dividir la lista en tres partes:
Los elementos menores que el de referencia.
Los elementos iguales al de referencia.
Los elementos mayores que el de referencia.
Ordenar recursivamente la parte de los menores y la parte de los mayores.
Unir los resultados: primero los menores ordenados, después los iguales, y por último los mayores ordenados.
" " "

**RADIX SORT:**
algoritmo no comparativo que ordena números por dígitos, aplicando un ordenamiento estable  en cada posición decimal. 

análisis de complejidad: 
Se comporta como O(n) → el tiempo crece linealmente con la entrada → O(d·n), donde d es el número de dígitos (en este caso 5), crece lineal con n. Ordena por cada dígito del número, si los números tienen pocos dígitos, el tiempo crece solo con la cantidad de elementos.

pseudocódigo descriptivo: 
" " "
Identificar el número con más dígitos en la lista (el máximo).
Empezar por el dígito menos significativo (las unidades).
Ordenar la lista según ese dígito, usando un algoritmo auxiliar como Counting Sort.
Repetir el proceso con el siguiente dígito (decenas, centenas, etc.) hasta llegar al más significativo.
Cuando todos los dígitos han sido procesados, la lista queda ordenada.
" " "

**SORTED:** 
La función  incorporada de python que toma una lista o tupla y devuelve una nueva lista con los elementos ordenados, es rápida y estable.

análisis de complejidad: 
mejor caso: O(n) → lista ya ordenada, el tiempo crece linealmente con la entrada.
peor caso: O (n log n) → Combina dos algoritmos: uno rápido para listas grandes y otro eficiente para listas pequeñas o ya ordenadas, por eso se adapta tan bien a ambos casos.


**CONCLUSIONES:**
Se comprobó que los algoritmos ordenan correctamente pero no con igual eficiencia, Bubble Sort cumplió con la función de ordenar, pero más ineficiente, su tiempo de ejecución aumentó muy rápido a medida que aumentó el tamaño de la lista, confirmando la complejidad O(n²) ya que es un algoritmo cuadrático, por ende es  poco práctico para  listas grandes. QuickSort tuvo mejor  rendimiento que  Bubble Sort, en la mayoría de los casos se comportó con complejidad  O(n log n), lo que se reflejó en los tiempos de ejecución  más bajos. Radix Sort fue el algoritmo más rápido en estas pruebas, esto se debe a que trabaja con dígitos. Finalmente la función sorted resultó ser la más rápida y eficiente, comportándose de manera lineal.


