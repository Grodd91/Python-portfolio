import heapq

def k_closest(points, k):
    def distance(point):
        return point[0] ** 2 + point[1] ** 2

    max_heap = []

    for point in points:
        heapq.heappush(max_heap, (-distance(point), point))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [point for _, point in max_heap]
