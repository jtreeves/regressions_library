def sort(data):
    pivot = data[0]
    pivots = []
    less = []
    more = []
    for i in range(len(data)):
        if data[i] < pivot:
            less.append(data[i])
        elif data[i] > pivot:
            more.append(data[i])
        else:
            pivots.append(data[i])
    less = sort(less)
    more = sort(more)
    result = less + pivots + more
    return result