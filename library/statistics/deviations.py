from library.errors.scalars import scalar_value
from library.errors.vectors import vector_of_scalars
from .mean import mean_value

def single_deviation(actual, mean): 
    """
    Calculates the difference between the actual value from a data set and the mean of that data set

    Parameters
    ----------
    actual : int or float
        Value actually provided by an initial data set
    mean : int or float
        Average value of the data set

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    deviation : int or float
        Difference between the actual value and the mean of the data set

    See Also
    --------
    :func:`~library.statistics.mean.mean_value`, :func:`~library.statistics.residuals.single_residual`, :func:`~library.statistics.correlation.correlation_coefficient`

    Notes
    -----
    - Observed value: :math:`y`
    - Mean of all observed values: :math:`\\bar{y}`
    - Deviation: :math:`d = y - \\bar{y}`
    - |deviation|

    Examples
    --------
    Determine the deviation for an actual value of 7.8 and a mean of 13.75
        >>> deviation_small = single_deviation(7.8, 13.75)
        >>> print(deviation_small)
        -5.95
    Determine the deviation between an actual value of 6.1 and an mean of -19.7
        >>> deviation_large = single_deviation(6.1, -19.7)
        >>> print(deviation_large)
        25.799999999999997
    """
    scalar_value(actual, 'first')
    scalar_value(mean, 'second')
    result = actual - mean
    return result

def multiple_deviations(actual_array):
    """
    Generates a list of the differences between the actual values from an original list and mean value of the actual values from that original list

    Parameters
    ----------
    actual_array : list or tuple
        List containing the actual values observed from a data set

    Raises
    ------
    TypeError
        Arguments must be 1-dimensional lists or tuples
    TypeError
        Elements of arguments must be integers or floats

    Returns
    -------
    deviations : list
        List of differences between the actual values and the mean value for all elements from the original list

    See Also
    --------
    :func:`~library.statistics.mean.mean_value`, :func:`~library.statistics.residuals.multiple_residuals`, :func:`~library.statistics.correlation.correlation_coefficient`

    Notes
    -----
    - Observed values: :math:`y_i = \\{ y_1, y_2, \\cdots, y_n \\}`
    - Mean of all observed values: :math:`\\bar{y} = \\frac{1}{n}\\cdot{\\sum\\limits_{i=1}^n y_i}`
    - Deviations: :math:`d_i = \\{ y_1 - \\bar{y}, y_2 - \\bar{y}, \\cdots, y_n - \\bar{y} \\}`
    - |deviation|

    Examples
    --------
    Generate a list of deviations from this data set [8.2, 9.41, 1.23, 34.7]
        >>> deviations_short = multiple_deviations([8.2, 9.41, 1.23, 34.7])
        >>> print(deviations_short)
        [-5.185000000000002, -3.9750000000000014, -12.155000000000001, 21.315]
    Generate a list of deviations from this data set [5.21, 8.2, 9.41, 1.23, 10.52, 21.76, 34.7]
        >>> deviations_long = multiple_deviations([5.21, 8.2, 9.41, 1.23, 10.52, 21.76, 34.7])
        >>> print(deviations_long)
        [-7.7942857142857145, -4.804285714285715, -3.5942857142857143, -11.774285714285714, -2.484285714285715, 8.755714285714287, 21.69571428571429]
    """
    vector_of_scalars(actual_array, 'only')
    results = []
    average = mean_value(actual_array)
    for element in actual_array:
        results.append(single_deviation(element, average))
    return results