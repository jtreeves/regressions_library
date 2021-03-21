from library.analyses.equations.linear import linear as linear_equation
from library.analyses.equations.quadratic import quadratic as quadratic_equation
from library.analyses.equations.cubic import cubic as cubic_equation
from library.analyses.equations.hyperbolic import hyperbolic as hyperbolic_equation
from library.analyses.equations.exponential import exponential as exponential_equation
from library.analyses.equations.logarithmic import logarithmic as logarithmic_equation
from library.analyses.roots.linear import linear as linear_roots
from library.analyses.roots.quadratic import quadratic as quadratic_roots
from library.analyses.roots.cubic import cubic as cubic_roots
from library.analyses.roots.hyperbolic import hyperbolic as hyperbolic_roots
from library.analyses.roots.exponential import exponential as exponential_roots
from library.analyses.roots.logarithmic import logarithmic as logarithmic_roots
from library.analyses.derivatives.linear import linear as linear_derivatives
from library.analyses.derivatives.quadratic import quadratic as quadratic_derivatives
from library.analyses.derivatives.cubic import cubic as cubic_derivatives
from library.analyses.derivatives.hyperbolic import hyperbolic as hyperbolic_derivatives
from library.analyses.derivatives.exponential import exponential as exponential_derivatives
from library.analyses.derivatives.logarithmic import logarithmic as logarithmic_derivatives
from library.analyses.integrals.linear import linear as linear_integral
from library.analyses.integrals.quadratic import quadratic as quadratic_integral
from library.analyses.integrals.cubic import cubic as cubic_integral
from library.analyses.integrals.hyperbolic import hyperbolic as hyperbolic_integral
from library.analyses.integrals.exponential import exponential as exponential_integral
from library.analyses.integrals.logarithmic import logarithmic as logarithmic_integral
from library.analyses.critical_points import critical_points
from library.analyses.intervals import intervals
from library.analyses.intercepts import intercepts
from library.analyses.maxima import maxima
from library.analyses.minima import minima
from library.analyses.extrema import extrema
from library.analyses.inflections import inflections
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values

coefficients = [2, 3, 5, 7]
precision = 4

linear_function = linear_equation(coefficients[0], coefficients[1])
quadratic_function = quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
cubic_function = cubic_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_function = hyperbolic_equation(coefficients[0], coefficients[1])
exponential_function = exponential_equation(coefficients[0], coefficients[1])
logarithmic_function = logarithmic_equation(coefficients[0], coefficients[1])

linear_zeroes = linear_roots(coefficients[0], coefficients[1], precision)
quadratic_zeroes = quadratic_roots(coefficients[0], coefficients[1], coefficients[2], precision)
cubic_zeroes = cubic_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3], precision)
hyperbolic_zeroes = hyperbolic_roots(coefficients[0], coefficients[1], precision)
exponential_zeroes = exponential_roots(coefficients[0], coefficients[1], precision)
logarithmic_zeroes = logarithmic_roots(coefficients[0], coefficients[1], precision)

linear_derivatives_object = linear_derivatives(coefficients[0], coefficients[1])
quadratic_derivatives_object = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])
cubic_derivatives_object = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_derivatives_object = hyperbolic_derivatives(coefficients[0], coefficients[1])
exponential_derivatives_object = exponential_derivatives(coefficients[0], coefficients[1])
logarithmic_derivatives_object = logarithmic_derivatives(coefficients[0], coefficients[1])

linear_integral_object = linear_integral(coefficients[0], coefficients[1])
quadratic_integral_object = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])
cubic_integral_object = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_integral_object = hyperbolic_integral(coefficients[0], coefficients[1])
exponential_integral_object = exponential_integral(coefficients[0], coefficients[1])
logarithmic_integral_object = logarithmic_integral(coefficients[0], coefficients[1])

