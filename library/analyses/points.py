from library.errors.analyses import select_equations, callable_function
from library.errors.scalars import positive_integer
from library.errors.vectors import vector_of_scalars
from library.statistics.rounding import rounded_value
from library.vectors.unify import unite_vectors
from .intercepts import intercept_points
from .extrema import extrema_points
from .inflections import inflection_points

def key_coordinates(equation_type, coefficients, equation, first_derivative, second_derivative, precision):
    """
    Calculates the key points of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which extrema must be determined (e.g., 'linear', 'quadratic')
    coefficients : list or tuple
        Coefficients to use to generate the equation to investigate
    equation : function
        Function to use for evaluating the y-coordinates of each point
    first_derivative : function
        Function of the first derivative to use for generating a list of critical points
    second_derivative : function
        Function of the second derivative to use for generating a list of critical points
    precision : int
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a 1-dimensional list or tuple containing elements that are integers or floats
    TypeError
        Third, fourth, and fifth arguments must be callable functions
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points['roots'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a root; second elements of those lists will be 0; if the function has no roots, then it will return a list of `None`
    points['maxima'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a relative maximum; second elements of those lists will be the y-coordinate of that maximum; if the function has no maxima, then it will return a list of `None`
    points['minima'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a relative minimum; second elements of those lists will be the y-coordinate of that minimum; if the function has no minima, then it will return a list of `None`
    points['inflections'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has an inflection; second elements of those lists will be the y-coordinate of that inflection; if the function has no inflection points, then it will return a list of `None`

    Examples
    --------
    Calculate the key points of a cubic function with coefficients 1, -15, 63, and -7 (and round the results to four decimal places)
        >>> test = key_coordinates('cubic', [1, -15, 63, -7], lambda x : x**3 - 15 * x**2 + 63 * x - 7, lambda x : 3 * x**2 - 30 * x + 63, lambda x : 6 * x - 30, 4)
    Print results
        >>> print(test['roots'])
        [[0.1142, 0]]
        >>> print(test['maxima'])
        [[3.0, 74.0]]
        >>> print(test['minima'])
        [[7.0, 42.0]]
        >>> print(test['inflections'])
        [[5.0, 58.0]]
    """
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    callable_function(equation, 'third')
    callable_function(first_derivative, 'fourth')
    callable_function(second_derivative, 'fifth')
    positive_integer(precision)
    intercepts_inputs = intercept_points(equation_type, coefficients, precision)
    extrema_inputs = extrema_points(equation_type, coefficients, first_derivative, precision)
    maxima_inputs = extrema_inputs['maxima']
    minima_inputs = extrema_inputs['minima']
    inflections_inputs = inflection_points(equation_type, coefficients, second_derivative, precision)
    intercepts_outputs = []
    maxima_outputs = []
    minima_outputs = []
    inflections_outputs = []
    intercepts_coordinates = []
    maxima_coordinates = []
    minima_coordinates = []
    inflections_coordinates = []
    if intercepts_inputs[0] == None:
        intercepts_coordinates = [None]
    else:
        for intercept in intercepts_inputs:
            intercepts_outputs.append(0)
        intercepts_coordinates = unite_vectors(intercepts_inputs, intercepts_outputs)
    if maxima_inputs[0] == None:
        maxima_coordinates = [None]
    else:
        for i in range(len(maxima_inputs)):
            if isinstance(maxima_inputs[i], (int, float)):
                output = equation(maxima_inputs[i])
                rounded_output = rounded_value(output, precision)
                maxima_outputs.append(rounded_output)
            else:
                periodic_unit = 2 * float(maxima_inputs[i][:-1])
                initial_value = maxima_inputs[0]
                general_form = str(initial_value) + ' + ' + str(periodic_unit) + 'k'
                maxima_inputs[i] = general_form
                maxima_outputs.append(maxima_outputs[0])
        maxima_coordinates = unite_vectors(maxima_inputs, maxima_outputs)
    if minima_inputs[0] == None:
        minima_coordinates = [None]
    else:
        for i in range(len(minima_inputs)):
            if isinstance(minima_inputs[i], (int, float)):
                output = equation(minima_inputs[i])
                rounded_output = rounded_value(output, precision)
                minima_outputs.append(rounded_output)
            else:
                periodic_unit = 2 * float(minima_inputs[i][:-1])
                initial_value = minima_inputs[0]
                general_form = str(initial_value) + ' + ' + str(periodic_unit) + 'k'
                minima_inputs[i] = general_form
                minima_outputs.append(minima_outputs[0])
        minima_coordinates = unite_vectors(minima_inputs, minima_outputs)
    if inflections_inputs[0] == None:
        inflections_coordinates = [None]
    else:
        for inflection in inflections_inputs:
            if isinstance(inflection, (int, float)):
                output = equation(inflection)
                rounded_output = rounded_value(output, precision)
                inflections_outputs.append(rounded_output)
            else:
                inflections_outputs.append(inflections_outputs[0])
        inflections_coordinates = unite_vectors(inflections_inputs, inflections_outputs)
    result = {
        'roots': intercepts_coordinates,
        'maxima': maxima_coordinates,
        'minima': minima_coordinates,
        'inflections': inflections_coordinates
    }
    return result