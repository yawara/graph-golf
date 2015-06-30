from random import shuffle
import networkx as nx
import numpy as np
from numpy.linalg import matrix_power

from create_random import *

def flip(G,e1,e2):
  H = G.copy()
  
  a, b = e1[0], e1[1]
  c, d = e2[0], e2[1]

  H.remove_edge(a,b)
  H.remove_edge(c,d)
  
  H.add_edge(a,d)
  H.add_edge(c,b)
    
  return H
    
def diam_aspl(G):
  hops = nx.shortest_path_length(G)
  diam, aspl = max_avg_for_matrix(hops)
  
  return diam, aspl 

def cnt_triangles(G):
  M = nx.to_numpy_matrix(G)
  return np.trace(matrix_power(M,3)/6)

def cnt_rectangles(G):
  d = max(G.degree().values())
  n = len(G)
  M = nx.to_numpy_matrix(G)
  return np.trace(((matrix_power(M,2) - d * np.identity(n)).dot(M) - (d-1) * M ).dot(M))
  
  
def opt(G):
  H = G.copy()
  
  diam, aspl = diam_aspl(H)
  
  print("START")
  
  while True:
    print(diam, aspl)
    print(cnt_triangles(H),cnt_rectangles(H))
    print(sum(H.degree().values()))
    es = H.edges()
    shuffle(es)
    iter_es = iter(es)
    for e1, e2 in zip(iter_es,iter_es):
      tmp = flip(H,e1,e2) 
      if nx.is_connected(tmp):
        tmp_diam, tmp_aspl = diam_aspl(tmp)
        if tmp_diam < diam:
          H = tmp
          diam, aspl = tmp_diam, tmp_aspl
        elif tmp_diam == diam and tmp_aspl < aspl:
          H = tmp
          diam, aspl = tmp_diam, tmp_aspl
        else:
          pass