import heapq

def prim(graph):
    mst = []
    start = next(iter(graph))
    visited = {start}
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost_next in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost_next, to, to_next))

    return mst
