from library.errors.vectors import compare_vectors

def unite_vectors(vector_one, vector_two):
    """
    Unites two row vectors into a single matrix whose columns coincide with the input vectors

    Parameters
    ----------
    vector_one : list or tuple
        List of numbers representing a vector
    vector_two : list or tuple
        List of numbers representing a vector

    Raises
    ------
    TypeError
        Arguments must be 1-dimensional lists or tuples
    TypeError
        Elements of arguments must be integers or floats
    ValueError
        Both arguments must contain the same number of elements

    Returns
    -------
    matrix : list
        List containing lists; length of outer list will equal lengths of supplied vectors; length of inner lists will equal two

    Examples
    --------
    Unite [1, 2, 3] and [4, 5, 6]
        >>> matrix_3x2 = unite_vectors([1, 2, 3], [4, 5, 6])
        >>> print(matrix_2x3)
        [[1, 4], [2, 5], [3, 6]]
    Unite [-5, 12] and [3, -7]
        >>> matrix_2x2 = unite_vectors([-5, 12], [3, -7])
        >>> print(matrix_2x2)
        [[-5, 3], [12, -7]]
    """
    compare_vectors(vector_one, vector_two)
    result = []
    if vector_one[0] == None:
        result.append(None)
    else:
        for i in range(len(vector_one)):
            result.append([vector_one[i], vector_two[i]])
    return result