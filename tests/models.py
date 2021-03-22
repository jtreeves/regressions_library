import unittest

from library.models.linear import linear
from library.models.quadratic import quadratic
from library.models.cubic import cubic
from library.models.hyperbolic import hyperbolic
from library.models.exponential import exponential
from library.models.logarithmic import logarithmic

linear_set = [
    [1, 30],
    [2, 27],
    [3, 24],
    [4, 21],
    [5, 18],
    [6, 15],
    [7, 12],
    [8, 9],
    [9, 6],
    [10, 3]
]

quadratic_set = [
    [1, 10],
    [2, 27],
    [3, 40],
    [4, 49],
    [5, 54],
    [6, 55],
    [7, 52],
    [8, 45],
    [9, 34],
    [10, 19]
]

cubic_set = [
    [1, 42],
    [2, 67],
    [3, 74],
    [4, 69],
    [5, 58],
    [6, 47],
    [7, 42],
    [8, 49],
    [9, 74],
    [10, 123]
]

hyperbolic_set = [
    [1, 2519],
    [2, 1259],
    [3, 839],
    [4, 629],
    [5, 503],
    [6, 419],
    [7, 359],
    [8, 314],
    [9, 279],
    [10, 251]
]

exponential_set = [
    [1, 6],
    [2, 12],
    [3, 24],
    [4, 48],
    [5, 96],
    [6, 192],
    [7, 384],
    [8, 768],
    [9, 1536],
    [10, 3072]
]

logarithmic_set = [
    [1, 2],
    [2, 4.0794],
    [3, 5.2958],
    [4, 6.1589],
    [5, 6.8283],
    [6, 7.3753],
    [7, 7.8377],
    [8, 8.2383],
    [9, 8.5917],
    [10, 8.9078]
]

low_precision = 2
high_precision = 6

linear_model_low = linear(linear_set, low_precision)
linear_model_high = linear(linear_set, high_precision)

