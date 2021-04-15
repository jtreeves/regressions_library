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
from library.analyses.points import key_coordinates, points_within_range
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
        self.assertEqual(exponential_function_negative, 0.6666666666666666)
    
    # LOGARITHMIC EVALUATIONS
    def test_logarithmic_function_positive(self):
        logarithmic_function_positive = logarithmic_equation(coefficients[0], coefficients[1])(1)
        self.assertEqual(logarithmic_function_positive, 3.0)
    
    def test_logarithmic_function_zero(self):
        logarithmic_function_zero = logarithmic_equation(coefficients[0], coefficients[1])(0)
        self.assertEqual(logarithmic_function_zero, -15.420680743952364)
    
    def test_logarithmic_function_negative(self):
        logarithmic_function_negative = logarithmic_equation(coefficients[0], coefficients[1])(-1)
        self.assertEqual(logarithmic_function_negative, 3.0)
    
    # LOGISTIC EVALUATIONS
    def test_logistic_function_positive(self):
        logistic_function_positive = logistic_equation(coefficients[0], coefficients[1], coefficients[2])(1)
        self.assertEqual(logistic_function_positive, 1.2288349204429436e-05)
    
    def test_logistic_function_zero(self):
        logistic_function_zero = logistic_equation(coefficients[0], coefficients[1], coefficients[2])(0)
        self.assertEqual(logistic_function_zero, 6.118044538512494e-07)
    
    def test_logistic_function_negative(self):
        logistic_function_negative = logistic_equation(coefficients[0], coefficients[1], coefficients[2])(-1)
        self.assertEqual(logistic_function_negative, 3.04599590255207e-08)
    
    # SINUSOIDAL EVALUATIONS
    def test_sinusoidal_function_positive(self):
        sinusoidal_function_positive = sinusoidal_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(1)
        self.assertEqual(sinusoidal_function_positive, 8.07314583600087)
    
    def test_sinusoidal_function_zero(self):
        sinusoidal_function_zero = sinusoidal_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(0)
        self.assertEqual(sinusoidal_function_zero, 5.699424319685766)
    
    def test_sinusoidal_function_negative(self):
        sinusoidal_function_negative = sinusoidal_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])(-1)
        self.assertEqual(sinusoidal_function_negative, 8.501974493543353)

