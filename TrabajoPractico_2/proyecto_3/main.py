# main.py
import sys
from modules.io_utils import load_aldeas_from_file
from modules.mst import kruskal_mst, build_tree_adj_from_mst, parent_child_from_tree

def main(path_ald: str, source: str = "Peligros"):
    # cargar grafo
    graph = load_aldeas_from_file(path_ald)
    nodes = sorted(graph.nodes())

    # 1) Mostrar lista de aldeas en orden alfabético
    print("Aldeas (alfabético):")
    for n in nodes:
        print(" -", n)
    print()

    # 2) Calcular MST
    mst_edges, total_weight = kruskal_mst(graph)
    print("Aristas del MST (u, v, distancia):")
    for e in mst_edges:
        print(e)
    print(f"Peso total del MST (suma de distancias): {total_weight}\n")

    # 3) Construir árbol y padres/hijos desde source
    tree_adj = build_tree_adj_from_mst(nodes, mst_edges)
    if source not in tree_adj:
        print(f"Atención: la aldea fuente '{source}' no está en el grafo.")
        return

    parents, children, edge_weight = parent_child_from_tree(tree_adj, source)

    # 4) Mostrar para cada aldea de qué vecina recibe la noticia y a qué vecinas envía réplicas,
    #    y la distancia que envía desde su palomar (suma de distancias a sus hijos)
    print("Envíos por aldea (padre -> hijos) y sumas enviadas desde cada palomar:")
    total_sent_per_palomar = {}
    for a in nodes:
        parent = parents.get(a)
        childs = children.get(a, [])
        s = sum(edge_weight[(a, c)] for c in childs)
        total_sent_per_palomar[a] = s
        print(f"Aldea: {a}")
        print(f"  recibe de: {parent}")
        print(f"  envía a: {childs}")
        print(f"  distancia total enviada desde su palomar: {s}")
        print()

    # 5) Suma total (control):
    print("Suma total de distancias (verificación):", sum(total_sent_per_palomar.values()))
    print("Nota: debe coincidir con peso total del MST.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py data/aldeas.txt [NombreFuente]")
    else:
        path = sys.argv[1]
        src = sys.argv[2] if len(sys.argv) >= 3 else "Peligros"
        main(path, src)
