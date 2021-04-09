from library.errors.vectors import compare_vectors

def vector_sum(vector_one, vector_two):
    """
    Calculates the sum of two vectors

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
    vector : list
        List in which each element is the sum of the corresponding elements from the input vectors

    See Also
    --------
    :func:`~library.matrices.addition.matrix_sum`, :func:`~library.vectors.multiplication.scalar_product_vector`

    Notes
    -----
    - Sum of vector :math:`\\mathbf{a}` with form :math:`\\langle a_1, a_2, \\cdots, a_n \\rangle` and vector :math:`\\mathbf{b}` with form :math:`\\langle b_1, b_2, \\cdots, b_n \\rangle`: :math:`\\mathbf{a} + \\mathbf{b} = \\langle a_1 + b_1, a_2 + b_2, \\cdots, a_n + b_n \\rangle`
    - |vector_addition|

    Examples
    --------
    Add [1, 2, 3] and [4, 5, 6]
        >>> vector_3d = vector_sum([1, 2, 3], [4, 5, 6])
        >>> print(vector_3d)
        [5, 7, 9]
    Add [-5, 12] and [3, -7]
        >>> vector_2d = vector_sum([-5, 12], [3, -7])
        >>> print(vector_2d)
        [-2, 5]
    """
    compare_vectors(vector_one, vector_two)
    result = []
    for i in range(len(vector_one)):
        result.append(vector_one[i] + vector_two[i])
    return result