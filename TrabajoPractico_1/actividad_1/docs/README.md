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
len():  lo que se esperaba de este método era una eficiencia de O(1) (tiempo constante) y el comportamiento observado fueron
tiempos de ejecución extremadamente bajos y constantes, independientemente del tamaño de la lista, por lo que se concluye que es altamente eficiente. 

copiar(): este método recorre la lista original y genera una nueva lista con los mismos elementos, manteniendo el orden. Su complejidad es O(n), ya que debe visitar cada nodo una vez. De esta manera, la lista copiada es independiente de la original, evitando que cambios en una afecten a la otra. Su comportamiento es el esperado y se vuelve más costoso para listas grandes, por esa razón observamos un "pico" en la gráfica.

invertir(): este método recorre la lista e intercambia los punteros siguiente y anterior de cada nodo, además de intercambiar la cabeza y la cola. Esto permite invertir la lista en O(n) tiempo, de forma eficiente y sin necesidad de crear una nueva estructura auxiliar. En conclusión, resulta muy eficiente ya que realiza la inversión in-place, es decir, sin necesidad de memoria extra significativa. Su complejidad es O(n), lo cual es óptimo para este tipo de operación. Esto lo hace especialmente adecuado para listas de gran tamaño, ya que evita la sobrecarga de crear estructuras adicionales.
