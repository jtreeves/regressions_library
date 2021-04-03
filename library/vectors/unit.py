from library.errors.vectors import vector_of_scalars
from .magnitude import vector_magnitude
from .multiplication import scalar_product

def unit_vector(vector):
    """
    Calculates the unit vector corresponding to a given vector (and therefore having the same direction)

    Parameters
    ----------
    vector : list or tuple
        List of numbers representing a vector

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    unit : list
        Vector with a magnitue of 1 in the same direction as the original vector

    Examples
    --------
    Determine the unit vector of the vector with components [7, 5, -1]
        >>> unit_3d = unit_vector([7, 5, -1])
        >>> print(unit_3d)
        [0.8082903768654759, 0.5773502691896257, -0.11547005383792514]
    Determine the unit vector of the vector with components [3, 2]
        >>> unit_2d = unit_vector([3, 2])
        >>> print(unit_2d)
        [0.8320502943378437, 0.5547001962252291]
    """
    vector_of_scalars(vector, 'only')
    magnitude = vector_magnitude(vector)
    reciprocal_magnitude = 1 / magnitude
    result = scalar_product(vector, reciprocal_magnitude)
    return result