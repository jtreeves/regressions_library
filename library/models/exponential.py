from math import log, exp
from library.errors.matrices import matrix_of_scalars
from library.errors.vectors import long_vector
from library.errors.scalars import positive_integer
from library.vectors.dimension import single_dimension
from library.vectors.column import column_conversion
from library.matrices.solve import system_solution
from library.analyses.equations.exponential import exponential_equation
from library.analyses.derivatives.exponential import exponential_derivatives
from library.analyses.integrals.exponential import exponential_integral
from library.analyses.points import key_coordinates
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values
from library.statistics.summary import five_number_summary
from library.statistics.correlation import correlation_coefficient
from library.statistics.rounding import rounded_value

def exponential_model(data, precision):
    """
    Generates an exponential regression model from a given data set

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
        Coefficients of the resultant exponential model; the first element is the constant multiple of the exponential function, and the second element is the base rate of the variable in the exponential function
    model['evaluations']['equation'] : function
        Function that evaluates the equation of the exponential model at a given numeric input (e.g., model['evaluations']['equation'](10) would evaluate the equation of the exponential model when the independent variable is 10)
    model['evaluations']['derivative'] : function
        Function that evaluates the first derivative of the exponential model at a given numeric input (e.g., model['evaluations']['derivative'](10) would evaluate the first derivative of the exponential model when the independent variable is 10)
    model['evaluations']['integral'] : function
        Function that evaluates the integral of the exponential model at a given numeric input (e.g., model['evaluations']['integral'](10) would evaluate the integral of the exponential model when the independent variable is 10)
    model['points']['roots'] : list
        List of lists of numbers representing the coordinate pairs of all the x-intercepts of the exponential model (will always be `None`)
    model['points']['maxima'] : list
        List of lists of numbers representing the coordinate pairs of all the maxima of the exponential model (will always be `None`)
    model['points']['minima'] : list
        List of lists of numbers representing the coordinate pairs of all the minima of the exponential model (will always be `None`)
    model['points']['inflections'] : list
        List of lists of numbers representing the coordinate pairs of all the inflection points of the exponential model (will always be `None`)
    model['accumulations']['range'] : float
        Total area under the curve represented by the exponential model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided (i.e., over the range)
    model['accumulations']['iqr'] : float
        Total area under the curve represented by the exponential model between the first and third quartiles of all the independent coordinates originally provided (i.e., over the interquartile range)
    model['averages']['range']['average_value_derivative'] : float
        Average rate of change of the curve represented by the exponential model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided
    model['averages']['range']['mean_values_derivative'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their instantaneous rate of change equals the function's average rate of change over that interval
    model['averages']['range']['average_value_integral'] : float
        Average value of the curve represented by the exponential model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided
    model['averages']['range']['mean_values_integral'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their value equals the function's average value over that interval
    model['averages']['iqr']['average_value_derivative'] : float
        Average rate of change of the curve represented by the exponential model between the first and third quartiles of all the independent coordinates originally provided
    model['averages']['iqr']['mean_values_derivative'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their instantaneous rate of change equals the function's average rate of change over that interval
    model['averages']['iqr']['average_value_integral'] : float
        Average value of the curve represented by the exponential model between the first and third quartiles of all the independent coordinates originally provided
    model['averages']['iqr']['mean_values_integral'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their value equals the function's average value over that interval
    model['correlation'] : float
        Correlation coefficient indicating how well the model fits the original data set (values range between 0.0, implying no fit, and 1.0, implying a perfect fit)

    Examples
    --------
    Generate an exponential regression model for the data set [[1, 6], [2, 12], [3, 24], [4, 48], [5, 96], [6, 192], [7, 384], [8, 768], [9, 1536], [10, 3072]], then print its coefficients, roots, total accumulation over its interquartile range, and correlation (and round the results to four decimal places)
        >>> model_perfect = exponential_model([[1, 6], [2, 12], [3, 24], [4, 48], [5, 96], [6, 192], [7, 384], [8, 768], [9, 1536], [10, 3072]], 4)
        >>> print(model_perfect['constants'])
        [3.0, 1.9999]
        >>> print(model_perfect['points']['roots'])
        [None]
        >>> print(model_perfect['accumulations']['iqr'])
        1073.0046
        >>> print(model_perfect['correlation'])
        1.0
    Generate an exponential regression model for the data set [[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], then print its coefficients, inflections, total accumulation over its range, and correlation (and round the results to four decimal places)
        >>> model_agnostic = exponential_model([[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], 4)
        >>> print(model_agnostic['constants'])
        [22.1049, 1.0692]
        >>> print(model_agnostic['points']['inflections'])
        [None]
        >>> print(model_agnostic['accumulations']['range'])
        291.8084
        >>> print(model_agnostic['correlation'])
        0.5069
    """
    matrix_of_scalars(data, 'first')
    long_vector(data)
    positive_integer(precision)
    independent_variable = single_dimension(data, 1)
    dependent_variable = single_dimension(data, 2)
    filtered_dependent = []
    for element in dependent_variable:
        if element <= 0:
            filtered_dependent.append(10**(-precision))
        else:
            filtered_dependent.append(element)
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([independent_variable[i], 1])
        dependent_matrix.append([log(filtered_dependent[i])])
    solution = system_solution(independent_matrix, dependent_matrix, precision)
    constants = [exp(solution[1]), exp(solution[0])]
    coefficients = [rounded_value(constants[0], precision), rounded_value(constants[1], precision)]
    equation = exponential_equation(*coefficients)
    derivative = exponential_derivatives(*coefficients)
    integral = exponential_integral(*coefficients)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_coordinates('exponential', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulated_area(integral, min_value, max_value, precision)
    accumulated_iqr = accumulated_area(integral, q1, q3, precision)
    averages_range = average_values('exponential', equation, integral, min_value, max_value, coefficients, precision)
    averages_iqr = average_values('exponential', equation, integral, q1, q3, coefficients, precision)
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
        'constants': coefficients,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result