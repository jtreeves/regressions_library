import unittest

from library.analyses.equations.linear import linear_equation
from library.analyses.equations.quadratic import quadratic_equation
from library.analyses.equations.cubic import cubic_equation
from library.analyses.equations.hyperbolic import hyperbolic_equation
from library.analyses.equations.exponential import exponential_equation
from library.analyses.equations.logarithmic import logarithmic_equation
from library.analyses.equations.logistic import logistic_equation
from library.analyses.equations.sinusoidal import sinusoidal_equation
from library.analyses.roots.linear import linear_roots
from library.analyses.roots.quadratic import quadratic_roots
from library.analyses.roots.cubic import cubic_roots
from library.analyses.roots.hyperbolic import hyperbolic_roots
from library.analyses.roots.exponential import exponential_roots
from library.analyses.roots.logarithmic import logarithmic_roots
from library.analyses.roots.logistic import logistic_roots
from library.analyses.roots.sinusoidal import sinusoidal_roots
from library.analyses.derivatives.linear import linear_derivatives
from library.analyses.derivatives.quadratic import quadratic_derivatives
from library.analyses.derivatives.cubic import cubic_derivatives
from library.analyses.derivatives.hyperbolic import hyperbolic_derivatives
from library.analyses.derivatives.exponential import exponential_derivatives
from library.analyses.derivatives.logarithmic import logarithmic_derivatives
from library.analyses.derivatives.logistic import logistic_derivatives
from library.analyses.derivatives.sinusoidal import sinusoidal_derivatives
from library.analyses.integrals.linear import linear_integral
from library.analyses.integrals.quadratic import quadratic_integral
from library.analyses.integrals.cubic import cubic_integral
from library.analyses.integrals.hyperbolic import hyperbolic_integral
from library.analyses.integrals.exponential import exponential_integral
from library.analyses.integrals.logarithmic import logarithmic_integral
from library.analyses.integrals.logistic import logistic_integral
from library.analyses.integrals.sinusoidal import sinusoidal_integral
from library.analyses.criticals import critical_points
from library.analyses.intervals import sign_chart
from library.analyses.intercepts import intercept_points
from library.analyses.maxima import maxima_points
from library.analyses.minima import minima_points
from library.analyses.extrema import extrema_points
from library.analyses.inflections import inflection_points
from library.analyses.points import key_coordinates
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values

coefficients = [2, 3, 5, 7]
precision = 4

linear_function = linear_equation(coefficients[0], coefficients[1])
quadratic_function = quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
cubic_function = cubic_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_function = hyperbolic_equation(coefficients[0], coefficients[1])
exponential_function = exponential_equation(coefficients[0], coefficients[1])
logarithmic_function = logarithmic_equation(coefficients[0], coefficients[1])
logistic_function = logistic_equation(coefficients[0], coefficients[1], coefficients[2])
sinusoidal_function = sinusoidal_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])

class TestEquations(unittest.TestCase):
    def test_linear_function(self):
        self.assertEqual(linear_function(10), 23)
    
    def test_quadratic_function(self):
        self.assertEqual(quadratic_function(10), 235)
    
    def test_cubic_function(self):
        self.assertEqual(cubic_function(10), 2357)
    
    def test_hyperbolic_function(self):
        self.assertEqual(hyperbolic_function(10), 3.2)
    
    def test_exponential_function(self):
        self.assertEqual(exponential_function(10), 118098)
    
    def test_logarithmic_function(self):
        self.assertEqual(logarithmic_function(10), 7.605170185988092)
    
    def test_logistic_function(self):
        self.assertEqual(logistic_function(10), 1.999999388195546)
    
    def test_sinusoidal_function(self):
        self.assertEqual(sinusoidal_function(10), 8.300575680314234)

linear_derivatives_object = linear_derivatives(coefficients[0], coefficients[1])
quadratic_derivatives_object = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])
cubic_derivatives_object = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_derivatives_object = hyperbolic_derivatives(coefficients[0], coefficients[1])
exponential_derivatives_object = exponential_derivatives(coefficients[0], coefficients[1])
logarithmic_derivatives_object = logarithmic_derivatives(coefficients[0], coefficients[1])
logistic_derivatives_object = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])
sinusoidal_derivatives_object = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])

