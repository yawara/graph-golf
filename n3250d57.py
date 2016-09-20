import random

import networkx as nx

from common import nx_to_ig, show, random_regularize
from nd2_construct_non2 import nd2


P = nx.petersen_graph()
P.remove_node(P.nodes()[-1])
G = nx.tensor_product(P, nd2(19, 1))
show(G)

G.add_node(0)
G = random_regularize(G)
show(G)
