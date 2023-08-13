def count_elements(arr):
    num_count = collections.Counter(arr)
    result = 0

    for num in num_count:
        if num + 1 in num_count:
            result += num_count[num]

    return result