class TestDerivatives(unittest.TestCase):
    def test_linear_derivatives_object_first_constants(self):
        self.assertEqual(linear_derivatives_object['first']['constants'], [2])
    
    def test_quadratic_derivatives_object_first_constants(self):
        self.assertEqual(quadratic_derivatives_object['first']['constants'], [4, 3])
    
    def test_cubic_derivatives_object_first_constants(self):
        self.assertEqual(cubic_derivatives_object['first']['constants'], [6, 6, 5])
    
    def test_hyperbolic_derivatives_object_first_constants(self):
        self.assertEqual(hyperbolic_derivatives_object['first']['constants'], [-2])
    
    def test_exponential_derivatives_object_first_constants(self):
        self.assertEqual(exponential_derivatives_object['first']['constants'], [2.1972245773362196, 3])
    
    def test_logarithmic_derivatives_object_first_constants(self):
        self.assertEqual(logarithmic_derivatives_object['first']['constants'], [2])
    
    def test_logistic_derivatives_object_first_constants(self):
        self.assertEqual(logistic_derivatives_object['first']['constants'], [6, 3, 5])
    
    def test_sinusoidal_derivatives_object_first_constants(self):
        self.assertEqual(sinusoidal_derivatives_object['first']['constants'], [6, 3, 5])
    
    def test_linear_derivatives_object_second_constants(self):
        self.assertEqual(linear_derivatives_object['second']['constants'], [0])
    
    def test_quadratic_derivatives_object_second_constants(self):
        self.assertEqual(quadratic_derivatives_object['second']['constants'], [4])
    
    def test_cubic_derivatives_object_second_constants(self):
        self.assertEqual(cubic_derivatives_object['second']['constants'], [12, 6])
    
    def test_hyperbolic_derivatives_object_second_constants(self):
        self.assertEqual(hyperbolic_derivatives_object['second']['constants'], [4])
    
    def test_exponential_derivatives_object_second_constants(self):
        self.assertEqual(exponential_derivatives_object['second']['constants'], [2.413897921625164, 3])
    
    def test_logarithmic_derivatives_object_second_constants(self):
        self.assertEqual(logarithmic_derivatives_object['second']['constants'], [-2])
    
    def test_logistic_derivatives_object_second_constants(self):
        self.assertEqual(logistic_derivatives_object['second']['constants'], [18, 3, 5])
    
    def test_sinusoidal_derivatives_object_second_constants(self):
        self.assertEqual(sinusoidal_derivatives_object['second']['constants'], [-18, 3, 5])

linear_integral_object = linear_integral(coefficients[0], coefficients[1])
quadratic_integral_object = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])
cubic_integral_object = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_integral_object = hyperbolic_integral(coefficients[0], coefficients[1])
exponential_integral_object = exponential_integral(coefficients[0], coefficients[1])
logarithmic_integral_object = logarithmic_integral(coefficients[0], coefficients[1])
logistic_integral_object = logistic_integral(coefficients[0], coefficients[1], coefficients[2])
sinusoidal_integral_object = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])

class TestIntegrals(unittest.TestCase):
    def test_linear_integral_object(self):
        self.assertEqual(linear_integral_object['constants'], [1.0, 3])
    
    def test_quadratic_integral_object(self):
        self.assertEqual(quadratic_integral_object['constants'], [0.6666666666666666, 1.5, 5])
    
    def test_cubic_integral_object(self):
        self.assertEqual(cubic_integral_object['constants'], [0.5, 1.0, 2.5, 7])
    
    def test_hyperbolic_integral_object(self):
        self.assertEqual(hyperbolic_integral_object['constants'], [2, 3])
    
    def test_exponential_integral_object(self):
        self.assertEqual(exponential_integral_object['constants'], [1.8204784532536746, 3])
    
    def test_logarithmic_integral_object(self):
        self.assertEqual(logarithmic_integral_object['constants'], [2, 3])
    
    def test_logistic_integral_object(self):
        self.assertEqual(logistic_integral_object['constants'], [0.6666666666666666, 3, 5])
    
    def test_sinusoidal_integral_object(self):
        self.assertEqual(sinusoidal_integral_object['constants'], [-0.6666666666666666, 3, 5, 7])

