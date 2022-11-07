# Import the library
from dsagraph import dsagraph

print()

#Graph
graph = dsagraph.Graph()

graph.add_edge(0, 1, 25)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 3)
graph.add_edge(3, 4, 1)
graph.add_edge(4, 5, 15)

print()
graph.print_edge_list()


# Plotting the graph
pltgraph = dsagraph.GraphPlot()
pltgraph.plotGraph()