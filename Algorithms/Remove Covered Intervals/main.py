def remove_covered_intervals(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    count = 0
    end = float('-inf')

    for start, curr_end in intervals:
        if curr_end > end:
            count += 1
            end = curr_end

    return count
