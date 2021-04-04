from math import floor
from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from library.errors.matrices import matrix_of_scalars
from .sort import sorted_list, sorted_dimension

def partition(data):
    """
    Splits an unsorted data set into two unsorted data sets, each containing the same amount of elements, with elements allocated soley according to where they happen to appear in the original data set (in sets with an odd amount of elements, the median is not included in either half)

    Parameters
    ----------
    data : list or tuple
        List of numbers to analyze

    Returns
    -------
    sections['upper'] : list
        List of all elements from the upper half of a data set
    sections['lower'] : list
        List of all elements from the lower half of a data set

    Examples
    --------
    Determine the upper half of the set [5, 2, 9, 8]
        >>> sections_short = partition([5, 2, 9, 8])
        >>> print(sections_short['upper'])
        [9, 8]
    Determine the lower half of the set [11, 3, 52, 25, 21, 25, 6]
        >>> sections_long = partition([11, 3, 52, 25, 21, 25, 6])
        >>> print(sections_long['lower'])
        [11, 3, 52]
    """
    length = len(data)
    upper = []
    lower = []
    if length % 2 == 0:
        index = int(length / 2)
        upper = data[index:]
        lower = data[:index]
    else:
        index = int(floor(length / 2))
        upper = data[index + 1:]
        lower = data[:index]
    result = {
        'upper': upper,
        'lower': lower
    }
    return result

def half(data):
    """
    Splits an unsorted data set into two sorted data sets, each containing the same amount of elements (in sets with an odd amount of elements, the median is not included in either half)

    Parameters
    ----------
    data : list or tuple
        List of numbers to analyze
    
    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    sections['upper'] : list
        List of all elements from the upper half of a sorted data set
    sections['lower'] : list
        List of all elements from the lower half of a sorted data set

    Examples
    --------
    Determine the sorted upper half of the set [5, 2, 9, 8]
        >>> sections_short = half([5, 2, 9, 8])
        >>> print(sections_short['upper'])
        [8, 9]
    Determine the sorted lower half of the set [11, 3, 52, 25, 21, 25, 6]
        >>> sections_long = half([11, 3, 52, 25, 21, 25, 6])
        >>> print(sections_long['lower'])
        [3, 6, 11]
    """
    vector_of_scalars(data, 'only')
    sorted_data = sorted_list(data)
    result = partition(sorted_data)
    return result

def half_dimension(data, dimension):
    """
    Splits an unsorted 2-dimensional data set into two sorted 2-dimensional data sets, each containing the same amount of elements, in which the sorting occurs based on the elements of the nested lists indicated by the dimension parameter (in sets with an odd amount of elements, the median is not included in either half)

    Parameters
    ----------
    data : list or tuple
        List of lists of numbers to analyze
    dimension : int
        Number indicating by which element of the nested lists to sort
    
    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list or tuple
    TypeError
        Elements nested within first argument must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    sections['upper'] : list
        List of all elements from the upper half of a data set, sorted according to the elements occupying a provided position
    sections['lower'] : list
        List of all elements from the lower half of a data set, sorted according to the elements occupying a provided position

    Examples
    --------
    Determine the upper half of the set [[3, 7, 1], [1, 8, 11], [6, 6, 6], [2, 15, 3], [10, 5, 9]] based on the second dimension
        >>> sections_2d = half_dimension([[3, 7, 1], [1, 8, 11], [6, 6, 6], [2, 15, 3], [10, 5, 9]], 2)
        >>> print(sections_2d['upper'])
        [[1, 8, 11], [2, 15, 3]]
    Determine the lower half of the set [[3, 7, 1], [1, 8, 11], [6, 6, 6], [2, 15, 3], [10, 5, 9]] based on the third dimension
        >>> sections_3d = half_dimension([[3, 7, 1], [1, 8, 11], [6, 6, 6], [2, 15, 3], [10, 5, 9]], 3)
        >>> print(sections_3d['lower'])
        [[3, 7, 1], [2, 15, 3]]
    """
    matrix_of_scalars(data, 'first')
    positive_integer(dimension)
    sorted_data = sorted_dimension(data, dimension)
    result = partition(sorted_data)
    return result