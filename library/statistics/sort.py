def sort(data):
    pivots = []
    less = []
    more = []
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        for i in data:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivots.append(i)
        less = sort(less)
        more = sort(more)
        result = less + pivots + more
        return result

def sort_dimension(data, dimension):
    pivots = []
    less = []
    more = []
    if len(data) <= 1:
        return data
    else:
        pivot = data[0][dimension - 1]
        for i in data:
            if i[dimension - 1] < pivot:
                less.append(i)
            elif i[dimension - 1] > pivot:
                more.append(i)
            else:
                pivots.append(i)
        less = sort_dimension(less, dimension)
        more = sort_dimension(more, dimension)
        result = less + pivots + more
        return result