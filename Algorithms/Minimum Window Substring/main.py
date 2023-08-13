def min_window(s, t):
    if not s or not t:
        return ''

    target_count = defaultdict(int)
    for char in t:
        target_count[char] += 1

    required_chars = len(target_count)
    formed_chars = 0
    window_count = defaultdict(int)
    left, right = 0, 0
    min_length = float('inf')
    min_window = ''

    while right < len(s):
        char = s[right]
        window_count[char] += 1
        if char in target_count and window_count[char] == target_count[char]:
            formed_chars += 1

        while left <= right and formed_chars == required_chars:
            char = s[left]

            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right + 1]

            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed_chars -= 1

            left += 1

        right += 1

    return min_window
