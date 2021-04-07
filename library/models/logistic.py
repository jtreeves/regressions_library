from numpy import exp, inf
from scipy.optimize import curve_fit
from library.errors.matrices import matrix_of_scalars
from library.errors.vectors import long_vector
from library.errors.scalars import positive_integer
from library.vectors.dimension import single_dimension
from library.analyses.equations.logistic import logistic_equation
from library.analyses.derivatives.logistic import logistic_derivatives
from library.analyses.integrals.logistic import logistic_integral
from library.analyses.points import key_coordinates
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values
from library.statistics.halve import half_dimension
from library.statistics.mean import mean_value
from library.statistics.summary import five_number_summary
from library.statistics.correlation import correlation_coefficient
from library.statistics.rounding import rounded_value

def logistic_model(data, precision):
    """
    Generates a logistic regression model from a given data set

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
        Coefficients of the resultant logistic model; the first element is the carrying capacity, the second element is the growth rate, and the third element is the sigmoid's midpoint
    model['evaluations']['equation'] : function
        Function that evaluates the equation of the logistic model at a given numeric input (e.g., model['evaluations']['equation'](10) would evaluate the equation of the logistic model when the independent variable is 10)
    model['evaluations']['derivative'] : function
        Function that evaluates the first derivative of the logistic model at a given numeric input (e.g., model['evaluations']['derivative'](10) would evaluate the first derivative of the logistic model when the independent variable is 10)
    model['evaluations']['integral'] : function
        Function that evaluates the integral of the logistic model at a given numeric input (e.g., model['evaluations']['integral'](10) would evaluate the integral of the logistic model when the independent variable is 10)
    model['points']['roots'] : list
        List of lists of numbers representing the coordinate pairs of all the x-intercepts of the logistic model (will always be `None`)
    model['points']['maxima'] : list
        List of lists of numbers representing the coordinate pairs of all the maxima of the logistic model (will always be `None`)
    model['points']['minima'] : list
        List of lists of numbers representing the coordinate pairs of all the minima of the logistic model (will always be `None`)
    model['points']['inflections'] : list
        List of lists of numbers representing the coordinate pairs of all the inflection points of the logistic model (will contain exactly one point)
    model['accumulations']['range'] : float
        Total area under the curve represented by the logistic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided (i.e., over the range)
    model['accumulations']['iqr'] : float
        Total area under the curve represented by the logistic model between the first and third quartiles of all the independent coordinates originally provided (i.e., over the interquartile range)
    model['averages']['range']['average_value_derivative'] : float
        Average rate of change of the curve represented by the logistic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided
    model['averages']['range']['mean_values_derivative'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their instantaneous rate of change equals the function's average rate of change over that interval
    model['averages']['range']['average_value_integral'] : float
        Average value of the curve represented by the logistic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided
    model['averages']['range']['mean_values_integral'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their value equals the function's average value over that interval
    model['averages']['iqr']['average_value_derivative'] : float
        Average rate of change of the curve represented by the logistic model between the first and third quartiles of all the independent coordinates originally provided
    model['averages']['iqr']['mean_values_derivative'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their instantaneous rate of change equals the function's average rate of change over that interval
    model['averages']['iqr']['average_value_integral'] : float
        Average value of the curve represented by the logistic model between the first and third quartiles of all the independent coordinates originally provided
    model['averages']['iqr']['mean_values_integral'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their value equals the function's average value over that interval
    model['correlation'] : float
        Correlation coefficient indicating how well the model fits the original data set (values range between 0.0, implying no fit, and 1.0, implying a perfect fit)

    Examples
    --------
    Generate a logistic regression model for the data set [[1, 0.0000122], [2, 0.000247], [3, 0.004945], [4, 0.094852], [5, 1.0], [6, 1.905148], [7, 1.995055], [8, 1.999753], [9, 1.999988], [10, 1.999999]], then print its coefficients, roots, total accumulation over its interquartile range, and correlation (and round the results to four decimal places)
        >>> model_perfect = logistic_model([[1, 0.0000122], [2, 0.000247], [3, 0.004945], [4, 0.094852], [5, 1.0], [6, 1.905148], [7, 1.995055], [8, 1.999753], [9, 1.999988], [10, 1.999999]], 4)
        >>> print(model_perfect['constants'])
        [2.0, 3.0, 5.0]
        >>> print(model_perfect['points']['roots'])
        [None]
        >>> print(model_perfect['accumulations']['iqr'])
        5.9984
        >>> print(model_perfect['correlation'])
        1.0
    Generate a logistic regression model for the data set [[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], then print its coefficients, inflections, total accumulation over its range, and correlation (and round the results to four decimal places)
        >>> model_agnostic = logistic_model([[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], 4)
        >>> print(model_agnostic['constants'])
        [43.983, 0.3076, 0.9746]
        >>> print(model_agnostic['points']['inflections'])
        [[0.9746, 21.9914]]
        >>> print(model_agnostic['accumulations']['range'])
        305.924
        >>> print(model_agnostic['correlation'])
        0.5875
    """
    matrix_of_scalars(data, 'first')
    long_vector(data)
    positive_integer(precision)
    independent_variable = single_dimension(data, 1)
    dependent_variable = single_dimension(data, 2)
    halved_data = half_dimension(data, 1)
    dependent_lower = single_dimension(halved_data['lower'], 2)
    dependent_upper = single_dimension(halved_data['upper'], 2)
    mean_lower = mean_value(dependent_lower)
    mean_upper = mean_value(dependent_upper)
    dependent_max = max(dependent_variable)
    dependent_min = min(dependent_variable)
    dependent_range = dependent_max - dependent_min
    solution = []
    def logistic_fit(variable, first_constant, second_constant, third_constant):
        evaluation = first_constant / (1 + exp(-1 * second_constant * (variable - third_constant)))
        return evaluation
    if mean_upper >= mean_lower:
        parameters, covariance = curve_fit(logistic_fit, independent_variable, dependent_variable, bounds=[(dependent_max - dependent_range, 0, -inf), (dependent_max + dependent_range, inf, inf)])
        solution = list(parameters)
    else:
        parameters, covariance = curve_fit(logistic_fit, independent_variable, dependent_variable, bounds=[(dependent_max - dependent_range, -inf, -inf), (dependent_max + dependent_range, 0, inf)])
        solution = list(parameters)
    constants = []
    for number in solution:
        constants.append(rounded_value(number, precision))
    equation = logistic_equation(*solution)
    derivative = logistic_derivatives(*solution)
    integral = logistic_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_coordinates('logistic', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulated_area(integral, min_value, max_value, precision)
    accumulated_iqr = accumulated_area(integral, q1, q3, precision)
    averages_range = average_values('logistic', equation, integral, min_value, max_value, solution, precision)
    averages_iqr = average_values('logistic', equation, integral, q1, q3, solution, precision)
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
        'constants': constants,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result