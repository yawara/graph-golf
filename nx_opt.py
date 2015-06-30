import networkx as nx
from opt import diam_aspl

def opt(G,n):
  H = G.copy()
  diam, aspl = diam_aspl(H)
  while True:
    tmp = H.copy()
    cnt_swapped = nx.connected_double_edge_swap(tmp,nswap=n)
    tmp_diam, tmp_aspl = diam_aspl(tmp)
    if tmp_diam < diam or ( tmp_diam == diam and tmp_aspl < aspl):
      H, diam, aspl = tmp, tmp_diam, tmp_aspl
      print(cnt_swapped)
      print(diam,aspl)