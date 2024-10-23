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

### Notes on Kosaraju’s Algorithm
1. Utilises depth First Algorithm
2. After complete run of the depth first alg, a reverse Depth First Alg is done on the graph. Basically just changes the direction of the directed graph
3. From the above two procedure, find the strongly connected components
4. Build the Directed graph using the strongly connected groups.

**NOTE**: 
Our requirement goes beyond `Kosaraju’s Algorithm` by constructing the missing edge from the starting node to determine the minimum required length.
