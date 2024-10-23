from collections import defaultdict


class FlightRoutes:

    # parameterised constructor for the Flight routes
    def __init__(self, airports, routes, start_airport):
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

    

