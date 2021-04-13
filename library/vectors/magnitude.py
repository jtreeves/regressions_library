from library.errors.vectors import vector_of_scalars
from library.statistics.summation import sum_value

def vector_magnitude(vector):
    """
    Calculates the magnitude of a vector

    Parameters
    ----------
    vector : list
        List of numbers representing a vector

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    magnitude : float
        Measure of the size of the vector, as determined by taking the root of the sum of the squares of its components

    See Also
    --------
    :func:`~library.vectors.components.component_form`, :func:`~library.vectors.direction.vector_direction`,
    :func:`~library.vectors.unit.unit_vector`

    Notes
    -----
    - Vector: :math:`\\mathbf{a} = \\langle a_1, a_2, \\cdots, a_n \\rangle`
    - Magnitude of vector: :math:`\\|\\mathbf{a}\\| = \\sqrt{a_1^2 + a_2^2 + \\cdots + a_n^2}`
    - |magnitude|

    Examples
    --------
    Determine the magnitude of the vector with components [7, 5, -1]
        >>> magnitude_3d = vector_magnitude([7, 5, -1])
        >>> print(magnitude_3d)
        8.660254037844387
    Determine the magnitude of the vector with components [3, 2]
        >>> magnitude_2d = vector_magnitude([3, 2])
        >>> print(magnitude_2d)
        3.605551275463989
    """
    vector_of_scalars(vector, 'only')
    squares = []
    for element in vector:
        squares.append(element**2)
    sum_squares = sum_value(squares)
    result = sum_squares**(1/2)
    return result