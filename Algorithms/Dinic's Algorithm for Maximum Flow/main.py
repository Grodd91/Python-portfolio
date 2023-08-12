class Dinic:
    def __init__(self, graph):
        self.graph = graph
        self.levels = [0] * len(graph)
        self.visited = [0] * len(graph)

    def add_edge(self, u, v, capacity):
        self.graph[u].append({'v': v, 'capacity': capacity, 'flow': 0})
        self.graph[v].append({'v': u, 'capacity': 0, 'flow': 0})

    def bfs(self, s, t):
        self.levels = [-1] * len(self.graph)
        self.levels[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for edge in self.graph[u]:
                v, capacity, flow = edge['v'], edge['capacity'], edge['flow']
                if self.levels[v] < 0 and flow < capacity:
                    self.levels[v] = self.levels[u] + 1
                    queue.append(v)

    def dfs(self, u, t, flow):
        if u == t:
            return flow
        self.visited[u] = 1
        for edge in self.graph[u]:
            v, capacity, edge_flow = edge['v'], edge['capacity'], edge['flow']
            if not self.visited[v] and self.levels[v] == self.levels[u] + 1 and edge_flow < capacity:
                new_flow = min(flow, capacity - edge_flow)
                augmented_flow = self.dfs(v, t, new_flow)
                if augmented_flow > 0:
                    edge['flow'] += augmented_flow
                    for reverse_edge in self.graph[v]:
                        if reverse_edge['v'] == u:
                            reverse_edge['flow'] -= augmented_flow
                            break
                    return augmented_flow
        return 0

    def max_flow(self, s, t):
        max_flow = 0
        while True:
            self.bfs(s, t)
            if self.levels[t] < 0:
                break
            self.visited = [0] * len(self.graph)
            while True:
                flow = self.dfs(s, t, float('inf'))
                if flow <= 0:
                    break
                max_flow += flow
        return max_flow
