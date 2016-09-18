#!/usr/bin/env sage

from sage.all import *

from itertools import product
from collections import defaultdict
import pickle

import networkx as nx

from common import nx_to_ig
from common_sage import gbc
from nd2_verify import predicted_aspl_before_adding_edges, predicted_aspl_after_adding_edges


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
    G.remove_node(G.neighbors(second_layer[1])[0])

    return G


if __name__ == '__main__':
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('k', type=int)
    # parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    G = nd2(args.p, args.k)
    q = args.p ** args.k

    G = nx.relabel.convert_node_labels_to_integers(G)

    if not os.path.exists('results'):
        os.mkdir('results')

    ig_G = nx_to_ig(G)
    N, ds, D, aspl = len(G), set(
        G.degree().values()), ig_G.diameter(), ig_G.average_path_length()
    print N, ds, D, aspl

    filename = os.path.join('results', 'n' + str(len(G)) + 'd' +
                            str(max(G.degree().values())) + 'or' + str(min(G.degree().values())) + '_revised_edgelist.txt')
    nx.write_edgelist(G, filename)

    for node in G.nodes():
        if G.degree()[node] == q - 1:
            for node2 in G.nodes():
                if G.degree()[node2] == q - 1:
                    if nx_to_ig(G).shortest_paths()[node][node2] == 3:
                        G.add_edge(node, node2)
                        break

    ig_G = nx_to_ig(G)
    N, ds, D, aspl = len(G), set(
        G.degree().values()), ig_G.diameter(), ig_G.average_path_length()
    print N, ds, D, aspl

    H = nx.read_edgelist(os.path.join('results', 'n' + str(len(G)) + 'd' +
                                      str(max(G.degree().values())) + '_edgelist.txt'))
    original_aspl = nx_to_ig(H).average_path_length()
    predicted_original_aspl = predicted_aspl_after_adding_edges(float(q))
    print "original aspl:", original_aspl
    print "predicted original aspl:", predicted_original_aspl
    assert original_aspl == predicted_original_aspl
    print "revised aspl:", aspl
    assert aspl < predicted_aspl_after_adding_edges(float(q))

    filename = os.path.join('results', 'n' + str(len(G)) + 'd' +
                            str(max(G.degree().values())) + '_revised_edgelist.txt')
    nx.write_edgelist(G, filename)
