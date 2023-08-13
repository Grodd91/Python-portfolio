def can_partition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    dp = [False] * (target_sum + 1)
    dp[0] = True

    for num in nums:
        for i in range(target_sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target_sum]
