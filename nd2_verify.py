import networkx as nx
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('k', type=int)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    q = args.p ** args.k

    G = nx.read_edgelist('results/n' + str(q**2) + 'd' + str(q) +
                         'or' + str(q - 1) + '_edgelist.txt')
    H = nx.read_edgelist('results/n' + str(q**2) + 'd' + str(q) +
                          '_edgelist.txt')

    predicted_aspl_before_adding_edges = 2 * (q**2 + q - 1) / (q**2 + q)
    predicted_aspl_after_adding_edges = 2 * (q**3 + q**2 - q - 2) / (q**3 + q**2)
    aspl_before_adding_edges = nx.average_shortest_path_length(G)
    aspl_after_adding_edges = nx.average_shortest_path_length(H)

    #assert predicted_aspl == aspl
    print("predicted_aspl_before_adding_edges:", predicted_aspl_before_adding_edges)
    print("predicted_aspl_after_adding_edges:", predicted_aspl_after_adding_edges)
    print("aspl_before_adding_edges:", aspl_before_adding_edges)
    print("aspl_after_adding_edges:", aspl_after_adding_edges)