first_linear_critical_points = critical_points('linear', 1, coefficients[:2], precision)
first_quadratic_critical_points = critical_points('quadratic', 1, coefficients[:3], precision)
first_cubic_critical_points = critical_points('cubic', 1, coefficients, precision)
first_hyperbolic_critical_points = critical_points('hyperbolic', 1, coefficients[:2], precision)
first_exponential_critical_points = critical_points('exponential', 1, coefficients[:2], precision)
first_logarithmic_critical_points = critical_points('logarithmic', 1, coefficients[:2], precision)
first_logistic_critical_points = critical_points('logistic', 1, coefficients[:3], precision)
first_sinusoidal_critical_points = critical_points('sinusoidal', 1, coefficients, precision)

second_linear_critical_points = critical_points('linear', 2, coefficients[:2], precision)
second_quadratic_critical_points = critical_points('quadratic', 2, coefficients[:3], precision)
second_cubic_critical_points = critical_points('cubic', 2, coefficients, precision)
second_hyperbolic_critical_points = critical_points('hyperbolic', 2, coefficients[:2], precision)
second_exponential_critical_points = critical_points('exponential', 2, coefficients[:2], precision)
second_logarithmic_critical_points = critical_points('logarithmic', 2, coefficients[:2], precision)
second_logistic_critical_points = critical_points('logistic', 2, coefficients[:3], precision)
second_sinusoidal_critical_points = critical_points('sinusoidal', 2, coefficients, precision)

class TestCriticalPoints(unittest.TestCase):
    def test_first_linear_critical_points(self):
        self.assertEqual(first_linear_critical_points, [None])
    
    def test_first_quadratic_critical_points(self):
        self.assertEqual(first_quadratic_critical_points, [-0.75])
    
    def test_first_cubic_critical_points(self):
        self.assertEqual(first_cubic_critical_points, [None])
    
    def test_first_hyperbolic_critical_points(self):
        self.assertEqual(first_hyperbolic_critical_points, [0])
    
    def test_first_exponential_critical_points(self):
        self.assertEqual(first_exponential_critical_points, [None])
    
    def test_first_logarithmic_critical_points(self):
        self.assertEqual(first_logarithmic_critical_points, [None])
    
    def test_first_logistic_critical_points(self):
        self.assertEqual(first_logistic_critical_points, [None])
    
    def test_first_sinusoidal_critical_points(self):
        self.assertEqual(first_sinusoidal_critical_points, [5.5236, 6.5708, 7.618, 8.6652, 9.7124, '5.5236 + 1.0472k'])
    
    def test_second_linear_critical_points(self):
        self.assertEqual(second_linear_critical_points, [None])
    
    def test_second_quadratic_critical_points(self):
        self.assertEqual(second_quadratic_critical_points, [None])
    
    def test_second_cubic_critical_points(self):
        self.assertEqual(second_cubic_critical_points, [-0.5])
    
    def test_second_hyperbolic_critical_points(self):
        self.assertEqual(second_hyperbolic_critical_points, [0])
    
    def test_second_exponential_critical_points(self):
        self.assertEqual(second_exponential_critical_points, [None])
    
    def test_second_logarithmic_critical_points(self):
        self.assertEqual(second_logarithmic_critical_points, [None])
    
    def test_second_logistic_critical_points(self):
        self.assertEqual(second_logistic_critical_points, [5])
    
    def test_second_sinusoidal_critical_points(self):
        self.assertEqual(second_sinusoidal_critical_points, [5, 6.0472, 7.0944, 8.1416, 9.1888, '5 + 1.0472k'])

