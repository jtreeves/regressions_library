from numpy import exp, inf
from scipy.optimize import curve_fit
from library.errors.matrices import matrix_of_scalars
from library.errors.scalars import positive_integer
from library.vectors.dimension import single_dimension
from library.analyses.equations.logistic import logistic_equation
from library.analyses.derivatives.logistic import logistic_derivatives
from library.analyses.integrals.logistic import logistic_integral
from library.analyses.points import key_coordinates
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values
from library.statistics.summary import five_number_summary
from library.statistics.correlation import correlation_coefficient
from library.statistics.rounding import rounded_value
from library.statistics.halve import half_dimension
from library.statistics.mean import mean_value

def logistic_model(data, precision):
    matrix_of_scalars(data, 'first')
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
        'constants': constants,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result