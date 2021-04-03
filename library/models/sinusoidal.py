from math import pi
from numpy import sin, inf
from scipy.optimize import curve_fit
from library.errors.matrices import matrix_of_scalars
from library.errors.vectors import long_vector
from library.errors.scalars import positive_integer
from library.vectors.dimension import single_dimension
from library.vectors.unify import unite_vectors
from library.analyses.equations.sinusoidal import sinusoidal_equation
from library.analyses.derivatives.sinusoidal import sinusoidal_derivatives
from library.analyses.integrals.sinusoidal import sinusoidal_integral
from library.analyses.points import key_coordinates
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values
from library.statistics.halve import half_dimension
from library.statistics.mean import mean_value
from library.statistics.summary import five_number_summary
from library.statistics.sort import sorted_list
from library.statistics.correlation import correlation_coefficient
from library.statistics.rounding import rounded_value

def sinusoidal_model(data, precision):
    matrix_of_scalars(data, 'first')
    long_vector(data)
    positive_integer(precision)
    independent_variable = single_dimension(data, 1)
    dependent_variable = single_dimension(data, 2)
    independent_max = max(independent_variable)
    independent_min = min(independent_variable)
    independent_range = independent_max - independent_min
    dependent_max = max(dependent_variable)
    dependent_min = min(dependent_variable)
    dependent_range = dependent_max - dependent_min
    solution = []
    def sinusoidal_fit(variable, first_constant, second_constant, third_constant, fourth_constant):
        evaluation = first_constant * sin(second_constant * (variable - third_constant)) + fourth_constant
        return evaluation
    try:
        parameters, covariance = curve_fit(sinusoidal_fit, independent_variable, dependent_variable, bounds=[(-dependent_range, -inf, -independent_range, dependent_min), (dependent_range, inf, independent_range, dependent_max)])
        solution = list(parameters)
    except RuntimeError:
        parameters, covariance = curve_fit(sinusoidal_fit, independent_variable, dependent_variable, bounds=[(dependent_range - 1, -independent_range, -independent_range, dependent_min), (dependent_range + 1, independent_range, independent_range, dependent_max)])
        solution = list(parameters)
    constants = []
    for number in solution:
        constants.append(rounded_value(number, precision))
    equation = sinusoidal_equation(*solution)
    derivative = sinusoidal_derivatives(*solution)
    integral = sinusoidal_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_coordinates('sinusoidal', solution, equation, first_derivative, second_derivative, precision)
    period = abs(2 * pi / solution[1])
    interval = 2 * period
    final_roots = []
    if points['roots'][0] is not None:
        general_roots = []
        for root in points['roots']:
            if isinstance(root[0], str):
                general_roots.append(root[0])
        optional_roots = []
        for root in general_roots:
            initial_value_index = root.find(' + ')
            initial_value = float(root[:initial_value_index])
            periodic_unit_index = initial_value_index + 3
            periodic_unit = float(root[periodic_unit_index:-1])
            if periodic_unit > 0:
                while initial_value > independent_max:
                    initial_value -= periodic_unit
                while initial_value < independent_min:
                    initial_value += periodic_unit
            else:
                while initial_value > independent_max:
                    initial_value += periodic_unit
                while initial_value < independent_min:
                    initial_value -= periodic_unit
            first_value = initial_value + 1 * periodic_unit
            second_value = initial_value + 2 * periodic_unit
            third_value = initial_value + 3 * periodic_unit
            fourth_value = initial_value + 4 * periodic_unit
            rounded_initial_value = rounded_value(initial_value, precision)
            rounded_periodic_unit = rounded_value(periodic_unit, precision)
            general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
            optional_roots += [initial_value, first_value, second_value, third_value, fourth_value, general_form]
        numerical_roots = []
        other_roots = []
        for root in optional_roots:
            if isinstance(root, (int, float)):
                numerical_roots.append(root)
            else:
                other_roots.append(root)
        sorted_roots = sorted_list(numerical_roots)
        selected_roots = [x for x in sorted_roots if x >= sorted_roots[0] and x <= sorted_roots[0] + interval]
        rounded_roots = []
        for root in selected_roots:
            rounded_roots.append(rounded_value(root, precision))
        sorted_other_roots = []
        if len(other_roots) > 0:
            if len(other_roots) == 1:
                sorted_other_roots = other_roots
            else:
                first_index = other_roots[0].find(' + ') - 1
                first_value = float(other_roots[0][:first_index])
                second_index = other_roots[1].find(' + ') - 1
                second_value = float(other_roots[1][:second_index])
                if first_value < second_value:
                    sorted_other_roots = other_roots
                else:
                    sorted_other_roots = [other_roots[1], other_roots[0]]
        input_roots = rounded_roots + sorted_other_roots
        output_roots = []
        for root in input_roots:
            output_roots.append(points['roots'][0][1])
        final_roots = unite_vectors(input_roots, output_roots)
    else:
        final_roots = points['roots']
    general_maxima = []
    for point in points['maxima']:
        if isinstance(point[0], str):
            general_maxima.append(point[0])
    optional_maxima = []
    for point in general_maxima:
        initial_value_index = point.find(' + ')
        initial_value = float(point[:initial_value_index])
        periodic_unit_index = initial_value_index + 3
        periodic_unit = float(point[periodic_unit_index:-1])
        if periodic_unit > 0:
            while initial_value > independent_max:
                initial_value -= periodic_unit
            while initial_value < independent_min:
                initial_value += periodic_unit
        else:
            while initial_value > independent_max:
                initial_value += periodic_unit
            while initial_value < independent_min:
                initial_value -= periodic_unit
        first_value = initial_value + 1 * periodic_unit
        second_value = initial_value + 2 * periodic_unit
        third_value = initial_value + 3 * periodic_unit
        fourth_value = initial_value + 4 * periodic_unit
        rounded_initial_value = rounded_value(initial_value, precision)
        rounded_periodic_unit = rounded_value(periodic_unit, precision)
        general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
        optional_maxima += [initial_value, first_value, second_value, third_value, fourth_value, general_form]
    numerical_maxima = []
    other_maxima = []
    for point in optional_maxima:
        if isinstance(point, (int, float)):
            numerical_maxima.append(point)
        else:
            other_maxima.append(point)
    sorted_maxima = sorted_list(numerical_maxima)
    selected_maxima = [x for x in sorted_maxima if x >= sorted_maxima[0] and x <= sorted_maxima[0] + interval]
    rounded_maxima = []
    for point in selected_maxima:
        rounded_maxima.append(rounded_value(point, precision))
    sorted_other_maxima = []
    if len(other_maxima) > 0:
        if len(other_maxima) == 1:
            sorted_other_maxima = other_maxima
        else:
            first_index = other_maxima[0].find(' + ') - 1
            first_value = float(other_maxima[0][:first_index])
            second_index = other_maxima[1].find(' + ') - 1
            second_value = float(other_maxima[1][:second_index])
            if first_value < second_value:
                sorted_other_maxima = other_maxima
            else:
                sorted_other_maxima = [other_maxima[1], other_maxima[0]]
    input_maxima = rounded_maxima + sorted_other_maxima
    output_maxima = []
    for point in input_maxima:
        output_maxima.append(points['maxima'][0][1])
    final_maxima = unite_vectors(input_maxima, output_maxima)
    general_minima = []
    for point in points['minima']:
        if isinstance(point[0], str):
            general_minima.append(point[0])
    optional_minima = []
    for point in general_minima:
        initial_value_index = point.find(' + ')
        initial_value = float(point[:initial_value_index])
        periodic_unit_index = initial_value_index + 3
        periodic_unit = float(point[periodic_unit_index:-1])
        if periodic_unit > 0:
            while initial_value > independent_max:
                initial_value -= periodic_unit
            while initial_value < independent_min:
                initial_value += periodic_unit
        else:
            while initial_value > independent_max:
                initial_value += periodic_unit
            while initial_value < independent_min:
                initial_value -= periodic_unit
        first_value = initial_value + 1 * periodic_unit
        second_value = initial_value + 2 * periodic_unit
        third_value = initial_value + 3 * periodic_unit
        fourth_value = initial_value + 4 * periodic_unit
        rounded_initial_value = rounded_value(initial_value, precision)
        rounded_periodic_unit = rounded_value(periodic_unit, precision)
        general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
        optional_minima += [initial_value, first_value, second_value, third_value, fourth_value, general_form]
    numerical_minima = []
    other_minima = []
    for point in optional_minima:
        if isinstance(point, (int, float)):
            numerical_minima.append(point)
        else:
            other_minima.append(point)
    sorted_minima = sorted_list(numerical_minima)
    selected_minima = [x for x in sorted_minima if x >= sorted_minima[0] and x <= sorted_minima[0] + interval]
    rounded_minima = []
    for point in selected_minima:
        rounded_minima.append(rounded_value(point, precision))
    sorted_other_minima = []
    if len(other_minima) > 0:
        if len(other_minima) == 1:
            sorted_other_minima = other_minima
        else:
            first_index = other_minima[0].find(' + ') - 1
            first_value = float(other_minima[0][:first_index])
            second_index = other_minima[1].find(' + ') - 1
            second_value = float(other_minima[1][:second_index])
            if first_value < second_value:
                sorted_other_minima = other_minima
            else:
                sorted_other_minima = [other_minima[1], other_minima[0]]
    input_minima = rounded_minima + sorted_other_minima
    output_minima = []
    for point in input_minima:
        output_minima.append(points['minima'][0][1])
    final_minima = unite_vectors(input_minima, output_minima)
    general_inflections = []
    for point in points['inflections']:
        if isinstance(point[0], str):
            general_inflections.append(point[0])
    optional_inflections = []
    for point in general_inflections:
        initial_value_index = point.find(' + ')
        initial_value = float(point[:initial_value_index])
        periodic_unit_index = initial_value_index + 3
        periodic_unit = float(point[periodic_unit_index:-1])
        if periodic_unit > 0:
            while initial_value > independent_max:
                initial_value -= periodic_unit
            while initial_value < independent_min:
                initial_value += periodic_unit
        else:
            while initial_value > independent_max:
                initial_value += periodic_unit
            while initial_value < independent_min:
                initial_value -= periodic_unit
        first_value = initial_value + 1 * periodic_unit
        second_value = initial_value + 2 * periodic_unit
        third_value = initial_value + 3 * periodic_unit
        fourth_value = initial_value + 4 * periodic_unit
        rounded_initial_value = rounded_value(initial_value, precision)
        rounded_periodic_unit = rounded_value(periodic_unit, precision)
        general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'
        optional_inflections += [initial_value, first_value, second_value, third_value, fourth_value, general_form]
    numerical_inflections = []
    other_inflections = []
    for point in optional_inflections:
        if isinstance(point, (int, float)):
            numerical_inflections.append(point)
        else:
            other_inflections.append(point)
    sorted_inflections = sorted_list(numerical_inflections)
    selected_inflections = [x for x in sorted_inflections if x >= sorted_inflections[0] and x <= sorted_inflections[0] + interval]
    rounded_inflections = []
    for point in selected_inflections:
        rounded_inflections.append(rounded_value(point, precision))
    sorted_other_inflections = []
    if len(other_inflections) > 0:
        if len(other_inflections) == 1:
            sorted_other_inflections = other_inflections
        else:
            first_index = other_inflections[0].find(' + ') - 1
            first_value = float(other_inflections[0][:first_index])
            second_index = other_inflections[1].find(' + ') - 1
            second_value = float(other_inflections[1][:second_index])
            if first_value < second_value:
                sorted_other_inflections = other_inflections
            else:
                sorted_other_inflections = [other_inflections[1], other_inflections[0]]
    input_inflections = rounded_inflections + sorted_other_inflections
    output_inflections = []
    for point in input_inflections:
        output_inflections.append(points['inflections'][0][1])
    final_inflections = unite_vectors(input_inflections, output_inflections)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulated_area(integral, min_value, max_value, precision)
    accumulated_iqr = accumulated_area(integral, q1, q3, precision)
    averages_range = average_values('sinusoidal', equation, integral, min_value, max_value, solution, precision)
    averages_iqr = average_values('sinusoidal', equation, integral, q1, q3, solution, precision)
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
        'roots': final_roots,
        'maxima': final_maxima,
        'minima': final_minima,
        'inflections': final_inflections
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