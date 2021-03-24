from numpy import exp
from scipy.optimize import curve_fit
from library.vectors.dimension import dimension
from library.vectors.column import column
from library.matrices.solve import solve
from library.analyses.equations.logistic import logistic as logistic_equation
from library.analyses.derivatives.logistic import logistic as logistic_derivative
from library.analyses.integrals.logistic import logistic as logistic_integral
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values
from library.statistics.five_number_summary import five_number_summary
from library.statistics.correlation import correlation

def logistic(data, precision):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    def logistic_function(variable, first_constant, second_constant, third_constant):
        evaluation = first_constant / (1 + exp(-1 * second_constant * (variable - third_constant)))
        return evaluation
    parameters, parameters_covariance = curve_fit(logistic_function, independent_variable, dependent_variable)
    solution = list(parameters)
    equation = logistic_equation(*solution)
    derivative = logistic_derivative(*solution)
    integral = logistic_integral(*solution)['evaluation']
    first_derivative = derivative['first']['evaluation']
    second_derivative = derivative['second']['evaluation']
    points = key_points('logistic', solution, equation, first_derivative, second_derivative, precision)
    five_numbers = five_number_summary(independent_variable, precision)
    min_value = five_numbers['minimum']
    max_value = five_numbers['maximum']
    q1 = five_numbers['q1']
    q3 = five_numbers['q3']
    accumulated_range = accumulation(integral, min_value, max_value, precision)
    accumulated_iqr = accumulation(integral, q1, q3, precision)
    averages_range = average_values('logistic', equation, integral, min_value, max_value, solution, precision)
    averages_iqr = average_values('logistic', equation, integral, q1, q3, solution, precision)
    predicted = []
    for i in range(len(data)):
        predicted.append(equation(independent_variable[i]))
    accuracy = correlation(dependent_variable, predicted, precision)
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

data_set = [
    [1, 0.0000122],
    [2, 0.000247],
    [3, 0.004945],
    [4, 0.094852],
    [5, 1.0],
    [6, 1.905148],
    [7, 1.995055],
    [8, 1.999753],
    [9, 1.999988],
    [10, 1.999999],
]

test_case = logistic(data_set, 4)

print(test_case)
# {'constants': [1.9999999846356367, 2.9999975882265435, 4.999999993353611], 'evaluations': {'equation': <function logistic.<locals>.logistic_equation at 0x11f9ab3a0>, 'derivative': <function logistic.<locals>.first_derivative at 0x11f9ab550>, 'integral': <function logistic.<locals>.logistic_integral at 0x11f9ab430>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[4.999999993353611, 1.0]]}, 'accumulations': {'range': 10.0, 'iqr': 5.9984}, 'averages': {'range': {'average_value_derivative': 0.2222, 'mean_values_derivative': [3.9275, 6.0721], 'average_value_integral': 1.1111, 'mean_values_integral': [5.0744]}, 'iqr': {'average_value_derivative': 0.399, 'mean_values_derivative': [4.146, 5.8538], 'average_value_integral': 1.1997, 'mean_values_integral': [5.1349]}}, 'correlation': 1.0}