from math import log, exp, acos, pi
from library.errors.analyses import callable_function, select_equations
from library.errors.scalars import compare_scalars, positive_integer
from library.errors.vectors import vector_of_scalars
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value
from .roots.linear import linear_roots
from .roots.quadratic import quadratic_roots
from .roots.cubic import cubic_roots
from .roots.hyperbolic import hyperbolic_roots
from .roots.logarithmic import logarithmic_roots
from .roots.sinusoidal import sinusoidal_roots
from .accumulation import accumulated_area

def average_value_derivative(equation, start, end, precision):
    """
    Evaluates the average rate of change between two points for a given function

    Parameters
    ----------
    equation : function
        Function to use for evaluating the average rate of change
    start : int or float
        Value of the x-coordinate of the first point to use for evaluating the rate of change
    end : int or float
        Value of the x-coordinate of the second point to use for evaluating the rate of change
    precision : int
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    TypeError
        First argument must be a callable function
    TypeError
        Second and third arguments must be integers or floats
    ValueError
        Second argument must be less than third argument
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    average : float
        Slope of a function between two points

    Examples
    --------
    Evaluate the average rate of change of a cubic function with coefficients 2, 3, 5, and 7 between end points of 10 and 20 (and round the result to four decimal places)
        >>> average_cubic = average_value_derivative(lambda x : 2 * x**3 + 3 * x**2 + 5 * x + 7, 10, 20, 4)
        >>> print(average_cubic)
        1495.0
    Evaluate the average rate of change of a sinusoidal function with coefficients 2, 3, 5, and 7 between end points of 10 and 20 (and round the result to four decimal places)
        >>> average_sinusoidal = average_value_derivative(lambda x : 2 * sin(3 * (x - 5)) + 7, 10, 20, 4)
        >>> print(average_sinusoidal)
        0.0401
    """
    callable_function(equation, 'first')
    compare_scalars(start, end, 'second', 'third')
    positive_integer(precision)
    vertical_change = equation(end) - equation(start)
    horizontal_change = end - start
    ratio = vertical_change / horizontal_change
    result = rounded_value(ratio, precision)
    return result

