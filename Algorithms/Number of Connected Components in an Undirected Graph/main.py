def count_components(n, edges):
    def find(node):
        if parent[node] == -1:
            return node
        parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1

    parent = [-1] * n

    for edge in edges:
        union(edge[0], edge[1])

    components = set()
    for i in range(n):
        components.add(find(i))

    return len(components)
