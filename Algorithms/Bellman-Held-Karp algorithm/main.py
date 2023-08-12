def min_partition(arr):
    total_sum = sum(arr)
    n = len(arr)
    dp = [[False for _ in range(total_sum // 2 + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, total_sum // 2 + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]

    j = total_sum // 2
    while not dp[n][j]:
        j -= 1

    return total_sum - 2 * j
