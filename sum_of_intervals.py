def sum_of_intervals(intervals):
    interval_sum = 0
    while intervals:
        # i marks the start of the current interval
        i = j = min(start for start, _ in intervals)
        j = end_of_interval(intervals, j)
        interval_sum += j - i
        # filter out intervals that have been passed
        intervals = [interval for interval in intervals if interval[0] > j]
    return interval_sum


def end_of_interval(intervals, j):
    """
    given a position j, finds the rightmost position of the interval it is in.
    >>> end_of_interval([(4, 6), (1, 3), (2, 5), (8, 10)], 2)
    6
    """
    done = False
    while not done:
        done = True
        for start, end in intervals:
            if start <= j < end:
                j = end
                done = False  # need to check again for intervals we skipped
    return j


print(sum_of_intervals([
    [1, 4],
    [7, 10],
    [3, 5]
]))
