class BiconnectedComponents:
    def __init__(self, graph):
        self.graph = graph
        self.time = 0
        self.visited = [False] * len(graph)
        self.disc = [0] * len(graph)
        self.low = [0] * len(graph)
        self.parent = [-1] * len(graph)
        self.components = []

    def dfs(self, u):
        children = 0
        self.visited[u] = True
        self.time += 1
        self.disc[u] = self.low[u] = self.time
        for v in self.graph[u]:
            if not self.visited[v]:
                children += 1
                self.parent[v] = u
                self.dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] >= self.disc[u]:
                    self.components.append((u, v))
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])

    def find_biconnected_components(self):
        for u in range(len(self.graph)):
            if not self.visited[u]:
                self.dfs(u)

        return self.components
