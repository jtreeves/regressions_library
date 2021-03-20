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

linear_function = linear_equation(coefficients[0], coefficients[1])
quadratic_function = quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
cubic_function = cubic_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_function = hyperbolic_equation(coefficients[0], coefficients[1])
exponential_function = exponential_equation(coefficients[0], coefficients[1])
logarithmic_function = logarithmic_equation(coefficients[0], coefficients[1])

linear_zeroes = linear_roots(coefficients[0], coefficients[1])
quadratic_zeroes = quadratic_roots(coefficients[0], coefficients[1], coefficients[2])
cubic_zeroes = cubic_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_zeroes = hyperbolic_roots(coefficients[0], coefficients[1])
exponential_zeroes = exponential_roots(coefficients[0], coefficients[1])
logarithmic_zeroes = logarithmic_roots(coefficients[0], coefficients[1])

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

first_linear_critical_points = critical_points('linear', 1, coefficients)
first_quadratic_critical_points = critical_points('quadratic', 1, coefficients)
first_cubic_critical_points = critical_points('cubic', 1, coefficients)
first_hyperbolic_critical_points = critical_points('hyperbolic', 1, coefficients)
first_exponential_critical_points = critical_points('exponential', 1, coefficients)
first_logarithmic_critical_points = critical_points('logarithmic', 1, coefficients)

second_linear_critical_points = critical_points('linear', 2, coefficients)
second_quadratic_critical_points = critical_points('quadratic', 2, coefficients)
second_cubic_critical_points = critical_points('cubic', 2, coefficients)
second_hyperbolic_critical_points = critical_points('hyperbolic', 2, coefficients)
second_exponential_critical_points = critical_points('exponential', 2, coefficients)
second_logarithmic_critical_points = critical_points('logarithmic', 2, coefficients)

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

linear_intercepts = intercepts('linear', coefficients)
quadratic_intercepts = intercepts('quadratic', coefficients)
cubic_intercepts = intercepts('cubic', coefficients)
hyperbolic_intercepts = intercepts('hyperbolic', coefficients)
exponential_intercepts = intercepts('exponential', coefficients)
logarithmic_intercepts = intercepts('logarithmic', coefficients)

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

linear_extrema = extrema(first_linear_intervals)
quadratic_extrema = extrema(first_quadratic_intervals)
cubic_extrema = extrema(first_cubic_intervals)
hyperbolic_extrema = extrema(first_hyperbolic_intervals)
exponential_extrema = extrema(first_exponential_intervals)
logarithmic_extrema = extrema(first_logarithmic_intervals)

linear_inflections = inflections(second_linear_intervals)
quadratic_inflections = inflections(second_quadratic_intervals)
cubic_inflections = inflections(second_cubic_intervals)
hyperbolic_inflections = inflections(second_hyperbolic_intervals)
exponential_inflections = inflections(second_exponential_intervals)
logarithmic_inflections = inflections(second_logarithmic_intervals)

linear_key_points = key_points('linear', coefficients, linear_function, linear_derivatives_object['first']['evaluation'], linear_derivatives_object['second']['evaluation'])
quadratic_key_points = key_points('quadratic', coefficients, quadratic_function, quadratic_derivatives_object['first']['evaluation'], quadratic_derivatives_object['second']['evaluation'])
cubic_key_points = key_points('cubic', coefficients, cubic_function, cubic_derivatives_object['first']['evaluation'], cubic_derivatives_object['second']['evaluation'])
hyperbolic_key_points = key_points('hyperbolic', coefficients, hyperbolic_function, hyperbolic_derivatives_object['first']['evaluation'], hyperbolic_derivatives_object['second']['evaluation'])
exponential_key_points = key_points('exponential', coefficients, exponential_function, exponential_derivatives_object['first']['evaluation'], exponential_derivatives_object['second']['evaluation'])
logarithmic_key_points = key_points('logarithmic', coefficients, logarithmic_function, logarithmic_derivatives_object['first']['evaluation'], logarithmic_derivatives_object['second']['evaluation'])

linear_accumulation = accumulation(linear_integral_object['evaluation'], 10, 20)
quadratic_accumulation = accumulation(quadratic_integral_object['evaluation'], 10, 20)
cubic_accumulation = accumulation(cubic_integral_object['evaluation'], 10, 20)
hyperbolic_accumulation = accumulation(hyperbolic_integral_object['evaluation'], 10, 20)
exponential_accumulation = accumulation(exponential_integral_object['evaluation'], 10, 20)
logarithmic_accumulation = accumulation(logarithmic_integral_object['evaluation'], 10, 20)

linear_averages = average_values('linear', linear_function, linear_integral_object['evaluation'], 10, 20, coefficients)
quadratic_averages = average_values('quadratic', quadratic_function, quadratic_integral_object['evaluation'], 10, 20, coefficients)
cubic_averages = average_values('cubic', cubic_function, cubic_integral_object['evaluation'], 10, 20, coefficients)
hyperbolic_averages = average_values('hyperbolic', hyperbolic_function, hyperbolic_integral_object['evaluation'], 10, 20, coefficients)
exponential_averages = average_values('exponential', exponential_function, exponential_integral_object['evaluation'], 10, 20, coefficients)
logarithmic_averages = average_values('logarithmic', logarithmic_function, logarithmic_integral_object['evaluation'], 10, 20, coefficients)