from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, airports, routes):
        self.graph = defaultdict(list)
        self.airports = airports
        self.routes = routes
        self.build_graph()

    def build_graph(self):
        for u, v in self.routes:
            self.graph[u].append(v)

    def add_route(self, u, v):
        self.graph[u].append(v)

    # def plot_graph(self):
    #     G = nx.DiGraph()
    #     G.add_edges_from(self.routes)
    #
    #     pos = nx.spring_layout(G)
    #     plt.figure(figsize=(8, 6))
    #
    #     # Draw nodes and edges
    #     nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue', alpha=0.8)
    #     nx.draw_networkx_edges(G, pos, edgelist=self.routes, edge_color='gray', arrows=True, arrowstyle='->', arrowsize=20)
    #     nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')
    #
    #     plt.title('Airports and Flight Routes')
    #     plt.axis('off')
    #     plt.show()