class TestLinearModel(unittest.TestCase):
    def test_linear_model_low_constants(self):
        self.assertEqual(linear_model_low['constants'], [-3.0, 33.0])
    
    def test_linear_model_low_roots(self):
        self.assertEqual(linear_model_low['points']['roots'], [[11.0, 0]])
    
    def test_linear_model_low_maxima(self):
        self.assertEqual(linear_model_low['points']['maxima'], [None])
    
    def test_linear_model_low_minima(self):
        self.assertEqual(linear_model_low['points']['minima'], [None])
    
    def test_linear_model_low_inflections(self):
        self.assertEqual(linear_model_low['points']['inflections'], [None])
    
    def test_linear_model_low_accumulations_range(self):
        self.assertEqual(linear_model_low['accumulations']['range'], 148.5)
    
    def test_linear_model_low_accumulations_iqr(self):
        self.assertEqual(linear_model_low['accumulations']['iqr'], 82.5)
    
    def test_linear_model_low_averages_range_derivative_value(self):
        self.assertEqual(linear_model_low['averages']['range']['average_value_derivative'], -3.0)
    
    def test_linear_model_low_averages_range_derivative_points(self):
        self.assertEqual(linear_model_low['averages']['range']['mean_values_derivative'], ['All'])
    
    def test_linear_model_low_averages_range_integral_value(self):
        self.assertEqual(linear_model_low['averages']['range']['average_value_integral'], 16.5)
    
    def test_linear_model_low_averages_range_integral_points(self):
        self.assertEqual(linear_model_low['averages']['range']['mean_values_integral'], [5.5])
    
    def test_linear_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(linear_model_low['averages']['iqr']['average_value_derivative'], -3.0)
    
    def test_linear_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(linear_model_low['averages']['iqr']['mean_values_derivative'], ['All'])
    
    def test_linear_model_low_averages_iqr_integral_value(self):
        self.assertEqual(linear_model_low['averages']['iqr']['average_value_integral'], 16.5)
    
    def test_linear_model_low_averages_iqr_integral_points(self):
        self.assertEqual(linear_model_low['averages']['iqr']['mean_values_integral'], [5.5])
    
    def test_linear_model_low_correlation(self):
        self.assertEqual(linear_model_low['correlation'], 1.0)
    
    def test_linear_model_high_constants(self):
        self.assertEqual(linear_model_high['constants'], [-3.0, 33.0])
    
    def test_linear_model_high_roots(self):
        self.assertEqual(linear_model_high['points']['roots'], [[11.0, 0]])
    
    def test_linear_model_high_maxima(self):
        self.assertEqual(linear_model_high['points']['maxima'], [None])
    
    def test_linear_model_high_minima(self):
        self.assertEqual(linear_model_high['points']['minima'], [None])
    
    def test_linear_model_high_inflections(self):
        self.assertEqual(linear_model_high['points']['inflections'], [None])
    
    def test_linear_model_high_accumulations_range(self):
        self.assertEqual(linear_model_high['accumulations']['range'], 148.5)
    
    def test_linear_model_high_accumulations_iqr(self):
        self.assertEqual(linear_model_high['accumulations']['iqr'], 82.5)
    
    def test_linear_model_high_averages_range_derivative_value(self):
        self.assertEqual(linear_model_high['averages']['range']['average_value_derivative'], -3.0)
    
    def test_linear_model_high_averages_range_derivative_points(self):
        self.assertEqual(linear_model_high['averages']['range']['mean_values_derivative'], ['All'])
    
    def test_linear_model_high_averages_range_integral_value(self):
        self.assertEqual(linear_model_high['averages']['range']['average_value_integral'], 16.5)
    
    def test_linear_model_high_averages_range_integral_points(self):
        self.assertEqual(linear_model_high['averages']['range']['mean_values_integral'], [5.5])
    
    def test_linear_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(linear_model_high['averages']['iqr']['average_value_derivative'], -3.0)
    
    def test_linear_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(linear_model_high['averages']['iqr']['mean_values_derivative'], ['All'])
    
    def test_linear_model_high_averages_iqr_integral_value(self):
        self.assertEqual(linear_model_high['averages']['iqr']['average_value_integral'], 16.5)
    
    def test_linear_model_high_averages_iqr_integral_points(self):
        self.assertEqual(linear_model_high['averages']['iqr']['mean_values_integral'], [5.5])
    
    def test_linear_model_high_correlation(self):
        self.assertEqual(linear_model_high['correlation'], 1.0)

quadratic_model_low = quadratic(quadratic_set, low_precision)
quadratic_model_high = quadratic(quadratic_set, high_precision)

class TestQuadraticModel(unittest.TestCase):
    def test_quadratic_model_low_constants(self):
        self.assertEqual(quadratic_model_low['constants'], [-2.0, 23.0, -11.0])
    
    def test_quadratic_model_low_roots(self):
        self.assertEqual(quadratic_model_low['points']['roots'], [[0.5, 0], [11.0, 0]])
    
    def test_quadratic_model_low_maxima(self):
        self.assertEqual(quadratic_model_low['points']['maxima'], [[5.75, 55.12]])
    
    def test_quadratic_model_low_minima(self):
        self.assertEqual(quadratic_model_low['points']['minima'], [None])
    
    def test_quadratic_model_low_inflections(self):
        self.assertEqual(quadratic_model_low['points']['inflections'], [None])
    
    def test_quadratic_model_low_accumulations_range(self):
        self.assertEqual(quadratic_model_low['accumulations']['range'], 373.5)
    
    def test_quadratic_model_low_accumulations_iqr(self):
        self.assertEqual(quadratic_model_low['accumulations']['iqr'], 254.17)
    
    def test_quadratic_model_low_averages_range_derivative_value(self):
        self.assertEqual(quadratic_model_low['averages']['range']['average_value_derivative'], 1.0)
    
    def test_quadratic_model_low_averages_range_derivative_points(self):
        self.assertEqual(quadratic_model_low['averages']['range']['mean_values_derivative'], [5.5])
    
    def test_quadratic_model_low_averages_range_integral_value(self):
        self.assertEqual(quadratic_model_low['averages']['range']['average_value_integral'], 41.5)
    
    def test_quadratic_model_low_averages_range_integral_points(self):
        self.assertEqual(quadratic_model_low['averages']['range']['mean_values_integral'], [3.14, 8.36])
    
    def test_quadratic_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(quadratic_model_low['averages']['iqr']['average_value_derivative'], 1.0)
    
    def test_quadratic_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(quadratic_model_low['averages']['iqr']['mean_values_derivative'], [5.5])
    
    def test_quadratic_model_low_averages_iqr_integral_value(self):
        self.assertEqual(quadratic_model_low['averages']['iqr']['average_value_integral'], 50.83)
    
    def test_quadratic_model_low_averages_iqr_integral_points(self):
        self.assertEqual(quadratic_model_low['averages']['iqr']['mean_values_integral'], [4.28, 7.22])
    
    def test_quadratic_model_low_correlation(self):
        self.assertEqual(quadratic_model_low['correlation'], 1.0)
    
    def test_quadratic_model_high_constants(self):
        self.assertEqual(quadratic_model_high['constants'], [-2.0, 23.0, -11.0])
    
    def test_quadratic_model_high_roots(self):
        self.assertEqual(quadratic_model_high['points']['roots'], [[0.5, 0], [11.0, 0]])
    
    def test_quadratic_model_high_maxima(self):
        self.assertEqual(quadratic_model_high['points']['maxima'], [[5.75, 55.125]])
    
    def test_quadratic_model_high_minima(self):
        self.assertEqual(quadratic_model_high['points']['minima'], [None])
    
    def test_quadratic_model_high_inflections(self):
        self.assertEqual(quadratic_model_high['points']['inflections'], [None])
    
    def test_quadratic_model_high_accumulations_range(self):
        self.assertEqual(quadratic_model_high['accumulations']['range'], 373.5)
    
    def test_quadratic_model_high_accumulations_iqr(self):
        self.assertEqual(quadratic_model_high['accumulations']['iqr'], 254.166667)
    
    def test_quadratic_model_high_averages_range_derivative_value(self):
        self.assertEqual(quadratic_model_high['averages']['range']['average_value_derivative'], 1.0)
    
    def test_quadratic_model_high_averages_range_derivative_points(self):
        self.assertEqual(quadratic_model_high['averages']['range']['mean_values_derivative'], [5.5])
    
    def test_quadratic_model_high_averages_range_integral_value(self):
        self.assertEqual(quadratic_model_high['averages']['range']['average_value_integral'], 41.5)
    
    def test_quadratic_model_high_averages_range_integral_points(self):
        self.assertEqual(quadratic_model_high['averages']['range']['mean_values_integral'], [3.139923, 8.360077])
    
    def test_quadratic_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(quadratic_model_high['averages']['iqr']['average_value_derivative'], 1.0)
    
    def test_quadratic_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(quadratic_model_high['averages']['iqr']['mean_values_derivative'], [5.5])
    
    def test_quadratic_model_high_averages_iqr_integral_value(self):
        self.assertEqual(quadratic_model_high['averages']['iqr']['average_value_integral'], 50.833333)
    
    def test_quadratic_model_high_averages_iqr_integral_points(self):
        self.assertEqual(quadratic_model_high['averages']['iqr']['mean_values_integral'], [4.285134, 7.214866])
    
    def test_quadratic_model_high_correlation(self):
        self.assertEqual(quadratic_model_high['correlation'], 1.0)

cubic_model_low = cubic(cubic_set, low_precision)
cubic_model_high = cubic(cubic_set, high_precision)

