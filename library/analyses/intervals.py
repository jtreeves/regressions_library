from library.errors.analyses import callable_function
from library.errors.vectors import allow_none_vector
from library.statistics.sort import sorted_list

def sign_chart(derivative, points):
    """
    Creates a sign chart for a given derivative

    Parameters
    ----------
    derivative : function
        Function of the derivative to use when testing values to construct the sign chart
    points : list or tuple
        Values where the derivative either crosses the x-axis or does not exist

    Raises
    ------
    TypeError
        First argument must be a callable function
    TypeError
        Second argument must be a 1-dimensional list or tuple that only contains integers, floats, `None`, or a final string; if it contains a second element, then its second element must be an integer or a float

    Returns
    -------
    chart : list
        Strings describing the sign (e.g., 'positive', 'negative') of the derivative between its critical points; as a result, its elements will alternate between strings (indicating the signs) and floats (indicating the end points); if the function is sinusoidal, then only the initial results within a two period interval will be listed, but a general form to determine other end points will also be included (see `sinusoidal_roots`)

    Examples
    --------
    Create the sign chart for the first derivative of a cubic function with coefficients 1, -15, 63, and -7
        >>> chart_cubic = sign_chart(lambda x : 3 * x**2 - 30 * x + 63, [3.0, 7.0])
        >>> print(chart_cubic)
        ['positive', 3.0, 'negative', 7.0, 'positive']
    Create the sign chart for the second derivative of a sinusoidal function with coefficients 2, 3, 5, and 7
        >>> chart_sinusoidal = sign_chart(lambda x : -18 * sin(3 * (x - 5)), [5, 6.0472, 7.0944, 8.1416, 9.1888, '5 + 1.0472k'])
        >>> print(chart_sinusoidal)
        ['positive', 5, 'negative', 6.0472, 'positive', 7.0944, 'negative', 8.1416, 'positive', 9.1888, 'negative', '5 + 1.0472k']
    """
    callable_function(derivative, 'first')
    allow_none_vector(points, 'second')
    result = []
    if points[0] == None:
        if derivative(10) > 0:
            result = ['positive']
        elif derivative(10) < 0:
            result = ['negative']
        else:
            result = ['constant']
    elif len(points) == 1:
        turning_point = points[0]
        before = turning_point - 1
        after = turning_point + 1
        if derivative(before) > 0:
            before = 'positive'
        elif derivative(before) < 0:
            before = 'negative'
        if derivative(after) > 0 :
            after = 'positive'
        elif derivative(after) < 0:
            after = 'negative'
        result = [before, turning_point, after]
    elif len(points) == 2:
        sorted_points = sorted_list(points)
        first_point = sorted_points[0]
        second_point = sorted_points[1]
        middle = (first_point + second_point) / 2
        before = first_point - 1
        after = second_point + 1
        if derivative(before) > 0:
            before = 'positive'
        elif derivative(before) < 0:
            before = 'negative'
        if derivative(middle) > 0 :
            middle = 'positive'
        elif derivative(middle) < 0:
            middle = 'negative'
        if derivative(after) > 0:
            after = 'positive'
        elif derivative(after) < 0:
            after = 'negative'
        result = [before, first_point, middle, second_point, after]
    else:
        numerical_points = []
        other_points = []
        for item in points:
            if isinstance(item, (int, float)):
                numerical_points.append(item)
            else:
                other_points.append(item)
        sorted_points = sorted_list(numerical_points)
        difference = sorted_points[1] - sorted_points[0]
        halved_difference = difference / 2
        before_first = sorted_points[0] - halved_difference
        between_first_second = sorted_points[0] + halved_difference
        between_second_third = sorted_points[1] + halved_difference
        between_third_fourth = sorted_points[2] + halved_difference
        between_fourth_last = sorted_points[3] + halved_difference
        after_last = sorted_points[4] + halved_difference
        test_points = [before_first, between_first_second, between_second_third, between_third_fourth, between_fourth_last, after_last]
        signs = []
        for point in test_points:
            if derivative(point) > 0:
                signs.append('positive')
            elif derivative(point) < 0:
                signs.append('negative')
        result = [signs[0], sorted_points[0], signs[1], sorted_points[1], signs[2], sorted_points[2], signs[3], sorted_points[3], signs[4], sorted_points[4], signs[5], *other_points]
    return result