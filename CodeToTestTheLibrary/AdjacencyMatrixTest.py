# Import the library
from dsagraph import dsagraph

# Adjacency Matrix
print()

n = int(input("Enter the number of nodes you want to enter: "))

adj_matrix = dsagraph.Adj_matrix(n)

adj_matrix.add_edge_adj_matrix(0, 1, 25)
adj_matrix.add_edge_adj_matrix(1, 2, 5)
adj_matrix.add_edge_adj_matrix(2, 3, 3)
adj_matrix.add_edge_adj_matrix(3, 4)
adj_matrix.add_edge_adj_matrix(4, 0, 15)

print()
adj_matrix.print_adj_matrix()