import networkx as nx
import random
import matplotlib.pyplot as plt


def add_edges():
    nodes = list(G.nodes())
    for s in nodes:
        for t in nodes:
            if s != t:
                r = random.random()
                if r <= 0.5:
                    G.add_edge(s, t)

    return G


G = nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=add_edges()

nx.draw(G,with_labels=True)
plt.show()


def assign_points(G):
    nodes = list(G.node s())
    p = []
    for each in nodes:
        p.append(100)
    return p



points = assign_points(G)