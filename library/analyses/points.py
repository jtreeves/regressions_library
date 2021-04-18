from library.errors.analyses import select_equations, select_points
from library.errors.scalars import scalar_value, compare_scalars, positive_integer
from library.errors.vectors import vector_of_scalars, allow_none_vector
from library.errors.matrices import allow_none_matrix, allow_vector_matrix
from library.statistics.rounding import rounded_value, rounded_list
from library.statistics.sort import sorted_list, sorted_strings
from library.statistics.ranges import shift_into_range
from library.vectors.unify import unite_vectors
from library.vectors.separate import separate_elements
from library.vectors.generate import generate_elements
from .equations.linear import linear_equation
from .equations.quadratic import quadratic_equation
from .equations.cubic import cubic_equation
from .equations.hyperbolic import hyperbolic_equation
from .equations.exponential import exponential_equation
from .equations.logarithmic import logarithmic_equation
from .equations.logistic import logistic_equation
from .equations.sinusoidal import sinusoidal_equation
from .intercepts import intercept_points
from .extrema import extrema_points
from .inflections import inflection_points

def coordinate_pairs(equation_type, coefficients, inputs, point_type = 'point', precision = 4):
    # Handle input errors
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    allow_none_vector(inputs, 'third')
    select_points(point_type, 'fourth')
    positive_integer(precision)

    # Create equations for evaluating inputs (based on equation type)
    equation = lambda x : x
    if equation_type == 'linear':
        equation = linear_equation(*coefficients)
    elif equation_type == 'quadratic':
        equation = quadratic_equation(*coefficients)
    elif equation_type == 'cubic':
        equation = cubic_equation(*coefficients)
    elif equation_type == 'hyperbolic':
        equation = hyperbolic_equation(*coefficients)
    elif equation_type == 'exponential':
        equation = exponential_equation(*coefficients)
    elif equation_type == 'logarithmic':
        equation = logarithmic_equation(*coefficients)
    elif equation_type == 'logistic':
        equation = logistic_equation(*coefficients)
    elif equation_type == 'sinusoidal':
        equation = sinusoidal_equation(*coefficients)

    # Round inputs
    rounded_inputs = []
    for point in inputs:
        if isinstance(point, (int, float)):
            rounded_inputs.append(rounded_value(point, precision))
        else:
            rounded_inputs.append(point)

    # Create empty lists
    outputs = []
    coordinates = []
    
    # Handle no points
    if rounded_inputs[0] == None:
        coordinates.append(None)
    
    # Fill outputs list with output value at each input
    else:
        for value in rounded_inputs:
            # Circumvent inaccurate rounding
            if point_type == 'intercepts':
                outputs.append(0.0)
            
            # Evaluate function at inputs
            else:
                # Evaluate numerical inputs
                if isinstance(value, (int, float)):
                    output = equation(value)
                    rounded_output = rounded_value(output, precision)
                    outputs.append(rounded_output)
                
                # Handle non-numerical inputs
                else:
                    outputs.append(outputs[0])

        # Unite inputs and outputs for maxima into single list
        coordinates.extend(unite_vectors(rounded_inputs, outputs))
    
    # Return final coordinate pairs
    return coordinates

