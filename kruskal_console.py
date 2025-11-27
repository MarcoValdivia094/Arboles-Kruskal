# Algoritmo de Kruskal para Árbol de Expansión Mínimo y Máximo
# Usa estructura de conjuntos disjuntos (Union-Find)

class UnionFind:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 0 for n in nodes}

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return False
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

def kruskal(graph_edges, nodes, mode="min"):
    """
    graph_edges: lista de (peso, u, v)
    nodes: lista de nodos
    mode: "min" para MST mínimo, "max" para MST máximo
    """
    # Ordenamos aristas por peso (ascendente o descendente)
    graph_edges = sorted(graph_edges, key=lambda x: x[0], reverse=(mode=="max"))
    uf = UnionFind(nodes)
    mst = []

    print(f"=== Simulador Kruskal ({'mínimo' if mode=='min' else 'máximo'}) ===\n")

    for w, u, v in graph_edges:
        if uf.union(u, v):  # Si conecta dos componentes distintos
            mst.append((u, v, w))
            print(f"Conecto {u} - {v} con peso {w}")

    print("\nÁrbol construido:")
    for u, v, w in mst:
        print(f"{u} - {v} (peso {w})")

    return mst

# Ejemplo de uso
nodes = ["A", "B", "C", "D", "E"]
edges = [
    (2, "A", "B"),
    (3, "A", "C"),
    (1, "B", "C"),
    (4, "B", "D"),
    (5, "C", "D"),
    (6, "C", "E"),
    (7, "D", "E")
]

# Árbol de mínimo coste
mst_min = kruskal(edges, nodes, mode="min")

# Árbol de máximo coste
mst_max = kruskal(edges, nodes, mode="max")
