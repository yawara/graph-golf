import graph_tool as gt
from graph_tool.generation import random_graph, random_rewire
from graph_tool import topology
import numpy as np


def diam_aspl(g):
  n = g.num_vertices()
  sd = topology.shortest_distance(g)
  
  sda = np.array([sd[v] for v in g.vertices()])
  
  diam = np.max(sda)
  aspl = np.sum(sda)
  aspl /= n*(n-1)
  
  return diam, aspl

def opt(g,model="uncorrelated"):
  h = gt.Graph(g)
  diam, aspl = diam_aspl(h)
  
  while True:
    print(diam,aspl)
    tmp = gt.Graph(h)
    print(random_rewire(tmp,model=model))
    tmp_diam, tmp_aspl = diam_aspl(tmp)
    if tmp_diam < diam or ( tmp_diam == diam and tmp_aspl < aspl ):
      h, diam, aspl = tmp, tmp_diam, tmp_aspl