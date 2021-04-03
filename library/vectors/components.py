from library.errors.vectors import compare_vectors
from .addition import vector_sum
from .multiplication import scalar_product

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
    vector : list
        List in which each element is the difference of the corresponding elements from the input points (specifically, the change from the initial point to the terminal point)

    Examples
    --------
    Determince coordinate form of a vector with an initial point of [1, 2, 3] and a terminal point of [4, 5, 6]
        >>> vector_3d = component_form([1, 2, 3], [4, 5, 6])
        >>> print(vector_3d)
        [3, 3, 3]
    Determince coordinate form of a vector with an initial point of [-5, 12] and a terminal point of [3, -7]
        >>> vector_2d = component_form([-5, 12], [3, -7])
        >>> print(vector_2d)
        [8, -19]
    """
    compare_vectors(initial_point, terminal_point)
    result = vector_sum(terminal_point, scalar_product(initial_point, -1))
    return result