def decreasing(intervals):
    result = []
    for i in range(len(intervals)):
        if intervals[i] == 'decreasing':
            result.append(True)
        elif intervals[i] == 'increasing':
            result.append(False)
        else:
            result.append(intervals[i])
    return result