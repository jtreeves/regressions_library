from library.errors.vectors import compare_vectors
from .addition import vector_sum
from .multiplication import scalar_product_vector

def component_form(initial_point, terminal_point):
    """
    Calculates the component form for a vector by using two points

    Parameters
    ----------
    initial_point : list or tuple
        List of numbers representing a point
    terminal_point : list or tuple
        List of numbers representing a point

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
    components : list
        List in which each element is the difference of the corresponding elements from the input points (specifically, the change from the initial point to the terminal point)

    See Also
    --------
    :func:`~library.vectors.addition.vector_sum`, :func:`~library.vectors.multiplication.scalar_product_vector`, :func:`~library.vectors.direction.vector_direction`, :func:`~library.vectors.magnitude.vector_magnitude`

    Notes
    -----
    - Component form of vector beginning at point :math:`A` with coordinates :math:`(a_1, a_2, \\cdots, a_n)` and ending at point :math:`B` with coordinates :math:`(b_1, b_2, \\cdots, b_n)`: :math:`\\overrightarrow{AB} = \\langle b_1 - a_1, b_2 - a_2, \\cdots, b_n - a_n \\rangle`
    - |component_form|

    Examples
    --------
    Determine the component form of a vector with an initial point of [1, 2, 3] and a terminal point of [4, 5, 6]
        >>> components_3d = component_form([1, 2, 3], [4, 5, 6])
        >>> print(components_3d)
        [3, 3, 3]
    Determine the component form of a vector with an initial point of [-5, 12] and a terminal point of [3, -7]
        >>> components_2d = component_form([-5, 12], [3, -7])
        >>> print(components_2d)
        [8, -19]
    """
    compare_vectors(initial_point, terminal_point)
    result = vector_sum(terminal_point, scalar_product_vector(initial_point, -1))
    return result