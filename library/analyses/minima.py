from library.errors.analyses import multitype_vector

def minima_points(intervals):
    multitype_vector(intervals)
    result = []
    for i in range(len(intervals)):
        try:
            if intervals[i] == 'negative' and intervals[i + 2] == 'positive':
                result.append(intervals[i + 1])
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    return result