first_linear_intervals = sign_chart(linear_derivatives_object['first']['evaluation'], first_linear_critical_points)
first_quadratic_intervals = sign_chart(quadratic_derivatives_object['first']['evaluation'], first_quadratic_critical_points)
first_cubic_intervals = sign_chart(cubic_derivatives_object['first']['evaluation'], first_cubic_critical_points)
first_hyperbolic_intervals = sign_chart(hyperbolic_derivatives_object['first']['evaluation'], first_hyperbolic_critical_points)
first_exponential_intervals = sign_chart(exponential_derivatives_object['first']['evaluation'], first_exponential_critical_points)
first_logarithmic_intervals = sign_chart(logarithmic_derivatives_object['first']['evaluation'], first_logarithmic_critical_points)
first_logistic_intervals = sign_chart(logistic_derivatives_object['first']['evaluation'], first_logistic_critical_points)
first_sinusoidal_intervals = sign_chart(sinusoidal_derivatives_object['first']['evaluation'], first_sinusoidal_critical_points)

second_linear_intervals = sign_chart(linear_derivatives_object['second']['evaluation'], second_linear_critical_points)
second_quadratic_intervals = sign_chart(quadratic_derivatives_object['second']['evaluation'], second_quadratic_critical_points)
second_cubic_intervals = sign_chart(cubic_derivatives_object['second']['evaluation'], second_cubic_critical_points)
second_hyperbolic_intervals = sign_chart(hyperbolic_derivatives_object['second']['evaluation'], second_hyperbolic_critical_points)
second_exponential_intervals = sign_chart(exponential_derivatives_object['second']['evaluation'], second_exponential_critical_points)
second_logarithmic_intervals = sign_chart(logarithmic_derivatives_object['second']['evaluation'], second_logarithmic_critical_points)
second_logistic_intervals = sign_chart(logistic_derivatives_object['second']['evaluation'], second_logistic_critical_points)
second_sinusoidal_intervals = sign_chart(sinusoidal_derivatives_object['second']['evaluation'], second_sinusoidal_critical_points)

class TestIntervals(unittest.TestCase):
    def test_first_linear_intervals(self):
        self.assertEqual(first_linear_intervals, ['positive'])
    
    def test_first_quadratic_intervals(self):
        self.assertEqual(first_quadratic_intervals, ['negative', -0.75, 'positive'])
    
    def test_first_cubic_intervals(self):
        self.assertEqual(first_cubic_intervals, ['positive'])
    
    def test_first_hyperbolic_intervals(self):
        self.assertEqual(first_hyperbolic_intervals, ['negative', 0, 'negative'])
    
    def test_first_exponential_intervals(self):
        self.assertEqual(first_exponential_intervals, ['positive'])
    
    def test_first_logarithmic_intervals(self):
        self.assertEqual(first_logarithmic_intervals, ['positive'])
    
    def test_first_logistic_intervals(self):
        self.assertEqual(first_logistic_intervals, ['positive'])
    
    def test_first_sinusoidal_intervals(self):
        self.assertEqual(first_sinusoidal_intervals, ['positive', 5.5236, 'negative', 6.5708, 'positive', 7.618, 'negative', 8.6652, 'positive', 9.7124, 'negative', '5.5236 + 1.0472k'])
    
    def test_second_linear_intervals(self):
        self.assertEqual(second_linear_intervals, ['constant'])
    
    def test_second_quadratic_intervals(self):
        self.assertEqual(second_quadratic_intervals, ['positive'])
    
    def test_second_cubic_intervals(self):
        self.assertEqual(second_cubic_intervals, ['negative', -0.5, 'positive'])
    
    def test_second_hyperbolic_intervals(self):
        self.assertEqual(second_hyperbolic_intervals, ['negative', 0, 'positive'])
    
    def test_second_exponential_intervals(self):
        self.assertEqual(second_exponential_intervals, ['positive'])
    
    def test_second_logarithmic_intervals(self):
        self.assertEqual(second_logarithmic_intervals, ['negative'])
    
    def test_second_logistic_intervals(self):
        self.assertEqual(second_logistic_intervals, ['positive', 5, 'negative'])
    
    def test_second_sinusoidal_intervals(self):
        self.assertEqual(second_sinusoidal_intervals, ['positive', 5, 'negative', 6.0472, 'positive', 7.0944, 'negative', 8.1416, 'positive', 9.1888, 'negative', '5 + 1.0472k'])