class TestCubicModel(unittest.TestCase):
    def test_cubic_model_low_constants(self):
        self.assertEqual(cubic_model_low['constants'], [1.0, -15.0, 63.0, -7.0])
    
    def test_cubic_model_low_roots(self):
        self.assertEqual(cubic_model_low['points']['roots'], [[0.11, 0]])
    
    def test_cubic_model_low_maxima(self):
        self.assertEqual(cubic_model_low['points']['maxima'], [[3.0, 74.0]])
    
    def test_cubic_model_low_minima(self):
        self.assertEqual(cubic_model_low['points']['minima'], [[7.0, 42.0]])
    
    def test_cubic_model_low_inflections(self):
        self.assertEqual(cubic_model_low['points']['inflections'], [[5.0, 58.0]])
    
    def test_cubic_model_low_accumulations_range(self):
        self.assertEqual(cubic_model_low['accumulations']['range'], 560.25)
    
    def test_cubic_model_low_accumulations_iqr(self):
        self.assertEqual(cubic_model_low['accumulations']['iqr'], 276.25)
    
    def test_cubic_model_low_averages_range_derivative_value(self):
        self.assertEqual(cubic_model_low['averages']['range']['average_value_derivative'], 9.0)
    
    def test_cubic_model_low_averages_range_derivative_points(self):
        self.assertEqual(cubic_model_low['averages']['range']['mean_values_derivative'], [2.35, 7.65])
    
    def test_cubic_model_low_averages_range_integral_value(self):
        self.assertEqual(cubic_model_low['averages']['range']['average_value_integral'], 62.25)
    
    def test_cubic_model_low_averages_range_integral_points(self):
        self.assertEqual(cubic_model_low['averages']['range']['mean_values_integral'], [1.73, 4.64, 8.63])
    
    def test_cubic_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(cubic_model_low['averages']['iqr']['average_value_derivative'], -5.0)
    
    def test_cubic_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(cubic_model_low['averages']['iqr']['mean_values_derivative'], [3.47, 6.53])
    
    def test_cubic_model_low_averages_iqr_integral_value(self):
        self.assertEqual(cubic_model_low['averages']['iqr']['average_value_integral'], 55.25)
    
    def test_cubic_model_low_averages_iqr_integral_points(self):
        self.assertEqual(cubic_model_low['averages']['iqr']['mean_values_integral'], [5.23])
    
    def test_cubic_model_low_correlation(self):
        self.assertEqual(cubic_model_low['correlation'], 1.0)
    
    def test_cubic_model_high_constants(self):
        self.assertEqual(cubic_model_high['constants'], [1.0, -15.0, 63.0, -7.0])
    
    def test_cubic_model_high_roots(self):
        self.assertEqual(cubic_model_high['points']['roots'], [[0.114192, 0]])
    
    def test_cubic_model_high_maxima(self):
        self.assertEqual(cubic_model_high['points']['maxima'], [[3.0, 74.0]])
    
    def test_cubic_model_high_minima(self):
        self.assertEqual(cubic_model_high['points']['minima'], [[7.0, 42.0]])
    
    def test_cubic_model_high_inflections(self):
        self.assertEqual(cubic_model_high['points']['inflections'], [[5.0, 58.0]])
    
    def test_cubic_model_high_accumulations_range(self):
        self.assertEqual(cubic_model_high['accumulations']['range'], 560.25)
    
    def test_cubic_model_high_accumulations_iqr(self):
        self.assertEqual(cubic_model_high['accumulations']['iqr'], 276.25)
    
    def test_cubic_model_high_averages_range_derivative_value(self):
        self.assertEqual(cubic_model_high['averages']['range']['average_value_derivative'], 9.0)
    
    def test_cubic_model_high_averages_range_derivative_points(self):
        self.assertEqual(cubic_model_high['averages']['range']['mean_values_derivative'], [2.354249, 7.645751])
    
    def test_cubic_model_high_averages_range_integral_value(self):
        self.assertEqual(cubic_model_high['averages']['range']['average_value_integral'], 62.25)
    
    def test_cubic_model_high_averages_range_integral_points(self):
        self.assertEqual(cubic_model_high['averages']['range']['mean_values_integral'], [1.728795, 4.64201, 8.629195])
    
    def test_cubic_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(cubic_model_high['averages']['iqr']['average_value_derivative'], -5.0)
    
    def test_cubic_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(cubic_model_high['averages']['iqr']['mean_values_derivative'], [3.472475, 6.527525])
    
    def test_cubic_model_high_averages_iqr_integral_value(self):
        self.assertEqual(cubic_model_high['averages']['iqr']['average_value_integral'], 55.25)
    
    def test_cubic_model_high_averages_iqr_integral_points(self):
        self.assertEqual(cubic_model_high['averages']['iqr']['mean_values_integral'], [5.230183])
    
    def test_cubic_model_high_correlation(self):
        self.assertEqual(cubic_model_high['correlation'], 1.0)

