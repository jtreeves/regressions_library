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

single_dimension_set = [5, 2, 9, 1, 3, 5, 3, 8, 7, 6]
double_dimension_set = [[2, 7], [1, 9], [5, 2], [3, 4], [4, 3], [8, 1], [2, 3], [7, 7], [1, 1], [5, 3]]

sort_single = sort(single_dimension_set)
sort_double = sort_dimension(double_dimension_set, 1)

print(f'SINGLE SORT: {sort_single}')
print(f'DOUBLE SORT: {sort_double}')