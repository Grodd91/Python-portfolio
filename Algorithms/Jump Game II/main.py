def jump(nums):
    if len(nums) <= 1:
        return 0

    steps = jumps = 0
    max_reach = curr_reach = 0

    for i in range(len(nums) - 1):
        max_reach = max(max_reach, i + nums[i])
        if i == curr_reach:
            jumps += 1
            curr_reach = max_reach

    return jumps
