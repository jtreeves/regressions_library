from library.errors.scalars import scalar_value
from library.errors.vectors import vector_of_scalars, compare_vectors

def scalar_product_vector(vector, scalar):
    """
    Calculates the product of a vector and a scalar

    Parameters
    ----------
    vector : list or tuple
        List of numbers representing a vector
    scalar : int or float
        Number representing a scalar

    Raises
    ------
    TypeError
        First argument must be a 1-dimensional list or tuple
    TypeError
        Elements of first argument must be integers or floats
    TypeError
        Second argument must be an integer or a float

    Returns
    -------
    product : list
        List of numbers in which each element is the product of the scalar factor and the corresponding element from the input vector

    See Also
    --------
    :func:`~library.matrices.multiplication.scalar_product_matrix`, :func:`~library.vectors.addition.vector_sum`

    Notes
    -----
    - Scalar product of vector :math:`\\mathbf{a}` with form :math:`\\langle a_1, a_2, \\cdots, a_n \\rangle` and scalar :math:`c`: :math:`c\\cdot{\\mathbf{a}} = \\langle c\\cdot{a_1}, c\\cdot{a_2}, \\cdots, c\\cdot{a_n} \\rangle`
    - |scalar_multiplication|

    Examples
    --------
    Multiply [1, 2, 3] and -2
        >>> product_3d = scalar_product([1, 2, 3], -2)
        >>> print(product_3d)
        [-2, -4, -6]
    Multiply [-5, 12] and 3
        >>> product_2d = scalar_product([-5, 12], 3)
        >>> print(product_2d)
        [-15, 36]
    """
    vector_of_scalars(vector, 'first')
    scalar_value(scalar, 'second')
    result = []
    for element in vector:
        result.append(element * scalar)
    return result

def dot_product(vector_one, vector_two):
    """
    Calculates the product of two vectors

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
    product : float
        Number created by summing the products of the corresponding terms from each input vector

    See Also
    --------
    :func:`~library.matrices.multiplication.matrix_product`

    Notes
    -----
    - Dot product of vector :math:`\\mathbf{a}` with form :math:`\\langle a_1, a_2, \\cdots, a_n \\rangle` and vector :math:`\\mathbf{b}` with form :math:`\\langle b_1, b_2, \\cdots, b_n \\rangle`: :math:`\\mathbf{a}\\cdot{\\mathbf{b}} = a_1\\cdot{b_1} + a_2\\cdot{b_2} + \\cdots + a_n\\cdot{b_n}`
    - |dot_product|

    Examples
    --------
    Multiply [1, 2, 3] and [4, 5, 6]
        >>> product_3d = dot_product([1, 2, 3], [4, 5, 6])
        >>> print(product_3d)
        32
    Multiply [-5, 12] and [3, -7]
        >>> product_2d = dot_product([-5, 12], [3, -7])
        >>> print(product_2d)
        -99
    """
    compare_vectors(vector_one, vector_two)
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result