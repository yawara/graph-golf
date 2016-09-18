import random

import networkx as nx

# BEST ASPL: 1.92659


def odp13():
    '''
    DEFINITION: odp13()
                            (2,0,k) for k in range(2)
                                        |
                                      (1,0)
                                        |
    (2,1,k) for k in range(2) - (1,1) - 0 - (1,3) - (2,3,k) for k in range(2)
                                        |
                                      (1,2)
                                        |
                            (2,2,k) for k in range(2)
    '''

    G = nx.Graph()
    for j in range(4):
        G.add_edge(0, (1, j))
        for k in range(2):
            G.add_edge((1, j), (2, j, k))
    for j in range(3):
        for k in range(2):
            G.add_edge((2, 3, k), (2, j, k))
            G.add_edge((2, j, k), (2, (j + 1) % 3, (k + 1) % 2))
    return G


def odp14():
    '''
    DEFINITION: odp14()
                            (2,0,k) for k in range(2)
                                        |
                                      (1,0)
                                        |
    (2,1,k) for k in range(2) - (1,1) - 0 or 1 - (1,3) - (2,3,k) for k in range(2)
                                        |
                                      (1,2)
                                        |
                            (2,2,k) for k in range(2)
    '''
    G = odp13()
    G.add_node(1)
    for i in range(4):
        G.add_edge(1, (1, i))

    return G


def hsg():
    G = nx.read_edgelist("HoffmanSingletonGraph_edgelist.txt")
    return G

G = nx.disjoint_union(hsg(), odp14())

G.add_edge(0, 50)
print(len(G), set(G.degree().values()), nx.average_shortest_path_length(G), nx.diameter(G))

for i in range(1, 50):
    spl = nx.shortest_path_length(G)
    max_spl = 0
    for j in range(50, 64):
        if spl[i][j] > max_spl and G.degree()[j] < 8:
            max_spl, max_node = spl[i][j], j
    if max_spl == 0:
        continue
    print(i, max_node)
    G.add_edge(i, max_node)

for k in range(3):
    for i in range(50, 64):
        spl = nx.shortest_path_length(G)
        degs = G.degree()
        max_spl = 0
        for j in range(50, 64):
            if i < j and degs[i] < 8 and degs[j] < 8 and spl[i][j] > max_spl:
                max_spl, max_node = spl[i][j], j
        if max_spl == 0:
            continue
        G.add_edge(i, max_node)
    print(len(G), set(G.degree().values()), nx.average_shortest_path_length(G), nx.diameter(G))
