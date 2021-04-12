from math import log
from library.errors.matrices import matrix_of_scalars
from library.errors.vectors import long_vector
from library.errors.scalars import positive_integer
from library.vectors.dimension import single_dimension
from library.vectors.column import column_conversion
from library.matrices.solve import system_solution
from library.analyses.equations.logarithmic import logarithmic_equation
from library.analyses.derivatives.logarithmic import logarithmic_derivatives
from library.analyses.integrals.logarithmic import logarithmic_integral
from library.analyses.points import key_coordinates
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values
from library.statistics.summary import five_number_summary
from library.statistics.correlation import correlation_coefficient

def logarithmic_model(data, precision):
    """
    Generates a logarithmic regression model from a given data set

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
        Coefficients of the resultant logarithmic model; the first element is the coefficient of the logarithmic term, and the second element is the coefficient of the constant term
    model['evaluations']['equation'] : function
        Function that evaluates the equation of the logarithmic model at a given numeric input (e.g., model['evaluations']['equation'](10) would evaluate the equation of the logarithmic model when the independent variable is 10)
    model['evaluations']['derivative'] : function
        Function that evaluates the first derivative of the logarithmic model at a given numeric input (e.g., model['evaluations']['derivative'](10) would evaluate the first derivative of the logarithmic model when the independent variable is 10)
    model['evaluations']['integral'] : function
        Function that evaluates the integral of the logarithmic model at a given numeric input (e.g., model['evaluations']['integral'](10) would evaluate the integral of the logarithmic model when the independent variable is 10)
    model['points']['roots'] : list
        List of lists of numbers representing the coordinate pairs of all the x-intercepts of the logarithmic model (will contain exactly one point)
    model['points']['maxima'] : list
        List of lists of numbers representing the coordinate pairs of all the maxima of the logarithmic model (will always be `None`)
    model['points']['minima'] : list
        List of lists of numbers representing the coordinate pairs of all the minima of the logarithmic model (will always be `None`)
    model['points']['inflections'] : list
        List of lists of numbers representing the coordinate pairs of all the inflection points of the logarithmic model (will always be `None`)
    model['accumulations']['range'] : float
        Total area under the curve represented by the logarithmic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided (i.e., over the range)
    model['accumulations']['iqr'] : float
        Total area under the curve represented by the logarithmic model between the first and third quartiles of all the independent coordinates originally provided (i.e., over the interquartile range)
    model['averages']['range']['average_value_derivative'] : float
        Average rate of change of the curve represented by the logarithmic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided
    model['averages']['range']['mean_values_derivative'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their instantaneous rate of change equals the function's average rate of change over that interval
    model['averages']['range']['average_value_integral'] : float
        Average value of the curve represented by the logarithmic model between the smallest independent coordinate originally provided and the largest independent coordinate originally provided
    model['averages']['range']['mean_values_integral'] : list
        All points between the smallest independent coordinate originally provided and the largest independent coordinate originally provided where their value equals the function's average value over that interval
    model['averages']['iqr']['average_value_derivative'] : float
        Average rate of change of the curve represented by the logarithmic model between the first and third quartiles of all the independent coordinates originally provided
    model['averages']['iqr']['mean_values_derivative'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their instantaneous rate of change equals the function's average rate of change over that interval
    model['averages']['iqr']['average_value_integral'] : float
        Average value of the curve represented by the logarithmic model between the first and third quartiles of all the independent coordinates originally provided
    model['averages']['iqr']['mean_values_integral'] : list
        All points between the first and third quartiles of all the independent coordinates originally provided where their value equals the function's average value over that interval
    model['correlation'] : float
        Correlation coefficient indicating how well the model fits the original data set (values range between 0.0, implying no fit, and 1.0, implying a perfect fit)

    See Also
    --------
    :func:`~library.analyses.equations.logarithmic.logarithmic_equation`, :func:`~library.analyses.derivatives.logarithmic.logarithmic_derivatives`, :func:`~library.analyses.integrals.logarithmic.logarithmic_integral`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.statistics.correlation.correlation_coefficient`, :func:`~library.execute.run_all`

    Notes
    -----
    - Provided ordered pairs for the data set: :math:`p_i = \\{ (p_{1,x}, p_{1,y}), (p_{2,x}, p_{2,y}), \\cdots, (p_{n,x}, p_{n,y}) \\}`
    - Provided values for the independent variable: :math:`X_i = \\{ p_{1,x}, p_{2,x}, \\cdots, p_{n,x} \\}`
    - Provided values for the dependent variable: :math:`Y_i = \\{ p_{1,y}, p_{2,y}, \\cdots, p_{n,y} \\}`
    - Minimum value of the provided values for the independent variable: :math:`X_{min} \\leq p_{j,x}, \\forall p_{j,x} \\in X_i`
    - Maximum value of the provided values for the independent variable: :math:`X_{max} \\geq p_{j,x}, \\forall p_{j,x} \\in X_i`
    - First quartile of the provided values for the independent variable: :math:`X_{Q1}`
    - Third quartile of the provided values for the independent variable: :math:`X_{Q3}`
    - Mean of all provided values for the dependent variable: :math:`\\bar{y} = \\frac{1}{n}\\cdot{\\sum\\limits_{i=1}^n Y_i}`
    - Resultant values for the coefficients of the logarithmic model: :math:`C_i = \\{ a, b \\}`
    - Standard form for the equation of the logarithmic model: :math:`f(x) = a\\cdot{\\ln{x}} + b`
    - First derivative of the logarithmic model: :math:`f'(x) = a\\cdot{\\frac{1}{x}}`
    - Second derivative of the logarithmic model: :math:`f''(x) = -a\\cdot{\\frac{1}{x^2}}`
    - Integral of the logarithmic model: :math:`F(x) = a\\cdot{x}\\cdot(\\ln{x} - 1) + b\\cdot{x}`
    - Potential x-values of the roots of the logarithmic model: :math:`x_{intercepts} = \\{ \\text{e}^{-\\frac{b}{a}} \\}`
    - Potential x-values of the maxima of the logarithmic model: :math:`x_{maxima} = \\{ \\varnothing \\}`
    - Potential x-values of the minima of the logarithmic model: :math:`x_{minima} = \\{ \\varnothing \\}`
    - Potential x-values of the inflection points of the logarithmic model: :math:`x_{inflections} = \\{ \\varnothing \\}`
    - Accumulatation of the logarithmic model over its range: :math:`A_{range} = \\int_{X_{min}}^{X_{max}} f(x) \\,dx`
    - Accumulatation of the logarithmic model over its interquartile range: :math:`A_{iqr} = \\int_{X_{Q1}}^{X_{Q3}} f(x) \\,dx`
    - Average rate of change of the logarithmic model over its range: :math:`m_{range} = \\frac{f(X_{max}) - f(X_{min})}{X_{max} - X_{min}}`
    - Potential x-values at which the logarithmic model's instantaneous rate of change equals its average rate of change over its range: :math:`x_{m,range} = \\{ \\frac{a}{m_{range}} \\}`
    - Average value of the logarithmic model over its range: :math:`v_{range} = \\frac{1}{X_{max} - X_{min}}\\cdot{A_{range}}`
    - Potential x-values at which the logarithmic model's value equals its average value over its range: :math:`x_{v,range} = \\{ \\text{e}^{-\\frac{b - v_{range}}{a}} \\}`
    - Average rate of change of the logarithmic model over its interquartile range: :math:`m_{iqr} = \\frac{f(X_{Q3}) - f(X_{Q1})}{X_{Q3} - X_{Q1}}`
    - Potential x-values at which the logarithmic model's instantaneous rate of change equals its average rate of change over its interquartile range: :math:`x_{m,iqr} = \\{ \\frac{a}{m_{iqr}} \\}`
    - Average value of the logarithmic model over its interquartile range: :math:`v_{iqr} = \\frac{1}{X_{Q3} - X_{Q1}}\\cdot{A_{iqr}}`
    - Potential x-values at which the logarithmic model's value equals its average value over its interquartile range: :math:`x_{v,iqr} = \\{ \\text{e}^{-\\frac{b - v_{iqr}}{a}} \\}`
    - Predicted values based on the logarithmic model: :math:`\\hat{y}_i = \\{ \\hat{y}_1, \\hat{y}_2, \\cdots, \\hat{y}_n \\}`
    - Residuals of the dependent variable: :math:`e_i = \\{ p_{1,y} - \\hat{y}_1, p_{2,y} - \\hat{y}_2, \\cdots, p_{n,y} - \\hat{y}_n \\}`
    - Deviations of the dependent variable: :math:`d_i = \\{ p_{1,y} - \\bar{y}, p_{2,y} - \\bar{y}, \\cdots, p_{n,y} - \\bar{y} \\}`
    - Sum of squares of residuals: :math:`SS_{res} = \\sum\\limits_{i=1}^n e_i^2`
    - Sum of squares of deviations: :math:`SS_{dev} = \\sum\\limits_{i=1}^n d_i^2`
    - Correlation coefficient for the logarithmic model: :math:`r = \\sqrt{1 - \\frac{SS_{res}}{SS_{dev}}}`
    - |regression_analysis|

    Examples
    --------
    Generate a logarithmic regression model for the data set [[1, 2], [2, 4.0794], [3, 5.2958], [4, 6.1589], [5, 6.8283], [6, 7.3753], [7, 7.8377], [8, 8.2383], [9, 8.5917], [10, 8.9078]], then print its coefficients, roots, total accumulation over its interquartile range, and correlation (and round the results to four decimal places)
        >>> model_perfect = logarithmic_model([[1, 2], [2, 4.0794], [3, 5.2958], [4, 6.1589], [5, 6.8283], [6, 7.3753], [7, 7.8377], [8, 8.2383], [9, 8.5917], [10, 8.9078]], 4)
        >>> print(model_perfect['constants'])
        [3.0, 2.0]
        >>> print(model_perfect['points']['roots'])
        [[0.5134, 0]]
        >>> print(model_perfect['accumulations']['iqr'])
        35.0191
        >>> print(model_perfect['correlation'])
        1.0
    Generate a logarithmic regression model for the data set [[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], then print its coefficients, inflections, total accumulation over its range, and correlation (and round the results to four decimal places)
        >>> model_agnostic = logarithmic_model([[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], 4)
        >>> print(model_agnostic['constants'])
        [7.4791, 22.5032]
        >>> print(model_agnostic['points']['inflections'])
        [None]
        >>> print(model_agnostic['accumulations']['range'])
        307.4295
        >>> print(model_agnostic['correlation'])
        0.5086
    """
    matrix_of_scalars(data, 'first')
    long_vector(data)
    positive_integer(precision)
    independent_variable = single_dimension(data, 1)
    dependent_variable = single_dimension(data, 2)
    filtered_independent = []
    for element in independent_variable:
        if element <= 0:
            filtered_independent.append(10**(-precision))
        else:
            filtered_independent.append(element)
    independent_matrix = []
    dependent_matrix = column_conversion(dependent_variable)
    for element in filtered_independent:
        independent_matrix.append([log(element), 1])
    solution = system_solution(independent_matrix, dependent_matrix, precision)
    equation = logarithmic_equation(*solution)
    derivative = logarithmic_derivatives(*solution)
    integral = logarithmic_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_coordinates('logarithmic', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulated_area(integral, min_value, max_value, precision)
    accumulated_iqr = accumulated_area(integral, q1, q3, precision)
    averages_range = average_values('logarithmic', equation, integral, min_value, max_value, solution, precision)
    averages_iqr = average_values('logarithmic', equation, integral, q1, q3, solution, precision)
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