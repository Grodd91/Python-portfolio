def find_min_height_trees(n, edges):
    if n == 1:
        return [0]

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    leaves = [node for node in graph if len(graph[node]) == 1]
    remaining_nodes = n

    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves

    return leaves
