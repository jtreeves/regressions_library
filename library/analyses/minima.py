def minima(intervals):
    result = []
    for i in range(len(intervals)):
        if intervals[i] == 'decreasing' and intervals[i + 2] == 'increasing':
            result.append(intervals[i + 1])
    return result