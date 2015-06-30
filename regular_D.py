#!/usr/bin/env python3 
import networkx as nx

def regular_D(n,d,D):
  while True:
    G=nx.random_regular_graph(d,n)
    if nx.is_connected(G):
      diameter = nx.diameter(G)
      if diameter == D:
        return G

if __name__ == "__main__":
  import sys
  
  n=int(sys.argv[1])

  try:
    d=int(sys.argv[2])
  except IndexError:
    pd=int(n**(3/4))
    if pd % 2 == 0:
      d = pd + 2
    else:
      d = pd + 1

  print(regular2(n,d))