class TestRoots(unittest.TestCase):
    def test_linear_zeroes(self):
        linear_zeroes = linear_roots(coefficients[0], coefficients[1], precision)
        self.assertEqual(linear_zeroes, [-1.5])
    
    def test_quadratic_zeroes(self):
        quadratic_zeroes = quadratic_roots(coefficients[0], coefficients[1], coefficients[2], precision)
        self.assertEqual(quadratic_zeroes, [None])
    
    def test_cubic_zeroes(self):
        cubic_zeroes = cubic_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3], precision)
        self.assertEqual(cubic_zeroes, [-1.4455])
    
    def test_hyperbolic_zeroes(self):
        hyperbolic_zeroes = hyperbolic_roots(coefficients[0], coefficients[1], precision)
        self.assertEqual(hyperbolic_zeroes, [-0.6667])
    
    def test_exponential_zeroes(self):
        exponential_zeroes = exponential_roots(coefficients[0], coefficients[1], precision)
        self.assertEqual(exponential_zeroes, [None])
    
    def test_logarithmic_zeroes(self):
        logarithmic_zeroes = logarithmic_roots(coefficients[0], coefficients[1], precision)
        self.assertEqual(logarithmic_zeroes, [0.2231])
    
    def test_logistic_zeroes(self):
        logistic_zeroes = logistic_roots(coefficients[0], coefficients[1], coefficients[2], precision)
        self.assertEqual(logistic_zeroes, [None])
    
    def test_sinusoidal_zeroes(self):
        sinusoidal_zeroes = sinusoidal_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3], precision)
        self.assertEqual(sinusoidal_zeroes, [None])

class TestIntercepts(unittest.TestCase):
    def test_linear_intercepts(self):
        linear_intercepts = intercept_points('linear', coefficients[:2], precision)
        self.assertEqual(linear_intercepts, [-1.5])
    
    def test_quadratic_intercepts(self):
        quadratic_intercepts = intercept_points('quadratic', coefficients[:3], precision)
        self.assertEqual(quadratic_intercepts, [None])
    
    def test_cubic_intercepts(self):
        cubic_intercepts = intercept_points('cubic', coefficients, precision)
        self.assertEqual(cubic_intercepts, [-1.4455])
    
    def test_hyperbolic_intercepts(self):
        hyperbolic_intercepts = intercept_points('hyperbolic', coefficients[:2], precision)
        self.assertEqual(hyperbolic_intercepts, [-0.6667])
    
    def test_exponential_intercepts(self):
        exponential_intercepts = intercept_points('exponential', coefficients[:2], precision)
        self.assertEqual(exponential_intercepts, [None])
    
    def test_logarithmic_intercepts(self):
        logarithmic_intercepts = intercept_points('logarithmic', coefficients[:2], precision)
        self.assertEqual(logarithmic_intercepts, [0.2231])
    
    def test_logistic_intercepts(self):
        logistic_intercepts = intercept_points('logistic', coefficients[:3], precision)
        self.assertEqual(logistic_intercepts, [None])
    
    def test_sinusoidal_intercepts(self):
        sinusoidal_intercepts = intercept_points('sinusoidal', coefficients, precision)
        self.assertEqual(sinusoidal_intercepts, [None])