class TestDerivatives(unittest.TestCase):
    # LINEAR FIRST DERIVATIVE
    def test_linear_first_derivative_constants(self):
        linear_first_derivative_constants = linear_derivatives(coefficients[0], coefficients[1])['first']['constants']
        self.assertEqual(linear_first_derivative_constants, [2])

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
        self.assertEqual(quadratic_first_derivative_constants, [4, 3])
    
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
        self.assertEqual(cubic_first_derivative_constants, [6, 6, 5])
    
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
        self.assertEqual(hyperbolic_first_derivative_constants, [-2])
    
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
        self.assertEqual(exponential_first_derivative_constants, [2.1972245773362196, 3])
    
    def test_exponential_first_derivative_evaluation_positive(self):
        exponential_first_derivative_evaluation_positive = exponential_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](1)
        self.assertEqual(exponential_first_derivative_evaluation_positive, 6.591673732008658)
    
    def test_exponential_first_derivative_evaluation_zero(self):
        exponential_first_derivative_evaluation_zero = exponential_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](0)
        self.assertEqual(exponential_first_derivative_evaluation_zero, 2.1972245773362196)
    
    def test_exponential_first_derivative_evaluation_negative(self):
        exponential_first_derivative_evaluation_negative = exponential_derivatives(coefficients[0], coefficients[1])['first']['evaluation'](-1)
        self.assertEqual(exponential_first_derivative_evaluation_negative, 0.7324081924454064)
    
    # LOGARITHMIC FIRST DERIVATIVE
    def test_logarithmic_first_derivative_constants(self):
        logarithmic_first_derivative_constants = logarithmic_derivatives(coefficients[0], coefficients[1])['first']['constants']
        self.assertEqual(logarithmic_first_derivative_constants, [2])
    
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
        self.assertEqual(logistic_first_derivative_constants, [6, 3, 5])
    
    def test_logistic_first_derivative_evaluation_positive(self):
        logistic_first_derivative_evaluation_positive = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](1)
        self.assertEqual(logistic_first_derivative_evaluation_positive, 3.6864821107999056e-05)
    
    def test_logistic_first_derivative_evaluation_zero(self):
        logistic_first_derivative_evaluation_zero = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](0)
        self.assertEqual(logistic_first_derivative_evaluation_zero, 1.8354128000967137e-06)
    
    def test_logistic_first_derivative_evaluation_negative(self):
        logistic_first_derivative_evaluation_negative = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['first']['evaluation'](-1)
        self.assertEqual(logistic_first_derivative_evaluation_negative, 9.137987568484845e-08)

    # SINUSOIDAL FIRST DERIVATIVE
    def test_sinusoidal_first_derivative_constants(self):
        sinusoidal_first_derivative_constants = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['constants']
        self.assertEqual(sinusoidal_first_derivative_constants, [6, 3, 5])
    
    def test_sinusoidal_first_derivative_evaluation_positive(self):
        sinusoidal_first_derivative_evaluation_positive = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](1)
        self.assertEqual(sinusoidal_first_derivative_evaluation_positive, 5.063123752394953)
    
    def test_sinusoidal_first_derivative_evaluation_zero(self):
        sinusoidal_first_derivative_evaluation_zero = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](0)
        self.assertEqual(sinusoidal_first_derivative_evaluation_zero, -4.558127477152928)
    
    def test_sinusoidal_first_derivative_evaluation_negative(self):
        sinusoidal_first_derivative_evaluation_negative = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['first']['evaluation'](-1)
        self.assertEqual(sinusoidal_first_derivative_evaluation_negative, 3.961900249464481)

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
        self.assertEqual(exponential_second_derivative_constants, [2.413897921625164, 3])
    
    def test_exponential_second_derivative_evaluation_positive(self):
        exponential_second_derivative_evaluation_positive = exponential_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](1)
        self.assertEqual(exponential_second_derivative_evaluation_positive, 7.241693764875492)
    
    def test_exponential_second_derivative_evaluation_zero(self):
        exponential_second_derivative_evaluation_zero = exponential_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](0)
        self.assertEqual(exponential_second_derivative_evaluation_zero, 2.413897921625164)
    
    def test_exponential_second_derivative_evaluation_negative(self):
        exponential_second_derivative_evaluation_negative = exponential_derivatives(coefficients[0], coefficients[1])['second']['evaluation'](-1)
        self.assertEqual(exponential_second_derivative_evaluation_negative, 0.8046326405417213)
    
    # LOGARITHMIC SECOND DERIVATIVE
    def test_logarithmic_second_derivative_constants(self):
        logarithmic_second_derivative_constants = logarithmic_derivatives(coefficients[0], coefficients[1])['second']['constants']
        self.assertEqual(logarithmic_second_derivative_constants, [-2])
    
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
        self.assertEqual(logistic_second_derivative_constants, [18, 3, 5])
    
    def test_logistic_second_derivative_evaluation_positive(self):
        logistic_second_derivative_evaluation_positive = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](1)
        self.assertEqual(logistic_second_derivative_evaluation_positive, 0.00011059310430061176)
    
    def test_logistic_second_derivative_evaluation_zero(self):
        logistic_second_derivative_evaluation_zero = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](0)
        self.assertEqual(logistic_second_derivative_evaluation_zero, 5.506235031548964e-06)
    
    def test_logistic_second_derivative_evaluation_negative(self):
        logistic_second_derivative_evaluation_negative = logistic_derivatives(coefficients[0], coefficients[1], coefficients[2])['second']['evaluation'](-1)
        self.assertEqual(logistic_second_derivative_evaluation_negative, 2.741396187042635e-07)

    # SINUSOIDAL SECOND DERIVATIVE
    def test_sinusoidal_second_derivative_constants(self):
        sinusoidal_second_derivative_constants = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['constants']
        self.assertEqual(sinusoidal_second_derivative_constants, [-18, 3, 5])

    def test_sinusoidal_second_derivative_evaluation_positive(self):
        sinusoidal_second_derivative_evaluation_positive = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](1)
        self.assertEqual(sinusoidal_second_derivative_evaluation_positive, -9.65831252400783)
    
    def test_sinusoidal_second_derivative_evaluation_zero(self):
        sinusoidal_second_derivative_evaluation_zero = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](0)
        self.assertEqual(sinusoidal_second_derivative_evaluation_zero, 11.705181122828105)
    
    def test_sinusoidal_second_derivative_evaluation_negative(self):
        sinusoidal_second_derivative_evaluation_negative = sinusoidal_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['second']['evaluation'](-1)
        self.assertEqual(sinusoidal_second_derivative_evaluation_negative, -13.51777044189017)

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
        self.assertEqual(quadratic_integral_constants, [0.6666666666666666, 1.5, 5.0])
    
    def test_quadratic_integral_constants_ones(self):
        quadratic_integral_constants_ones = quadratic_integral(1, 1, 1)['constants']
        self.assertEqual(quadratic_integral_constants_ones, [0.3333333333333333, 0.5, 1.0])
    
    def test_quadratic_integral_evaluation_positive(self):
        quadratic_integral_evaluation_positive = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](1)
        self.assertEqual(quadratic_integral_evaluation_positive, 7.166666666666666)
    
    def test_quadratic_integral_evaluation_zero(self):
        quadratic_integral_evaluation_zero = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](0)
        self.assertEqual(quadratic_integral_evaluation_zero, 0.0)
    
    def test_quadratic_integral_evaluation_negative(self):
        quadratic_integral_evaluation_negative = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](-1)
        self.assertEqual(quadratic_integral_evaluation_negative, -4.166666666666667)
    
    # CUBIC INTEGRAL
    def test_cubic_integral_constants(self):
        cubic_integral_constants = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['constants']
        self.assertEqual(cubic_integral_constants, [0.5, 1.0, 2.5, 7.0])
    
    def test_cubic_integral_constants_ones(self):
        cubic_integral_constants_ones = cubic_integral(1, 1, 1, 1)['constants']
        self.assertEqual(cubic_integral_constants_ones, [0.25, 0.3333333333333333, 0.5, 1.0])
    
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
        self.assertEqual(hyperbolic_integral_evaluation_zero, -18.420380743952364)
    
    def test_hyperbolic_integral_evaluation_negative(self):
        hyperbolic_integral_evaluation_negative = hyperbolic_integral(coefficients[0], coefficients[1])['evaluation'](-1)
        self.assertEqual(hyperbolic_integral_evaluation_negative, -3.0)
    
    # EXPONENTIAL INTEGRAL
    def test_exponential_integral_constants(self):
        exponential_integral_constants = exponential_integral(coefficients[0], coefficients[1])['constants']
        self.assertEqual(exponential_integral_constants, [1.8204784532536746, 3.0])
    
    def test_exponential_integral_constants_ones(self):
        exponential_integral_constants_ones = exponential_integral(1, 1)['constants']
        self.assertEqual(exponential_integral_constants_ones, [10000.499991668185, 1.0001])
    
    def test_exponential_integral_evaluation_positive(self):
        exponential_integral_evaluation_positive = exponential_integral(coefficients[0], coefficients[1])['evaluation'](1)
        self.assertEqual(exponential_integral_evaluation_positive, 5.461435359761024)
    
    def test_exponential_integral_evaluation_zero(self):
        exponential_integral_evaluation_zero = exponential_integral(coefficients[0], coefficients[1])['evaluation'](0)
        self.assertEqual(exponential_integral_evaluation_zero, 1.8204784532536746)
    
    def test_exponential_integral_evaluation_negative(self):
        exponential_integral_evaluation_negative = exponential_integral(coefficients[0], coefficients[1])['evaluation'](-1)
        self.assertEqual(exponential_integral_evaluation_negative, 0.6068261510845582)
    
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
        self.assertEqual(logarithmic_integral_evaluation_zero, -0.0017420680743952363)
    
    def test_logarithmic_integral_evaluation_negative(self):
        logarithmic_integral_evaluation_negative = logarithmic_integral(coefficients[0], coefficients[1])['evaluation'](-1)
        self.assertEqual(logarithmic_integral_evaluation_negative, -1.0)
    
    # LOGISTIC INTEGRAL
    def test_logistic_integral_constants(self):
        logistic_integral_constants = logistic_integral(coefficients[0], coefficients[1], coefficients[2])['constants']
        self.assertEqual(logistic_integral_constants, [0.6666666666666666, 3.0, 5.0])
    
    def test_logistic_integral_constants_ones(self):
        logistic_integral_constants_ones = logistic_integral(1, 1, 1)['constants']
        self.assertEqual(logistic_integral_constants_ones, [1.0, 1.0, 1.0])
    
    def test_logistic_integral_evaluation_positive(self):
        logistic_integral_evaluation_positive = logistic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](1)
        self.assertEqual(logistic_integral_evaluation_positive, 4.096128985164955e-06)
    
    def test_logistic_integral_evaluation_zero(self):
        logistic_integral_evaluation_zero = logistic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](0)
        self.assertEqual(logistic_integral_evaluation_zero, 2.0393484919817015e-07)
    
    def test_logistic_integral_evaluation_negative(self):
        logistic_integral_evaluation_negative = logistic_integral(coefficients[0], coefficients[1], coefficients[2])['evaluation'](-1)
        self.assertEqual(logistic_integral_evaluation_negative, 1.015331973722202e-08)
    
    # SINUSOIDAL INTEGRAL
    def test_sinusoidal_integral_constants(self):
        sinusoidal_integral_constants = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['constants']
        self.assertEqual(sinusoidal_integral_constants, [-0.6666666666666666, 3.0, 5.0, 7.0])
    
    def test_sinusoidal_integral_constants_ones(self):
        sinusoidal_integral_constants_ones = sinusoidal_integral(1, 1, 1, 1)['constants']
        self.assertEqual(sinusoidal_integral_constants_ones, [-1.0, 1.0, 1.0, 1.0])
    
    def test_sinusoidal_integral_evaluation_positive(self):
        sinusoidal_integral_evaluation_positive = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](1)
        self.assertEqual(sinusoidal_integral_evaluation_positive, 6.437430694178339)
    
    def test_sinusoidal_integral_evaluation_zero(self):
        sinusoidal_integral_evaluation_zero = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](0)
        self.assertEqual(sinusoidal_integral_evaluation_zero, 0.5064586085725474)
    
    def test_sinusoidal_integral_evaluation_negative(self):
        sinusoidal_integral_evaluation_negative = sinusoidal_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])['evaluation'](-1)
        self.assertEqual(sinusoidal_integral_evaluation_negative, -7.440211138829387)

