from sage.all import *

from itertools import product
from collections import defaultdict
import pickle

import networkx as nx

from common_sage import gbc


def nd2(p, k):
    assert is_prime(p)
    assert k >= 1

    q = p**k
    G = gbc(GF(q))

    second_layer = []
    for node in G.nodes():
        if G.degree()[node] == q:
            second_layer.append(node)
    tmp = set(G.neighbors(second_layer[0]))
    for s in second_layer[1:]:
        tmp = tmp.intersection(G.neighbors(s))
    first_node = tmp.pop()
    assert tmp == set()
    third_layer = []
    for node in G.nodes():
        if G.degree()[node] == q + 1 and node != first_node:
            third_layer.append(node)
    kind_table = {}
    for node in G.nodes():
        if node == first_node:
            kind_table[node] = 'first'
        elif node in second_layer:
            kind_table[node] = 'second'
        elif node in third_layer:
            kind_table[node] = 'third'
        else:
            raise Exception

    removed_third = []
    for n in G.neighbors(second_layer[0]):
        if n in third_layer:
            removed_third.append(n)
    G.remove_nodes_from(removed_third)
    G.remove_node(second_layer[0])
    G.remove_node(second_layer[1])

    for node in G.nodes():
        if G.degree()[node] == q - 1:
            for node2 in G.nodes():
                if G.degree()[node2] == q - 1:
                    if nx.shortest_path_length(G)[node][node2] == 3:
                        G.add_edge(node, node2)
                        break

    return G


def nd2_minus(p, k):
    pass

if __name__ == '__main__':
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('k', type=int)
    args = parser.parse_args()

    G = nd2(args.p, args.k)
    print(len(G), set(G.degree().values()), nx.diameter(G), nx.average_shortest_path_length(G))

    G = nx.relabel.convert_node_labels_to_integers(G)
    if not os.path.exists('results'):
        os.mkdir('results')
    filename = os.path.join('results', 'n' + str(len(G)) + 'd' +
                            str(max(G.degree().values())) + '_edgelist.txt')
    nx.write_edgelist(G, filename)

    G = nx.read_edgelist(filename)
    print(len(G), set(G.degree().values()), nx.diameter(G), nx.average_shortest_path_length(G))
