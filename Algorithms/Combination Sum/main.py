def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            backtrack(i, target - candidates[i], path + [candidates[i]])

    result = []
    candidates.sort()
    backtrack(0, target, [])
    return result