def key_coordinates(equation_type, coefficients, precision = 4):
    """
    Calculates the key points of a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which key points must be determined (e.g., 'linear', 'quadratic')
    coefficients : list
        Coefficients to use to generate the equation to investigate
    precision : int, default=4
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a 1-dimensional list containing elements that are integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    points['roots'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a root; second elements of those lists will be 0; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but general forms will also be included; if the function has no roots, then it will return a list of `None`
    points['maxima'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a relative maximum; second elements of those lists will be the y-coordinate of that maximum; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but a general form will also be included; if the function has no maxima, then it will return a list of `None`
    points['minima'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has a relative minimum; second elements of those lists will be the y-coordinate of that minimum; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but a general form will also be included; if the function has no minima, then it will return a list of `None`
    points['inflections'] : list
        List containing two-element lists for each point; first elements of those lists will be the value of the x-coordinate at which the original function has an inflection; second elements of those lists will be the y-coordinate of that inflection; if the function is sinusoidal, then only the initial results within a two period interval will be listed, but a general form will also be included; if the function has no inflection points, then it will return a list of `None`

    See Also
    --------
    - Roots for key functions: :func:`~library.analyses.roots.linear.linear_roots`, :func:`~library.analyses.roots.quadratic.quadratic_roots`, :func:`~library.analyses.roots.cubic.cubic_roots`, :func:`~library.analyses.roots.hyperbolic.hyperbolic_roots`, :func:`~library.analyses.roots.exponential.exponential_roots`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.analyses.roots.logistic.logistic_roots`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`
    - Graphical analysis: :func:`~library.analyses.criticals.critical_points`, :func:`~library.analyses.intervals.sign_chart`, :func:`~library.analyses.maxima.maxima_points`, :func:`~library.analyses.minima.minima_points`, :func:`~library.analyses.extrema.extrema_points`, :func:`~library.analyses.inflections.inflection_points`

    Notes
    -----
    - Key points include x-intercepts, maxima, minima, and points of inflection
    - |intercepts|
    - |extrema|
    - |inflections|

    Examples
    --------
    Calculate the key points of a cubic function with coefficients 1, -15, 63, and -7
        >>> points_cubic = key_coordinates('cubic', [1, -15, 63, -7])
        >>> print(points_cubic['roots'])
        [[0.1142, 0]]
        >>> print(points_cubic['maxima'])
        [[3.0, 74.0]]
        >>> print(points_cubic['minima'])
        [[7.0, 42.0]]
        >>> print(points_cubic['inflections'])
        [[5.0, 58.0]]
    Calculate the key points of a sinusoidal function with coefficients 2, 3, 5, and 1
        >>> points_sinusoidal = key_coordinates('sinusoidal', [2, 3, 5, 1])
        >>> print(points_sinusoidal['roots'])
        [[4.8255, 0], [6.2217, 0], [6.9199, 0], [8.3161, 0], [9.0143, 0], [10.4105, 0], ['4.8255 + 2.0944k', 0], ['6.2217 + 2.0944k', 0]]
        >>> print(points_sinusoidal['maxima'])
        [[5.5236, 3.0], [7.618, 3.0], [9.7124, 3.0], ['5.5236 + 2.0944k', 3.0]]
        >>> print(points_sinusoidal['minima'])
        [[6.5708, -1.0], [8.6652, -1.0], ['6.5708 + 2.0944k', -1.0]]
        >>> print(points_sinusoidal['inflections'])
        [[5, 1.0], [6.0472, 1.0], [7.0944, 1.0], [8.1416, 1.0], [9.1888, 1.0001], ['5 + 1.0472k', 1.0]]
    """
    # Handle input errors
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    positive_integer(precision)
    
    # Create lists of inputs
    intercepts_inputs = intercept_points(equation_type, coefficients, precision)
    extrema_inputs = extrema_points(equation_type, coefficients, precision)
    maxima_inputs = extrema_inputs['maxima']
    minima_inputs = extrema_inputs['minima']
    inflections_inputs = inflection_points(equation_type, coefficients, precision)

    # Generate coordinate pairs for all x-intercepts
    intercepts_coordinates = coordinate_pairs(equation_type, coefficients, intercepts_inputs, 'intercepts', precision)
    
    # Generate coordinate pairs for all maxima
    maxima_coordinates = coordinate_pairs(equation_type, coefficients, maxima_inputs, 'maxima', precision)
    
    # Generate coordinate pairs for all minima
    minima_coordinates = coordinate_pairs(equation_type, coefficients, minima_inputs, 'minima', precision)
    
    # Generate coordinate pairs for all points of inflection
    inflections_coordinates = coordinate_pairs(equation_type, coefficients, inflections_inputs, 'inflections', precision)
    
    # Create dictionary to return
    result = {
        'roots': intercepts_coordinates,
        'maxima': maxima_coordinates,
        'minima': minima_coordinates,
        'inflections': inflections_coordinates
    }
    return result

def points_within_range(points, start, end):
    # Handle input errors
    allow_none_vector(points, 'first')
    compare_scalars(start, end, 'second', 'third')

    # Separate numerical results from string results
    separated_results = separate_elements(points)
    numerical_results = separated_results['numerical']
    other_results = separated_results['other']

    # Eliminate numerical results outside of range
    selected_results = [x for x in numerical_results if x >= start and x <= end]

    # Create list to return
    final_results = []

    # Handle no results
    if not selected_results and not other_results:
        final_results.append(None)
    
    # Handle general case
    else:
        final_results.extend(selected_results + other_results)
    
    # Return results
    return final_results

def shifted_points_within_range(points, minimum, maximum, precision = 4):
    # Handle input errors
    allow_vector_matrix(points, 'first')
    compare_scalars(minimum, maximum, 'second', 'third')
    positive_integer(precision)

    # Grab general points
    general_points = []
    for point in points:
        # Handle coordinate pairs
        if isinstance(point, list):
            if isinstance(point[0], str):
                general_points.append(point[0])
        
        # Handle single coordinates
        else:
            if isinstance(point, str):
                general_points.append(point)
    
    # Generate options for inputs
    optional_points = []
    for point in general_points:
        # Grab initial value and periodic unit
        initial_value_index = point.find(' + ')
        initial_value = float(point[:initial_value_index])
        periodic_unit_index = initial_value_index + 3
        periodic_unit = float(point[periodic_unit_index:-1])
        
        # Increase or decrease initial value to fit into range
        alternative_initial_value = shift_into_range(initial_value, periodic_unit, minimum, maximum)
        
        # Generate additional values within range
        generated_elements = generate_elements(alternative_initial_value, periodic_unit, precision)
        optional_points += generated_elements
    
    # Separate numerical inputs from string inputs
    separated_points = separate_elements(optional_points)
    numerical_points = separated_points['numerical']
    other_points = separated_points['other']

    # Sort numerical inputs
    sorted_points = sorted_list(numerical_points)

    # Reduce numerical inputs to within a given range
    selected_points = [x for x in sorted_points if x >= minimum and x <= maximum]
    
    # Round numerical inputs
    rounded_points = rounded_list(selected_points, precision)
    
    # Sort string inputs
    sorted_other_points = sorted_strings(other_points)
    
    # Combine numerical and string inputs
    result = rounded_points + sorted_other_points
    return result

def shifted_coordinates_within_range(coordinates, minimum, maximum, precision = 4):
    # Handle input errors
    allow_none_matrix(coordinates, 'first')
    compare_scalars(minimum, maximum, 'second', 'third')
    positive_integer(precision)

    # Create list to return
    result = []

    # Handle general case
    if coordinates[0] is not None:
        # Generate inputs
        input_points = shifted_points_within_range(coordinates, minimum, maximum, precision)
        
        # Generate outputs
        output_points = []
        for point in input_points:
            output_points.append(coordinates[0][1])
        
        # Unite inputs and outputs into single list
        result = unite_vectors(input_points, output_points)
    
    # Handle no points
    else:
        result = coordinates
    
    # Return result
    return result