class TestCriticalPoints(unittest.TestCase):
    # FIRST DERIVATIVE CRITICAL POINTS
    def test_first_linear_critical_points(self):
        first_linear_critical_points = critical_points('linear', coefficients[:2], 1)
        self.assertEqual(first_linear_critical_points, [None])
    
    def test_first_quadratic_critical_points(self):
        first_quadratic_critical_points = critical_points('quadratic', coefficients[:3], 1)
        self.assertEqual(first_quadratic_critical_points, [-0.75])
    
    def test_first_cubic_critical_points(self):
        first_cubic_critical_points = critical_points('cubic', coefficients[:4], 1)
        self.assertEqual(first_cubic_critical_points, [None])
    
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
    
    def test_first_cubic_intervals(self):
        first_cubic_intervals = sign_chart('cubic', coefficients[:4], 1)
        self.assertEqual(first_cubic_intervals, ['positive'])
    
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

    def test_linear_zeroes(self):
        linear_zeroes = linear_roots(coefficients[0], coefficients[1])
        self.assertEqual(linear_zeroes, [-1.5])
    
    def test_quadratic_zeroes_none(self):
        quadratic_zeroes_none = quadratic_roots(coefficients[0], coefficients[1], coefficients[2])
        self.assertEqual(quadratic_zeroes_none, [None])
    
    def test_quadratic_zeroes_one(self):
        quadratic_zeroes_one = quadratic_roots(1, -2, 1)
        self.assertEqual(quadratic_zeroes_one, [1.0])
    
    def test_quadratic_zeroes_two(self):
        quadratic_zeroes_two = quadratic_roots(1, -5, 6)
        self.assertEqual(quadratic_zeroes_two, [2.0, 3.0])
    
    def test_cubic_zeroes_one(self):
        cubic_zeroes_one = cubic_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        self.assertEqual(cubic_zeroes_one, [-1.4455])
    
    def test_cubic_zeroes_two(self):
        cubic_zeroes_two = cubic_roots(1, -4, 5, -2)
        self.assertEqual(cubic_zeroes_two, [1.0, 2.0])
    
    def test_cubic_zeroes_three(self):
        cubic_zeroes_three = cubic_roots(1, -10, 31, -30)
        self.assertEqual(cubic_zeroes_three, [2.0, 3.0, 5.0])
    
    def test_hyperbolic_zeroes(self):
        hyperbolic_zeroes = hyperbolic_roots(coefficients[0], coefficients[1])
        self.assertEqual(hyperbolic_zeroes, [-0.6667])
    
    def test_exponential_zeroes(self):
        exponential_zeroes = exponential_roots(coefficients[0], coefficients[1])
        self.assertEqual(exponential_zeroes, [None])
    
    def test_logarithmic_zeroes(self):
        logarithmic_zeroes = logarithmic_roots(coefficients[0], coefficients[1])
        self.assertEqual(logarithmic_zeroes, [0.2231])
    
    def test_logistic_zeroes(self):
        logistic_zeroes = logistic_roots(coefficients[0], coefficients[1], coefficients[2])
        self.assertEqual(logistic_zeroes, [None])
    
    def test_sinusoidal_zeroes_none(self):
        sinusoidal_zeroes_none = sinusoidal_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        self.assertEqual(sinusoidal_zeroes_none, [None])
    
    def test_sinusoidal_zeroes_many_bounce(self):
        sinusoidal_zeroes_many_bounce = sinusoidal_roots(2, 3, 5, 2)
        self.assertEqual(sinusoidal_zeroes_many_bounce, [4.4764, 6.5708, 8.6652, '4.4764 + 2.0944k'])
    
    def test_sinusoidal_zeroes_many_cross(self):
        sinusoidal_zeroes_many_cross = sinusoidal_roots(2, 3, 5, 1)
        self.assertEqual(sinusoidal_zeroes_many_cross, [4.8255, 6.2217, 6.9199, 8.3161, 9.0143, 10.4105, '4.8255 + 2.0944k', '6.2217 + 2.0944k'])

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
    
    def test_cubic_maxima(self):
        cubic_maxima = maxima_points('cubic', coefficients[:4])
        self.assertEqual(cubic_maxima, [None])
    
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
    
    def test_cubic_minima(self):
        cubic_minima = minima_points('cubic', coefficients[:4])
        self.assertEqual(cubic_minima, [None])
    
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
        self.assertEqual(sinusoidal_extrema, {'maxima': [5.5236, 7.618, 9.7124, '1.0472k'], 'minima': [6.5708, 8.6652, '1.0472k']})

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

    def test_points_in_range(self):
        good_range = points_within_range([[11, 1], [13, 1], [15, 1], [17, 1], [19, 1], ['1 + 2k', 1]], 11, 19, 8, 2)
        self.assertEqual(good_range, [[11.0, 1], [13.0, 1], [15.0, 1], [17.0, 1], [19.0, 1], ['11.0 + 2.0k', 1]])
    
    def test_points_not_in_range(self):
        bad_range = points_within_range([[11, 1], [13, 1], [15, 1], [17, 1], [19, 1], ['1 + 2k', 1]], 50, 60, 5, 2)
        self.assertEqual(bad_range, [[51.0, 1], [53.0, 1], [55.0, 1], ['51.0 + 2.0k', 1]])
    
    def test_no_points(self):
        no_points = points_within_range([None], 50, 60, 5, 2)
        self.assertEqual(no_points, [None])

