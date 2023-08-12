def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        index = int(n * num)
        buckets[index].append(num)
    for i in range(n):
        buckets[i].sort()
    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr
