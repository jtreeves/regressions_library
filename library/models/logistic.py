from numpy import exp
from numpy import inf
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
from library.statistics.rounding import rounding
from library.statistics.halve import halve_dimension
from library.statistics.mean import mean

def logistic(data, precision):
    independent_variable = dimension(data, 1)
    dependent_variable = dimension(data, 2)
    halved_data = halve_dimension(data, 1)
    dependent_lower = dimension(halved_data['lower'], 2)
    dependent_upper = dimension(halved_data['upper'], 2)
    mean_lower = mean(dependent_lower)
    mean_upper = mean(dependent_upper)
    dependent_max = max(dependent_variable)
    dependent_average = dependent_max / 2
    print(f'DEPENDENT MAX: {dependent_max}')
    print(f'DEPENDENT AVERAGE: {dependent_average}')
    deviations_coordinates = {}
    for i in range(len(data)):
        deviations_coordinates[i] = {
            'coordinates': data[i],
            'deviation': abs(data[i][1] - dependent_average)
        }
    print(f'DEVIATIONS COORDINATES: {deviations_coordinates}')
    dependent_deviations = []
    for i in deviations_coordinates:
        dependent_deviations.append(deviations_coordinates[i]['deviation'])
    print(f'DEPENDENT DEVIATIONS: {dependent_deviations}')
    smallest_deviation = min(dependent_deviations)
    print(f'SMALLEST DEVIATION: {smallest_deviation}')
    closest_independent = 0
    for i in deviations_coordinates:
        if deviations_coordinates[i]['deviation'] == smallest_deviation:
            closest_independent = deviations_coordinates[i]['coordinates'][0]
    print(f'CLOSEST INDEPENDENT: {closest_independent}')
    solution = []
    if mean_upper > mean_lower:
        def logistic_function(variable, first_constant, second_constant, third_constant):
            evaluation = first_constant / (1 + exp(-1 * second_constant * (variable - third_constant)))
            return evaluation
        parameters, parameters_covariance = curve_fit(logistic_function, independent_variable, dependent_variable, bounds=[(-inf, 0, -inf), (inf, inf, inf)])
        solution = list(parameters)
    else:
        def logistic_function(variable, first_constant, second_constant, third_constant):
            evaluation = first_constant / (1 + exp(-1 * second_constant * (variable - third_constant)))
            return evaluation
        parameters, parameters_covariance = curve_fit(logistic_function, independent_variable, dependent_variable, bounds=[(-inf, -inf, -inf), (inf, 0, inf)])
        solution = list(parameters)
    constants = []
    for number in solution:
        constants.append(rounding(number, precision))
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
        'constants': constants,
        'evaluations': evaluations,
        'points': points,
        'accumulations': accumulations,
        'averages': averages,
        'correlation': accuracy
    }
    return result