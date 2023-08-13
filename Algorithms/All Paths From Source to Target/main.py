def all_paths_source_target(graph):
    def backtrack(node, path):
        if node == len(graph) - 1:
            result.append(path)
            return
        for neighbor in graph[node]:
            backtrack(neighbor, path + [neighbor])

    result = []
    backtrack(0, [0])
    return result
