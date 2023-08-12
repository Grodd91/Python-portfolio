def kruskal(graph):
    parent = {}
    rank = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    minimum_spanning_tree = []
    for vertex in graph['vertices']:
        parent[vertex] = vertex
        rank[vertex] = 0

    edges = graph['edges']
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        node1, node2, weight = edge
        if find(node1) != find(node2):
            union(node1, node2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree
