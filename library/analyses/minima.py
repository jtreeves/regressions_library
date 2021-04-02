from library.errors.vectors import multitype_vector

def minima_points(intervals):
    """
    Calculates the minima of a specific function

    Parameters
    ----------
    intervals : list or tuple
        Array containing the sign chart of the specific function's first derivative

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple
    ValueError
        First element of argument must be either 'constant', 'positive', or 'negative'
    TypeError
        Second element of argument must be an integer or a float

    Returns
    -------
    points : list
        Values of the x-coordinates at which the original function has a relative minimum; if the function is sinusoidal, then only two or three results within a two period interval will be listed, but a general form will also be included (see `sinusoidal_roots`); if the function has no minima, then it will return a list of `None`

    Examples
    --------
    Calculate the minima of a cubic function with coefficients 1, -15, 63, and -7
        >>> points_cubic = minima_points(['positive', 3.0, 'negative', 7.0, 'positive'])
        >>> print(points_cubic)
        [7.0]
    Calculate the minima of a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> points_sinusoidal = minima_points(['positive', 5.5236, 'negative', 6.5708, 'positive', 7.618, 'negative', 8.6652, 'positive', 9.7124, 'negative', '1.0472k'])
        >>> print(points_sinusoidal)
        [6.5708, 8.6652, '1.0472k']
    """
    multitype_vector(intervals)
    result = []
    for i in range(len(intervals)):
        try:
            if intervals[i] == 'negative' and intervals[i + 2] == 'positive':
                result.append(intervals[i + 1])
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    return result