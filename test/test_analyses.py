import unittest

from library.analyses.equations.linear import linear_equation
from library.analyses.equations.quadratic import quadratic_equation
from library.analyses.equations.cubic import cubic_equation
from library.analyses.equations.hyperbolic import hyperbolic_equation
from library.analyses.equations.exponential import exponential_equation
from library.analyses.equations.logarithmic import logarithmic_equation
from library.analyses.equations.logistic import logistic_equation
from library.analyses.equations.sinusoidal import sinusoidal_equation
from library.analyses.roots.linear import linear_roots, linear_roots_first_derivative, linear_roots_second_derivative, linear_roots_initial_value, linear_roots_derivative_initial_value
from library.analyses.roots.quadratic import quadratic_roots, quadratic_roots_first_derivative, quadratic_roots_second_derivative, quadratic_roots_initial_value, quadratic_roots_derivative_initial_value
from library.analyses.roots.cubic import cubic_roots, cubic_roots_first_derivative, cubic_roots_second_derivative, cubic_roots_initial_value, cubic_roots_derivative_initial_value
from library.analyses.roots.hyperbolic import hyperbolic_roots, hyperbolic_roots_first_derivative, hyperbolic_roots_second_derivative, hyperbolic_roots_initial_value, hyperbolic_roots_derivative_initial_value
from library.analyses.roots.exponential import exponential_roots, exponential_roots_first_derivative, exponential_roots_second_derivative, exponential_roots_initial_value, exponential_roots_derivative_initial_value
from library.analyses.roots.logarithmic import logarithmic_roots, logarithmic_roots_first_derivative, logarithmic_roots_second_derivative, logarithmic_roots_initial_value, logarithmic_roots_derivative_initial_value
from library.analyses.roots.logistic import logistic_roots, logistic_roots_first_derivative, logistic_roots_second_derivative, logistic_roots_initial_value, logistic_roots_derivative_initial_value
from library.analyses.roots.sinusoidal import sinusoidal_roots, sinusoidal_roots_first_derivative, sinusoidal_roots_second_derivative, sinusoidal_roots_initial_value, sinusoidal_roots_derivative_initial_value
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
from library.analyses.points import coordinate_pairs, key_coordinates, points_within_range, shifted_points_within_range, shifted_coordinates_within_range
from library.analyses.accumulation import accumulated_area
from library.analyses.mean_values import average_values

coefficients = [2, 3, 5, 7]

class TestEquations(unittest.TestCase):
    # LINEAR EVALUATIONS
    def test_linear_function_positive(self):
        linear_function_positive = linear_equation(coefficients[0], coefficients[1])(1)
        self.assertEqual(linear_function_positive, 5.0)
    
    def test_linear_function_zero(self):
        linear_function_zero = linear_equation(coefficients[0], coefficients[1])(0)
        self.assertEqual(linear_function_zero, 3.0)
    
    def test_linear_function_negative(self):
        linear_function_negative = linear_equation(coefficients[0], coefficients[1])(-1)
        self.assertEqual(linear_function_negative, 1.0)
    
    # QUADRATIC EVALUATIONS
    def test_quadratic_function_positive(self):
        quadratic_function_positive = quadratic_equation(coefficients[0], coefficients[1], coefficients[2])(1)
        self.assertEqual(quadratic_function_positive, 10.0)
    
    def test_quadratic_function_zero(self):
        quadratic_function_zero = quadratic_equation(coefficients[0], coefficients[1], coefficients[2])(0)
        self.assertEqual(quadratic_function_zero, 5.0)
    
    def test_quadratic_function_negative(self):
        quadratic_function_negative = quadratic_equation(coefficients[0], coefficients[1], coefficients[2])(-1)
        self.assertEqual(quadratic_function_negative, 4.0)
    
    # CUBIC EVALUATIONS
    def test_cubic_function_positive(self):
        cubic_function_positive = cubic_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(1)
        self.assertEqual(cubic_function_positive, 17.0)
    
    def test_cubic_function_zero(self):
        cubic_function_zero = cubic_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(0)
        self.assertEqual(cubic_function_zero, 7.0)
    
    def test_cubic_function_negative(self):
        cubic_function_negative = cubic_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(-1)
        self.assertEqual(cubic_function_negative, 3.0)
    
    # HYPERBOLIC EVALUATIONS
    def test_hyperbolic_function_positive(self):
        hyperbolic_function_positive = hyperbolic_equation(coefficients[0], coefficients[1])(1)
        self.assertEqual(hyperbolic_function_positive, 5.0)
    
    def test_hyperbolic_function_zero(self):
        hyperbolic_function_zero = hyperbolic_equation(coefficients[0], coefficients[1])(0)
        self.assertEqual(hyperbolic_function_zero, 20003.0)
    
    def test_hyperbolic_function_negative(self):
        hyperbolic_function_negative = hyperbolic_equation(coefficients[0], coefficients[1])(-1)
        self.assertEqual(hyperbolic_function_negative, 1.0)
    
    # EXPONENTIAL EVALUATIONS
    def test_exponential_function_positive(self):
        exponential_function_positive = exponential_equation(coefficients[0], coefficients[1])(1)
        self.assertEqual(exponential_function_positive, 6.0)
    
    def test_exponential_function_zero(self):
        exponential_function_zero = exponential_equation(coefficients[0], coefficients[1])(0)
        self.assertEqual(exponential_function_zero, 2.0)
    
    def test_exponential_function_negative(self):
        exponential_function_negative = exponential_equation(coefficients[0], coefficients[1])(-1)
        self.assertEqual(exponential_function_negative, 0.6667)
    
    # LOGARITHMIC EVALUATIONS
    def test_logarithmic_function_positive(self):
        logarithmic_function_positive = logarithmic_equation(coefficients[0], coefficients[1])(1)
        self.assertEqual(logarithmic_function_positive, 3.0)
    
    def test_logarithmic_function_zero(self):
        logarithmic_function_zero = logarithmic_equation(coefficients[0], coefficients[1])(0)
        self.assertEqual(logarithmic_function_zero, -15.4207)
    
    def test_logarithmic_function_negative(self):
        logarithmic_function_negative = logarithmic_equation(coefficients[0], coefficients[1])(-1)
        self.assertEqual(logarithmic_function_negative, 3.0)
    
    # LOGISTIC EVALUATIONS
    def test_logistic_function_positive(self):
        logistic_function_positive = logistic_equation(coefficients[0], coefficients[1], coefficients[2])(1)
        self.assertEqual(logistic_function_positive, 0.0001)
    
    def test_logistic_function_zero(self):
        logistic_function_zero = logistic_equation(coefficients[0], coefficients[1], coefficients[2])(0)
        self.assertEqual(logistic_function_zero, 0.0001)
    
    def test_logistic_function_negative(self):
        logistic_function_negative = logistic_equation(coefficients[0], coefficients[1], coefficients[2])(-1)
        self.assertEqual(logistic_function_negative, 0.0001)
    
    # SINUSOIDAL EVALUATIONS
    def test_sinusoidal_function_positive(self):
        sinusoidal_function_positive = sinusoidal_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(1)
        self.assertEqual(sinusoidal_function_positive, 8.0731)
    
    def test_sinusoidal_function_zero(self):
        sinusoidal_function_zero = sinusoidal_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(0)
        self.assertEqual(sinusoidal_function_zero, 5.6994)
    
    def test_sinusoidal_function_negative(self):
        sinusoidal_function_negative = sinusoidal_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(-1)
        self.assertEqual(sinusoidal_function_negative, 8.502)

