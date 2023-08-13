def num_islands2(m, n, positions):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False

    grid = [[0] * n for _ in range(m)]
    parent = [i for i in range(m * n)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []

    for i, (x, y) in enumerate(positions):
        if grid[x][y] == 1:
            result.append(result[i - 1])
            continue

        grid[x][y] = 1
        count = 1

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                if union(x * n + y, new_x * n + new_y):
                    count -= 1

        result.append(result[i - 1] + count)

    return result
