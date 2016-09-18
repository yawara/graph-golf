#!/usr/bin/env python3

import networkx as nx
import argparse

from common import nx_to_ig


def predicted_aspl_before_adding_edges(q):
    return 2 * (q**2 + q - 1) / (q**2 + q)


def predicted_aspl_after_adding_edges(q):
    return 2 * (q**3 + q**2 - q - 2) / (q**3 + q**2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('k', type=int)
    args = parser.parse_args()

    q = args.p ** args.k

    G = nx.read_edgelist('results/n' + str(q**2) + 'd' + str(q) +
                         'or' + str(q - 1) + '_edgelist.txt')
    H = nx.read_edgelist('results/n' + str(q**2) + 'd' + str(q) +
                         '_edgelist.txt')

    predicted_aspl_before = predicted_aspl_before_adding_edges(q)
    predicted_aspl_after = predicted_aspl_after_adding_edges(q)
    aspl_before_adding_edges = nx_to_ig(G).average_path_length()
    aspl_after_adding_edges = nx_to_ig(H).average_path_length()

    assert predicted_aspl_before == aspl_before_adding_edges
    assert predicted_aspl_after == aspl_after_adding_edges
    print("predicted_aspl_before_adding_edges:", predicted_aspl_before)
    print("predicted_aspl_after_adding_edges:", predicted_aspl_after)
    print("aspl_before_adding_edges:", aspl_before_adding_edges)
    print("aspl_after_adding_edges:", aspl_after_adding_edges)
