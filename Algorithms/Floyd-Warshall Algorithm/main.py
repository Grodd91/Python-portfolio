def floyd_warshall(graph):
    distances = {vertex: {vertex: float('infinity') for vertex in graph} for vertex in graph}
    for vertex in graph:
        distances[vertex][vertex] = 0
    for edge in graph['edges']:
        start, end, weight = edge
        distances[start][end] = weight

    for intermediate in graph:
        for start in graph:
            for end in graph:
                distances[start][end] = min(distances[start][end],
                                            distances[start][intermediate] + distances[intermediate][end])

    return distances