hyperbolic_model_low = hyperbolic(hyperbolic_set, low_precision)
hyperbolic_model_high = hyperbolic(hyperbolic_set, high_precision)

class TestHyperbolicModel(unittest.TestCase):
    def test_hyperbolic_model_low_constants(self):
        self.assertEqual(hyperbolic_model_low['constants'], [2520.0, -1.0])
    
    def test_hyperbolic_model_low_roots(self):
        self.assertEqual(hyperbolic_model_low['points']['roots'], [[2520.0, 0]])
    
    def test_hyperbolic_model_low_maxima(self):
        self.assertEqual(hyperbolic_model_low['points']['maxima'], [None])
    
    def test_hyperbolic_model_low_minima(self):
        self.assertEqual(hyperbolic_model_low['points']['minima'], [None])
    
    def test_hyperbolic_model_low_inflections(self):
        self.assertEqual(hyperbolic_model_low['points']['inflections'], [None])
    
    def test_hyperbolic_model_low_accumulations_range(self):
        self.assertEqual(hyperbolic_model_low['accumulations']['range'], 5793.51)
    
    def test_hyperbolic_model_low_accumulations_iqr(self):
        self.assertEqual(hyperbolic_model_low['accumulations']['iqr'], 2466.69)
    
    def test_hyperbolic_model_low_averages_range_derivative_value(self):
        self.assertEqual(hyperbolic_model_low['averages']['range']['average_value_derivative'], -252.0)
    
    def test_hyperbolic_model_low_averages_range_derivative_points(self):
        self.assertEqual(hyperbolic_model_low['averages']['range']['mean_values_derivative'], [3.16])
    
    def test_hyperbolic_model_low_averages_range_integral_value(self):
        self.assertEqual(hyperbolic_model_low['averages']['range']['average_value_integral'], 643.72)
    
    def test_hyperbolic_model_low_averages_range_integral_points(self):
        self.assertEqual(hyperbolic_model_low['averages']['range']['mean_values_integral'], [3.91])
    
    def test_hyperbolic_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(hyperbolic_model_low['averages']['iqr']['average_value_derivative'], -105.0)
    
    def test_hyperbolic_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(hyperbolic_model_low['averages']['iqr']['mean_values_derivative'], [4.9])
    
    def test_hyperbolic_model_low_averages_iqr_integral_value(self):
        self.assertEqual(hyperbolic_model_low['averages']['iqr']['average_value_integral'], 493.34)
    
    def test_hyperbolic_model_low_averages_iqr_integral_points(self):
        self.assertEqual(hyperbolic_model_low['averages']['iqr']['mean_values_integral'], [5.1])
    
    def test_hyperbolic_model_low_correlation(self):
        self.assertEqual(hyperbolic_model_low['correlation'], 1.0)
    
    def test_hyperbolic_model_high_constants(self):
        self.assertEqual(hyperbolic_model_high['constants'], [2520.0, -1.0])
    
    def test_hyperbolic_model_high_roots(self):
        self.assertEqual(hyperbolic_model_high['points']['roots'], [[2520.0, 0]])
    
    def test_hyperbolic_model_high_maxima(self):
        self.assertEqual(hyperbolic_model_high['points']['maxima'], [None])
    
    def test_hyperbolic_model_high_minima(self):
        self.assertEqual(hyperbolic_model_high['points']['minima'], [None])
    
    def test_hyperbolic_model_high_inflections(self):
        self.assertEqual(hyperbolic_model_high['points']['inflections'], [None])
    
    def test_hyperbolic_model_high_accumulations_range(self):
        self.assertEqual(hyperbolic_model_high['accumulations']['range'], 5793.514434)
    
    def test_hyperbolic_model_high_accumulations_iqr(self):
        self.assertEqual(hyperbolic_model_high['accumulations']['iqr'], 2466.689718)
    
    def test_hyperbolic_model_high_averages_range_derivative_value(self):
        self.assertEqual(hyperbolic_model_high['averages']['range']['average_value_derivative'], -252.0)
    
    def test_hyperbolic_model_high_averages_range_derivative_points(self):
        self.assertEqual(hyperbolic_model_high['averages']['range']['mean_values_derivative'], [3.162278])
    
    def test_hyperbolic_model_high_averages_range_integral_value(self):
        self.assertEqual(hyperbolic_model_high['averages']['range']['average_value_integral'], 643.723826)
    
    def test_hyperbolic_model_high_averages_range_integral_points(self):
        self.assertEqual(hyperbolic_model_high['averages']['range']['mean_values_integral'], [3.90865])
    
    def test_hyperbolic_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(hyperbolic_model_high['averages']['iqr']['average_value_derivative'], -105.0)
    
    def test_hyperbolic_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(hyperbolic_model_high['averages']['iqr']['mean_values_derivative'], [4.898979])
    
    def test_hyperbolic_model_high_averages_iqr_integral_value(self):
        self.assertEqual(hyperbolic_model_high['averages']['iqr']['average_value_integral'], 493.337944)
    
    def test_hyperbolic_model_high_averages_iqr_integral_points(self):
        self.assertEqual(hyperbolic_model_high['averages']['iqr']['mean_values_integral'], [5.097727])
    
    def test_hyperbolic_model_high_correlation(self):
        self.assertEqual(hyperbolic_model_high['correlation'], 1.0)