first_linear_critical_points = critical_points('linear', 1, coefficients[:2], precision)
first_quadratic_critical_points = critical_points('quadratic', 1, coefficients[:3], precision)
first_cubic_critical_points = critical_points('cubic', 1, coefficients, precision)
first_hyperbolic_critical_points = critical_points('hyperbolic', 1, coefficients[:2], precision)
first_exponential_critical_points = critical_points('exponential', 1, coefficients[:2], precision)
first_logarithmic_critical_points = critical_points('logarithmic', 1, coefficients[:2], precision)

second_linear_critical_points = critical_points('linear', 2, coefficients[:2], precision)
second_quadratic_critical_points = critical_points('quadratic', 2, coefficients[:3], precision)
second_cubic_critical_points = critical_points('cubic', 2, coefficients, precision)
second_hyperbolic_critical_points = critical_points('hyperbolic', 2, coefficients[:2], precision)
second_exponential_critical_points = critical_points('exponential', 2, coefficients[:2], precision)
second_logarithmic_critical_points = critical_points('logarithmic', 2, coefficients[:2], precision)

first_linear_intervals = intervals(linear_derivatives_object['first']['evaluation'], first_linear_critical_points)
first_quadratic_intervals = intervals(quadratic_derivatives_object['first']['evaluation'], first_quadratic_critical_points)
first_cubic_intervals = intervals(cubic_derivatives_object['first']['evaluation'], first_cubic_critical_points)
first_hyperbolic_intervals = intervals(hyperbolic_derivatives_object['first']['evaluation'], first_hyperbolic_critical_points)
first_exponential_intervals = intervals(exponential_derivatives_object['first']['evaluation'], first_exponential_critical_points)
first_logarithmic_intervals = intervals(logarithmic_derivatives_object['first']['evaluation'], first_logarithmic_critical_points)

second_linear_intervals = intervals(linear_derivatives_object['second']['evaluation'], second_linear_critical_points)
second_quadratic_intervals = intervals(quadratic_derivatives_object['second']['evaluation'], second_quadratic_critical_points)
second_cubic_intervals = intervals(cubic_derivatives_object['second']['evaluation'], second_cubic_critical_points)
second_hyperbolic_intervals = intervals(hyperbolic_derivatives_object['second']['evaluation'], second_hyperbolic_critical_points)
second_exponential_intervals = intervals(exponential_derivatives_object['second']['evaluation'], second_exponential_critical_points)
second_logarithmic_intervals = intervals(logarithmic_derivatives_object['second']['evaluation'], second_logarithmic_critical_points)

linear_intercepts = intercepts('linear', coefficients[:2], precision)
quadratic_intercepts = intercepts('quadratic', coefficients[:3], precision)
cubic_intercepts = intercepts('cubic', coefficients, precision)
hyperbolic_intercepts = intercepts('hyperbolic', coefficients[:2], precision)
exponential_intercepts = intercepts('exponential', coefficients[:2], precision)
logarithmic_intercepts = intercepts('logarithmic', coefficients[:2], precision)

linear_maxima = maxima(first_linear_intervals)
quadratic_maxima = maxima(first_quadratic_intervals)
cubic_maxima = maxima(first_cubic_intervals)
hyperbolic_maxima = maxima(first_hyperbolic_intervals)
exponential_maxima = maxima(first_exponential_intervals)
logarithmic_maxima = maxima(first_logarithmic_intervals)

linear_minima = minima(first_linear_intervals)
quadratic_minima = minima(first_quadratic_intervals)
cubic_minima = minima(first_cubic_intervals)
hyperbolic_minima = minima(first_hyperbolic_intervals)
exponential_minima = minima(first_exponential_intervals)
logarithmic_minima = minima(first_logarithmic_intervals)

