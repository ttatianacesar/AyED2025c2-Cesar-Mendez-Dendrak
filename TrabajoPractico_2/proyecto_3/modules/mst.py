"""
algoritmos.py
Contiene el algoritmo de Kruskal (MST) y la función para orientar el árbol desde una raíz.
"""

from collections import defaultdict, deque
from typing import List, Tuple, Dict, Set
from modules.grafo import UnionFind

def kruskal_mst(nodes: Set[str], edges: Set[Tuple[int, str, str]]):
    """
    Aplica el algoritmo de Kruskal para obtener el Árbol de Recubrimiento Mínimo.
    Retorna (lista_de_aristas, suma_total_pesos)
    """
    sorted_edges = sorted(edges, key=lambda x: x[0])  # orden por peso
    uf = UnionFind()
    for n in nodes:
        uf.make_set(n)

    mst = []
    total = 0
    for w, u, v in sorted_edges:
        if uf.union(u, v):  # si no genera ciclo
            mst.append((u, v, w))
            total += w
    return mst, total


def orient_tree_from_root(mst_edges: List[Tuple[str, str, int]], root: str):
    """
    Orienta las aristas del MST desde la raíz dada.
    Retorna:
      - parent[node]: quién le manda la noticia
      - children[node]: a quiénes envía la noticia
    """
    adj = defaultdict(list)
    for u, v, w in mst_edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = {root: None}
    children = defaultdict(list)

    q = deque([root])
    visited = {root}

    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                children[u].append(v)
                q.append(v)

    return parent, children
