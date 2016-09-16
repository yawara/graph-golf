#!/usr/bin/env python3

import networkx as nx
from opt import diam_aspl


def opt(G, n):
    H = G.copy()
    diam, aspl = diam_aspl(H)
    print(diam, aspl)
    print("")
    while True:
        tmp = H.copy()
        cnt_swapped = nx.connected_double_edge_swap(tmp, nswap=n)
        tmp_diam, tmp_aspl = diam_aspl(tmp)
        print(tmp_diam, tmp_aspl)
        if tmp_diam < diam or (tmp_diam == diam and tmp_aspl < aspl):
            H, diam, aspl = tmp, tmp_diam, tmp_aspl
            print("GOOD")
            print(cnt_swapped)
            print(diam, aspl)

if __name__ == "__main__":
    G = nx.random_regular_graph(3, 64)
    opt(G, 2)