class TestMaxima(unittest.TestCase):
    def test_linear_maxima(self):
        linear_maxima = maxima_points(first_linear_intervals)
        self.assertEqual(linear_maxima, [None])
    
    def test_quadratic_maxima(self):
        quadratic_maxima = maxima_points(first_quadratic_intervals)
        self.assertEqual(quadratic_maxima, [None])
    
    def test_cubic_maxima(self):
        cubic_maxima = maxima_points(first_cubic_intervals)
        self.assertEqual(cubic_maxima, [None])
    
    def test_hyperbolic_maxima(self):
        hyperbolic_maxima = maxima_points(first_hyperbolic_intervals)
        self.assertEqual(hyperbolic_maxima, [None])
    
    def test_exponential_maxima(self):
        exponential_maxima = maxima_points(first_exponential_intervals)
        self.assertEqual(exponential_maxima, [None])
    
    def test_logarithmic_maxima(self):
        logarithmic_maxima = maxima_points(first_logarithmic_intervals)
        self.assertEqual(logarithmic_maxima, [None])
    
    def test_logistic_maxima(self):
        logistic_maxima = maxima_points(first_logistic_intervals)
        self.assertEqual(logistic_maxima, [None])
    
    def test_sinusoidal_maxima(self):
        sinusoidal_maxima = maxima_points(first_sinusoidal_intervals)
        self.assertEqual(sinusoidal_maxima, [5.5236, 7.618, 9.7124])

class TestMinima(unittest.TestCase):
    def test_linear_minima(self):
        linear_minima = minima_points(first_linear_intervals)
        self.assertEqual(linear_minima, [None])
    
    def test_quadratic_minima(self):
        quadratic_minima = minima_points(first_quadratic_intervals)
        self.assertEqual(quadratic_minima, [-0.75])
    
    def test_cubic_minima(self):
        cubic_minima = minima_points(first_cubic_intervals)
        self.assertEqual(cubic_minima, [None])
    
    def test_hyperbolic_minima(self):
        hyperbolic_minima = minima_points(first_hyperbolic_intervals)
        self.assertEqual(hyperbolic_minima, [None])
    
    def test_exponential_minima(self):
        exponential_minima = minima_points(first_exponential_intervals)
        self.assertEqual(exponential_minima, [None])
    
    def test_logarithmic_minima(self):
        logarithmic_minima = minima_points(first_logarithmic_intervals)
        self.assertEqual(logarithmic_minima, [None])
    
    def test_logistic_minima(self):
        logistic_minima = minima_points(first_logistic_intervals)
        self.assertEqual(logistic_minima, [None])
    
    def test_sinusoidal_minima(self):
        sinusoidal_minima = minima_points(first_sinusoidal_intervals)
        self.assertEqual(sinusoidal_minima, [6.5708, 8.6652])

