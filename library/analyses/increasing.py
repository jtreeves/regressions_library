def increasing(intervals):
    result = []
    for i in range(len(intervals)):
        if intervals[i] == 'increasing':
            result.append(True)
        elif intervals[i] == 'decreasing':
            result.append(False)
        else:
            result.append(intervals[i])
    return result