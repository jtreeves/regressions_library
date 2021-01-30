def minima(intervals):
    result = []
    for i in range(len(intervals)):
        if intervals[i] == True and intervals[i + 2] == False:
            result.append(intervals[i + 1])
    return result