class TestAccumulation(unittest.TestCase):
    def test_linear_accumulation(self):
        linear_accumulation = accumulated_area('linear', coefficients[:2], 10, 20)
        self.assertEqual(linear_accumulation, 330.0)
    
    def test_quadratic_accumulation(self):
        quadratic_accumulation = accumulated_area('quadratic', coefficients[:3], 10, 20)
        self.assertEqual(quadratic_accumulation, 5166.6667)
    
    def test_cubic_accumulation(self):
        cubic_accumulation = accumulated_area('cubic', coefficients[:4], 10, 20)
        self.assertEqual(cubic_accumulation, 82820.0)
    
    def test_hyperbolic_accumulation(self):
        hyperbolic_accumulation = accumulated_area('hyperbolic', coefficients[:2], 10, 20)
        self.assertEqual(hyperbolic_accumulation, 31.3863)
    
    def test_exponential_accumulation(self):
        exponential_accumulation = accumulated_area('exponential', coefficients[:2], 10, 20)
        self.assertEqual(exponential_accumulation, 6347508375.7293)
    
    def test_logarithmic_accumulation(self):
        logarithmic_accumulation = accumulated_area('logarithmic', coefficients[:2], 10, 20)
        self.assertEqual(logarithmic_accumulation, 83.7776)
    
    def test_logistic_accumulation(self):
        logistic_accumulation = accumulated_area('logistic', coefficients[:3], 10, 20)
        self.assertEqual(logistic_accumulation, 20.0)
    
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
        self.assertEqual(quadratic_averages, {'average_value_derivative': 63.0, 'mean_values_derivative': [15.0], 'average_value_integral': 516.6667, 'mean_values_integral': [15.2624]})
    
    def test_cubic_averages(self):
        cubic_averages = average_values('cubic', coefficients[:4], 10, 20)
        self.assertEqual(cubic_averages, {'average_value_derivative': 1495.0, 'mean_values_derivative': [15.2665], 'average_value_integral': 8282.0, 'mean_values_integral': [15.5188]})
    
    def test_hyperbolic_averages(self):
        hyperbolic_averages = average_values('hyperbolic', coefficients[:2], 10, 20)
        self.assertEqual(hyperbolic_averages, {'average_value_derivative': -0.01, 'mean_values_derivative': [14.1421], 'average_value_integral': 3.1386, 'mean_values_integral': [14.43]})
    
    def test_exponential_averages(self):
        exponential_averages = average_values('exponential', coefficients[:2], 10, 20)
        self.assertEqual(exponential_averages, {'average_value_derivative': 697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': 634750837.5729, 'mean_values_integral': [19.4815]})
    
    def test_exponential_averages_unary_base(self):
        exponential_averages_unary_base = average_values('exponential', [2, 1], 10, 20)
        self.assertEqual(exponential_averages_unary_base, {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 2.003, 'mean_values_integral': [None]})
    
    def test_exponential_averages_negative_base(self):
        exponential_averages_negative_base = average_values('exponential', [2, -3], 10, 20)
        self.assertEqual(exponential_averages_negative_base, {'average_value_derivative': 697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': 634750837.5729, 'mean_values_integral': [19.4815]})
    
    def test_exponential_averages_negative_lead(self):
        exponential_averages_negative_lead = average_values('exponential', [-2, 3], 10, 20)
        self.assertEqual(exponential_averages_negative_lead, {'average_value_derivative': -697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': -634750837.5729, 'mean_values_integral': [19.4815]})
    
    def test_logarithmic_averages(self):
        logarithmic_averages = average_values('logarithmic', coefficients[:2], 10, 20)
        self.assertEqual(logarithmic_averages, {'average_value_derivative': 0.1386, 'mean_values_derivative': [14.43], 'average_value_integral': 8.3778, 'mean_values_integral': [14.7155]})
    
    def test_logistic_averages(self):
        logistic_averages = average_values('logistic', coefficients[:3], 10, 20)
        self.assertEqual(logistic_averages, {'average_value_derivative': 0.0001, 'mean_values_derivative': [None], 'average_value_integral': 2.0, 'mean_values_integral': [None]})
    
    def test_sinusoidal_averages(self):
        sinusoidal_averages = average_values('sinusoidal', coefficients[:4], 10, 20)
        self.assertEqual(sinusoidal_averages, {'average_value_derivative': 0.0401, 'mean_values_derivative': [10.7618, 11.8046, 12.8562, 13.899, 14.9506, 15.9933, '10.7618 + 2.0944k', '11.8046 + 2.0944k'], 'average_value_integral': 6.9143, 'mean_values_integral': [10.2503, 11.2689, 12.3447, 13.3633, 14.4391, 15.4577, 16.5335, 17.5521, 18.6279, 19.6465, '10.2503 + 2.0944k', '11.2689 + 2.0944k']})
    
    def test_averages_start_end(self):
        averages_start_end = average_values('cubic', coefficients[:4], 1, 1)
        self.assertEqual(averages_start_end, {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 0.0, 'mean_values_integral': [None]})

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 245 tests in 0.035s ---------- OK ---------- #