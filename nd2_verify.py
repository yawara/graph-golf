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

    predicted_aspl = 2 * (q**2 + q - 1) / (q**2 + q)
    aspl = nx.average_shortest_path_length(G)

    assert predicted_aspl == aspl
    print("predicted_aspl:", predicted_aspl)
    print("aspl:", aspl)
