from common import show
import networkx as nx


def hoffman_singleton_graph():
    '''Return the Hoffman-Singleton Graph.'''
    G = nx.Graph()
    for i in range(5):
        for j in range(5):
            G.add_edge(('pentagon', i, j), ('pentagon', i, (j - 1) % 5))
            G.add_edge(('pentagon', i, j), ('pentagon', i, (j + 1) % 5))
            G.add_edge(('pentagram', i, j), ('pentagram', i, (j - 2) % 5))
            G.add_edge(('pentagram', i, j), ('pentagram', i, (j + 2) % 5))
            for k in range(5):
                G.add_edge(('pentagon', i, j),
                           ('pentagram', k, (i * k + j) % 5))
    G = nx.convert_node_labels_to_integers(G)
    G.name = 'Hoffman-Singleton Graph'
    return G

if __name__ == '__main__':
    G = hoffman_singleton_graph()
    show(G)