class TestDerivatives(unittest.TestCase):
    # LINEAR FIRST DERIVATIVE
    def test_linear_first_derivative_constants(self):
        linear_first_derivative_constants = linear_derivatives(coefficients[0], coefficients[1])['first']['constants']
        self.assertEqual(linear_first_derivative_constants, [2.0])

    def test_linear_first_derivative_evaluation_positive(self):
        linear_first_derivative_evaluation_positive = linear_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](1)
        self.assertEqual(linear_first_derivative_evaluation_positive, 2.0)
    
    def test_linear_first_derivative_evaluation_zero(self):
        linear_first_derivative_evaluation_zero = linear_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](0)
        self.assertEqual(linear_first_derivative_evaluation_zero, 2.0)
    
    def test_linear_first_derivative_evaluation_negative(self):
        linear_first_derivative_evaluation_negative = linear_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](-1)
        self.assertEqual(linear_first_derivative_evaluation_negative, 2.0)
    
    # QUADRATIC FIRST DERIVATIVE
    def test_quadratic_first_derivative_constants(self):
        quadratic_first_derivative_constants = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['constants']
        self.assertEqual(quadratic_first_derivative_constants, [4.0, 3.0])
    
    def test_quadratic_first_derivative_evaluation_positive(self):
        quadratic_first_derivative_evaluation_positive = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](1)
        self.assertEqual(quadratic_first_derivative_evaluation_positive, 7.0)
    
    def test_quadratic_first_derivative_evaluation_zero(self):
        quadratic_first_derivative_evaluation_zero = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](0)
        self.assertEqual(quadratic_first_derivative_evaluation_zero, 3.0)
    
    def test_quadratic_first_derivative_evaluation_negative(self):
        quadratic_first_derivative_evaluation_negative = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](-1)
        self.assertEqual(quadratic_first_derivative_evaluation_negative, -1.0)

    # CUBIC FIRST DERIVATIVE
    def test_cubic_first_derivative_constants(self):
        cubic_first_derivative_constants = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['constants']
        self.assertEqual(cubic_first_derivative_constants, [6.0, 6.0, 5.0])
    
    def test_cubic_first_derivative_evaluation_positive(self):
        cubic_first_derivative_evaluation_positive = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](1)
        self.assertEqual(cubic_first_derivative_evaluation_positive, 17.0)
    
    def test_cubic_first_derivative_evaluation_zero(self):
        cubic_first_derivative_evaluation_zero = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](0)
        self.assertEqual(cubic_first_derivative_evaluation_zero, 5.0)
    
    def test_cubic_first_derivative_evaluation_negative(self):
        cubic_first_derivative_evaluation_negative = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](-1)
        self.assertEqual(cubic_first_derivative_evaluation_negative, 5.0)

    # HYPERBOLIC FIRST DERIVATIVE
    def test_hyperbolic_first_derivative_constants(self):
        hyperbolic_first_derivative_constants = hyperbolic_derivatives(coefficients[0], coefficients[1])['first']['constants']
        self.assertEqual(hyperbolic_first_derivative_constants, [-2.0])
    
    def test_hyperbolic_first_derivative_evaluation_positive(self):
        hyperbolic_first_derivative_evaluation_positive = hyperbolic_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](1)
        self.assertEqual(hyperbolic_first_derivative_evaluation_positive, -2.0)
    
    def test_hyperbolic_first_derivative_evaluation_zero(self):
        hyperbolic_first_derivative_evaluation_zero = hyperbolic_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](0)
        self.assertEqual(hyperbolic_first_derivative_evaluation_zero, -200000000.0)
    
    def test_hyperbolic_first_derivative_evaluation_negative(self):
        hyperbolic_first_derivative_evaluation_negative = hyperbolic_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](-1)
        self.assertEqual(hyperbolic_first_derivative_evaluation_negative, -2.0)

    # EXPONENTIAL FIRST DERIVATIVE
    def test_exponential_first_derivative_constants(self):
        exponential_first_derivative_constants = exponential_derivatives(coefficients[0], coefficients[1])['first']['constants']
        self.assertEqual(exponential_first_derivative_constants, [2.1972, 3.0])
    
    def test_exponential_first_derivative_evaluation_positive(self):
        exponential_first_derivative_evaluation_positive = exponential_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](1)
        self.assertEqual(exponential_first_derivative_evaluation_positive, 6.5916)
    
    def test_exponential_first_derivative_evaluation_zero(self):
        exponential_first_derivative_evaluation_zero = exponential_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](0)
        self.assertEqual(exponential_first_derivative_evaluation_zero, 2.1972)
    
    def test_exponential_first_derivative_evaluation_negative(self):
        exponential_first_derivative_evaluation_negative = exponential_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](-1)
        self.assertEqual(exponential_first_derivative_evaluation_negative, 0.7324)
    
    # LOGARITHMIC FIRST DERIVATIVE
    def test_logarithmic_first_derivative_constants(self):
        logarithmic_first_derivative_constants = logarithmic_derivatives(coefficients[0], coefficients[1])['first']['constants']
        self.assertEqual(logarithmic_first_derivative_constants, [2.0])
    
    def test_logarithmic_first_derivative_evaluation_positive(self):
        logarithmic_first_derivative_evaluation_positive = logarithmic_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](1)
        self.assertEqual(logarithmic_first_derivative_evaluation_positive, 2.0)
    
    def test_logarithmic_first_derivative_evaluation_zero(self):
        logarithmic_first_derivative_evaluation_zero = logarithmic_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](0)
        self.assertEqual(logarithmic_first_derivative_evaluation_zero, 20000.0)
    
    def test_logarithmic_first_derivative_evaluation_negative(self):
        logarithmic_first_derivative_evaluation_negative = logarithmic_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](-1)
        self.assertEqual(logarithmic_first_derivative_evaluation_negative, -2.0)
    
    # LOGISTIC FIRST DERIVATIVE
    def test_logistic_first_derivative_constants(self):
        logistic_first_derivative_constants = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['constants']
        self.assertEqual(logistic_first_derivative_constants, [6.0, 3.0, 5.0])
    
    def test_logistic_first_derivative_evaluation_positive(self):
        logistic_first_derivative_evaluation_positive = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](1)
        self.assertEqual(logistic_first_derivative_evaluation_positive, 0.0001)
    
    def test_logistic_first_derivative_evaluation_zero(self):
        logistic_first_derivative_evaluation_zero = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](0)
        self.assertEqual(logistic_first_derivative_evaluation_zero, 0.0001)
    
    def test_logistic_first_derivative_evaluation_negative(self):
        logistic_first_derivative_evaluation_negative = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](-1)
        self.assertEqual(logistic_first_derivative_evaluation_negative, 0.0001)

    # SINUSOIDAL FIRST DERIVATIVE
    def test_sinusoidal_first_derivative_constants(self):
        sinusoidal_first_derivative_constants = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['constants']
        self.assertEqual(sinusoidal_first_derivative_constants, [6.0, 3.0, 5.0])
    
    def test_sinusoidal_first_derivative_evaluation_positive(self):
        sinusoidal_first_derivative_evaluation_positive = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](1)
        self.assertEqual(sinusoidal_first_derivative_evaluation_positive, 5.0631)
    
    def test_sinusoidal_first_derivative_evaluation_zero(self):
        sinusoidal_first_derivative_evaluation_zero = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](0)
        self.assertEqual(sinusoidal_first_derivative_evaluation_zero, -4.5581)
    
    def test_sinusoidal_first_derivative_evaluation_negative(self):
        sinusoidal_first_derivative_evaluation_negative = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](-1)
        self.assertEqual(sinusoidal_first_derivative_evaluation_negative, 3.9619)

    # LINEAR SECOND DERIVATIVE
    def test_linear_second_derivative_constants(self):
        linear_second_derivative_constants = linear_derivatives(coefficients[0], coefficients[1])['second']['constants']
        self.assertEqual(linear_second_derivative_constants, [0])
    
    def test_linear_second_derivative_evaluation_positive(self):
        linear_second_derivative_evaluation_positive = linear_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](1)
        self.assertEqual(linear_second_derivative_evaluation_positive, 0.0)
    
    def test_linear_second_derivative_evaluation_zero(self):
        linear_second_derivative_evaluation_zero = linear_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](0)
        self.assertEqual(linear_second_derivative_evaluation_zero, 0.0)
    
    def test_linear_second_derivative_evaluation_negative(self):
        linear_second_derivative_evaluation_negative = linear_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](-1)
        self.assertEqual(linear_second_derivative_evaluation_negative, 0.0)
    
    # QUADRATIC SECOND DERIVATIVE
    def test_quadratic_second_derivative_constants(self):
        quadratic_second_derivative_constants = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['constants']
        self.assertEqual(quadratic_second_derivative_constants, [4])
    
    def test_quadratic_second_derivative_evaluation_positive(self):
        quadratic_second_derivative_evaluation_positive = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](1)
        self.assertEqual(quadratic_second_derivative_evaluation_positive, 4.0)
    
    def test_quadratic_second_derivative_evaluation_zero(self):
        quadratic_second_derivative_evaluation_zero = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](0)
        self.assertEqual(quadratic_second_derivative_evaluation_zero, 4.0)
    
    def test_quadratic_second_derivative_evaluation_negative(self):
        quadratic_second_derivative_evaluation_negative = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](-1)
        self.assertEqual(quadratic_second_derivative_evaluation_negative, 4.0)

    # CUBIC SECOND DERIVATIVE
    def test_cubic_second_derivative_constants(self):
        cubic_second_derivative_constants = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['constants']
        self.assertEqual(cubic_second_derivative_constants, [12, 6])
    
    def test_cubic_second_derivative_evaluation_positive(self):
        cubic_second_derivative_evaluation_positive = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](1)
        self.assertEqual(cubic_second_derivative_evaluation_positive, 18.0)
    
    def test_cubic_second_derivative_evaluation_zero(self):
        cubic_second_derivative_evaluation_zero = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](0)
        self.assertEqual(cubic_second_derivative_evaluation_zero, 6.0)
    
    def test_cubic_second_derivative_evaluation_negative(self):
        cubic_second_derivative_evaluation_negative = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](-1)
        self.assertEqual(cubic_second_derivative_evaluation_negative, -6.0)

    # HYPERBOLIC SECOND DERIVATIVE
    def test_hyperbolic_second_derivative_constants(self):
        hyperbolic_second_derivative_constants = hyperbolic_derivatives(coefficients[0], coefficients[1])['second']['constants']
        self.assertEqual(hyperbolic_second_derivative_constants, [4])
    
    def test_hyperbolic_second_derivative_evaluation_positive(self):
        hyperbolic_second_derivative_evaluation_positive = hyperbolic_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](1)
        self.assertEqual(hyperbolic_second_derivative_evaluation_positive, 4.0)
    
    def test_hyperbolic_second_derivative_evaluation_zero(self):
        hyperbolic_second_derivative_evaluation_zero = hyperbolic_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](0)
        self.assertEqual(hyperbolic_second_derivative_evaluation_zero, 3999999999999.9995)
    
    def test_hyperbolic_second_derivative_evaluation_negative(self):
        hyperbolic_second_derivative_evaluation_negative = hyperbolic_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](-1)
        self.assertEqual(hyperbolic_second_derivative_evaluation_negative, -4.0)

    # EXPONENTIAL SECOND DERIVATIVE
    def test_exponential_second_derivative_constants(self):
        exponential_second_derivative_constants = exponential_derivatives(coefficients[0], coefficients[1])['second']['constants']
        self.assertEqual(exponential_second_derivative_constants, [2.4139, 3])
    
    def test_exponential_second_derivative_evaluation_positive(self):
        exponential_second_derivative_evaluation_positive = exponential_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](1)
        self.assertEqual(exponential_second_derivative_evaluation_positive, 7.2417)
    
    def test_exponential_second_derivative_evaluation_zero(self):
        exponential_second_derivative_evaluation_zero = exponential_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](0)
        self.assertEqual(exponential_second_derivative_evaluation_zero, 2.4139)
    
    def test_exponential_second_derivative_evaluation_negative(self):
        exponential_second_derivative_evaluation_negative = exponential_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](-1)
        self.assertEqual(exponential_second_derivative_evaluation_negative, 0.8046)
    
    # LOGARITHMIC SECOND DERIVATIVE
    def test_logarithmic_second_derivative_constants(self):
        logarithmic_second_derivative_constants = logarithmic_derivatives(coefficients[0], coefficients[1])['second']['constants']
        self.assertEqual(logarithmic_second_derivative_constants, [-2.0])
    
    def test_logarithmic_second_derivative_evaluation_positive(self):
        logarithmic_second_derivative_evaluation_positive = logarithmic_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](1)
        self.assertEqual(logarithmic_second_derivative_evaluation_positive, -2.0)
    
    def test_logarithmic_second_derivative_evaluation_zero(self):
        logarithmic_second_derivative_evaluation_zero = logarithmic_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](0)
        self.assertEqual(logarithmic_second_derivative_evaluation_zero, -200000000.0)
    
    def test_logarithmic_second_derivative_evaluation_negative(self):
        logarithmic_second_derivative_evaluation_negative = logarithmic_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](-1)
        self.assertEqual(logarithmic_second_derivative_evaluation_negative, -2.0)
    
    # LOGISTIC SECOND DERIVATIVE
    def test_logistic_second_derivative_constants(self):
        logistic_second_derivative_constants = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['constants']
        self.assertEqual(logistic_second_derivative_constants, [18.0, 3.0, 5.0])
    
    def test_logistic_second_derivative_evaluation_positive(self):
        logistic_second_derivative_evaluation_positive = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](1)
        self.assertEqual(logistic_second_derivative_evaluation_positive, 0.0001)
    
    def test_logistic_second_derivative_evaluation_zero(self):
        logistic_second_derivative_evaluation_zero = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](0)
        self.assertEqual(logistic_second_derivative_evaluation_zero, 0.0001)
    
    def test_logistic_second_derivative_evaluation_negative(self):
        logistic_second_derivative_evaluation_negative = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](-1)
        self.assertEqual(logistic_second_derivative_evaluation_negative, 0.0001)

    # SINUSOIDAL SECOND DERIVATIVE
    def test_sinusoidal_second_derivative_constants(self):
        sinusoidal_second_derivative_constants = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['constants']
        self.assertEqual(sinusoidal_second_derivative_constants, [-18.0, 3.0, 5.0])

    def test_sinusoidal_second_derivative_evaluation_positive(self):
        sinusoidal_second_derivative_evaluation_positive = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](1)
        self.assertEqual(sinusoidal_second_derivative_evaluation_positive, -9.6583)
    
    def test_sinusoidal_second_derivative_evaluation_zero(self):
        sinusoidal_second_derivative_evaluation_zero = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](0)
        self.assertEqual(sinusoidal_second_derivative_evaluation_zero, 11.7052)
    
    def test_sinusoidal_second_derivative_evaluation_negative(self):
        sinusoidal_second_derivative_evaluation_negative = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](-1)
        self.assertEqual(sinusoidal_second_derivative_evaluation_negative, -13.5178)

