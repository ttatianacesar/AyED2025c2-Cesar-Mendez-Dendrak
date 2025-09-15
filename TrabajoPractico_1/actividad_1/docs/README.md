Actividad 1: creación de ListaDobleEnlazada

Con este codigo se implementó una estructura de datos Lista Doblemente Enlazada lo que permite almacenar elementos en nodos conectados por referencias hacia adelante y hacia atras.

Cada nodo cuenta con su datos y las dos referencias "siguiente" y "anterior", y la lista mantiene los punteros en la cabeza y cola que permite insertar y extraer de los extremos.

Se implementaron operaciones básicas como:
esta_vacia (verifica si la lista no tiene elementos).
agregar_al_inicio y agregar_al_final (inserción eficiente en extremos).
insertar (inserción en una posición específica).
extraer (eliminación de un nodo por posición, con casos especiales en cabeza y cola).
copiar (genera una copia en O(n)).
invertir (invierte la lista in-place en O(n)).
concatenar y __add__ (unir listas).
__len__ y __iter__ (compatibilidad con funciones de Python).

Esta estructura esta diseñada para ser eficiente, modular y extensible, pero a su vez que sea simple y funcional. 

Análisis de los métodos len, copiar, invertir:
