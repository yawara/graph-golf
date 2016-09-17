import igraph as ig
import networkx as nx


def nx_to_ig(G):
    G = nx.convert_node_labels_to_integers(G)
    ig_G = ig.Graph()

    ig_G.add_vertices(G)
    ig_G.add_edges(G.edges())

    return ig_G