class TestIntegrals(unittest.TestCase):
    # LINEAR INTEGRAL
    def test_linear_integral_constants(self):
        linear_integral_constants = linear_integral(coefficients[0], coefficients[1])['constants']
        self.assertEqual(linear_integral_constants, [1.0, 3.0])
    
    def test_linear_integral_constants_ones(self):
        linear_integral_constants_ones = linear_integral(1, 1)['constants']
        self.assertEqual(linear_integral_constants_ones, [0.5, 1.0])
    
    def test_linear_integral_evaluation_positive(self):
        linear_integral_evaluation_positive = linear_integral(coefficients[0], coefficients[1])['evaluation'](1)
        self.assertEqual(linear_integral_evaluation_positive, 4.0)
    
    def test_linear_integral_evaluation_zero(self):
        linear_integral_evaluation_zero = linear_integral(coefficients[0], coefficients[1])['evaluation'](0)
        self.assertEqual(linear_integral_evaluation_zero, 0.0)
    
    def test_linear_integral_evaluation_negative(self):
        linear_integral_evaluation_negative = linear_integral(coefficients[0], coefficients[1])['evaluation'](-1)
        self.assertEqual(linear_integral_evaluation_negative, -2.0)
    
    # QUADRATIC INTEGRAL
    def test_quadratic_integral_constants(self):
        quadratic_integral_constants = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])['constants']
        self.assertEqual(quadratic_integral_constants, [0.6667, 1.5, 5.0])
    
    def test_quadratic_integral_constants_ones(self):
        quadratic_integral_constants_ones = quadratic_integral(1, 1, 1)['constants']
        self.assertEqual(quadratic_integral_constants_ones, [0.3333, 0.5, 1.0])
    
    def test_quadratic_integral_evaluation_positive(self):
        quadratic_integral_evaluation_positive = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](1)
        self.assertEqual(quadratic_integral_evaluation_positive, 7.1667)
    
    def test_quadratic_integral_evaluation_zero(self):
        quadratic_integral_evaluation_zero = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](0)
        self.assertEqual(quadratic_integral_evaluation_zero, 0.0)
    
    def test_quadratic_integral_evaluation_negative(self):
        quadratic_integral_evaluation_negative = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](-1)
        self.assertEqual(quadratic_integral_evaluation_negative, -4.1667)
    
    # CUBIC INTEGRAL
    def test_cubic_integral_constants(self):
        cubic_integral_constants = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['constants']
        self.assertEqual(cubic_integral_constants, [0.5, 1.0, 2.5, 7.0])
    
    def test_cubic_integral_constants_ones(self):
        cubic_integral_constants_ones = cubic_integral(1, 1, 1, 1)['constants']
        self.assertEqual(cubic_integral_constants_ones, [0.25, 0.3333, 0.5, 1.0])
    
    def test_cubic_integral_evaluation_positive(self):
        cubic_integral_evaluation_positive = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](1)
        self.assertEqual(cubic_integral_evaluation_positive, 11.0)
    
    def test_cubic_integral_evaluation_zero(self):
        cubic_integral_evaluation_zero = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](0)
        self.assertEqual(cubic_integral_evaluation_zero, 0.0)
    
    def test_cubic_integral_evaluation_negative(self):
        cubic_integral_evaluation_negative = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](-1)
        self.assertEqual(cubic_integral_evaluation_negative, -5.0)
    
    # HYPERBOLIC INTEGRAL
    def test_hyperbolic_integral_constants(self):
        hyperbolic_integral_constants = hyperbolic_integral(coefficients[0], coefficients[1])['constants']
        self.assertEqual(hyperbolic_integral_constants, [2.0, 3.0])
    
    def test_hyperbolic_integral_constants_ones(self):
        hyperbolic_integral_constants_ones = hyperbolic_integral(1, 1)['constants']
        self.assertEqual(hyperbolic_integral_constants_ones, [1.0, 1.0])
    
    def test_hyperbolic_integral_evaluation_positive(self):
        hyperbolic_integral_evaluation_positive = hyperbolic_integral(coefficients[0], coefficients[1])['evaluation'](1)
        self.assertEqual(hyperbolic_integral_evaluation_positive, 3.0)
    
    def test_hyperbolic_integral_evaluation_zero(self):
        hyperbolic_integral_evaluation_zero = hyperbolic_integral(coefficients[0], coefficients[1])['evaluation'](0)
        self.assertEqual(hyperbolic_integral_evaluation_zero, -18.4204)
    
    def test_hyperbolic_integral_evaluation_negative(self):
        hyperbolic_integral_evaluation_negative = hyperbolic_integral(coefficients[0], coefficients[1])['evaluation'](-1)
        self.assertEqual(hyperbolic_integral_evaluation_negative, -3.0)
    
    # EXPONENTIAL INTEGRAL
    def test_exponential_integral_constants(self):
        exponential_integral_constants = exponential_integral(coefficients[0], coefficients[1])['constants']
        self.assertEqual(exponential_integral_constants, [1.8205, 3.0])
    
    def test_exponential_integral_constants_ones(self):
        exponential_integral_constants_ones = exponential_integral(1, 1)['constants']
        self.assertEqual(exponential_integral_constants_ones, [10000.5, 1.0001])
    
    def test_exponential_integral_evaluation_positive(self):
        exponential_integral_evaluation_positive = exponential_integral(coefficients[0], coefficients[1])['evaluation'](1)
        self.assertEqual(exponential_integral_evaluation_positive, 5.4615)
    
    def test_exponential_integral_evaluation_zero(self):
        exponential_integral_evaluation_zero = exponential_integral(coefficients[0], coefficients[1])['evaluation'](0)
        self.assertEqual(exponential_integral_evaluation_zero, 1.8205)
    
    def test_exponential_integral_evaluation_negative(self):
        exponential_integral_evaluation_negative = exponential_integral(coefficients[0], coefficients[1])['evaluation'](-1)
        self.assertEqual(exponential_integral_evaluation_negative, 0.6068)
    
    # LOGARITHMIC INTEGRAL
    def test_logarithmic_integral_constants(self):
        logarithmic_integral_constants = logarithmic_integral(coefficients[0], coefficients[1])['constants']
        self.assertEqual(logarithmic_integral_constants, [2.0, 3.0])
    
    def test_logarithmic_integral_constants_ones(self):
        logarithmic_integral_constants_ones = logarithmic_integral(1, 1)['constants']
        self.assertEqual(logarithmic_integral_constants_ones, [1.0, 1.0])
    
    def test_logarithmic_integral_evaluation_positive(self):
        logarithmic_integral_evaluation_positive = logarithmic_integral(coefficients[0], coefficients[1])['evaluation'](1)
        self.assertEqual(logarithmic_integral_evaluation_positive, 1.0)
    
    def test_logarithmic_integral_evaluation_zero(self):
        logarithmic_integral_evaluation_zero = logarithmic_integral(coefficients[0], coefficients[1])['evaluation'](0)
        self.assertEqual(logarithmic_integral_evaluation_zero, -0.0017)
    
    def test_logarithmic_integral_evaluation_negative(self):
        logarithmic_integral_evaluation_negative = logarithmic_integral(coefficients[0], coefficients[1])['evaluation'](-1)
        self.assertEqual(logarithmic_integral_evaluation_negative, -1.0)
    
    # LOGISTIC INTEGRAL
    def test_logistic_integral_constants(self):
        logistic_integral_constants = logistic_integral(coefficients[0], coefficients[1], coefficients[2])['constants']
        self.assertEqual(logistic_integral_constants, [0.6667, 3.0, 5.0])
    
    def test_logistic_integral_constants_ones(self):
        logistic_integral_constants_ones = logistic_integral(1, 1, 1)['constants']
        self.assertEqual(logistic_integral_constants_ones, [1.0, 1.0, 1.0])
    
    def test_logistic_integral_evaluation_positive(self):
        logistic_integral_evaluation_positive = logistic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](1)
        self.assertEqual(logistic_integral_evaluation_positive, 0.0001)
    
    def test_logistic_integral_evaluation_zero(self):
        logistic_integral_evaluation_zero = logistic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](0)
        self.assertEqual(logistic_integral_evaluation_zero, 0.0001)
    
    def test_logistic_integral_evaluation_negative(self):
        logistic_integral_evaluation_negative = logistic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](-1)
        self.assertEqual(logistic_integral_evaluation_negative, 0.0001)
    
    # SINUSOIDAL INTEGRAL
    def test_sinusoidal_integral_constants(self):
        sinusoidal_integral_constants = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['constants']
        self.assertEqual(sinusoidal_integral_constants, [-0.6667, 3.0, 5.0, 7.0])
    
    def test_sinusoidal_integral_constants_ones(self):
        sinusoidal_integral_constants_ones = sinusoidal_integral(1, 1, 1, 1)['constants']
        self.assertEqual(sinusoidal_integral_constants_ones, [-1.0, 1.0, 1.0, 1.0])
    
    def test_sinusoidal_integral_evaluation_positive(self):
        sinusoidal_integral_evaluation_positive = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](1)
        self.assertEqual(sinusoidal_integral_evaluation_positive, 6.4374)
    
    def test_sinusoidal_integral_evaluation_zero(self):
        sinusoidal_integral_evaluation_zero = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](0)
        self.assertEqual(sinusoidal_integral_evaluation_zero, 0.5065)
    
    def test_sinusoidal_integral_evaluation_negative(self):
        sinusoidal_integral_evaluation_negative = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](-1)
        self.assertEqual(sinusoidal_integral_evaluation_negative, -7.4402)

