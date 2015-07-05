import igraph

def opt(G):
  H = G.copy()
  diam, aspl = H.diameter(), H.average_path_length()
  
  while True:
    print(diam, aspl)
    
    tmp = H.copy()
    tmp.rewire(n=1)
    tmp_diam, tmp_aspl = tmp.diameter(), tmp.average_path_length()
    
    if tmp_diam < diam or ( tmp_diam == diam and tmp_aspl < aspl ):
      H, diam, aspl = tmp, tmp_diam, tmp_aspl