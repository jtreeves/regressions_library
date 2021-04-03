from library.errors.matrices import matrix_of_scalars, level
from library.errors.scalars import positive_integer

def single_dimension(matrix, scalar):
    """
    Extracts a column vector from a matrix according to an integer corresponding to the column's position

    Parameters
    ----------
    matrix : list or tuple
        List containing other lists, where each inner list is a row and elements within those inner lists correspond to columns
    scalar : int
        Number corresponding to the column's position

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list or tuple
    TypeError
        Elements nested within the first argument's lists must be integers or floats
    ValueError
        Last argument must be a positive integer

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
    matrix_of_scalars(matrix, 'first')
    positive_integer(scalar)
    level(matrix, scalar)
    result = []
    for element in matrix:
        result.append(element[scalar - 1])
    return result