#!/usr/bin/env sage

from sage.all import *

from itertools import product
from collections import defaultdict
import pickle

import networkx as nx

from common import nx_to_ig, show
from common_sage import gbc


def nd2(p, k):
    assert is_prime(p) and p > 2
    assert k >= 1

    q = p**k
    G = gbc(GF(q))

    # REMARK: missing frist layer
    second_layer = []
    for node in G.nodes():
        if G.degree()[node] == q:
            second_layer.append(node)
    third_layer = []
    for node in G.nodes():
        if G.degree()[node] == q + 1:
            third_layer.append(node)
    kind_table = {}
    for node in G.nodes():
        if node in second_layer:
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

    return G


def nd2_minus(p, k):
    pass

if __name__ == '__main__':
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('k', type=int)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    G = nd2(args.p, args.k)
    q = args.p ** args.k

    G = nx.relabel.convert_node_labels_to_integers(G)

    '''
    if not os.path.exists('results'):
        os.mkdir('results')
    '''

    ig_G = nx_to_ig(G)
    N1, ds1, D1, aspl1 = len(G), set(
        G.degree().values()), ig_G.diameter(), ig_G.average_path_length()
    print N1, ds1, D1, aspl1

    '''
    filename = os.path.join('results', 'n' + str(len(G)) + 'd' +
                            str(max(G.degree().values())) + 'or' + str(min(G.degree().values())) + '_edgelist.txt')
    nx.write_edgelist(G, filename)

    if args.verbose:
        G = nx.relabel.convert_node_labels_to_integers(nx.read_edgelist(filename))
        ig_G = nx_to_ig(G)
        N2, ds2, D2, aspl2 = len(G), set(
            G.degree().values()), ig_G.diameter(), ig_G.average_path_length()
        assert (N1, ds1, D1, aspl1) == (N2, ds2, D2, aspl2)
        print N2, ds2, D2, aspl2
    '''

    for node in G.nodes():
        if G.degree()[node] == q - 1:
            for node2 in G.nodes():
                if G.degree()[node2] == q - 1:
                    if nx_to_ig(G).shortest_paths()[node][node2] == 3:
                        G.add_edge(node, node2)
                        break

    show(G)

    '''
    filename = os.path.join('results', 'n' + str(len(G)) + 'd' +
                            str(max(G.degree().values())) + '_edgelist.txt')
    nx.write_edgelist(G, filename)

    if args.verbose:
        G = nx.read_edgelist(filename)
        ig_G = nx_to_ig(G)
        N2, ds2, D2, aspl2 = len(G), set(
            G.degree().values()), ig_G.diameter(), ig_G.average_path_length()
        assert (N1, ds1, D1, aspl1) == (N2, ds2, D2, aspl2)
        print N2, ds2, D2, aspl2
    '''
