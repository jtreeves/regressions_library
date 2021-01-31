def maxima(intervals):
    result = []
    for i in range(len(intervals)):
        try:
            if intervals[i] == 'increasing' and intervals[i + 2] == 'decreasing':
                result.append(intervals[i + 1])
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    return result