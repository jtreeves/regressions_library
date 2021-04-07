from library.errors.matrices import matrix_of_scalars
from library.errors.vectors import long_vector
from library.errors.scalars import positive_integer
from library.vectors.dimension import single_dimension
from library.vectors.column import column_conversion
from library.matrices.solve import system_solution
from library.analyses.equations.cubic import cubic_equation
from library.analyses.derivatives.cubic import cubic_derivatives
from library.analyses.integrals.cubic import cubic_integral
from library.analyses.points import key_coordinates
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values
from library.statistics.summary import five_number_summary
from library.statistics.correlation import correlation_coefficient

def cubic_model(data, precision):
    """
    Generates a cubic regression model from a given data set

    Parameters
    ----------
    data : list or tuple
        List of lists of numbers representing a collection of coordinate pairs
    precision : int
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list or tuple
    TypeError
        Elements nested within first argument must be integers or floats
    ValueError
        First argument must contain at least 10 elements
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    model['constants'] : list
        Coefficients of the resultant cubic model; the first element is the coefficient of the cubic term, the second element is the coefficient of the quadratic term, the third element is the coefficient of the linear term, and the fourth element is the coefficient of the constant term
    model['evaluations']['equation'] : function
        Function that evaluates the equation of the cubic model at a given numeric input (e.g., model['evaluations']['equation'](10) would evaluate the equation of the cubic model when the independent variable is 10)
    model['evaluations']['derivative'] : function
        Function that evaluates the first derivative of the cubic model at a given numeric input (e.g., model['evaluations']['derivative'](10) would evaluate the first derivative of the cubic model when the independent variable is 10)
    model['evaluations']['integral'] : function
        Function that evaluates the integral of the cubic model at a given numeric input (e.g., model['evaluations']['integral'](10) would evaluate the integral of the cubic model when the independent variable is 10)
    model['points']['roots'] : list
        List of lists of numbers representing the coordinate pairs of all the x-intercepts of the cubic model (will contain at least one and at most three points)
    model['points']['maxima'] : list
        List of lists of numbers representing the coordinate pairs of all the maxima of the cubic model (will contain either `None` or one point)
    model['points']['minima'] : list
        List of lists of numbers representing the coordinate pairs of all the minima of the cubic model (will contain either `None` or one point)
    model['points']['inflections'] : list
        List of lists of numbers representing the coordinate pairs of all the inflection points of the cubic model (will contain exactly one point)
    model['accumulations']['range'] : float
        Total area under the curve represented by the cubic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided (i.e., over the range)
    model['accumulations']['iqr'] : float
        Total area under the curve represented by the cubic model between the first and third quartiles of all the independent coordinates originally provided (i.e., over the interquartile range)
    model['averages']['range']['average_value_derivative'] : float
        Average rate of change of the curve represented by the cubic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided (see `Mean Value Theorem for Derivatives <https://tutorial.math.lamar.edu/classes/calci/MeanValueTheorem.aspx>`_)
    model['averages']['range']['mean_values_derivative'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their instantaneous rate of change equals the function's average rate of change over that interval (see `Mean Value Theorem for Derivatives <https://tutorial.math.lamar.edu/classes/calci/MeanValueTheorem.aspx>`_)
    model['averages']['range']['average_value_integral'] : float
        Average value of the curve represented by the cubic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided (see `Mean Value Theorem for Integrals <https://tutorial.math.lamar.edu/classes/calci/avgfcnvalue.aspx>`_)
    model['averages']['range']['mean_values_integral'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their value equals the function's average value over that interval (see `Mean Value Theorem for Integrals <https://tutorial.math.lamar.edu/classes/calci/avgfcnvalue.aspx>`_)
    model['averages']['iqr']['average_value_derivative'] : float
        Average rate of change of the curve represented by the cubic model between the first and third quartiles of all the independent coordinates originally provided (see `Mean Value Theorem for Derivatives <https://tutorial.math.lamar.edu/classes/calci/MeanValueTheorem.aspx>`_)
    model['averages']['iqr']['mean_values_derivative'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their instantaneous rate of change equals the function's average rate of change over that interval (see `Mean Value Theorem for Derivatives <https://tutorial.math.lamar.edu/classes/calci/MeanValueTheorem.aspx>`_)
    model['averages']['iqr']['average_value_integral'] : float
        Average value of the curve represented by the cubic model between the first and third quartiles of all the independent coordinates originally provided (see `Mean Value Theorem for Integrals <https://tutorial.math.lamar.edu/classes/calci/avgfcnvalue.aspx>`_)
    model['averages']['iqr']['mean_values_integral'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their value equals the function's average value over that interval (see `Mean Value Theorem for Integrals <https://tutorial.math.lamar.edu/classes/calci/avgfcnvalue.aspx>`_)
    model['correlation'] : float
        Correlation coefficient indicating how well the model fits the original data set (values range between 0.0, implying no fit, and 1.0, implying a perfect fit)

    Examples
    --------
    Generate a cubic regression model for the data set [[1, 42], [2, 67], [3, 74], [4, 69], [5, 58], [6, 47], [7, 42], [8, 49], [9, 74], [10, 123]], then print its coefficients, roots, total accumulation over its interquartile range, and correlation (and round the results to four decimal places)
        >>> model_perfect = cubic_model([[1, 42], [2, 67], [3, 74], [4, 69], [5, 58], [6, 47], [7, 42], [8, 49], [9, 74], [10, 123]], 4)
        >>> print(model_perfect['constants'])
        [1.0, -15.0, 63.0, -7.0]
        >>> print(model_perfect['points']['roots'])
        [[0.1142, 0]]
        >>> print(model_perfect['accumulations']['iqr'])
        276.25
        >>> print(model_perfect['correlation'])
        1.0
    Generate a cubic regression model for the data set [[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], then print its coefficients, inflections, total accumulation over its range, and correlation (and round the results to four decimal places)
        >>> model_agnostic = cubic_model([[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], 4)
        >>> print(model_agnostic['constants'])
        [-0.3881, 6.0932, -24.155, 49.4667]
        >>> print(model_agnostic['points']['inflections'])
        [[5.2334, 34.3091]]
        >>> print(model_agnostic['accumulations']['range'])
        308.4104
        >>> print(model_agnostic['correlation'])
        0.8933
    """
    matrix_of_scalars(data, 'first')
    long_vector(data)
    positive_integer(precision)
    independent_variable = single_dimension(data, 1)
    dependent_variable = single_dimension(data, 2)
    independent_matrix = []
    dependent_matrix = column_conversion(dependent_variable)
    for element in independent_variable:
        independent_matrix.append([element**3, element**2, element, 1])
    solution = system_solution(independent_matrix, dependent_matrix, precision)
    equation = cubic_equation(*solution)
    derivative = cubic_derivatives(*solution)
    integral = cubic_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_coordinates('cubic', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulated_area(integral, min_value, max_value, precision)
    accumulated_iqr = accumulated_area(integral, q1, q3, precision)
    averages_range = average_values('cubic', equation, integral, min_value, max_value, solution, precision)
    averages_iqr = average_values('cubic', equation, integral, q1, q3, solution, precision)
    predicted = []
    for element in independent_variable:
        predicted.append(equation(element))
    accuracy = correlation_coefficient(dependent_variable, predicted, precision)
    evaluations = {
        'equation': equation,
        'derivative': first_derivative,
        'integral': integral
    }
    points = {
        'roots': points['roots'],
        'maxima': points['maxima'],
        'minima': points['minima'],
        'inflections': points['inflections']
    }
    accumulations = {
        'range': accumulated_range,
        'iqr': accumulated_iqr
    }
    averages = {
        'range': averages_range,
        'iqr': averages_iqr
    }
    result = {
        'constants': solution,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result