# modules/graph.py
from typing import Dict, List, Tuple, Set

class Graph:
    """
    Grafo no dirigido con pesos.
    Almacenamos adyacencia y un conjunto de aristas (u,v,w) con u <= v para evitar duplicados.
    """
    def __init__(self):
        self.adj: Dict[str, List[Tuple[str,int]]] = {}
        self._edges: Set[Tuple[str,str,int]] = set()

    def add_edge(self, u: str, v: str, w: int):
        if u == v:
            raise ValueError("No se permiten lazos (u == v).")
        u = u.strip()
        v = v.strip()
        if w < 0:
            raise ValueError("Distancia negativa no permitida.")
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, []).append((u, w))
        a, b = (u, v) if u <= v else (v, u)
        self._edges.add((a, b, int(w)))

    def nodes(self) -> List[str]:
        return list(self.adj.keys())

    def edges(self) -> List[Tuple[str,str,int]]:
        # devuelve cada arista una vez
        return list(self._edges)

    def neighbors(self, node: str) -> List[Tuple[str,int]]:
        return self.adj.get(node, [])
