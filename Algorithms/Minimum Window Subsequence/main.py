def min_window(s, t):
    def find_subsequence(s, t):
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return j == len(t)

    left, right = 0, len(s)
    result = ""

    while left <= right:
        mid = (left + right) // 2
        found = False

        for i in range(len(s) - mid + 1):
            if find_subsequence(s[i:i + mid], t):
                found = True
                break

        if found:
            result = s[i:i + mid]
            right = mid - 1
        else:
            left = mid + 1

    return result
