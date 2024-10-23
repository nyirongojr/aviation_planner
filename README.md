# aviation_planner
Plans routes for aviation with specified airport routes

## Approach
* Each airport is considered to be a node as represented in the given graph

* The edges indicated the direction that flights take from one airport to another.
* Considering `Kosaraju’s Algorithm` in graph, we can utilize the concept of Strongly connected components and apply the same to the given graph.

## Implementation (Overview/solution)
* identify all Strongly Connected Components (SCC) from the given graph on paper
* construct a directed graph representing all the nodes in the graph
* Find out the strongly connected components that are not reachable from the SCC that contains the start point and as well the minimum edges(lines) that will be needed to connect them

