from collections import defaultdict
import random

import igraph as ig
import networkx as nx


def nx_to_ig(G):
    G = nx.convert_node_labels_to_integers(G)
    ig_G = ig.Graph()

    ig_G.add_vertices(G)
    ig_G.add_edges(G.edges())

    return ig_G


def show(G):
    ig_G = nx_to_ig(G)
    N, ds, D, aspl = len(G), set(
        G.degree().values()), ig_G.diameter(), ig_G.average_path_length()
    print(N, ds, D, aspl)


def random_regularize(G, d=None, seed=None):

    G = nx.convert_node_labels_to_integers(G)
    if not d:
        d = max(G.degree().values())

    if seed is not None:
        random.seed(seed)

    def _suitable(edges, potential_edges):
        # Helper subroutine to check if there are suitable edges remaining
        # If False, the generation of the graph has failed
        if not potential_edges:
            return True
        for s1 in potential_edges:
            for s2 in potential_edges:
                # Two iterators on the same dictionary are guaranteed
                # to visit it in the same order if there are no
                # intervening modifications.
                if s1 == s2:
                    # Only need to consider s1-s2 pair one time
                    break
                if s1 > s2:
                    s1, s2 = s2, s1
                if (s1, s2) not in edges:
                    return True
        return False

    def _try_creation():
        # Attempt to create an edge set
        edges = set(G.edges())
        degs = G.degree()
        stubs = [node for node in G.nodes() for _ in range(d - degs[node])]

        while stubs:
            potential_edges = defaultdict(lambda: 0)
            random.shuffle(stubs)
            stubiter = iter(stubs)
            for s1, s2 in zip(stubiter, stubiter):
                if s1 > s2:
                    s1, s2 = s2, s1
                if s1 != s2 and ((s1, s2) not in edges):
                    edges.add((s1, s2))
                else:
                    potential_edges[s1] += 1
                    potential_edges[s2] += 1

            if not _suitable(edges, potential_edges):
                return None  # failed to find suitable edge set

            stubs = [node for node, potential in potential_edges.items()
                     for _ in range(potential)]
        return edges

    # Even though a suitable edge set exists,
    # the generation of such a set is not guaranteed.
    # Try repeatedly to find one.
    edges = _try_creation()
    while edges is None:
        edges = _try_creation()

    H = nx.Graph()
    H.add_edges_from(edges)

    return H
