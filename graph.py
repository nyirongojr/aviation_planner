from collections import defaultdict


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
