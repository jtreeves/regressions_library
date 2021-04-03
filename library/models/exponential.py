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