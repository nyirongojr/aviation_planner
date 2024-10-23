from graph import Graph
from collections import defaultdict, deque


class FlightRoutes:

    # parameterised constructor for the Flight routes
    def __init__(self, airports, routes, start_airport):
        self.graph = Graph(airports, routes)
        self.start_airport = start_airport
        self.airports = airports
        self.routes = routes

    # Perform the Depth First transversing in the graph
    def do_depth_first(self, graph, node, visited, stack):
        # each visited note is added to the visited list to keep track
        visited.add(node)
        for nodeItem in graph[node]:
            if nodeItem not in visited:
                # This is sort of a recursive call
                self.do_depth_first(graph, nodeItem, visited, stack)
        stack.append(node)

    # Perform the Depth First transversing in the reversed graph
    def do_reverse_depth_first(self, graph, node, visited, component):
        # each visited note is added to the visited list to keep track
        visited.add(node)
        # Mark the strongly connected component
        component.append(node)
        for graphNodeItem in graph[node]:
            if graphNodeItem not in visited:
                # recursive call of the do_reverse_depth_first
                self.do_reverse_depth_first(graph, graphNodeItem, visited, component)

    # Kosaraju's Algorithm application in finding the Strongly connected components
    def get_connected_components(self):
        stack = []
        visited = set()

        # Step 1: Order nodes by finish time (when the node is visited) in the original graph
        for airport in self.airports:
            if airport not in visited:
                self.do_depth_first(self.graph.graph, airport, visited, stack)

        # Step 2: Reverse the graph
        reversed_graph = defaultdict(list)
        for airport in self.graph.graph:
            for airportItem in self.graph.graph[airport]:
                reversed_graph[airportItem].append(airport)

        # Step 3: Process nodes in the order of decreasing finish time
        visited.clear()
        # Strongly connected components array
        strongly_connected_components = []

        while stack:
            airport = stack.pop()
            if airport not in visited:
                component = []
                self.do_reverse_depth_first(reversed_graph, airport, visited, component)
                strongly_connected_components.append(component)

        return strongly_connected_components

    # Build a directed graph from the Strongly Connected component
    def build_scc_directed_graph(self, strongly_connected_components):
        component_map = {}
        scc_directed_graph = defaultdict(set)

        # Map each airport to its SCC index
        for idx, scc in enumerate(strongly_connected_components):
            for airport in scc:
                component_map[airport] = idx

        # Build the DAG where nodes are SCCs and edges are between SCCs
        for u in self.graph.graph:
            for v in self.graph.graph[u]:
                if component_map[u] != component_map[v]:
                    scc_directed_graph[component_map[u]].add(component_map[v])

        return component_map, scc_directed_graph

    # Function to find the minimum number of routes to make all airports reachable
    def find_min_routes_to_reach_all(self):
        # Step 1: Find all strongly connected components
        strongly_connected_comp = self.get_connected_components()

        # Step 2: Build the directed graph
        connected_component_map, connected_directed_graph = self.build_scc_directed_graph(strongly_connected_comp)

        # Step 3: Find the strong connected component that has the start airport in it
        start_strong_connected_component = connected_component_map[self.start_airport]

        # Step 4: Perform a depth First Search from the start component that is in the directed graph just built
        visited_strong_components = set()
        queue = deque([start_strong_connected_component])

        while queue:
            current_scc = queue.popleft()
            visited_strong_components.add(current_scc)
            for directed_graph_item in connected_directed_graph[current_scc]:
                if directed_graph_item not in visited_strong_components:
                    queue.append(directed_graph_item)

        # Step 5: Count strong connected components that are not reachable from the start connected component
        unreachable_strong_connected_component = len(strongly_connected_comp) - len(visited_strong_components)

        # Step 6: The minimum number of additional routes is the number of unreachable Strong connected components
        return unreachable_strong_connected_component
