def find_itinerary(tickets):
    graph = defaultdict(list)

    for start, end in tickets:
        graph[start].append(end)

    for start in graph:
        graph[start].sort(reverse=True)

    result = []

    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        result.append(node)

    dfs("JFK")
    return result[::-1]
