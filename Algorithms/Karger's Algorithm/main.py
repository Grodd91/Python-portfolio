import random

def karger_min_cut(graph):
    while len(graph) > 2:
        u, v = random.choice(list(graph.items()))
        w = random.choice(v)
        contract(graph, u, w)
        del graph[w]

    min_cut = min(len(edges) for edges in graph.values())
    return min_cut

def contract(graph, u, v):
    for node in graph[v]:
        graph[u].append(node)
        graph[node].remove(v)
        graph[node].append(u)
    graph[u] += graph[v]
    del graph[v]
    graph[u] = [x for x in graph[u] if x != u]
