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
                self.do_depth_first(graph, nodeItem, visited, stack)
        stack.append(node)

    # Perform the Depth First transversing in the reversed graph
