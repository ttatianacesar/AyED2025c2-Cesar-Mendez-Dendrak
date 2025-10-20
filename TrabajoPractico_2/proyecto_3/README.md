*Estructura del proyecto*


__data__
aldeas.txt
 Contiene la descripción del mapa de aldeas y sus conexiones.
Cada línea representa un camino entre dos aldeas, junto con la distancia (en leguas).
Este archivo se utiliza como entrada para construir el grafo del problema mediante el módulo grafo.py.

__modules__

Contiene los módulos de implmentacion y lógica del proyecto.
 *grafo.py: implementa la clase "Graph", que modela el grafo no dirigido de aldeas y la estructura UnionFind, utilizada por el algoritmos de Kruskal.
 Permite leer el archivo aldeas.txt, almacenar nodos y aristas, y obtener las componentes conexas del grafo.
 *mst.py: contiene el algoritmo de Kruskal para obtener el árbol de recubrimiento minimo (MST) y una funcion auxiliar orient_tree_from_root() para orientar el árbol desde una aldea raíz dada.
 *init.py: indica que la carpeta modules es un paquete python, permitiendo importar sus modulos desde main.py

 __docs__
 
 *README.md: explica el propósito del proyecto, como esta organizado y las instrucciones basicas para ejecutarlo.

 __main.py__

 
 Archivo principal del proyecto.
Ejecuta el programa general combinando las funcionalidades de los módulos:
Lee el archivo aldeas.txt y construye el grafo.
Aplica el algoritmo de Kruskal para obtener el MST.
Orienta el árbol desde una raíz elegida (por defecto, "Peligros").
Muestra por consola la distribución de noticias entre aldeas y el costo total del recorrido.


