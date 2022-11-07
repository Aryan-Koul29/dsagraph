# Import the library
from dsagraph import dsagraph

# Adjacency List
adj_list = dsagraph.Adj_list()

adj_list.add_edge_adj_list(1, 2)
adj_list.add_edge_adj_list(2, 3)
adj_list.add_edge_adj_list(3, 4)
adj_list.add_edge_adj_list(4, 5)
adj_list.add_edge_adj_list(1, 8)
adj_list.add_edge_adj_list(4, 1)
adj_list.add_edge_adj_list(5, 1)
adj_list.add_edge_adj_list(5, 1)
adj_list.add_edge_adj_list(5, 4)
adj_list.add_edge_adj_list(5, 5)
adj_list.add_edge_adj_list(5, 6)
adj_list.add_edge_adj_list(5, 7)

print()
adj_list.print_adj_list()