class TestCriticalPoints(unittest.TestCase):
    # FIRST DERIVATIVE CRITICAL POINTS
    def test_first_linear_critical_points(self):
        first_linear_critical_points = critical_points('linear', coefficients[:2], 1)
        self.assertEqual(first_linear_critical_points, [None])
    
    def test_first_quadratic_critical_points(self):
        first_quadratic_critical_points = critical_points('quadratic', coefficients[:3], 1)
        self.assertEqual(first_quadratic_critical_points, [-0.75])
    
    def test_first_cubic_critical_points_none(self):
        first_cubic_critical_points_none = critical_points('cubic', coefficients[:4], 1)
        self.assertEqual(first_cubic_critical_points_none, [None])
    
    def test_first_cubic_critical_points_one(self):
        first_cubic_critical_points_one = critical_points('cubic', [1, 3, 3, 7], 1)
        self.assertEqual(first_cubic_critical_points_one, [-1.0])
    
    def test_first_cubic_critical_points_two(self):
        first_cubic_critical_points_two = critical_points('cubic', [2, -15, 36, 7], 1)
        self.assertEqual(first_cubic_critical_points_two, [2.0, 3.0])
    
    def test_first_hyperbolic_critical_points(self):
        first_hyperbolic_critical_points = critical_points('hyperbolic', coefficients[:2], 1)
        self.assertEqual(first_hyperbolic_critical_points, [0])
    
    def test_first_exponential_critical_points(self):
        first_exponential_critical_points = critical_points('exponential', coefficients[:2], 1)
        self.assertEqual(first_exponential_critical_points, [None])
    
    def test_first_logarithmic_critical_points(self):
        first_logarithmic_critical_points = critical_points('logarithmic', coefficients[:2], 1)
        self.assertEqual(first_logarithmic_critical_points, [None])
    
    def test_first_logistic_critical_points(self):
        first_logistic_critical_points = critical_points('logistic', coefficients[:3], 1)
        self.assertEqual(first_logistic_critical_points, [None])
    
    def test_first_sinusoidal_critical_points(self):
        first_sinusoidal_critical_points = critical_points('sinusoidal', coefficients[:4], 1)
        self.assertEqual(first_sinusoidal_critical_points, [5.5236, 6.5708, 7.618, 8.6652, 9.7124, '5.5236 + 1.0472k'])
    
    # SECOND DERIVATIVE CRITICAL POINTS
    def test_second_linear_critical_points(self):
        second_linear_critical_points = critical_points('linear', coefficients[:2], 2)
        self.assertEqual(second_linear_critical_points, [None])
    
    def test_second_quadratic_critical_points(self):
        second_quadratic_critical_points = critical_points('quadratic', coefficients[:3], 2)
        self.assertEqual(second_quadratic_critical_points, [None])
    
    def test_second_cubic_critical_points(self):
        second_cubic_critical_points = critical_points('cubic', coefficients[:4], 2)
        self.assertEqual(second_cubic_critical_points, [-0.5])
    
    def test_second_hyperbolic_critical_points(self):
        second_hyperbolic_critical_points = critical_points('hyperbolic', coefficients[:2], 2)
        self.assertEqual(second_hyperbolic_critical_points, [0])
    
    def test_second_exponential_critical_points(self):
        second_exponential_critical_points = critical_points('exponential', coefficients[:2], 2)
        self.assertEqual(second_exponential_critical_points, [None])
    
    def test_second_logarithmic_critical_points(self):
        second_logarithmic_critical_points = critical_points('logarithmic', coefficients[:2], 2)
        self.assertEqual(second_logarithmic_critical_points, [None])
    
    def test_second_logistic_critical_points(self):
        second_logistic_critical_points = critical_points('logistic', coefficients[:3], 2)
        self.assertEqual(second_logistic_critical_points, [5])
    
    def test_second_sinusoidal_critical_points(self):
        second_sinusoidal_critical_points = critical_points('sinusoidal', coefficients[:4], 2)
        self.assertEqual(second_sinusoidal_critical_points, [5.0, 6.0472, 7.0944, 8.1416, 9.1888, '5.0 + 1.0472k'])

class TestIntervals(unittest.TestCase):
    maxDiff = None

    # FIRST DERIVATIVE SIGN CHARTS
    def test_first_linear_intervals(self):
        first_linear_intervals = sign_chart('linear', coefficients[:2], 1)
        self.assertEqual(first_linear_intervals, ['positive'])
    
    def test_first_quadratic_intervals(self):
        first_quadratic_intervals = sign_chart('quadratic', coefficients[:3], 1)
        self.assertEqual(first_quadratic_intervals, ['negative', -0.75, 'positive'])
    
    def test_first_cubic_intervals_none(self):
        first_cubic_intervals_none = sign_chart('cubic', coefficients[:4], 1)
        self.assertEqual(first_cubic_intervals_none, ['positive'])
    
    def test_first_cubic_intervals_one(self):
        first_cubic_intervals_one = sign_chart('cubic', [1, 3, 3, 7], 1)
        self.assertEqual(first_cubic_intervals_one, ['positive', -1.0, 'positive'])
    
    def test_first_cubic_intervals_two(self):
        first_cubic_intervals_two = sign_chart('cubic', [2, -15, 36, 7], 1)
        self.assertEqual(first_cubic_intervals_two, ['positive', 2.0, 'negative', 3.0, 'positive'])

    def test_first_hyperbolic_intervals(self):
        first_hyperbolic_intervals = sign_chart('hyperbolic', coefficients[:2], 1)
        self.assertEqual(first_hyperbolic_intervals, ['negative', 0, 'negative'])
    
    def test_first_exponential_intervals(self):
        first_exponential_intervals = sign_chart('exponential', coefficients[:2], 1)
        self.assertEqual(first_exponential_intervals, ['positive'])
    
    def test_first_logarithmic_intervals(self):
        first_logarithmic_intervals = sign_chart('logarithmic', coefficients[:2], 1)
        self.assertEqual(first_logarithmic_intervals, ['positive'])
    
    def test_first_logistic_intervals(self):
        first_logistic_intervals = sign_chart('logistic', coefficients[:3], 1)
        self.assertEqual(first_logistic_intervals, ['positive'])
    
    def test_first_sinusoidal_intervals(self):
        first_sinusoidal_intervals = sign_chart('sinusoidal', coefficients[:4], 1)
        self.assertEqual(first_sinusoidal_intervals, ['positive', 5.5236, 'negative', 6.5708, 'positive', 7.618, 'negative', 8.6652, 'positive', 9.7124, 'negative', '5.5236 + 1.0472k'])
    
    # SECOND DERIVATIVE SIGN CHARTS
    def test_second_linear_intervals(self):
        second_linear_intervals = sign_chart('linear', coefficients[:2], 2)
        self.assertEqual(second_linear_intervals, ['constant'])
    
    def test_second_quadratic_intervals(self):
        second_quadratic_intervals = sign_chart('quadratic', coefficients[:3], 2)
        self.assertEqual(second_quadratic_intervals, ['positive'])
    
    def test_second_cubic_intervals(self):
        second_cubic_intervals = sign_chart('cubic', coefficients[:4], 2)
        self.assertEqual(second_cubic_intervals, ['negative', -0.5, 'positive'])
    
    def test_second_hyperbolic_intervals(self):
        second_hyperbolic_intervals = sign_chart('hyperbolic', coefficients[:2], 2)
        self.assertEqual(second_hyperbolic_intervals, ['negative', 0, 'positive'])
    
    def test_second_exponential_intervals(self):
        second_exponential_intervals = sign_chart('exponential', coefficients[:2], 2)
        self.assertEqual(second_exponential_intervals, ['positive'])
    
    def test_second_logarithmic_intervals(self):
        second_logarithmic_intervals = sign_chart('logarithmic', coefficients[:2], 2)
        self.assertEqual(second_logarithmic_intervals, ['negative'])
    
    def test_second_logistic_intervals(self):
        second_logistic_intervals = sign_chart('logistic', coefficients[:3], 2)
        self.assertEqual(second_logistic_intervals, ['positive', 5, 'negative'])
    
    def test_second_sinusoidal_intervals(self):
        second_sinusoidal_intervals = sign_chart('sinusoidal', coefficients[:4], 2)
        self.assertEqual(second_sinusoidal_intervals, ['positive', 5.0, 'negative', 6.0472, 'positive', 7.0944, 'negative', 8.1416, 'positive', 9.1888, 'negative', '5.0 + 1.0472k'])

