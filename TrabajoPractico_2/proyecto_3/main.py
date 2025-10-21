"""
main.py
Usa los módulos grafo.py y mst.py para resolver la actividad 3.
"""

import os
from modules.grafo import Graph
from modules.mst import kruskal_mst, orient_tree_from_root

def main(root="Peligros"):
    # --- Armar ruta completa del archivo de datos ---
    base_dir = os.path.dirname(__file__)               # carpeta donde está main.py
    path = os.path.join(base_dir, "data", "aldeas.txt")  # data/aldeas.txt

    # --- Leer archivo y construir grafo ---
    g = Graph.from_file(path)

    # --- Mostrar lista alfabética ---
    aldeas_ordenadas = sorted(g.nodes)
    print("Lista de aldeas (orden alfabético):")
    for a in aldeas_ordenadas:
        print(f"- {a}")
    print()

    # --- Detectar si hay componentes ---
    comps = g.components()
    if len(comps) > 1:
        print(f"⚠ El grafo tiene {len(comps)} componentes. Solo se orientará la de '{root}'.")
        print()

    # --- Aplicar Kruskal ---
    mst_edges, total_weight = kruskal_mst(g.nodes, g.edges)

    # --- Orientar desde la raíz ---
    if root not in g.nodes:
        raise ValueError(f"La raíz '{root}' no existe.")
    parent, children = orient_tree_from_root(mst_edges, root)

    # --- Mostrar resultados ---
    print("Distribución de noticias:")
    for a in aldeas_ordenadas:
        p = parent.get(a)
        ch = children.get(a, [])
        if p is None and a == root:
            recv = "(origen - Peligros)"
        elif p is None:
            recv = "(no conectado a la raíz)"
        else:
            recv = p
        print(f"- {a}: recibe de -> {recv}; envía a -> {ch}")
    print()
    print(f"Suma total de distancias recorridas (MST): {total_weight}")


if __name__ == "__main__":
    main("Peligros")
