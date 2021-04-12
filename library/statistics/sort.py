def sorted_list(data):
    """
    Sorts all elements in a data set in increasing order

    Parameters
    ----------
    data : list or tuple
        List of numbers to analyze

    Returns
    -------
    order : list
        List of all elements from a data set sorted in increasing order

    See Also
    --------
    :func:`~library.statistics.minimum.minimum_value`, :func:`~library.statistics.maximum.maximum_value`, :func:`~library.statistics.median.median_value`, :func:`~library.statistics.halve.half`

    Notes
    -----
    - Set of numbers: :math:`a_i = \\{ a_1, a_2, \\cdots, a_n \\}`
    - Sorted version of set: :math:`A_i = ( A_1, A_2, \\cdots, A_n )`

        - For all terms in :math:`A_i`: :math:`A_{n-1} \\leq A_n`

    - |monotonic_function|

    Examples
    --------
    Sort the set [5, 2, 9, 8]
        >>> order1 = sorted_list([5, 2, 9, 8])
        >>> print(order1)
        [2, 5, 8, 9]
    Sort the set [11, 3, 52, 25, 21, 25, 6]
        >>> order2 = sorted_list([11, 3, 52, 25, 21, 25, 6])
        >>> print(order2)
        [3, 6, 11, 21, 25, 25, 52]
    """
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
    """
    Sorts all elements in a multidimensional data set in increasing order, according to particular dimension

    Parameters
    ----------
    data : list or tuple
        List of lists of numbers to analyze
    dimension: int
        Number representing the dimension to use for sorting

    Returns
    -------
    order : list
        List of lists of numbers sorted in increasing order, based on only one dimension of the nested list

    See Also
    --------
    :func:`~library.statistics.halve.half_dimension`, :func:`~library.vectors.dimension.single_dimension`

    Notes
    -----
    - Set of ordered pairs of numbers: :math:`a_i = \\{ ( a_{1,1}, a_{1,2}, \\cdots, a_{1,j}, a_{1,n} ), ( a_{2,1}, a_{2,2}, \\cdots, a_{2,j}, a_{2,n} ), \\cdots, ( a_{m,1}, a_{m,2}, \\cdots, a_{m,j}, a_{m,n} ) \\}`
    - Sorted version of set according to the values in the :math:`j`\ th position: :math:`A_i = ( ( A_{1,1}, A_{1,2}, \\cdots, A_{1,j}, A_{1,n} ), ( A_{2,1}, A_{2,2}, \\cdots, A_{2,j}, A_{2,n} ), \\cdots, ( A_{m,1}, A_{m,2}, \\cdots, A_{m,j}, A_{m,n} ) )`

        - For all terms in :math:`A_i`: :math:`A_{n-1,j} \\leq A_{n,j}`

    - |monotonic_function|

    Examples
    --------
    Sort the set [[1, 3, 5], [9, 2, 4], [6, 1, 8]] according to its second dimension
        >>> order1 = sorted_dimension([[1, 3, 5], [9, 2, 4], [6, 1, 8]], 2)
        >>> print(order1)
        [[6, 1, 8], [9, 2, 4], [1, 3, 5]]
    Sort the set [[1, 3, 5], [9, 2, 4], [6, 1, 8]] according to its third dimension
        >>> order2 = sorted_dimension([[1, 3, 5], [9, 2, 4], [6, 1, 8]], 3)
        >>> print(order2)
        [[9, 2, 4], [1, 3, 5], [6, 1, 8]]
    """
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