exponential_model_low = exponential(exponential_set, low_precision)
exponential_model_high = exponential(exponential_set, high_precision)

class TestExponentialModel(unittest.TestCase):
    def test_exponential_model_low_constants(self):
        self.assertEqual(exponential_model_low['constants'], [3.0, 1.99])
    
    def test_exponential_model_low_roots(self):
        self.assertEqual(exponential_model_low['points']['roots'], [None])
    
    def test_exponential_model_low_maxima(self):
        self.assertEqual(exponential_model_low['points']['maxima'], [None])
    
    def test_exponential_model_low_minima(self):
        self.assertEqual(exponential_model_low['points']['minima'], [None])
    
    def test_exponential_model_low_inflections(self):
        self.assertEqual(exponential_model_low['points']['inflections'], [None])
    
    def test_exponential_model_low_accumulations_range(self):
        self.assertEqual(exponential_model_low['accumulations']['range'], 4237.31)
    
    def test_exponential_model_low_accumulations_iqr(self):
        self.assertEqual(exponential_model_low['accumulations']['iqr'], 1037.84)
    
    def test_exponential_model_low_averages_range_derivative_value(self):
        self.assertEqual(exponential_model_low['averages']['range']['average_value_derivative'], 323.98)
    
    def test_exponential_model_low_averages_range_derivative_points(self):
        self.assertEqual(exponential_model_low['averages']['range']['mean_values_derivative'], [7.35])
    
    def test_exponential_model_low_averages_range_integral_value(self):
        self.assertEqual(exponential_model_low['averages']['range']['average_value_integral'], 470.81)
    
    def test_exponential_model_low_averages_range_integral_points(self):
        self.assertEqual(exponential_model_low['averages']['range']['mean_values_integral'], [7.35])
    
    def test_exponential_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(exponential_model_low['averages']['iqr']['average_value_derivative'], 142.83)
    
    def test_exponential_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(exponential_model_low['averages']['iqr']['mean_values_derivative'], [6.16])
    
    def test_exponential_model_low_averages_iqr_integral_value(self):
        self.assertEqual(exponential_model_low['averages']['iqr']['average_value_integral'], 207.57)
    
    def test_exponential_model_low_averages_iqr_integral_points(self):
        self.assertEqual(exponential_model_low['averages']['iqr']['mean_values_integral'], [6.16])
    
    def test_exponential_model_low_correlation(self):
        self.assertEqual(exponential_model_low['correlation'], 1.0)
    
    def test_exponential_model_high_constants(self):
        self.assertEqual(exponential_model_high['constants'], [2.999999, 2.0])
    
    def test_exponential_model_high_roots(self):
        self.assertEqual(exponential_model_high['points']['roots'], [None])
    
    def test_exponential_model_high_maxima(self):
        self.assertEqual(exponential_model_high['points']['maxima'], [None])
    
    def test_exponential_model_high_minima(self):
        self.assertEqual(exponential_model_high['points']['minima'], [None])
    
    def test_exponential_model_high_inflections(self):
        self.assertEqual(exponential_model_high['points']['inflections'], [None])
    
    def test_exponential_model_high_accumulations_range(self):
        self.assertEqual(exponential_model_high['accumulations']['range'], 4423.301521)
    
    def test_exponential_model_high_accumulations_iqr(self):
        self.assertEqual(exponential_model_high['accumulations']['iqr'], 1073.364753)
    
    def test_exponential_model_high_averages_range_derivative_value(self):
        self.assertEqual(exponential_model_high['averages']['range']['average_value_derivative'], 340.666553)
    
    def test_exponential_model_high_averages_range_derivative_points(self):
        self.assertEqual(exponential_model_high['averages']['range']['mean_values_derivative'], [7.356021])
    
    def test_exponential_model_high_averages_range_integral_value(self):
        self.assertEqual(exponential_model_high['averages']['range']['average_value_integral'], 491.477947)
    
    def test_exponential_model_high_averages_range_integral_points(self):
        self.assertEqual(exponential_model_high['averages']['range']['mean_values_integral'], [7.356021])
    
    def test_exponential_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(exponential_model_high['averages']['iqr']['average_value_derivative'], 148.79995)
    
    def test_exponential_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(exponential_model_high['averages']['iqr']['mean_values_derivative'], [6.161035])
    
    def test_exponential_model_high_averages_iqr_integral_value(self):
        self.assertEqual(exponential_model_high['averages']['iqr']['average_value_integral'], 214.672951)
    
    def test_exponential_model_high_averages_iqr_integral_points(self):
        self.assertEqual(exponential_model_high['averages']['iqr']['mean_values_integral'], [6.161035])
    
    def test_exponential_model_high_correlation(self):
        self.assertEqual(exponential_model_high['correlation'], 1.0)

