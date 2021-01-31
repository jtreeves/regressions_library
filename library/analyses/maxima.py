def maxima(intervals):
    result = []
    for i in range(len(intervals)):
        if intervals[i] == 'increasing' and intervals[i + 2] == 'decreasing':
            result.append(intervals[i + 1])
    return result