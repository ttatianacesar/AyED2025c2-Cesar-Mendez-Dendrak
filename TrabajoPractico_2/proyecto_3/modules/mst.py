# modules/mst.py
from typing import List, Tuple, Dict
from modules.graph import Graph
from modules.unionfind import UnionFind
from collections import deque

def kruskal_mst(graph: Graph) -> Tuple[List[Tuple[str,str,int]], int]:
    """
    Devuelve (lista_de_aristas_en_MST, peso_total).
    Cada arista es (u,v,w) con u <= v.
    """
    edges = graph.edges()
    edges.sort(key=lambda x: x[2])  # ordenar por peso
    uf = UnionFind(graph.nodes())
    mst = []
    total = 0
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total += w
    return mst, total

def build_tree_adj_from_mst(nodes: List[str], mst_edges: List[Tuple[str,str,int]]) -> Dict[str, List[Tuple[str,int]]]:
    tree_adj = {n: [] for n in nodes}
    for u, v, w in mst_edges:
        tree_adj[u].append((v, w))
        tree_adj[v].append((u, w))
    return tree_adj

def parent_child_from_tree(tree_adj: Dict[str, List[Tuple[str,int]]], source: str):
    """
    BFS desde source para definir padre (de dónde recibe cada aldea) y lista de hijos.
    Retorna (parents_dict, children_dict, edge_weight_dict)
    """
    parents = {source: None}
    children = {n: [] for n in tree_adj}
    edge_weight = {}
    visited = set([source])
    q = deque([source])
    while q:
        u = q.popleft()
        for v, w in tree_adj[u]:
            edge_weight[(u, v)] = w
            edge_weight[(v, u)] = w
            if v not in visited:
                visited.add(v)
                parents[v] = u
                children[u].append(v)
                q.append(v)
    return parents, children, edge_weight