logarithmic_model_low = logarithmic(logarithmic_set, low_precision)
logarithmic_model_high = logarithmic(logarithmic_set, high_precision)

class TestLogarithmicModel(unittest.TestCase):
    def test_logarithmic_model_low_constants(self):
        self.assertEqual(logarithmic_model_low['constants'], [3.0, 2.0])
    
    def test_logarithmic_model_low_roots(self):
        self.assertEqual(logarithmic_model_low['points']['roots'], [[0.51, 0]])
    
    def test_logarithmic_model_low_maxima(self):
        self.assertEqual(logarithmic_model_low['points']['maxima'], [None])
    
    def test_logarithmic_model_low_minima(self):
        self.assertEqual(logarithmic_model_low['points']['minima'], [None])
    
    def test_logarithmic_model_low_inflections(self):
        self.assertEqual(logarithmic_model_low['points']['inflections'], [None])
    
    def test_logarithmic_model_low_accumulations_range(self):
        self.assertEqual(logarithmic_model_low['accumulations']['range'], 60.08)
    
    def test_logarithmic_model_low_accumulations_iqr(self):
        self.assertEqual(logarithmic_model_low['accumulations']['iqr'], 35.02)
    
    def test_logarithmic_model_low_averages_range_derivative_value(self):
        self.assertEqual(logarithmic_model_low['averages']['range']['average_value_derivative'], 0.77)
    
    def test_logarithmic_model_low_averages_range_derivative_points(self):
        self.assertEqual(logarithmic_model_low['averages']['range']['mean_values_derivative'], [3.9])
    
    def test_logarithmic_model_low_averages_range_integral_value(self):
        self.assertEqual(logarithmic_model_low['averages']['range']['average_value_integral'], 6.68)
    
    def test_logarithmic_model_low_averages_range_integral_points(self):
        self.assertEqual(logarithmic_model_low['averages']['range']['mean_values_integral'], [4.76])
    
    def test_logarithmic_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(logarithmic_model_low['averages']['iqr']['average_value_derivative'], 0.59)
    
    def test_logarithmic_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(logarithmic_model_low['averages']['iqr']['mean_values_derivative'], [5.08])
    
    def test_logarithmic_model_low_averages_iqr_integral_value(self):
        self.assertEqual(logarithmic_model_low['averages']['iqr']['average_value_integral'], 7.0)
    
    def test_logarithmic_model_low_averages_iqr_integral_points(self):
        self.assertEqual(logarithmic_model_low['averages']['iqr']['mean_values_integral'], [5.29])
    
    def test_logarithmic_model_low_correlation(self):
        self.assertEqual(logarithmic_model_low['correlation'], 1.0)
    
    def test_logarithmic_model_high_constants(self):
        self.assertEqual(logarithmic_model_high['constants'], [3.000016, 1.999972])
    
    def test_logarithmic_model_high_roots(self):
        self.assertEqual(logarithmic_model_high['points']['roots'], [[0.513424, 0]])
    
    def test_logarithmic_model_high_maxima(self):
        self.assertEqual(logarithmic_model_high['points']['maxima'], [None])
    
    def test_logarithmic_model_high_minima(self):
        self.assertEqual(logarithmic_model_high['points']['minima'], [None])
    
    def test_logarithmic_model_high_inflections(self):
        self.assertEqual(logarithmic_model_high['points']['inflections'], [None])
    
    def test_logarithmic_model_high_accumulations_range(self):
        self.assertEqual(logarithmic_model_high['accumulations']['range'], 60.077525)
    
    def test_logarithmic_model_high_accumulations_iqr(self):
        self.assertEqual(logarithmic_model_high['accumulations']['iqr'], 35.01908)
    
    def test_logarithmic_model_high_averages_range_derivative_value(self):
        self.assertEqual(logarithmic_model_high['averages']['range']['average_value_derivative'], 0.767532)
    
    def test_logarithmic_model_high_averages_range_derivative_points(self):
        self.assertEqual(logarithmic_model_high['averages']['range']['mean_values_derivative'], [3.908653])
    
    def test_logarithmic_model_high_averages_range_integral_value(self):
        self.assertEqual(logarithmic_model_high['averages']['range']['average_value_integral'], 6.675281)
    
    def test_logarithmic_model_high_averages_range_integral_points(self):
        self.assertEqual(logarithmic_model_high['averages']['range']['mean_values_integral'], [4.751346])
    
    def test_logarithmic_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(logarithmic_model_high['averages']['iqr']['average_value_derivative'], 0.588501)
    
    def test_logarithmic_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(logarithmic_model_high['averages']['iqr']['mean_values_derivative'], [5.097725])
    
    def test_logarithmic_model_high_averages_iqr_integral_value(self):
        self.assertEqual(logarithmic_model_high['averages']['iqr']['average_value_integral'], 7.003816)
    
    def test_logarithmic_model_high_averages_iqr_integral_points(self):
        self.assertEqual(logarithmic_model_high['averages']['iqr']['mean_values_integral'], [5.301231])
    
    def test_logarithmic_model_high_correlation(self):
        self.assertEqual(logarithmic_model_high['correlation'], 1.0)

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 192 tests in 0.015s ---------- OK ---------- #