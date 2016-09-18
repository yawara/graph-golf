import networkx as nx
from common import nx_to_ig

G = nx.read_edgelist("results/n16384d128or127_edgelist.txt")

q = 2**7

ig_G = nx_to_ig(G)
print(ig_G.average_path_length())
predicted_aspl_before_adding_edges = 2 * (q**2 + q - 1) / (q**2 + q)
print(predicted_aspl_before_adding_edges)

'''
for node1 in G.nodes():
    for node2 in G.nodes():
        if G.degree()[node1] == 127 and G.degree()[node2] == 127:
            G.add_edge(node1, node2)
'''

nodes = []
degs = G.degree()
for node in G.nodes():
    if degs[node] == 127:
        nodes.append(node)
assert len(nodes) % 2 == 0
for i in range(len(nodes) // 2):
    G.add_edge(nodes[2 * i], nodes[2 * i + 1])

print(set(G.degree().values()))

ig_G = nx_to_ig(G)
print(ig_G.average_path_length())
predicted_aspl_after_adding_edges = 2 * (q**3 + q**2 - q - 2) / (q**3 + q**2)
print(predicted_aspl_after_adding_edges)

nx.write_edgelist(G, "n16384d128_edgelist.txt")
