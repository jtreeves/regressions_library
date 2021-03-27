from math import log
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
    independent_variable = single_dimension(data, 1)
    dependent_variable = single_dimension(data, 2)
    filtered_independent = []
    for i in independent_variable:
        if i <= 0:
            filtered_independent.append(10**(-precision))
        else:
            filtered_independent.append(i)
    independent_matrix = []
    dependent_matrix = column_conversion(dependent_variable)
    for i in range(len(data)):
        independent_matrix.append([log(filtered_independent[i]), 1])
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
    for i in range(len(data)):
        predicted.append(equation(independent_variable[i]))
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