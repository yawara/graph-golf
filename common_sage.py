from sage.all import *

from itertools import product
from collections import defaultdict

import networkx as nx


def gbc(R):
    lines = []
    check_table = defaultdict(bool)

    for p, q, r in product(R, repeat=3):
        if p == 0 and q == 0 and r == 0:
            pass
        else:
            flag = True
            if not check_table[(p, q, r)]:
                for k in R:
                    if k == 0:
                        pass
                    else:
                        kp, kq, kr = k * p, k * q, k * r
                        if kp == 0 and kq == 0 and kr == 0:
                            flag = False
                        else:
                            check_table[(kp, kq, kr)] = True
                if flag:
                    lines.append((p, q, r))

    G = nx.Graph()
    G.add_nodes_from(lines)

    for i, l1 in enumerate(lines):
        for j, l2 in enumerate(lines):
            if i < j:
                if l1[0] * l2[0] + l1[1] * l2[1] + l1[2] * l2[2] == 0:
                    G.add_edge(l1, l2)

    return G


def check_gbc(R):
    G = gbc(R)
    degs = G.degree()
    d = max(degs.values())

    second_layer = []
    for node in G.nodes():
        if degs[node] == d - 1:
            second_layer.append(node)
    tmp = set(G.neighbors(second_layer[0]))
    for s in second_layer[1:]:
        tmp = tmp.intersection(G.neighbors(s))

    if len(tmp) == 1:
        first_node = tmp.pop()
    elif len(tmp) == 0:
        first_node = None
    else:
        raise Exception

    third_layer = []
    for node in G.nodes():
        if degs[node] == d and node != first_node:
            third_layer.append(node)

    s = second_layer[0]
    print set(degs[n]for n in G.neighbors(s))

    for n in G.neighbors(s):
        deg_seq = defaultdict(int)
        for deg in [degs[m]for m in G.neighbors(n)]:
            deg_seq[deg] += 1
        print deg_seq


def psuedo_centers(R):
    G = gbc(R)
    degs = G.degree()
    d = max(degs.values())

    rtv = []

    for node in G.nodes():
        if degs[node] == d and set(degs[n] for n in G.neighbors(node)) == set([d]):
            rtv.append(node)

    return rtv

if __name__ == '__main__':
    G = gbc(GF(7))
    G = nx.relabel.convert_node_labels_to_integers(G)
    print len(G), set(G.degree().values()), nx.diameter(G), nx.average_shortest_path_length(G)
    nx.write_edgelist(G, os.path.join('results', 'n57d8or7_edgelist.txt'))
