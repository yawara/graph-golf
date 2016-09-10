import networkx as nx


def base():
    G = nx.Graph()

    for i in range(2):
        for j1 in range(4):
            G.add_edge((i, j1, "down", 0), (i, j1, "down", 1))
            G.add_edge((i, j1, "down", 1), (i, j1, "down", 2))
            G.add_edge((i, j1, "down", 2), (i, j1, "down", 0))
            for k in range(3):
                G.add_edge((i, j1, "up", 0), (i, j1, "mid", k))
                G.add_edge((i, j1, "up", 1), (i, j1, "mid", k))
                G.add_edge((i, j1, "mid", k), (i, j1, "down", k))
            for j2 in range(4):
                if j1 < j2:
                    G.add_edge((i, j1, "up", 0), (i, j2, "up", 1))
                    G.add_edge((i, j1, "up", 1), (i, j2, "up", 0))
                    for k in range(3):
                        G.add_edge((i, j1, "mid", k), (i, j2, "down", (k + 1) % 3))
                        G.add_edge((i, j1, "down", k), (i, j2, "mid", (k + 2) % 3))

    return G


def n64_d8():
    G = base()

    for j1 in range(2):
        for j2 in range(2):
            G.add_edge((0, j1, "up", 0), (1, j2, "up", 1))
            G.add_edge((0, j1, "up", 1), (1, j2, "up", 0))
            for k in range(3):
                G.add_edge((0, j1, "mid", k), (1, j2, "down", (k + 1) % 3))
                G.add_edge((0, j1, "down", k), (1, j2, "mid", (k + 2) % 3))

    for j1 in range(2, 4):
        for j2 in range(2, 4):
            G.add_edge((0, j1, "up", 0), (1, j2, "up", 1))
            G.add_edge((0, j1, "up", 1), (1, j2, "up", 0))
            for k in range(3):
                G.add_edge((0, j1, "mid", k), (1, j2, "down", (k + 1) % 3))
                G.add_edge((0, j1, "down", k), (1, j2, "mid", (k + 2) % 3))

    return G


def n64_d8_simple():
    G = base()

    for j in range(4):
        G.add_edge((0, j, "up", 0), (1, j, "up", 1))
        G.add_edge((0, j, "up", 0), (1, (j + 1) % 4, "up", 1))
        G.add_edge((0, j, "up", 1), (1, j, "up", 0))
        G.add_edge((0, j, "up", 1), (1, (j + 1) % 4, "up", 0))
        for k in range(3):
            G.add_edge((0, j, "mid", k), (1, j, "down", (k + 1) % 3))
            G.add_edge((0, j, "mid", k), (1, (j + 1) % 4, "down", (k + 1) % 3))
            G.add_edge((0, j, "down", k), (1, j, "mid", (k + 2) % 3))
            G.add_edge((0, j, "down", k), (1, (j + 1) % 4, "mid", (k + 2) % 3))

    return G


def get_score(G):
    print(len(G), set(G.degree().values()), nx.diameter(G), nx.average_shortest_path_length(G))