class TestRoots(unittest.TestCase):
    maxDiff = None

    # LINEAR ROOTS
    def test_linear_zeroes(self):
        linear_zeroes = linear_roots(coefficients[0], coefficients[1])
        self.assertEqual(linear_zeroes, [-1.5])
    
    def test_linear_zeroes_first_derivative(self):
        linear_zeroes_first_derivative = linear_roots_first_derivative(coefficients[0], coefficients[1])
        self.assertEqual(linear_zeroes_first_derivative, [None])
    
    def test_linear_zeroes_second_derivative(self):
        linear_zeroes_second_derivative = linear_roots_second_derivative(coefficients[0], coefficients[1])
        self.assertEqual(linear_zeroes_second_derivative, [None])
    
    def test_linear_zeroes_initial_value(self):
        linear_zeroes_initial_value = linear_roots_initial_value(coefficients[0], coefficients[1], 10)
        self.assertEqual(linear_zeroes_initial_value, [3.5])
    
    def test_linear_zeroes_derivative_initial_value_all(self):
        linear_zeroes_derivative_initial_value_all = linear_roots_derivative_initial_value(coefficients[0], coefficients[1], 2)
        self.assertEqual(linear_zeroes_derivative_initial_value_all, ['All'])
    
    def test_linear_zeroes_derivative_initial_value_none(self):
        linear_zeroes_derivative_initial_value_none = linear_roots_derivative_initial_value(coefficients[0], coefficients[1], 10)
        self.assertEqual(linear_zeroes_derivative_initial_value_none, [None])
    
    # QUADRATIC ROOTS
    def test_quadratic_zeroes_none(self):
        quadratic_zeroes_none = quadratic_roots(coefficients[0], coefficients[1], coefficients[2])
        self.assertEqual(quadratic_zeroes_none, [None])
    
    def test_quadratic_zeroes_one(self):
        quadratic_zeroes_one = quadratic_roots(1, -2, 1)
        self.assertEqual(quadratic_zeroes_one, [1.0])
    
    def test_quadratic_zeroes_two(self):
        quadratic_zeroes_two = quadratic_roots(1, -5, 6)
        self.assertEqual(quadratic_zeroes_two, [2.0, 3.0])

    def test_quadratic_zeroes_first_derivative(self):
        quadratic_zeroes_first_derivative = quadratic_roots_first_derivative(coefficients[0], coefficients[1], coefficients[2])
        self.assertEqual(quadratic_zeroes_first_derivative, [-0.75])
    
    def test_quadratic_zeroes_second_derivative(self):
        quadratic_zeroes_second_derivative = quadratic_roots_second_derivative(coefficients[0], coefficients[1], coefficients[2])
        self.assertEqual(quadratic_zeroes_second_derivative, [None])
    
    def test_quadratic_zeroes_initial_value_none(self):
        quadratic_zeroes_initial_value_none = quadratic_roots_initial_value(coefficients[0], coefficients[1], coefficients[2], -10)
        self.assertEqual(quadratic_zeroes_initial_value_none, [None])
    
    def test_quadratic_zeroes_initial_value_one(self):
        quadratic_zeroes_initial_value_one = quadratic_roots_initial_value(1, 2, 2, 1)
        self.assertEqual(quadratic_zeroes_initial_value_one, [-1.0])
    
    def test_quadratic_zeroes_initial_value_two(self):
        quadratic_zeroes_initial_value_two = quadratic_roots_initial_value(coefficients[0], coefficients[1], coefficients[2], 10)
        self.assertEqual(quadratic_zeroes_initial_value_two, [-2.5, 1.0])
    
    def test_quadratic_zeroes_derivative_initial_value(self):
        quadratic_zeroes_derivative_initial_value = quadratic_roots_derivative_initial_value(coefficients[0], coefficients[1], coefficients[2], 10)
        self.assertEqual(quadratic_zeroes_derivative_initial_value, [1.75])

    # CUBIC ROOTS
    def test_cubic_zeroes_one(self):
        cubic_zeroes_one = cubic_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        self.assertEqual(cubic_zeroes_one, [-1.4455])
    
    def test_cubic_zeroes_two(self):
        cubic_zeroes_two = cubic_roots(1, -4, 5, -2)
        self.assertEqual(cubic_zeroes_two, [1.0, 2.0])
    
    def test_cubic_zeroes_three(self):
        cubic_zeroes_three = cubic_roots(1, -10, 31, -30)
        self.assertEqual(cubic_zeroes_three, [2.0, 3.0, 5.0])

    def test_cubic_zeroes_first_derivative_none(self):
        cubic_zeroes_first_derivative_none = cubic_roots_first_derivative(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        self.assertEqual(cubic_zeroes_first_derivative_none, [None])

    def test_cubic_zeroes_first_derivative_one(self):
        cubic_zeroes_first_derivative_one = cubic_roots_first_derivative(3, 3, 1, 7)
        self.assertEqual(cubic_zeroes_first_derivative_one, [-0.3333])
    
    def test_cubic_zeroes_first_derivative_two(self):
        cubic_zeroes_first_derivative_two = cubic_roots_first_derivative(2, 7, 3, 5)
        self.assertEqual(cubic_zeroes_first_derivative_two, [-2.0946, -0.2387])
    
    def test_cubic_zeroes_second_derivative(self):
        cubic_zeroes_second_derivative = cubic_roots_second_derivative(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        self.assertEqual(cubic_zeroes_second_derivative, [-0.5])
    
    def test_cubic_zeroes_initial_value_one(self):
        cubic_zeroes_initial_value_one = cubic_roots_initial_value(coefficients[0], coefficients[1], coefficients[2], coefficients[3], 10)
        self.assertEqual(cubic_zeroes_initial_value_one, [0.4455])
    
    def test_cubic_zeroes_initial_value_two(self):
        cubic_zeroes_initial_value_two = cubic_roots_initial_value(1, -4, 5, 7, 9)
        self.assertEqual(cubic_zeroes_initial_value_two, [1.0, 2.0])
    
    def test_cubic_zeroes_initial_value_three(self):
        cubic_zeroes_initial_value_three = cubic_roots_initial_value(1, -10, 31, -20, 10)
        self.assertEqual(cubic_zeroes_initial_value_three, [2.0, 3.0, 5.0])

    def test_cubic_zeroes_derivative_initial_value_none(self):
        cubic_zeroes_derivative_initial_value_none = cubic_roots_derivative_initial_value(7, 2, 5, 3, -10)
        self.assertEqual(cubic_zeroes_derivative_initial_value_none, [None])

    def test_cubic_zeroes_derivative_initial_value_one(self):
        cubic_zeroes_derivative_initial_value_one = cubic_roots_derivative_initial_value(3, 3, 11, 1, 10)
        self.assertEqual(cubic_zeroes_derivative_initial_value_one, [-0.3333])
    
    def test_cubic_zeroes_derivative_initial_value_two(self):
        cubic_zeroes_derivative_initial_value_two = cubic_roots_derivative_initial_value(coefficients[0], coefficients[1], coefficients[2], coefficients[3], 10)
        self.assertEqual(cubic_zeroes_derivative_initial_value_two, [-1.5408, 0.5408])

    # HYPERBOLIC ROOTS
    def test_hyperbolic_zeroes(self):
        hyperbolic_zeroes = hyperbolic_roots(coefficients[0], coefficients[1])
        self.assertEqual(hyperbolic_zeroes, [-0.6667])
    
    def test_hyperbolic_zeroes_first_derivative(self):
        hyperbolic_zeroes_first_derivative = hyperbolic_roots_first_derivative(coefficients[0], coefficients[1])
        self.assertEqual(hyperbolic_zeroes_first_derivative, [0.0])
    
    def test_hyperbolic_zeroes_second_derivative(self):
        hyperbolic_zeroes_second_derivative = hyperbolic_roots_second_derivative(coefficients[0], coefficients[1])
        self.assertEqual(hyperbolic_zeroes_second_derivative, [0.0])
    
    def test_hyperbolic_zeroes_initial_value(self):
        hyperbolic_zeroes_initial_value = hyperbolic_roots_initial_value(coefficients[0], coefficients[1], 10)
        self.assertEqual(hyperbolic_zeroes_initial_value, [0.2857])
    
    def test_hyperbolic_zeroes_derivative_initial_value_none(self):
        hyperbolic_zeroes_derivative_initial_value_none = hyperbolic_roots_derivative_initial_value(coefficients[0], coefficients[1], 10)
        self.assertEqual(hyperbolic_zeroes_derivative_initial_value_none, [None])
    
    def test_hyperbolic_zeroes_derivative_initial_value_one(self):
        hyperbolic_zeroes_derivative_initial_value_one = hyperbolic_roots_derivative_initial_value(coefficients[0], coefficients[1], -10)
        self.assertEqual(hyperbolic_zeroes_derivative_initial_value_one, [0.4472])

    # EXPONENTIAL ROOTS
    def test_exponential_zeroes(self):
        exponential_zeroes = exponential_roots(coefficients[0], coefficients[1])
        self.assertEqual(exponential_zeroes, [None])
    
    def test_exponential_zeroes_first_derivative(self):
        exponential_zeroes_first_derivative = exponential_roots_first_derivative(coefficients[0], coefficients[1])
        self.assertEqual(exponential_zeroes_first_derivative, [None])
    
    def test_exponential_zeroes_second_derivative(self):
        exponential_zeroes_second_derivative = exponential_roots_second_derivative(coefficients[0], coefficients[1])
        self.assertEqual(exponential_zeroes_second_derivative, [None])
    
    def test_exponential_zeroes_initial_value(self):
        exponential_zeroes_initial_value = exponential_roots_initial_value(coefficients[0], coefficients[1], 10)
        self.assertEqual(exponential_zeroes_initial_value, [1.465])
    
    def test_exponential_zeroes_initial_value_log1(self):
        exponential_zeroes_initial_value_log1 = exponential_roots_initial_value(2, 1, 10)
        self.assertEqual(exponential_zeroes_initial_value_log1, [16094.3791])
    
    def test_exponential_zeroes_derivative_initial_value(self):
        exponential_zeroes_derivative_initial_value = exponential_roots_derivative_initial_value(coefficients[0], coefficients[1], 10)
        self.assertEqual(exponential_zeroes_derivative_initial_value, [1.3794])
    
    def test_exponential_zeroes_derivative_initial_value_log1(self):
        exponential_zeroes_derivative_initial_value_log1 = exponential_roots_derivative_initial_value(2, 1, -10)
        self.assertEqual(exponential_zeroes_derivative_initial_value_log1, [108197.7828])

    # LOGARITHMIC ROOTS
    def test_logarithmic_zeroes(self):
        logarithmic_zeroes = logarithmic_roots(coefficients[0], coefficients[1])
        self.assertEqual(logarithmic_zeroes, [0.2231])
    
    def test_logarithmic_zeroes_first_derivative(self):
        logarithmic_zeroes_first_derivative = logarithmic_roots_first_derivative(coefficients[0], coefficients[1])
        self.assertEqual(logarithmic_zeroes_first_derivative, [None])
    
    def test_logarithmic_zeroes_second_derivative(self):
        logarithmic_zeroes_second_derivative = logarithmic_roots_second_derivative(coefficients[0], coefficients[1])
        self.assertEqual(logarithmic_zeroes_second_derivative, [None])
    
    def test_logarithmic_zeroes_initial_value(self):
        logarithmic_zeroes_initial_value = logarithmic_roots_initial_value(coefficients[0], coefficients[1], 10)
        self.assertEqual(logarithmic_zeroes_initial_value, [33.1155])
    
    def test_logarithmic_zeroes_derivative_initial_value(self):
        logarithmic_zeroes_derivative_initial_value = logarithmic_roots_derivative_initial_value(coefficients[0], coefficients[1], 10)
        self.assertEqual(logarithmic_zeroes_derivative_initial_value, [0.2])
    
    # LOGISTIC ROOTS
    def test_logistic_zeroes(self):
        logistic_zeroes = logistic_roots(coefficients[0], coefficients[1], coefficients[2])
        self.assertEqual(logistic_zeroes, [None])
    
    def test_logistic_zeroes_first_derivative(self):
        logistic_zeroes_first_derivative = logistic_roots_first_derivative(coefficients[0], coefficients[1], coefficients[2])
        self.assertEqual(logistic_zeroes_first_derivative, [None])
    
    def test_logistic_zeroes_second_derivative(self):
        logistic_zeroes_second_derivative = logistic_roots_second_derivative(coefficients[0], coefficients[1], coefficients[2])
        self.assertEqual(logistic_zeroes_second_derivative, [5.0])
    
    def test_logistic_zeroes_initial_value(self):
        logistic_zeroes_initial_value = logistic_roots_initial_value(coefficients[0], coefficients[1], coefficients[2], 10)
        self.assertEqual(logistic_zeroes_initial_value, [5.0744])
    
    def test_logistic_zeroes_initial_value_log0(self):
        logistic_zeroes_initial_value_log0 = logistic_roots_initial_value(1, 2, 3, 1)
        self.assertEqual(logistic_zeroes_initial_value_log0, [7.6052])
    
    def test_logistic_zeroes_derivative_initial_value_none(self):
        logistic_zeroes_derivative_initial_value_none = logistic_roots_derivative_initial_value(coefficients[0], coefficients[1], coefficients[2], 10)
        self.assertEqual(logistic_zeroes_derivative_initial_value_none, [None])
    
    def test_logistic_zeroes_derivative_initial_value_one(self):
        logistic_zeroes_derivative_initial_value_one = logistic_roots_derivative_initial_value(1, 4, 2, 1)
        self.assertEqual(logistic_zeroes_derivative_initial_value_one, [2.0])
    
    def test_logistic_zeroes_derivative_initial_value_two(self):
        logistic_zeroes_derivative_initial_value_two = logistic_roots_derivative_initial_value(7, 5, 3, 2)
        self.assertEqual(logistic_zeroes_derivative_initial_value_two, [2.4527, 3.5473])

    # SINUSOIDAL ROOTS
    def test_sinusoidal_zeroes_none(self):
        sinusoidal_zeroes_none = sinusoidal_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        self.assertEqual(sinusoidal_zeroes_none, [None])
    
    def test_sinusoidal_zeroes_many_bounce(self):
        sinusoidal_zeroes_many_bounce = sinusoidal_roots(2, 3, 5, 2)
        self.assertEqual(sinusoidal_zeroes_many_bounce, [4.4764, 6.5708, 8.6652, 10.7596, 12.854, '4.4764 + 2.0944k'])
    
    def test_sinusoidal_zeroes_many_cross(self):
        sinusoidal_zeroes_many_cross = sinusoidal_roots(2, 3, 5, 1)
        self.assertEqual(sinusoidal_zeroes_many_cross, [4.8255, 6.2217, 6.9199, 8.3161, 9.0143, 10.4105, 11.1087, 12.5049, 13.203, 14.5993, '4.8255 + 2.0944k', '6.2217 + 2.0944k'])

    def test_sinusoidal_zeroes_first_derivative(self):
        sinusoidal_zeroes_first_derivative = sinusoidal_roots_first_derivative(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        self.assertEqual(sinusoidal_zeroes_first_derivative, [5.5236, 6.5708, 7.618, 8.6652, 9.7124, '5.5236 + 1.0472k'])
    
    def test_sinusoidal_zeroes_second_derivative(self):
        sinusoidal_zeroes_second_derivative = sinusoidal_roots_second_derivative(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        self.assertEqual(sinusoidal_zeroes_second_derivative, [5.0, 6.0472, 7.0944, 8.1416, 9.1888, '5.0 + 1.0472k'])
    
    def test_sinusoidal_zeroes_initial_value_none(self):
        sinusoidal_zeroes_initial_value_none = sinusoidal_roots_initial_value(coefficients[0], coefficients[1], coefficients[2], coefficients[3], 10)
        self.assertEqual(sinusoidal_zeroes_initial_value_none, [None])

    def test_sinusoidal_zeroes_initial_value_many_bounce(self):
        sinusoidal_zeroes_initial_value_many_bounce = sinusoidal_roots_initial_value(2, 3, 5, 9, 7)
        self.assertEqual(sinusoidal_zeroes_initial_value_many_bounce, [4.4764, 6.5708, 8.6652, 10.7596, 12.854, '4.4764 + 2.0944k'])
    
    def test_sinusoidal_zeroes_initial_value_many_cross(self):
        sinusoidal_zeroes_initial_value_many_cross = sinusoidal_roots_initial_value(7, 5, 3, 4, 2)
        self.assertEqual(sinusoidal_zeroes_initial_value_many_cross, [2.942, 3.6863, 4.1987, 4.9429, 5.4553, 6.1995, 6.712, 7.4562, 7.9686, 8.7128, '2.942 + 1.2566k', '3.6863 + 1.2566k'])
    
    def test_sinusoidal_zeroes_derivative_initial_value_none(self):
        sinusoidal_zeroes_derivative_initial_value_none = sinusoidal_roots_derivative_initial_value(coefficients[0], coefficients[1], coefficients[2], coefficients[3], 10)
        self.assertEqual(sinusoidal_zeroes_derivative_initial_value_none, [None])
    
    def test_sinusoidal_zeroes_derivative_initial_value_many_bounce(self):
        sinusoidal_zeroes_derivative_initial_value_many_bounce = sinusoidal_roots_derivative_initial_value(1, 1, 2, 3, 1)
        self.assertEqual(sinusoidal_zeroes_derivative_initial_value_many_bounce, [2.0, 8.2832, 14.5664, 20.8496, 27.1327, '2.0 + 6.2832k'])
    
    def test_sinusoidal_zeroes_derivative_initial_value_many_cross(self):
        sinusoidal_zeroes_derivative_initial_value_many_cross = sinusoidal_roots_derivative_initial_value(7, 5, 3, 4, 2)
        self.assertEqual(sinusoidal_zeroes_derivative_initial_value_many_cross, [3.3027, 3.9539, 4.5594, 5.2105, 5.816, 6.4672, 7.0726, 7.7238, 8.3293, 8.9805, '3.3027 + 1.2566k', '3.9539 + 1.2566k'])

class TestIntercepts(unittest.TestCase):
    maxDiff = None

    def test_linear_intercepts(self):
        linear_intercepts = intercept_points('linear', coefficients[:2])
        self.assertEqual(linear_intercepts, [-1.5])
    
    def test_quadratic_intercepts(self):
        quadratic_intercepts = intercept_points('quadratic', coefficients[:3])
        self.assertEqual(quadratic_intercepts, [None])
    
    def test_cubic_intercepts(self):
        cubic_intercepts = intercept_points('cubic', coefficients)
        self.assertEqual(cubic_intercepts, [-1.4455])
    
    def test_hyperbolic_intercepts(self):
        hyperbolic_intercepts = intercept_points('hyperbolic', coefficients[:2])
        self.assertEqual(hyperbolic_intercepts, [-0.6667])
    
    def test_exponential_intercepts(self):
        exponential_intercepts = intercept_points('exponential', coefficients[:2])
        self.assertEqual(exponential_intercepts, [None])
    
    def test_logarithmic_intercepts(self):
        logarithmic_intercepts = intercept_points('logarithmic', coefficients[:2])
        self.assertEqual(logarithmic_intercepts, [0.2231])
    
    def test_logistic_intercepts(self):
        logistic_intercepts = intercept_points('logistic', coefficients[:3])
        self.assertEqual(logistic_intercepts, [None])
    
    def test_sinusoidal_intercepts(self):
        sinusoidal_intercepts = intercept_points('sinusoidal', coefficients)
        self.assertEqual(sinusoidal_intercepts, [None])

class TestMaxima(unittest.TestCase):
    maxDiff = None

    def test_linear_maxima(self):
        linear_maxima = maxima_points('linear', coefficients[:2])
        self.assertEqual(linear_maxima, [None])
    
    def test_quadratic_maxima(self):
        quadratic_maxima = maxima_points('quadratic', coefficients[:3])
        self.assertEqual(quadratic_maxima, [None])
    
    def test_cubic_maxima_none(self):
        cubic_maxima_none = maxima_points('cubic', coefficients[:4])
        self.assertEqual(cubic_maxima_none, [None])
    
    def test_cubic_maxima_one(self):
        cubic_maxima_one = maxima_points('cubic', [2, -15, 36, 7])
        self.assertEqual(cubic_maxima_one, [2.0])
    
    def test_hyperbolic_maxima(self):
        hyperbolic_maxima = maxima_points('hyperbolic', coefficients[:2])
        self.assertEqual(hyperbolic_maxima, [None])
    
    def test_exponential_maxima(self):
        exponential_maxima = maxima_points('exponential', coefficients[:2])
        self.assertEqual(exponential_maxima, [None])
    
    def test_logarithmic_maxima(self):
        logarithmic_maxima = maxima_points('logarithmic', coefficients[:2])
        self.assertEqual(logarithmic_maxima, [None])
    
    def test_logistic_maxima(self):
        logistic_maxima = maxima_points('logistic', coefficients[:3])
        self.assertEqual(logistic_maxima, [None])
    
    def test_sinusoidal_maxima(self):
        sinusoidal_maxima = maxima_points('sinusoidal', coefficients[:4])
        self.assertEqual(sinusoidal_maxima, [5.5236, 7.618, 9.7124])

class TestMinima(unittest.TestCase):
    maxDiff = None

    def test_linear_minima(self):
        linear_minima = minima_points('linear', coefficients[:2])
        self.assertEqual(linear_minima, [None])
    
    def test_quadratic_minima(self):
        quadratic_minima = minima_points('quadratic', coefficients[:3])
        self.assertEqual(quadratic_minima, [-0.75])
    
    def test_cubic_minima_none(self):
        cubic_minima_none = minima_points('cubic', coefficients[:4])
        self.assertEqual(cubic_minima_none, [None])
    
    def test_cubic_minima_one(self):
        cubic_minima_one = minima_points('cubic', [2, -15, 36, 7])
        self.assertEqual(cubic_minima_one, [3.0])
    
    def test_hyperbolic_minima(self):
        hyperbolic_minima = minima_points('hyperbolic', coefficients[:2])
        self.assertEqual(hyperbolic_minima, [None])
    
    def test_exponential_minima(self):
        exponential_minima = minima_points('exponential', coefficients[:2])
        self.assertEqual(exponential_minima, [None])
    
    def test_logarithmic_minima(self):
        logarithmic_minima = minima_points('logarithmic', coefficients[:2])
        self.assertEqual(logarithmic_minima, [None])
    
    def test_logistic_minima(self):
        logistic_minima = minima_points('logistic', coefficients[:3])
        self.assertEqual(logistic_minima, [None])
    
    def test_sinusoidal_minima(self):
        sinusoidal_minima = minima_points('sinusoidal', coefficients[:4])
        self.assertEqual(sinusoidal_minima, [6.5708, 8.6652])

class TestExtrema(unittest.TestCase):
    maxDiff = None

    def test_linear_extrema(self):
        linear_extrema = extrema_points('linear', coefficients[:2])
        self.assertEqual(linear_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_quadratic_extrema(self):
        quadratic_extrema = extrema_points('quadratic', coefficients[:3])
        self.assertEqual(quadratic_extrema, {'maxima': [None], 'minima': [-0.75]})
    
    def test_cubic_extrema(self):
        cubic_extrema = extrema_points('cubic', coefficients[:4])
        self.assertEqual(cubic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_hyperbolic_extrema(self):
        hyperbolic_extrema = extrema_points('hyperbolic', coefficients[:2])
        self.assertEqual(hyperbolic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_exponential_extrema(self):
        exponential_extrema = extrema_points('exponential', coefficients[:2])
        self.assertEqual(exponential_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_logarithmic_extrema(self):
        logarithmic_extrema = extrema_points('logarithmic', coefficients[:2])
        self.assertEqual(logarithmic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_logistic_extrema(self):
        logistic_extrema = extrema_points('logistic', coefficients[:3])
        self.assertEqual(logistic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_sinusoidal_extrema(self):
        sinusoidal_extrema = extrema_points('sinusoidal', coefficients[:4])
        self.assertEqual(sinusoidal_extrema, {'maxima': [5.5236, 7.618, 9.7124, '5.5236 + 2.0944k'], 'minima': [6.5708, 8.6652, '6.5708 + 2.0944k']})

class TestInflections(unittest.TestCase):
    maxDiff = None

    def test_linear_inflections(self):
        linear_inflections = inflection_points('linear', coefficients[:2])
        self.assertEqual(linear_inflections, [None])
    
    def test_quadratic_inflections(self):
        quadratic_inflections = inflection_points('quadratic', coefficients[:3])
        self.assertEqual(quadratic_inflections, [None])
    
    def test_cubic_inflections(self):
        cubic_inflections = inflection_points('cubic', coefficients[:4])
        self.assertEqual(cubic_inflections, [-0.5])
    
    def test_hyperbolic_inflections(self):
        hyperbolic_inflections = inflection_points('hyperbolic', coefficients[:2])
        self.assertEqual(hyperbolic_inflections, [None])
    
    def test_exponential_inflections(self):
        exponential_inflections = inflection_points('exponential', coefficients[:2])
        self.assertEqual(exponential_inflections, [None])
    
    def test_logarithmic_inflections(self):
        logarithmic_inflections = inflection_points('logarithmic', coefficients[:2])
        self.assertEqual(logarithmic_inflections, [None])
    
    def test_logistic_inflections(self):
        logistic_inflections = inflection_points('logistic', coefficients[:3])
        self.assertEqual(logistic_inflections, [5])
    
    def test_sinusoidal_inflections(self):
        sinusoidal_inflections = inflection_points('sinusoidal', coefficients[:4])
        self.assertEqual(sinusoidal_inflections, [5.0, 6.0472, 7.0944, 8.1416, 9.1888, '5.0 + 1.0472k'])

class TestCoordinatePairs(unittest.TestCase):
    maxDiff = None

    def test_coordinate_pairs_linear(self):
        coordinate_pairs_linear = coordinate_pairs('linear', coefficients[:2], [1, 2, 3, 4])
        self.assertEqual(coordinate_pairs_linear, [[1.0, 5.0], [2.0, 7.0], [3.0, 9.0], [4.0, 11.0]])
    
    def test_coordinate_pairs_quadratic(self):
        coordinate_pairs_quadratic = coordinate_pairs('quadratic', coefficients[:3], [1, 2, 3, 4])
        self.assertEqual(coordinate_pairs_quadratic, [[1.0, 10.0], [2.0, 19.0], [3.0, 32.0], [4.0, 49.0]])
    
    def test_coordinate_pairs_cubic(self):
        coordinate_pairs_cubic = coordinate_pairs('cubic', coefficients[:4], [1, 2, 3, 4])
        self.assertEqual(coordinate_pairs_cubic, [[1.0, 17.0], [2.0, 45.0], [3.0, 103.0], [4.0, 203.0]])
    
    def test_coordinate_pairs_hyperbolic(self):
        coordinate_pairs_hyperbolic = coordinate_pairs('hyperbolic', coefficients[:2], [1, 2, 3, 4])
        self.assertEqual(coordinate_pairs_hyperbolic, [[1.0, 5.0], [2.0, 4.0], [3.0, 3.6667], [4.0, 3.5]])
    
    def test_coordinate_pairs_exponential(self):
        coordinate_pairs_exponential = coordinate_pairs('exponential', coefficients[:2], [1, 2, 3, 4])
        self.assertEqual(coordinate_pairs_exponential, [[1.0, 6.0], [2.0, 18.0], [3.0, 54.0], [4.0, 162.0]])
    
    def test_coordinate_pairs_logarithmic(self):
        coordinate_pairs_logarithmic = coordinate_pairs('logarithmic', coefficients[:2], [1, 2, 3, 4])
        self.assertEqual(coordinate_pairs_logarithmic, [[1.0, 3.0], [2.0, 4.3863], [3.0, 5.1972], [4.0, 5.7726]])
    
    def test_coordinate_pairs_logistic(self):
        coordinate_pairs_logistic = coordinate_pairs('logistic', coefficients[:3], [1, 2, 3, 4])
        self.assertEqual(coordinate_pairs_logistic, [[1.0, 0.0001], [2.0, 0.0002], [3.0, 0.0049], [4.0, 0.0949]])
    
    def test_coordinate_pairs_sinusoidal(self):
        coordinate_pairs_sinusoidal = coordinate_pairs('sinusoidal', coefficients[:4], [1, 2, 3, 4])
        self.assertEqual(coordinate_pairs_sinusoidal, [[1.0, 8.0731], [2.0, 6.1758], [3.0, 7.5588], [4.0, 6.7178]])
    
    def test_coordinate_pairs_sinusoidal_mixed(self):
        coordinate_pairs_sinusoidal_mixed = coordinate_pairs('sinusoidal', coefficients[:4], [1, 2, 3, 4, '1 + 1k'])
        self.assertEqual(coordinate_pairs_sinusoidal_mixed,  [[1.0, 8.0731], [2.0, 6.1758], [3.0, 7.5588], [4.0, 6.7178], ['1 + 1k', 8.0731]])
    
    def test_coordinate_pairs_sinusoidal_mixed_intercepts(self):
        coordinate_pairs_sinusoidal_mixed_intercepts = coordinate_pairs('sinusoidal', coefficients[:4], [1, 2, 3, 4, '1 + 1k'], 'intercepts')
        self.assertEqual(coordinate_pairs_sinusoidal_mixed_intercepts, [[1.0, 0.0], [2.0, 0.0], [3.0, 0.0], [4.0, 0.0], ['1 + 1k', 0.0]])
    
    def test_coordinate_pairs_sinusoidal_mixed_inflections(self):
        coordinate_pairs_sinusoidal_mixed_inflections = coordinate_pairs('sinusoidal', coefficients[:4], [1, 2, 3, 4, '1 + 1k'], 'inflections')
        self.assertEqual(coordinate_pairs_sinusoidal_mixed_inflections,  [[1.0, 8.0731], [2.0, 6.1758], [3.0, 7.5588], [4.0, 6.7178], ['1 + 1k', 8.0731]])
    
    def test_coordinate_pairs_sinusoidal_mixed_maxima(self):
        coordinate_pairs_sinusoidal_mixed_maxima = coordinate_pairs('sinusoidal', coefficients[:4], [1, 2, 3, 4, '1 + 1k'], 'maxima')
        self.assertEqual(coordinate_pairs_sinusoidal_mixed_maxima, [[1.0, 8.0731], [2.0, 6.1758], [3.0, 7.5588], [4.0, 6.7178], ['1 + 1k', 8.0731]])
    
    def test_coordinate_pairs_sinusoidal_mixed_minima(self):
        coordinate_pairs_sinusoidal_mixed_minima = coordinate_pairs('sinusoidal', coefficients[:4], [1, 2, 3, 4, '1 + 1k'], 'minima')
        self.assertEqual(coordinate_pairs_sinusoidal_mixed_minima, [[1.0, 8.0731], [2.0, 6.1758], [3.0, 7.5588], [4.0, 6.7178], ['1 + 1k', 8.0731]])

class TestKeyPoints(unittest.TestCase):
    maxDiff = None

    def test_linear_key_points(self):
        linear_key_points = key_coordinates('linear', coefficients[:2])
        self.assertEqual(linear_key_points, {'roots': [[-1.5, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_key_points(self):
        quadratic_key_points = key_coordinates('quadratic', coefficients[:3])
        self.assertEqual(quadratic_key_points, {'roots': [None], 'maxima': [None], 'minima': [[-0.75, 3.875]], 'inflections': [None]})
    
    def test_cubic_key_points(self):
        cubic_key_points = key_coordinates('cubic', coefficients[:4])
        self.assertEqual(cubic_key_points, {'roots': [[-1.4455, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[-0.5, 5.0]]})
    
    def test_hyperbolic_key_points(self):
        hyperbolic_key_points = key_coordinates('hyperbolic', coefficients[:2])
        self.assertEqual(hyperbolic_key_points, {'roots': [[-0.6667, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_key_points(self):
        exponential_key_points = key_coordinates('exponential', coefficients[:2])
        self.assertEqual(exponential_key_points, {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_key_points(self):
        logarithmic_key_points = key_coordinates('logarithmic', coefficients[:2])
        self.assertEqual(logarithmic_key_points, {'roots': [[0.2231, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_key_points(self):
        logistic_key_points = key_coordinates('logistic', coefficients[:3])
        self.assertEqual(logistic_key_points, {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[5, 1.0]]})
    
    def test_sinusoidal_key_points(self):
        sinusoidal_key_points = key_coordinates('sinusoidal', coefficients[:4])
        self.assertEqual(sinusoidal_key_points, {'roots': [None], 'maxima': [[5.5236, 9.0], [7.618, 9.0], [9.7124, 9.0], ['5.5236 + 2.0944k', 9.0]], 'minima': [[6.5708, 5.0], [8.6652, 5.0], ['6.5708 + 2.0944k', 5.0]], 'inflections': [[5.0, 7.0], [6.0472, 7.0], [7.0944, 7.0], [8.1416, 7.0], [9.1888, 7.0001], ['5.0 + 1.0472k', 7.0]]})

class TestPointsWithinRange(unittest.TestCase):
    maxDiff = None

    def test_points_range_all(self):
        points_range_all = points_within_range([11, 13, 15, 17, 19], 11, 19)
        self.assertEqual(points_range_all, [11, 13, 15, 17, 19])
    
    def test_points_range_some(self):
        points_range_some = points_within_range([11, 13, 15, 17, 19], 14, 18)
        self.assertEqual(points_range_some, [15, 17])
    
    def test_points_range_none(self):
        points_range_none = points_within_range([11, 13, 15, 17, 19], 50, 60)
        self.assertEqual(points_range_none, [None])

class TestShiftedPointsWithinRange(unittest.TestCase):
    maxDiff = None

    def test_shifted_points_in_range_1d(self):
        shifted_points_in_range_1d = shifted_points_within_range([11, 13, 15, 17, 19, '1 + 2k'], 11, 19)
        self.assertEqual(shifted_points_in_range_1d, [11.0, 13.0, 15.0, 17.0, 19.0, '11.0 + 2.0k'])
    
    def test_shifted_points_not_in_range_1d(self):
        shifted_points_not_in_range_1d = shifted_points_within_range([11, 13, 15, 17, 19, '1 + 2k'], 50, 60)
        self.assertEqual(shifted_points_not_in_range_1d, [51.0, 53.0, 55.0, 57.0, 59.0, '51.0 + 2.0k'])
    
    def test_shifted_points_in_range_2d(self):
        shifted_points_in_range_2d = shifted_points_within_range([[11, 1], [13, 1], [15, 1], [17, 1], [19, 1], ['1 + 2k', 1]], 11, 19)
        self.assertEqual(shifted_points_in_range_2d, [11.0, 13.0, 15.0, 17.0, 19.0, '11.0 + 2.0k'])
    
    def test_shifted_points_not_in_range_2d(self):
        shifted_points_not_in_range_2d = shifted_points_within_range([[11, 1], [13, 1], [15, 1], [17, 1], [19, 1], ['1 + 2k', 1]], 50, 60)
        self.assertEqual(shifted_points_not_in_range_2d, [51.0, 53.0, 55.0, 57.0, 59.0, '51.0 + 2.0k'])

class TestShiftedCoordinatesWithinRange(unittest.TestCase):
    maxDiff = None

    def test_shifted_coordinates_in_range(self):
        shifted_coordinates_in_range = shifted_coordinates_within_range([[11, 1], [13, 1], [15, 1], [17, 1], [19, 1], ['1 + 2k', 1]], 11, 19, 8)
        self.assertEqual(shifted_coordinates_in_range, [[11.0, 1], [13.0, 1], [15.0, 1], [17.0, 1], [19.0, 1], ['11.0 + 2.0k', 1]])
    
    def test_shifted_coordinates_not_in_range(self):
        shifted_coordinates_not_in_range = shifted_coordinates_within_range([[11, 1], [13, 1], [15, 1], [17, 1], [19, 1], ['1 + 2k', 1]], 50, 60, 5)
        self.assertEqual(shifted_coordinates_not_in_range, [[51.0, 1], [53.0, 1], [55.0, 1], [57.0, 1], [59.0, 1], ['51.0 + 2.0k', 1]])
    
    def test_shifted_coordinates_none(self):
        shifted_coordinates_none = shifted_coordinates_within_range([None], 50, 60, 5)
        self.assertEqual(shifted_coordinates_none, [None])

class TestAccumulation(unittest.TestCase):
    def test_linear_accumulation(self):
        linear_accumulation = accumulated_area('linear', coefficients[:2], 10, 20)
        self.assertEqual(linear_accumulation, 330.0)
    
    def test_quadratic_accumulation(self):
        quadratic_accumulation = accumulated_area('quadratic', coefficients[:3], 10, 20)
        self.assertEqual(quadratic_accumulation, 5166.9)
    
    def test_cubic_accumulation(self):
        cubic_accumulation = accumulated_area('cubic', coefficients[:4], 10, 20)
        self.assertEqual(cubic_accumulation, 82820.0)
    
    def test_hyperbolic_accumulation(self):
        hyperbolic_accumulation = accumulated_area('hyperbolic', coefficients[:2], 10, 20)
        self.assertEqual(hyperbolic_accumulation, 31.3863)
    
    def test_exponential_accumulation(self):
        exponential_accumulation = accumulated_area('exponential', coefficients[:2], 10, 20)
        self.assertEqual(exponential_accumulation, 6347583503.316)
    
    def test_logarithmic_accumulation(self):
        logarithmic_accumulation = accumulated_area('logarithmic', coefficients[:2], 10, 20)
        self.assertEqual(logarithmic_accumulation, 83.7776)
    
    def test_logistic_accumulation(self):
        logistic_accumulation = accumulated_area('logistic', coefficients[:3], 10, 20)
        self.assertEqual(logistic_accumulation, 20.001)
    
    def test_sinusoidal_accumulation(self):
        sinusoidal_accumulation = accumulated_area('sinusoidal', coefficients[:4], 10, 20)
        self.assertEqual(sinusoidal_accumulation, 69.1433)

class TestAverages(unittest.TestCase):
    maxDiff = None

    def test_linear_averages(self):
        linear_averages = average_values('linear', coefficients[:2], 10, 20)
        self.assertEqual(linear_averages, {'average_value_derivative': 2.0, 'mean_values_derivative': ['All'], 'average_value_integral': 33.0, 'mean_values_integral': [15.0]})
    
    def test_quadratic_averages(self):
        quadratic_averages = average_values('quadratic', coefficients[:3], 10, 20)
        self.assertEqual(quadratic_averages, {'average_value_derivative': 63.0, 'mean_values_derivative': [15.0], 'average_value_integral': 516.69, 'mean_values_integral': [15.2627]})
    
    def test_cubic_averages(self):
        cubic_averages = average_values('cubic', coefficients[:4], 10, 20)
        self.assertEqual(cubic_averages, {'average_value_derivative': 1495.0, 'mean_values_derivative': [15.2665], 'average_value_integral': 8282.0, 'mean_values_integral': [15.5188]})
    
    def test_hyperbolic_averages(self):
        hyperbolic_averages = average_values('hyperbolic', coefficients[:2], 10, 20)
        self.assertEqual(hyperbolic_averages, {'average_value_derivative': -0.01, 'mean_values_derivative': [14.1421], 'average_value_integral': 3.1386, 'mean_values_integral': [14.43]})
    
    def test_exponential_averages(self):
        exponential_averages = average_values('exponential', coefficients[:2], 10, 20)
        self.assertEqual(exponential_averages, {'average_value_derivative': 697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': 634758350.3316, 'mean_values_integral': [17.8185]})
    
    def test_exponential_averages_unary_base(self):
        exponential_averages_unary_base = average_values('exponential', [2, 1], 10, 20)
        self.assertEqual(exponential_averages_unary_base, {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 2.003, 'mean_values_integral': [14.9888]})
    
    def test_exponential_averages_negative_base(self):
        exponential_averages_negative_base = average_values('exponential', [2, -3], 10, 20)
        self.assertEqual(exponential_averages_negative_base, {'average_value_derivative': 697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': 634758350.3316, 'mean_values_integral': [17.8185]})
    
    def test_exponential_averages_negative_lead(self):
        exponential_averages_negative_lead = average_values('exponential', [-2, 3], 10, 20)
        self.assertEqual(exponential_averages_negative_lead, {'average_value_derivative': -697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': -634758350.3316, 'mean_values_integral': [17.8185]})
    
    def test_logarithmic_averages(self):
        logarithmic_averages = average_values('logarithmic', coefficients[:2], 10, 20)
        self.assertEqual(logarithmic_averages, {'average_value_derivative': 0.1386, 'mean_values_derivative': [14.43], 'average_value_integral': 8.3778, 'mean_values_integral': [14.7155]})
    
    def test_logistic_averages(self):
        logistic_averages = average_values('logistic', coefficients[:3], 10, 20)
        self.assertEqual(logistic_averages, {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 2.0001, 'mean_values_integral': [None]})
    
    def test_sinusoidal_averages(self):
        sinusoidal_averages = average_values('sinusoidal', coefficients[:4], 10, 20)
        self.assertEqual(sinusoidal_averages, {'average_value_derivative': 0.0401, 'mean_values_derivative': [10.7618, 11.8046, 12.8562, 13.899, 14.9506, 15.9934, 17.045, 18.0878, 19.1394, '10.7618 + 2.0944k', '11.8046 + 2.0944k'], 'average_value_integral': 6.9143, 'mean_values_integral': [10.2503, 11.2689, 12.3447, 13.3633, 14.4391, 15.4577, 16.5335, 17.5521, 18.6279, 19.6465, '10.2503 + 2.0944k', '11.2689 + 2.0944k']})
    
    def test_averages_start_end(self):
        averages_start_end = average_values('cubic', coefficients[:4], 1, 1)
        self.assertEqual(averages_start_end, {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 0.0, 'mean_values_integral': [None]})

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 322 tests in 0.049s ---------- OK ---------- #