# Import the library
from dsagraph import dsagraph

print()

#Graph
graph = dsagraph.Graph()
n = int(input("Enter the number of nodes you want to enter: "))

for i in range(n):
    src, dtn, *wei = input("Enter the source node, destination node and weight (if you wish): ").split()
    
    wei.append(1) if (len(wei)==0) else int(wei[0])
    
    src = int(src)
    dtn = int(dtn)
    wei = int(wei[0])
     
    graph.add_edge(src, dtn, wei)

print()
graph.print_edge_list()
