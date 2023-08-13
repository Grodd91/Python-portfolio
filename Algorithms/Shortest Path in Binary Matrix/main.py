def shortest_path_binary_matrix(grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(0, 0, 1)])
    visited = set([(0, 0)])

    while queue:
        row, col, steps = queue.popleft()

        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return steps

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, steps + 1))
                visited.add((new_row, new_col))

    return -1
