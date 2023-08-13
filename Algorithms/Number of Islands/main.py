def num_islands(grid):
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    if not grid:
        return 0

    num_rows, num_cols = len(grid), len(grid[0])
    islands = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == '1':
                islands += 1
                dfs(row, col)

    return islands
