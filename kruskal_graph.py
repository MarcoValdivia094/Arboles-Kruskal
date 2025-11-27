import networkx as nx
import matplotlib.pyplot as plt

def plot_mst(nodes, edges, mst, title):
    G = nx.Graph()
    for w, u, v in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(7, 5))
    nx.draw(G, pos, with_labels=True, node_color="#87CEFA", node_size=900, font_weight="bold")
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    mst_edges = [(u, v) for u, v, w in mst]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=3, edge_color="red")

    plt.title(title)
    plt.show()

plot_mst(nodes, edges, mst_min, "Árbol de Mínimo Coste (Kruskal)")
plot_mst(nodes, edges, mst_max, "Árbol de Máximo Coste (Kruskal)")
