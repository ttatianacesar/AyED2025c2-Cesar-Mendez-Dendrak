"""
grafo.py
Representa el grafo no dirigido y lee el archivo aldeas.txt.
Incluye la clase UnionFind para el algoritmo de Kruskal.
"""

from collections import defaultdict
from typing import Dict, List, Tuple, Set

# --- Estructura Union-Find (para Kruskal) ---
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        """Crea un conjunto nuevo donde x es su propio padre"""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        """Devuelve el representante del conjunto de x (con compresión de camino)"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Une los conjuntos de x e y si son distintos"""
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False  # ya están unidos
        # unión por rango (para mantener el árbol balanceado)
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        return True


# --- Clase principal del grafo ---
class Graph:
    def __init__(self):
        self.adj: Dict[str, List[Tuple[str, int]]] = defaultdict(list)  # vecinos
        self.edges: Set[Tuple[int, str, str]] = set()  # aristas únicas (peso, u, v)
        self.nodes: Set[str] = set()  # aldeas

    def add_edge(self, u: str, v: str, w: int):
        """Agrega una arista no dirigida entre u y v con peso w"""
        u, v = u.strip(), v.strip()
        self.nodes.update([u, v])
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        # guardo arista ordenada para evitar duplicados (u < v)
        a, b = (u, v) if u <= v else (v, u)
        self.edges.add((w, a, b))

    def add_node(self, u: str):
        """Agrega un nodo aislado"""
        u = u.strip()
        self.nodes.add(u)
        self.adj[u]  # asegura que tenga lista vacía

    @staticmethod
    def from_file(path: str):
        """Crea un grafo leyendo el archivo aldeas.txt"""
        g = Graph()
        with open(path, "r", encoding="utf-8") as f:
            for lineno, raw in enumerate(f, start=1):
                line = raw.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) == 1:
                    g.add_node(parts[0])
                    continue
                if len(parts) != 3:
                    raise ValueError(f"Formato inválido en línea {lineno}: {raw}")
                u, v, w = parts
                g.add_edge(u, v, int(w))
        return g

    def components(self):
        """Devuelve las componentes conectadas del grafo (como conjuntos)"""
        seen = set()
        comps = []
        for node in sorted(self.nodes):
            if node in seen:
                continue
            stack = [node]
            comp = set()
            while stack:
                u = stack.pop()
                if u in comp:
                    continue
                comp.add(u)
                seen.add(u)
                for v, _ in self.adj[u]:
                    if v not in comp:
                        stack.append(v)
            comps.append(comp)
        return comps