class TestExtrema(unittest.TestCase):
    def test_linear_extrema(self):
        linear_extrema = extrema_points('linear', coefficients[:2], linear_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(linear_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_quadratic_extrema(self):
        quadratic_extrema = extrema_points('quadratic', coefficients[:3], quadratic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(quadratic_extrema, {'maxima': [None], 'minima': [-0.75]})
    
    def test_cubic_extrema(self):
        cubic_extrema = extrema_points('cubic', coefficients, cubic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(cubic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_hyperbolic_extrema(self):
        hyperbolic_extrema = extrema_points('hyperbolic', coefficients[:2], hyperbolic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(hyperbolic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_exponential_extrema(self):
        exponential_extrema = extrema_points('exponential', coefficients[:2], exponential_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(exponential_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_logarithmic_extrema(self):
        logarithmic_extrema = extrema_points('logarithmic', coefficients[:2], logarithmic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(logarithmic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_logistic_extrema(self):
        logistic_extrema = extrema_points('logistic', coefficients[:3], logistic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(logistic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_sinusoidal_extrema(self):
        sinusoidal_extrema = extrema_points('sinusoidal', coefficients[:3], sinusoidal_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(sinusoidal_extrema, {'maxima': [5.5236, 7.618, 9.7124, '1.0472k'], 'minima': [6.5708, 8.6652, '1.0472k']})

class TestInflections(unittest.TestCase):
    def test_linear_inflections(self):
        linear_inflections = inflection_points('linear', coefficients[:2], linear_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(linear_inflections, [None])
    
    def test_quadratic_inflections(self):
        quadratic_inflections = inflection_points('quadratic', coefficients[:3], quadratic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(quadratic_inflections, [None])
    
    def test_cubic_inflections(self):
        cubic_inflections = inflection_points('cubic', coefficients, cubic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(cubic_inflections, [-0.5])
    
    def test_hyperbolic_inflections(self):
        hyperbolic_inflections = inflection_points('hyperbolic', coefficients[:2], hyperbolic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(hyperbolic_inflections, [None])
    
    def test_exponential_inflections(self):
        exponential_inflections = inflection_points('exponential', coefficients[:2], exponential_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(exponential_inflections, [None])
    
    def test_logarithmic_inflections(self):
        logarithmic_inflections = inflection_points('logarithmic', coefficients[:2], logarithmic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(logarithmic_inflections, [None])
    
    def test_logistic_inflections(self):
        logistic_inflections = inflection_points('logistic', coefficients[:3], logistic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(logistic_inflections, [5])
    
    def test_sinusoidal_inflections(self):
        sinusoidal_inflections = inflection_points('sinusoidal', coefficients[:3], sinusoidal_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(sinusoidal_inflections, [5, 6.0472, 7.0944, 8.1416, 9.1888, '5 + 1.0472k'])

class TestKeyPoints(unittest.TestCase):
    def test_linear_key_points(self):
        linear_key_points = key_coordinates('linear', coefficients[:2], linear_function, linear_derivatives_object['first']['evaluation'], linear_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(linear_key_points, {'roots': [[-1.5, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_key_points(self):
        quadratic_key_points = key_coordinates('quadratic', coefficients[:3], quadratic_function, quadratic_derivatives_object['first']['evaluation'], quadratic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(quadratic_key_points, {'roots': [None], 'maxima': [None], 'minima': [[-0.75, 3.875]], 'inflections': [None]})
    
    def test_cubic_key_points(self):
        cubic_key_points = key_coordinates('cubic', coefficients, cubic_function, cubic_derivatives_object['first']['evaluation'], cubic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(cubic_key_points, {'roots': [[-1.4455, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[-0.5, 5.0]]})
    
    def test_hyperbolic_key_points(self):
        hyperbolic_key_points = key_coordinates('hyperbolic', coefficients[:2], hyperbolic_function, hyperbolic_derivatives_object['first']['evaluation'], hyperbolic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(hyperbolic_key_points, {'roots': [[-0.6667, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_key_points(self):
        exponential_key_points = key_coordinates('exponential', coefficients[:2], exponential_function, exponential_derivatives_object['first']['evaluation'], exponential_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(exponential_key_points, {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_key_points(self):
        logarithmic_key_points = key_coordinates('logarithmic', coefficients[:2], logarithmic_function, logarithmic_derivatives_object['first']['evaluation'], logarithmic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(logarithmic_key_points, {'roots': [[0.2231, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_key_points(self):
        logistic_key_points = key_coordinates('logistic', coefficients[:3], logistic_function, logistic_derivatives_object['first']['evaluation'], logistic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(logistic_key_points, {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[5, 1.0]]})
    
    def test_sinusoidal_key_points(self):
        sinusoidal_key_points = key_coordinates('sinusoidal', coefficients, sinusoidal_function, sinusoidal_derivatives_object['first']['evaluation'], sinusoidal_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(sinusoidal_key_points, {'roots': [None], 'maxima': [[5.5236, 9.0], [7.618, 9.0], [9.7124, 9.0], ['5.5236 + 2.0944k', 9.0]], 'minima': [[6.5708, 5.0], [8.6652, 5.0], ['6.5708 + 2.0944k', 5.0]], 'inflections': [[5, 7.0], [6.0472, 7.0], [7.0944, 7.0], [8.1416, 7.0], [9.1888, 7.0001], ['5 + 1.0472k', 7.0]]})

class TestAccumulation(unittest.TestCase):
    def test_linear_accumulation(self):
        linear_accumulation = accumulated_area(linear_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(linear_accumulation, 330.0)
    
    def test_quadratic_accumulation(self):
        quadratic_accumulation = accumulated_area(quadratic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(quadratic_accumulation, 5166.6667)
    
    def test_cubic_accumulation(self):
        cubic_accumulation = accumulated_area(cubic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(cubic_accumulation, 82820.0)
    
    def test_hyperbolic_accumulation(self):
        hyperbolic_accumulation = accumulated_area(hyperbolic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(hyperbolic_accumulation, 31.3863)
    
    def test_exponential_accumulation(self):
        exponential_accumulation = accumulated_area(exponential_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(exponential_accumulation, 6347508375.7293)
    
    def test_logarithmic_accumulation(self):
        logarithmic_accumulation = accumulated_area(logarithmic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(logarithmic_accumulation, 83.7776)
    
    def test_logistic_accumulation(self):
        logistic_accumulation = accumulated_area(logistic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(logistic_accumulation, 20.0)
    
    def test_sinusoidal_accumulation(self):
        sinusoidal_accumulation = accumulated_area(sinusoidal_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(sinusoidal_accumulation, 69.1433)

class TestAverages(unittest.TestCase):
    def test_linear_averages(self):
        linear_averages = average_values('linear', linear_function, linear_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
        self.assertEqual(linear_averages, {'average_value_derivative': 2.0, 'mean_values_derivative': ['All'], 'average_value_integral': 33.0, 'mean_values_integral': [15.0]})
    
    def test_quadratic_averages(self):
        quadratic_averages = average_values('quadratic', quadratic_function, quadratic_integral_object['evaluation'], 10, 20, coefficients[:3], precision)
        self.assertEqual(quadratic_averages, {'average_value_derivative': 63.0, 'mean_values_derivative': [15.0], 'average_value_integral': 516.6667, 'mean_values_integral': [15.2624]})
    
    def test_cubic_averages(self):
        cubic_averages = average_values('cubic', cubic_function, cubic_integral_object['evaluation'], 10, 20, coefficients, precision)
        self.assertEqual(cubic_averages, {'average_value_derivative': 1495.0, 'mean_values_derivative': [15.2665], 'average_value_integral': 8282.0, 'mean_values_integral': [15.5188]})
    
    def test_hyperbolic_averages(self):
        hyperbolic_averages = average_values('hyperbolic', hyperbolic_function, hyperbolic_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
        self.assertEqual(hyperbolic_averages, {'average_value_derivative': -0.01, 'mean_values_derivative': [14.1421], 'average_value_integral': 3.1386, 'mean_values_integral': [14.43]})
    
    def test_exponential_averages(self):
        exponential_averages = average_values('exponential', exponential_function, exponential_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
        self.assertEqual(exponential_averages, {'average_value_derivative': 697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': 634750837.5729, 'mean_values_integral': [17.8185]})
    
    def test_logarithmic_averages(self):
        logarithmic_averages = average_values('logarithmic', logarithmic_function, logarithmic_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
        self.assertEqual(logarithmic_averages, {'average_value_derivative': 0.1386, 'mean_values_derivative': [14.43], 'average_value_integral': 8.3778, 'mean_values_integral': [14.7155]})
    
    def test_logistic_averages(self):
        logistic_averages = average_values('logistic', logistic_function, logistic_integral_object['evaluation'], 10, 20, coefficients[:3], precision)
        self.assertEqual(logistic_averages, {'average_value_derivative': 0.0001, 'mean_values_derivative': [None], 'average_value_integral': 2.0, 'mean_values_integral': [None]})
    
    def test_sinusoidal_averages(self):
        sinusoidal_averages = average_values('sinusoidal', sinusoidal_function, sinusoidal_integral_object['evaluation'], 10, 20, coefficients, precision)
        self.assertEqual(sinusoidal_averages, {'average_value_derivative': 0.0401, 'mean_values_derivative': [10.7618, 11.8046, 12.8562, 13.899, 14.9506, 15.9933, '10.7618 + 2.0944k', '11.8046 + 2.0944k'], 'average_value_integral': 6.9143, 'mean_values_integral': [10.2503, 11.2689, 12.3447, 13.3633, 14.4391, 15.4577, 16.5335, 17.5521, 18.6279, 19.6465, '10.2503 + 2.0944k', '11.2689 + 2.0944k']})

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 136 tests in 0.017s ---------- OK ---------- #