linear_extrema = extrema('linear', coefficients[:2], linear_derivatives_object['first']['evaluation'], precision)
quadratic_extrema = extrema('quadratic', coefficients[:3], quadratic_derivatives_object['first']['evaluation'], precision)
cubic_extrema = extrema('cubic', coefficients, cubic_derivatives_object['first']['evaluation'], precision)
hyperbolic_extrema = extrema('hyperbolic', coefficients[:2], hyperbolic_derivatives_object['first']['evaluation'], precision)
exponential_extrema = extrema('exponential', coefficients[:2], exponential_derivatives_object['first']['evaluation'], precision)
logarithmic_extrema = extrema('logarithmic', coefficients[:2], logarithmic_derivatives_object['first']['evaluation'], precision)

linear_inflections = inflections('linear', coefficients[:2], linear_derivatives_object['second']['evaluation'], precision)
quadratic_inflections = inflections('quadratic', coefficients[:3], quadratic_derivatives_object['second']['evaluation'], precision)
cubic_inflections = inflections('cubic', coefficients, cubic_derivatives_object['second']['evaluation'], precision)
hyperbolic_inflections = inflections('hyperbolic', coefficients[:2], hyperbolic_derivatives_object['second']['evaluation'], precision)
exponential_inflections = inflections('exponential', coefficients[:2], exponential_derivatives_object['second']['evaluation'], precision)
logarithmic_inflections = inflections('logarithmic', coefficients[:2], logarithmic_derivatives_object['second']['evaluation'], precision)

linear_key_points = key_points('linear', coefficients[:2], linear_function, linear_derivatives_object['first']['evaluation'], linear_derivatives_object['second']['evaluation'], precision)
quadratic_key_points = key_points('quadratic', coefficients[:3], quadratic_function, quadratic_derivatives_object['first']['evaluation'], quadratic_derivatives_object['second']['evaluation'], precision)
cubic_key_points = key_points('cubic', coefficients, cubic_function, cubic_derivatives_object['first']['evaluation'], cubic_derivatives_object['second']['evaluation'], precision)
hyperbolic_key_points = key_points('hyperbolic', coefficients[:2], hyperbolic_function, hyperbolic_derivatives_object['first']['evaluation'], hyperbolic_derivatives_object['second']['evaluation'], precision)
exponential_key_points = key_points('exponential', coefficients[:2], exponential_function, exponential_derivatives_object['first']['evaluation'], exponential_derivatives_object['second']['evaluation'], precision)
logarithmic_key_points = key_points('logarithmic', coefficients[:2], logarithmic_function, logarithmic_derivatives_object['first']['evaluation'], logarithmic_derivatives_object['second']['evaluation'], precision)

linear_accumulation = accumulation(linear_integral_object['evaluation'], 10, 20, precision)
quadratic_accumulation = accumulation(quadratic_integral_object['evaluation'], 10, 20, precision)
cubic_accumulation = accumulation(cubic_integral_object['evaluation'], 10, 20, precision)
hyperbolic_accumulation = accumulation(hyperbolic_integral_object['evaluation'], 10, 20, precision)
exponential_accumulation = accumulation(exponential_integral_object['evaluation'], 10, 20, precision)
logarithmic_accumulation = accumulation(logarithmic_integral_object['evaluation'], 10, 20, precision)