def mean_values_derivative(equation_type, equation, start, end, constants, precision):
    """
    Generates a list of all the x-coordinates whose instantaneous rates of change equal the function's average rate of change between two points

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which an average value must be determined (e.g., 'linear', 'quadratic')
    equation : function
        Function to use for evaluating the average rate of change
    start : int or float
        Value of the x-coordinate of the first point to use for evaluating the rate of change; all results must be greater than this value
    end : int or float
        Value of the x-coordinate of the second point to use for evaluating the rate of change; all results must be less than this value
    constants : list or tuple
        Coefficients to use to generate the equation to investigate
    precision : int
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a callable function
    TypeError
        Third and fourth arguments must be integers or floats
    ValueError
        Third argument must be less than fourth argument
    TypeError
        Fifth argument must be a 1-dimensional list or tuple containing elements that are integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points : list
        Values of the x-coordinates within the specified interval at which the original function has an instantaneous rate of change equal to its average rate of change over that entire interval; if the function is sinusoidal, then only the initial results within at most a two period interval within the specified interval will be listed, but general forms will also be included (however, their results may be outside the specified interval; see `sinusoidal_roots`); if the algorithm cannot determine any values, then it will return a list of `None`

    Examples
    --------
    Generate a list of all the x-coordinates whose instantaneous rates of change equal the function's average rate of change for a cubic function with coefficients 2, 3, 5, and 7 between end points of 10 and 20 (and round the result to four decimal places)
        >>> points_cubic = mean_values_derivative('cubic', lambda x : 2 * x**3 + 3 * x**2 + 5 * x + 7, 10, 20, [2, 3, 5, 7], 4)
        >>> print(points_cubic)
        [15.2665]
    Generate a list of all the x-coordinates whose instantaneous rates of change equal the function's average rate of change for a cubic function with coefficients 2, 3, 5, and 7 between end points of 10 and 20 (and round the result to four decimal places)
        >>> points_sinusoidal = mean_values_derivative('sinusoidal', lambda x : 2 * sin(3 * (x - 5)) + 7, 10, 20, [2, 3, 5, 7], 4)
        >>> print(points_sinusoidal)
        [10.7618, 11.8046, 12.8562, 13.899, 14.9506, 15.9933, '10.7618 + 2.0944k', '11.8046 + 2.0944k']
    """
    select_equations(equation_type)
    callable_function(equation, 'second')
    compare_scalars(start, end, 'third', 'fourth')
    vector_of_scalars(constants, 'fifth')
    positive_integer(precision)
    result = []
    average = average_value_derivative(equation, start, end, precision)
    if equation_type == 'linear':
        result.append('All')
        return result
    elif equation_type == 'quadratic':
        value = linear_roots(2 * constants[0], constants[1] -  average, precision)
        result = value
    elif equation_type == 'cubic':
        values = quadratic_roots(3 * constants[0], 2 * constants[1], constants[2] - average, precision)
        result = values
    elif equation_type == 'hyperbolic':
        ratio = -1 * constants[0] / average
        root = ratio ** (1/2)
        first_value = root
        second_value = -1 * root
        result.extend([first_value, second_value])
    elif equation_type == 'exponential':
        base_log = log(constants[1])
        numerator = log(average / (constants[0] * base_log))
        denominator = base_log
        value = numerator / denominator
        result.append(value)
    elif equation_type == 'logarithmic':
        value = hyperbolic_roots(constants[0], -1 * average, precision)
        result = value
    elif equation_type == 'logistic':
        quadratic_values = quadratic_roots(average, 2 * average - constants[0] * constants[1], average, precision)
        if quadratic_values[0] == None:
            result = [None]
            return result
        else:
            values = []
            for value in quadratic_values:
                if value <= 0:
                    values.append(constants[2] - log(10**(-precision)) / constants[1])
                else:
                    values.append(constants[2] - log(value) / constants[1])
            result = values
    elif equation_type == 'sinusoidal':
        ratio = average / (constants[0] * constants[1])
        radians = acos(ratio)
        periodic_radians = radians / constants[1]
        if ratio == 0:
            periodic_unit = pi / constants[1]
            initial_value = constants[2] + periodic_radians
            if periodic_unit > 0:
                while initial_value > end:
                    initial_value -= periodic_unit
                while initial_value < start:
                    initial_value += periodic_unit
            else:
                while initial_value > end:
                    initial_value += periodic_unit
                while initial_value < start:
                    initial_value -= periodic_unit
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            result = [initial_value, first_value, second_value, third_value, fourth_value, general_form]
        elif ratio == 1 or ratio == -1:
            periodic_unit = 2 * pi / constants[1]
            initial_value = constants[2] + periodic_radians
            if periodic_unit > 0:
                while initial_value > end:
                    initial_value -= periodic_unit
                while initial_value < start:
                    initial_value += periodic_unit
            else:
                while initial_value > end:
                    initial_value += periodic_unit
                while initial_value < start:
                    initial_value -= periodic_unit
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            result = [initial_value, first_value, second_value, general_form]
        else:
            periodic_unit = 2 * pi / constants[1]
            initial_value = constants[2] + periodic_radians
            if periodic_unit > 0:
                while initial_value > end:
                    initial_value -= periodic_unit
                while initial_value < start:
                    initial_value += periodic_unit
            else:
                while initial_value > end:
                    initial_value += periodic_unit
                while initial_value < start:
                    initial_value -= periodic_unit
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            alternative_initial_value = constants[2] + 2 * pi / constants[1] - periodic_radians
            if periodic_unit > 0:
                while alternative_initial_value > end:
                    alternative_initial_value -= periodic_unit
                while alternative_initial_value < start:
                    alternative_initial_value += periodic_unit
            else:
                while alternative_initial_value > end:
                    alternative_initial_value += periodic_unit
                while alternative_initial_value < start:
                    alternative_initial_value -= periodic_unit
            alternative_first_value = alternative_initial_value + 1 * periodic_unit
            alternative_second_value = alternative_initial_value + 2 * periodic_unit
            rounded_alternative_initial_value = rounded_value(alternative_initial_value, precision)
            alternative_general_form = str(rounded_alternative_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            result = [initial_value, first_value, second_value, alternative_initial_value, alternative_first_value, alternative_second_value, general_form, alternative_general_form]
    if not result:
        result = [None]
        return result
    numerical_results = []
    other_results = []
    for item in result:
        if isinstance(item, (int, float)):
            numerical_results.append(item)
        else:
            other_results.append(item)
    selected_results = [x for x in numerical_results if x > start and x < end]
    if not selected_results:
        final = [None]
        return final
    sorted_results = sorted_list(selected_results)
    rounded_results = []
    for number in sorted_results:
        rounded_results.append(rounded_value(number, precision))
    sorted_other_results = []
    if len(other_results) > 0:
        if len(other_results) == 1:
            sorted_other_results = other_results
        else:
            first_index = other_results[0].find(' + ') - 1
            first_value = float(other_results[0][:first_index])
            second_index = other_results[1].find(' + ') - 1
            second_value = float(other_results[1][:second_index])
            if first_value < second_value:
                sorted_other_results = other_results
            else:
                sorted_other_results = [other_results[1], other_results[0]]
    final_result = rounded_results + sorted_other_results
    return final_result

def average_value_integral(equation, start, end, precision):
    """
    Evaluates the average value of a given function between two points

    Parameters
    ----------
    equation : function
        Integral of the function for which one seeks the average value
    start : int or float
        Value of the x-coordinate of the first point to use for evaluating the average value
    end : int or float
        Value of the x-coordinate of the second point to use for evaluating the average value
    precision : int
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    TypeError
        First argument must be a callable function
    TypeError
        Second and third arguments must be integers or floats
    ValueError
        Second argument must be less than third argument
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    average : float
        Average value of the function between two points

    Examples
    --------
    Evaluate the average value of a cubic function with coefficients 2, 3, 5, and 7 between end points of 10 and 20 (and round the result to four decimal places)
        >>> average_cubic = average_value_integral(lambda x : 0.5 * x**4 + x**3 + 2.5 * x**2 + 7 * x, 10, 20, 4)
        >>> print(average_cubic)
        8282.0
    Evaluate the average value of a sinusoidal function with coefficients 2, 3, 5, and 7 between end points of 10 and 20 (and round the result to four decimal places)
        >>> average_sinusoidal = average_value_integral(lambda x : -2 / 3 * cos(3 * (x - 5)) + 7 * x, 10, 20, 4)
        >>> print(average_sinusoidal)
        6.9143
    """
    callable_function(equation, 'first')
    compare_scalars(start, end, 'second', 'third')
    positive_integer(precision)
    accumulated_value = accumulated_area(equation, start, end, precision)
    change = end - start
    ratio = accumulated_value / change
    result = rounded_value(ratio, precision)
    return result

def mean_values_integral(equation_type, equation, start, end, constants, precision):
    """
    Generates a list of all the x-coordinates between two points at which a function's value will equal its average value over that interval

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which an average value must be determined (e.g., 'linear', 'quadratic')
    equation : function
        Integral of the function for which one seeks the average value
    start : int or float
        Value of the x-coordinate of the first point to use for evaluating the average value; all results must be greater than this value
    end : int or float
        Value of the x-coordinate of the second point to use for evaluating the average value; all results must be less than this value
    constants : list or tuple
        Coefficients of the origianl function under investigation
    precision : int
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a callable function
    TypeError
        Third and fourth arguments must be integers or floats
    ValueError
        Third argument must be less than fourth argument
    TypeError
        Fifth argument must be a 1-dimensional list or tuple containing elements that are integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points : list
        Values of the x-coordinates within the specified interval at which the original function has a value equal to its average value over that entire interval; if the function is sinusoidal, then only the initial results within at most a two period interval within the specified interval will be listed, but general forms will also be included (however, their results may be outside the specified interval; see `sinusoidal_roots`); if the algorithm cannot determine any values, then it will return a list of `None`

    Examples
    --------
    Generate a list of all the x-coordinates of a cubic function with coefficients 2, 3, 5, and 7 at which the function's value will equal its average value between 10 and 20 (and round the result to four decimal places)
        >>> points_cubic = mean_values_integral('cubic', lambda x : 0.5 * x**4 + x**3 + 2.5 * x**2 + 7 * x, 10, 20, [2, 3, 5, 7], 4)
        >>> print(points_cubic)
        [15.5188]
    Generate a list of all the x-coordinates of a sinusoidal function with coefficients 2, 3, 5, and 7 at which the function's value will equal its average value between 10 and 20 (and round the result to four decimal places)
        >>> points_sinusoidal = mean_values_integral('sinusoidal', lambda x : -2 / 3 * cos(3 * (x - 5)) + 7 * x, 10, 20, [2, 3, 5, 7], 4)
        >>> print(points_sinusoidal)
        [10.2503, 11.2689, 12.3447, 13.3633, 14.4391, 15.4577, 16.5335, 17.5521, 18.6279, 19.6465, '10.2503 + 2.0944k', '11.2689 + 2.0944k']
    """
    select_equations(equation_type)
    callable_function(equation, 'second')
    compare_scalars(start, end, 'third', 'fourth')
    vector_of_scalars(constants, 'fifth')
    positive_integer(precision)
    result = []
    average = average_value_integral(equation, start, end, precision)
    if equation_type == 'linear':
        value = linear_roots(constants[0], constants[1] - average, precision)
        result = value
    elif equation_type == 'quadratic':
        values = quadratic_roots(constants[0], constants[1], constants[2] - average, precision)
        result = values
    elif equation_type == 'cubic':
        values = cubic_roots(constants[0], constants[1], constants[2], constants[3] - average, precision)
        result = values
    elif equation_type == 'hyperbolic':
        value = hyperbolic_roots(constants[0], constants[1] - average, precision)
        result = value
    elif equation_type == 'exponential':
        value = log(average / constants[0]) / log(constants[1])
        result.append(value)
    elif equation_type == 'logarithmic':
        value = logarithmic_roots(constants[0], constants[1] - average, precision)
        result = value
    elif equation_type == 'logistic':
        ratio = constants[0] / average
        if ratio <= 1:
            pass
        else:
            value = constants[2] - log(ratio - 1) / constants[1]
            result.append(value)
    elif equation_type == 'sinusoidal':
        values = sinusoidal_roots(constants[0], constants[1], constants[2], constants[3] - average, precision)
        general_forms = []
        for value in values:
            if isinstance(value, str):
                general_forms.append(value)
        options = []
        for form in general_forms:
            initial_value_index = form.find(' + ')
            initial_value = float(form[:initial_value_index])
            periodic_unit_index = initial_value_index + 3
            periodic_unit = float(form[periodic_unit_index:-1])
            if periodic_unit > 0:
                while initial_value > end:
                    initial_value -= periodic_unit
                while initial_value < start:
                    initial_value += periodic_unit
            else:
                while initial_value > end:
                    initial_value += periodic_unit
                while initial_value < start:
                    initial_value -= periodic_unit
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            options += [initial_value, first_value, second_value, third_value, fourth_value, general_form]
        result = options
    if not result:
        result = [None]
        return result
    numerical_results = []
    other_results = []
    for item in result:
        if isinstance(item, (int, float)):
            numerical_results.append(item)
        else:
            other_results.append(item)
    selected_results = [x for x in numerical_results if x > start and x < end]
    if not selected_results:
        final = [None]
        return final
    sorted_results = sorted_list(selected_results)
    rounded_results = []
    for number in sorted_results:
        rounded_results.append(rounded_value(number, precision))
    sorted_other_results = []
    if len(other_results) > 0:
        if len(other_results) == 1:
            sorted_other_results = other_results
        else:
            first_index = other_results[0].find(' + ') - 1
            first_value = float(other_results[0][:first_index])
            second_index = other_results[1].find(' + ') - 1
            second_value = float(other_results[1][:second_index])
            if first_value < second_value:
                sorted_other_results = other_results
            else:
                sorted_other_results = [other_results[1], other_results[0]]
    final_result = rounded_results + sorted_other_results
    return final_result

def average_values(equation_type, equation, integral, start, end, constants, precision):
    """
    Calculates the average values for a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which average values must be determined (e.g., 'linear', 'quadratic')
    equation : function
        Equation of the function for which one seeks the average values
    integral : function
        Integral of the function for which one seeks the average values
    start : int or float
        Value of the x-coordinate of the first point to use for evaluating the average values; results within lists must be greater than this value
    end : int or float
        Value of the x-coordinate of the second point to use for evaluating the average values; results within lists must be less than this value
    constants : list or tuple
        Coefficients of the origianl function under investigation
    precision : int
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second and third arguments must be callable functions
    TypeError
        Fourth and fifth arguments must be integers or floats
    ValueError
        Fourth argument must be less than fifth argument
    TypeError
        Sixth argument must be a 1-dimensional list or tuple containing elements that are integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    averages['average_value_derivative'] : float
        Slope of a function between two points
    averages['mean_values_derivative'] : list
        Values of the x-coordinates within the specified interval at which the original function has a value equal to its average value over that entire interval; if the function is sinusoidal, then only the initial results within at most a two period interval within the specified interval will be listed, but general forms will also be included (however, their results may be outside the specified interval; see `sinusoidal_roots`); if the algorithm cannot determine any values, then it will return a list of `None`
    averages['average_value_integral'] : float
        Average value of the function between two points
    averages['mean_values_integral'] : list
        Values of the x-coordinates within the specified interval at which the original function has a value equal to its average value over that entire interval; if the function is sinusoidal, then only the initial results within at most a two period interval within the specified interval will be listed, but general forms will also be included (however, their results may be outside the specified interval; see `sinusoidal_roots`); if the algorithm cannot determine any values, then it will return a list of `None`

    Examples
    --------
    Calculate the averages of a cubic function with coefficients 2, 3, 5, and 7 between 10 and 20 (and round the result to four decimal places)
        >>> averages_cubic = average_values('cubic', lambda x : 2 * x**3 + 3 * x**2 + 5 * x + 7, lambda x : 0.5 * x**4 + x**3 + 2.5 * x**2 + 7 * x, 10, 20, [2, 3, 5, 7], 4)
        >>> print(averages_cubic['average_value_derivative'])
        1495.0
        >>> print(averages_cubic['mean_values_derivative'])
        [15.2665]
        >>> print(averages_cubic['average_value_integral'])
        8282.0
        >>> print(averages_cubic['mean_values_integral'])
        [15.5188]
    Calculate the averages of a sinusoidal function with coefficients 2, 3, 5, and 7 between 10 and 20 (and round the result to four decimal places)
        >>> averages_sinusoidal = average_values('sinusoidal', lambda x : 2 * sin(3 * (x - 5)) + 7, lambda x : -2 / 3 * cos(3 * (x - 5)) + 7 * x, 10, 20, [2, 3, 5, 7], 4)
        >>> print(averages_sinusoidal['average_value_derivative'])
        0.0401
        >>> print(averages_sinusoidal['mean_values_derivative'])
        [10.7618, 11.8046, 12.8562, 13.899, 14.9506, 15.9933, '10.7618 + 2.0944k', '11.8046 + 2.0944k']
        >>> print(averages_sinusoidal['average_value_integral'])
        6.9143
        >>> print(averages_sinusoidal['mean_values_integral'])
        [10.2503, 11.2689, 12.3447, 13.3633, 14.4391, 15.4577, 16.5335, 17.5521, 18.6279, 19.6465, '10.2503 + 2.0944k', '11.2689 + 2.0944k']
    """
    select_equations(equation_type)
    callable_function(equation, 'second')
    callable_function(integral, 'third')
    compare_scalars(start, end, 'fourth', 'fifth')
    vector_of_scalars(constants, 'sixth')
    positive_integer(precision)
    derivative_value = average_value_derivative(equation, start, end, precision)
    derivative_inputs = mean_values_derivative(equation_type, equation, start, end, constants, precision)
    integral_value = average_value_integral(integral, start, end, precision)
    integral_inputs = mean_values_integral(equation_type, integral, start, end, constants, precision)
    results = {
        'average_value_derivative': derivative_value,
        'mean_values_derivative': derivative_inputs,
        'average_value_integral': integral_value,
        'mean_values_integral': integral_inputs
    }
    return results