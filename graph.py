import networkx as nx
import matplotlib.pyplot as plt

# Definieer de grafiek
akGraph = {
    'a': {'b': 5, 'c': 8, 'd': 10},
    'b': {'a': 5, 'e': 7, 'f': 6},
    'c': {'a': 8, 'g': 4},
    'd': {'a': 10, 'h': 9},
    'e': {'b': 7, 'i': 12},
    'f': {'b': 6, 'j': 14},
    'g': {'c': 4, 'k': 11},
    'h': {'d': 9, 'k': 3},
    'i': {'e': 12, 'j': 1},
    'j': {'f': 14, 'i': 1, 'k': 2},
    'k': {'g': 11, 'h': 3, 'j': 2}
}

# Maak een ongerichte grafiek
G = nx.Graph()

# Voeg randen toe met gewichten
for node, edges in akGraph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Definieer de lay-out
pos = nx.spring_layout(G)  # Posities voor alle nodes

# Teken de nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# Teken de randen
nx.draw_networkx_edges(G, pos, width=2)

# Voeg labels toe aan de nodes
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

# Voeg labels toe aan de randen (gewichten)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Toon de plot
plt.title("Dijkstra akGraph, (not to scale).")
plt.axis("off")  # Verberg assen
plt.show()