linear_averages = average_values('linear', linear_function, linear_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
quadratic_averages = average_values('quadratic', quadratic_function, quadratic_integral_object['evaluation'], 10, 20, coefficients[:3], precision)
cubic_averages = average_values('cubic', cubic_function, cubic_integral_object['evaluation'], 10, 20, coefficients, precision)
hyperbolic_averages = average_values('hyperbolic', hyperbolic_function, hyperbolic_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
exponential_averages = average_values('exponential', exponential_function, exponential_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
logarithmic_averages = average_values('logarithmic', logarithmic_function, logarithmic_integral_object['evaluation'], 10, 20, coefficients[:2], precision)

print(f'LINEAR EVALUATION: {linear_function(10)}') # 23
print(f'QUADRATIC EVALUATION: {quadratic_function(10)}') # 235
print(f'CUBIC EVALUATION: {cubic_function(10)}') # 2357
print(f'HYPERBOLIC EVALUATION: {hyperbolic_function(10)}') # 3.2
print(f'EXPONENTIAL EVALUATION: {exponential_function(10)}') # 118098
print(f'LOGARITHMIC EVALUATION: {logarithmic_function(10)}') # 7.605170185988092

print(f'LINEAR ROOTS: {linear_zeroes}') # [-1.5]
print(f'QUADRATIC ROOTS: {quadratic_zeroes}') # [None]
print(f'CUBIC ROOTS: {cubic_zeroes}') # [-1.4455]
print(f'HYPERBOLIC ROOTS: {hyperbolic_zeroes}') # [-0.6667]
print(f'EXPONENTIAL ROOTS: {exponential_zeroes}') # [None]
print(f'LOGARITHMIC ROOTS: {logarithmic_zeroes}') # [0.2231]

print(f"LINEAR FIRST DERIVATIVES CONSTANTS: {linear_derivatives_object['first']['constants']}") # [2]
print(f"QUADRATIC FIRST DERIVATIVES CONSTANTS: {quadratic_derivatives_object['first']['constants']}") # [4, 3]
print(f"CUBIC FIRST DERIVATIVES CONSTANTS: {cubic_derivatives_object['first']['constants']}") # [6, 6, 5]
print(f"HYPERBOLIC FIRST DERIVATIVES CONSTANTS: {hyperbolic_derivatives_object['first']['constants']}") # [-2]
print(f"EXPONENTIAL FIRST DERIVATIVES CONSTANTS: {exponential_derivatives_object['first']['constants']}") # [2.1972245773362196, 3]
print(f"LOGARITHMIC FIRST DERIVATIVES CONSTANTS: {logarithmic_derivatives_object['first']['constants']}") # [2]

print(f"LINEAR SECOND DERIVATIVES CONSTANTS: {linear_derivatives_object['second']['constants']}") # [0]
print(f"QUADRATIC SECOND DERIVATIVES CONSTANTS: {quadratic_derivatives_object['second']['constants']}") # [4]
print(f"CUBIC SECOND DERIVATIVES CONSTANTS: {cubic_derivatives_object['second']['constants']}") # [12, 6]
print(f"HYPERBOLIC SECOND DERIVATIVES CONSTANTS: {hyperbolic_derivatives_object['second']['constants']}") # [4]
print(f"EXPONENTIAL SECOND DERIVATIVES CONSTANTS: {exponential_derivatives_object['second']['constants']}") # [2.413897921625164, 3]
print(f"LOGARITHMIC SECOND DERIVATIVES CONSTANTS: {logarithmic_derivatives_object['second']['constants']}") # [-2]

print(f"LINEAR INTEGRAL CONSTANTS: {linear_integral_object['constants']}") # [1.0, 3]
print(f"QUADRATIC INTEGRAL CONSTANTS: {quadratic_integral_object['constants']}") # [0.6666666666666666, 1.5, 5]
print(f"CUBIC INTEGRAL CONSTANTS: {cubic_integral_object['constants']}") # [0.5, 1.0, 2.5, 7]
print(f"HYPERBOLIC INTEGRAL CONSTANTS: {hyperbolic_integral_object['constants']}") # [2, 3]
print(f"EXPONENTIAL INTEGRAL CONSTANTS: {exponential_integral_object['constants']}") # [1.8204784532536746, 3]
print(f"LOGARITHMIC INTEGRAL CONSTANTS: {logarithmic_integral_object['constants']}") # [2, 3]

print(f'FIRST LINEAR CRITICAL POINTS: {first_linear_critical_points}') # [None]
print(f'FIRST QUADRATIC CRITICAL POINTS: {first_quadratic_critical_points}') # [-0.75]
print(f'FIRST CUBIC CRITICAL POINTS: {first_cubic_critical_points}') # [None]
print(f'FIRST HYPERBOLIC CRITICAL POINTS: {first_hyperbolic_critical_points}') # [None]
print(f'FIRST EXPONENTIAL CRITICAL POINTS: {first_exponential_critical_points}') # [None]
print(f'FIRST LOGARITHMIC CRITICAL POINTS: {first_logarithmic_critical_points}') # [None]

print(f'SECOND LINEAR CRITICAL POINTS: {second_linear_critical_points}') # [None]
print(f'SECOND QUADRATIC CRITICAL POINTS: {second_quadratic_critical_points}') # [None]
print(f'SECOND CUBIC CRITICAL POINTS: {second_cubic_critical_points}') # [-0.5]
print(f'SECOND HYPERBOLIC CRITICAL POINTS: {second_hyperbolic_critical_points}') # [None]
print(f'SECOND EXPONENTIAL CRITICAL POINTS: {second_exponential_critical_points}') # [None]
print(f'SECOND LOGARITHMIC CRITICAL POINTS: {second_logarithmic_critical_points}') # [None]

print(f'FIRST LINEAR INTERVALS: {first_linear_intervals}') # ['positive']
print(f'FIRST QUADRATIC INTERVALS: {first_quadratic_intervals}') # ['negative', -0.75, 'positive']
print(f'FIRST CUBIC INTERVALS: {first_cubic_intervals}') # ['positive']
print(f'FIRST HYPERBOLIC INTERVALS: {first_hyperbolic_intervals}') # ['negative']
print(f'FIRST EXPONENTIAL INTERVALS: {first_exponential_intervals}') # ['positive']
print(f'FIRST LOGARITHMIC INTERVALS: {first_logarithmic_intervals}') # ['positive']

print(f'SECOND LINEAR INTERVALS: {second_linear_intervals}') # [0]
print(f'SECOND QUADRATIC INTERVALS: {second_quadratic_intervals}') # ['positive']
print(f'SECOND CUBIC INTERVALS: {second_cubic_intervals}') # ['negative', -0.5, 'positive']
print(f'SECOND HYPERBOLIC INTERVALS: {second_hyperbolic_intervals}') # ['positive']
print(f'SECOND EXPONENTIAL INTERVALS: {second_exponential_intervals}') # ['positive']
print(f'SECOND LOGARITHMIC INTERVALS: {second_logarithmic_intervals}') # ['negative']

print(f'LINEAR INTERCEPTS: {linear_intercepts}') # [-1.5]
print(f'QUADRATIC INTERCEPTS: {quadratic_intercepts}') # [None]
print(f'CUBIC INTERCEPTS: {cubic_intercepts}') # [-1.4455]
print(f'HYPERBOLIC INTERCEPTS: {hyperbolic_intercepts}') # [-0.6667]
print(f'EXPONENTIAL INTERCEPTS: {exponential_intercepts}') # [None]
print(f'LOGARITHMIC INTERCEPTS: {logarithmic_intercepts}') # [0.2231]

print(f'LINEAR MAXIMA: {linear_maxima}') # [None]
print(f'QUADRATIC MAXIMA: {quadratic_maxima}') # [None]
print(f'CUBIC MAXIMA: {cubic_maxima}') # [None]
print(f'HYPERBOLIC MAXIMA: {hyperbolic_maxima}') # [None]
print(f'EXPONENTIAL MAXIMA: {exponential_maxima}') # [None]
print(f'LOGARITHMIC MAXIMA: {logarithmic_maxima}') # [None]

print(f'LINEAR MINIMA: {linear_minima}') # [None]
print(f'QUADRATIC MINIMA: {quadratic_minima}') # [-0.75]
print(f'CUBIC MINIMA: {cubic_minima}') # [None]
print(f'HYPERBOLIC MINIMA: {hyperbolic_minima}') # [None]
print(f'EXPONENTIAL MINIMA: {exponential_minima}') # [None]
print(f'LOGARITHMIC MINIMA: {logarithmic_minima}') # [None]

print(f'LINEAR EXTREMA: {linear_extrema}') # {'maxima': [None], 'minima': [None]}
print(f'QUADRATIC EXTREMA: {quadratic_extrema}') # {'maxima': [None], 'minima': [-0.75]}
print(f'CUBIC EXTREMA: {cubic_extrema}') # {'maxima': [None], 'minima': [None]}
print(f'HYPERBOLIC EXTREMA: {hyperbolic_extrema}') # {'maxima': [None], 'minima': [None]}
print(f'EXPONENTIAL EXTREMA: {exponential_extrema}') # {'maxima': [None], 'minima': [None]}
print(f'LOGARITHMIC EXTREMA: {logarithmic_extrema}') # {'maxima': [None], 'minima': [None]}

print(f'LINEAR INFLECTIONS: {linear_inflections}') # [None]
print(f'QUADRATIC INFLECTIONS: {quadratic_inflections}') # [None]
print(f'CUBIC INFLECTIONS: {cubic_inflections}') # [-0.5]
print(f'HYPERBOLIC INFLECTIONS: {hyperbolic_inflections}') # [None]
print(f'EXPONENTIAL INFLECTIONS: {exponential_inflections}') # [None]
print(f'LOGARITHMIC INFLECTIONS: {logarithmic_inflections}') # [None]

print(f'LINEAR KEY POINTS: {linear_key_points}') # {'roots': [[-1.5, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}
print(f'QUADRATIC KEY POINTS: {quadratic_key_points}') # {'roots': [None], 'maxima': [None], 'minima': [[-0.75, 3.875]], 'inflections': [None]}
print(f'CUBIC KEY POINTS: {cubic_key_points}') # {'roots': [[-1.4455, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[-0.5, 5.0]]
print(f'HYPERBOLIC KEY POINTS: {hyperbolic_key_points}') # {'roots': [[-0.6667, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}
print(f'EXPONENTIAL KEY POINTS: {exponential_key_points}') # {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}
print(f'LOGARITHMIC KEY POINTS: {logarithmic_key_points}') # {'roots': [[0.2231, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}

print(f'LINEAR ACCUMULATION: {linear_accumulation}') # 330.0
print(f'QUADRATIC ACCUMULATION: {quadratic_accumulation}') # 5166.6667
print(f'CUBIC ACCUMULATION: {cubic_accumulation}') # 82820.0
print(f'HYPERBOLIC ACCUMULATION: {hyperbolic_accumulation}') # 31.3863
print(f'EXPONENTIAL ACCUMULATION: {exponential_accumulation}') # 6347508375.7293
print(f'LOGARITHMIC ACCUMULATION: {logarithmic_accumulation}') # 83.7776

print(f'LINEAR AVERAGES: {linear_averages}') # {'average_value_derivative': 2.0, 'mean_values_derivative': ['All'], 'average_value_integral': 33.0, 'mean_values_integral': [15.0]}
print(f'QUADRATIC AVERAGES: {quadratic_averages}') # {'average_value_derivative': 63.0, 'mean_values_derivative': [15.0], 'average_value_integral': 516.6667, 'mean_values_integral': [15.2624]}
print(f'CUBIC AVERAGES: {cubic_averages}') # {'average_value_derivative': 1495.0, 'mean_values_derivative': [15.2665], 'average_value_integral': 8282.0, 'mean_values_integral': [15.5188]}
print(f'HYPERBOLIC AVERAGES: {hyperbolic_averages}') # {'average_value_derivative': -0.01, 'mean_values_derivative': [14.1421], 'average_value_integral': 3.1386, 'mean_values_integral': [14.43]}
print(f'EXPONENTIAL AVERAGES: {exponential_averages}') # {'average_value_derivative': 697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': 634750837.5729, 'mean_values_integral': [17.8185]}
print(f'LOGARITHMIC AVERAGES: {logarithmic_averages}') # {'average_value_derivative': 0.1386, 'mean_values_derivative': [14.43], 'average_value_integral': 8.3778, 'mean_values_integral': [14.7155]}