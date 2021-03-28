from library.errors.vectors import first_vector
from library.errors.matrices import first_matrix, level

def sorted_list(data):
    first_vector(data)
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
        less = sorted_list(less)
        more = sorted_list(more)
        result = less + pivots + more
        return result

def sorted_dimension(data, dimension):
    first_matrix(data)
    level(data, dimension)
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
        less = sorted_dimension(less, dimension)
        more = sorted_dimension(more, dimension)
        result = less + pivots + more
        return result