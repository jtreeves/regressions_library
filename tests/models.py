import unittest

from library.models.linear import linear_model
from library.models.quadratic import quadratic_model
from library.models.cubic import cubic_model
from library.models.hyperbolic import hyperbolic_model
from library.models.exponential import exponential_model
from library.models.logarithmic import logarithmic_model
from library.models.logistic import logistic_model
from library.models.sinusoidal import sinusoidal_model

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

logistic_set = [
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

sinusoidal_set = [
    [1, 3], 
    [2, 8], 
    [3, 3], 
    [4, -2], 
    [5, 3], 
    [6, 8], 
    [7, 3], 
    [8, -2], 
    [9, 3], 
    [10, 8]
]

low_precision = 2
high_precision = 6

linear_model_low = linear_model(linear_set, low_precision)
linear_model_high = linear_model(linear_set, high_precision)

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

quadratic_model_low = quadratic_model(quadratic_set, low_precision)
quadratic_model_high = quadratic_model(quadratic_set, high_precision)

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

cubic_model_low = cubic_model(cubic_set, low_precision)
cubic_model_high = cubic_model(cubic_set, high_precision)

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

hyperbolic_model_low = hyperbolic_model(hyperbolic_set, low_precision)
hyperbolic_model_high = hyperbolic_model(hyperbolic_set, high_precision)

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

exponential_model_low = exponential_model(exponential_set, low_precision)
exponential_model_high = exponential_model(exponential_set, high_precision)

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

logarithmic_model_low = logarithmic_model(logarithmic_set, low_precision)
logarithmic_model_high = logarithmic_model(logarithmic_set, high_precision)

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

logistic_model_low = logistic_model(logistic_set, low_precision)
logistic_model_high = logistic_model(logistic_set, high_precision)

class TestLogisticModel(unittest.TestCase):
    def test_logistic_model_low_constants(self):
        self.assertEqual(logistic_model_low['constants'], [2.0, 3.0, 5.0])
    
    def test_logistic_model_low_roots(self):
        self.assertEqual(logistic_model_low['points']['roots'], [None])
    
    def test_logistic_model_low_maxima(self):
        self.assertEqual(logistic_model_low['points']['maxima'], [None])
    
    def test_logistic_model_low_minima(self):
        self.assertEqual(logistic_model_low['points']['minima'], [None])
    
    def test_logistic_model_low_inflections(self):
        self.assertEqual(logistic_model_low['points']['inflections'], [[5.0, 1.0]])
    
    def test_logistic_model_low_accumulations_range(self):
        self.assertEqual(logistic_model_low['accumulations']['range'], 10.0)
    
    def test_logistic_model_low_accumulations_iqr(self):
        self.assertEqual(logistic_model_low['accumulations']['iqr'], 6.0)
    
    def test_logistic_model_low_averages_range_derivative_value(self):
        self.assertEqual(logistic_model_low['averages']['range']['average_value_derivative'], 0.22)
    
    def test_logistic_model_low_averages_range_derivative_points(self):
        self.assertEqual(logistic_model_low['averages']['range']['mean_values_derivative'], [3.92, 6.07])
    
    def test_logistic_model_low_averages_range_integral_value(self):
        self.assertEqual(logistic_model_low['averages']['range']['average_value_integral'], 1.11)
    
    def test_logistic_model_low_averages_range_integral_points(self):
        self.assertEqual(logistic_model_low['averages']['range']['mean_values_integral'], [5.07])
    
    def test_logistic_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(logistic_model_low['averages']['iqr']['average_value_derivative'], 0.4)
    
    def test_logistic_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(logistic_model_low['averages']['iqr']['mean_values_derivative'], [4.15, 5.84])
    
    def test_logistic_model_low_averages_iqr_integral_value(self):
        self.assertEqual(logistic_model_low['averages']['iqr']['average_value_integral'], 1.2)
    
    def test_logistic_model_low_averages_iqr_integral_points(self):
        self.assertEqual(logistic_model_low['averages']['iqr']['mean_values_integral'], [5.14])
    
    def test_logistic_model_low_correlation(self):
        self.assertEqual(logistic_model_low['correlation'], 1.0)
    
    def test_logistic_model_high_constants(self):
        self.assertEqual(logistic_model_high['constants'], [2.0, 2.999998, 5.0])
    
    def test_logistic_model_high_roots(self):
        self.assertEqual(logistic_model_high['points']['roots'], [None])
    
    def test_logistic_model_high_maxima(self):
        self.assertEqual(logistic_model_high['points']['maxima'], [None])
    
    def test_logistic_model_high_minima(self):
        self.assertEqual(logistic_model_high['points']['minima'], [None])
    
    def test_logistic_model_high_inflections(self):
        self.assertEqual(logistic_model_high['points']['inflections'], [[5.0, 1.0]])
    
    def test_logistic_model_high_accumulations_range(self):
        self.assertEqual(logistic_model_high['accumulations']['range'], 9.999996)
    
    def test_logistic_model_high_accumulations_iqr(self):
        self.assertEqual(logistic_model_high['accumulations']['iqr'], 5.998432)
    
    def test_logistic_model_high_averages_range_derivative_value(self):
        self.assertEqual(logistic_model_high['averages']['range']['average_value_derivative'], 0.222221)
    
    def test_logistic_model_high_averages_range_derivative_points(self):
        self.assertEqual(logistic_model_high['averages']['range']['mean_values_derivative'], [3.927573, 6.072427])
    
    def test_logistic_model_high_averages_range_integral_value(self):
        self.assertEqual(logistic_model_high['averages']['range']['average_value_integral'], 1.111111)
    
    def test_logistic_model_high_averages_range_integral_points(self):
        self.assertEqual(logistic_model_high['averages']['range']['mean_values_integral'], [5.074381])
    
    def test_logistic_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(logistic_model_high['averages']['iqr']['average_value_derivative'], 0.398962)
    
    def test_logistic_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(logistic_model_high['averages']['iqr']['mean_values_derivative'], [4.145995, 5.854006])
    
    def test_logistic_model_high_averages_iqr_integral_value(self):
        self.assertEqual(logistic_model_high['averages']['iqr']['average_value_integral'], 1.199686)
    
    def test_logistic_model_high_averages_iqr_integral_points(self):
        self.assertEqual(logistic_model_high['averages']['iqr']['mean_values_integral'], [5.134937])
    
    def test_logistic_model_high_correlation(self):
        self.assertEqual(logistic_model_high['correlation'], 1.0)

sinusoidal_model_low = sinusoidal_model(sinusoidal_set, low_precision)
sinusoidal_model_high = sinusoidal_model(sinusoidal_set, high_precision)

class TestSinusoidalModel(unittest.TestCase):
    def test_sinusoidal_model_low_constants(self):
        self.assertEqual(sinusoidal_model_low['constants'], [-5.0, 1.57, 3.0, 3.0])
    
    def test_sinusoidal_model_low_roots(self):
        self.assertEqual(sinusoidal_model_low['points']['roots'], [[3.41, 0], [4.59, 0], [7.41, 0], [8.59, 0], ['3.41 + 4.0k', 0], ['4.59 + 4.0k', 0]])
    
    def test_sinusoidal_model_low_maxima(self):
        self.assertEqual(sinusoidal_model_low['points']['maxima'], [[6.0, 8.0], [10.0, 8.0], ['6.0 + 4.0k', 8.0]])
    
    def test_sinusoidal_model_low_minima(self):
        self.assertEqual(sinusoidal_model_low['points']['minima'], [[4.0, -2.0], [8.0, -2.0], ['4.0 + 4.0k', -2.0]])
    
    def test_sinusoidal_model_low_inflections(self):
        self.assertEqual(sinusoidal_model_low['points']['inflections'], [[3.0, 3.0], [5.0, 3.0], [7.0, 3.0], [9.0, 3.0], ['3.0 + 2.0k', 3.0]])
    
    def test_sinusoidal_model_low_accumulations_range(self):
        self.assertEqual(sinusoidal_model_low['accumulations']['range'], 30.18)
    
    def test_sinusoidal_model_low_accumulations_iqr(self):
        self.assertEqual(sinusoidal_model_low['accumulations']['iqr'], 11.82)
    
    def test_sinusoidal_model_low_averages_range_derivative_value(self):
        self.assertEqual(sinusoidal_model_low['averages']['range']['average_value_derivative'], 0.56)
    
    def test_sinusoidal_model_low_averages_range_derivative_points(self):
        self.assertEqual(sinusoidal_model_low['averages']['range']['mean_values_derivative'], [4.05, 5.95, 8.05, 9.95, '4.05 + 4.0k', '5.95 + 4.0k'])
    
    def test_sinusoidal_model_low_averages_range_integral_value(self):
        self.assertEqual(sinusoidal_model_low['averages']['range']['average_value_integral'], 3.35)
    
    def test_sinusoidal_model_low_averages_range_integral_points(self):
        self.assertEqual(sinusoidal_model_low['averages']['range']['mean_values_integral'], [2.96, 5.04, 6.96, 9.04, '2.96 + 4.0k', '5.04 + 4.0k'])
    
    def test_sinusoidal_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(sinusoidal_model_low['averages']['iqr']['average_value_derivative'], -1.0)
    
    def test_sinusoidal_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(sinusoidal_model_low['averages']['iqr']['mean_values_derivative'], [3.92, 6.08, 7.92, '3.92 + 4.0k', '6.08 + 4.0k'])
    
    def test_sinusoidal_model_low_averages_iqr_integral_value(self):
        self.assertEqual(sinusoidal_model_low['averages']['iqr']['average_value_integral'], 2.36)
    
    def test_sinusoidal_model_low_averages_iqr_integral_points(self):
        self.assertEqual(sinusoidal_model_low['averages']['iqr']['mean_values_integral'], [3.08, 4.92, 7.08, '3.08 + 4.0k', '4.92 + 4.0k'])
    
    def test_sinusoidal_model_low_correlation(self):
        self.assertEqual(sinusoidal_model_low['correlation'], 1.0)
    
    def test_sinusoidal_model_high_constants(self):
        self.assertEqual(sinusoidal_model_high['constants'], [-5.0, 1.570796, 3.0, 3.0])
    
    def test_sinusoidal_model_high_roots(self):
        self.assertEqual(sinusoidal_model_high['points']['roots'], [[3.409666, 0], [4.590334, 0], [7.409666, 0], [8.590334, 0], ['3.409666 + 4.0k', 0], ['4.590334 + 4.0k', 0]])
    
    def test_sinusoidal_model_high_maxima(self):
        self.assertEqual(sinusoidal_model_high['points']['maxima'], [[6.0, 8.0], [10.0, 8.0], ['6.0 + 4.0k', 8.0]])
    
    def test_sinusoidal_model_high_minima(self):
        self.assertEqual(sinusoidal_model_high['points']['minima'], [[4.0, -2.0], [8.0, -2.0], ['4.0 + 4.0k', -2.0]])
    
    def test_sinusoidal_model_high_inflections(self):
        self.assertEqual(sinusoidal_model_high['points']['inflections'], [[3.0, 3.0], [5.0, 3.0], [7.0, 3.0], [9.0, 3.0], ['3.0 + 2.0k', 3.0]])
    
    def test_sinusoidal_model_high_accumulations_range(self):
        self.assertEqual(sinusoidal_model_high['accumulations']['range'], 30.183099)
    
    def test_sinusoidal_model_high_accumulations_iqr(self):
        self.assertEqual(sinusoidal_model_high['accumulations']['iqr'], 11.816901)
    
    def test_sinusoidal_model_high_averages_range_derivative_value(self):
        self.assertEqual(sinusoidal_model_high['averages']['range']['average_value_derivative'], 0.555556)
    
    def test_sinusoidal_model_high_averages_range_derivative_points(self):
        self.assertEqual(sinusoidal_model_high['averages']['range']['mean_values_derivative'], [4.045069, 5.954931, 8.045069, 9.954931, '4.045069 + 4.0k', '5.954931 + 4.0k'])
    
    def test_sinusoidal_model_high_averages_range_integral_value(self):
        self.assertEqual(sinusoidal_model_high['averages']['range']['average_value_integral'], 3.353678)
    
    def test_sinusoidal_model_high_averages_range_integral_points(self):
        self.assertEqual(sinusoidal_model_high['averages']['range']['mean_values_integral'], [2.954931, 5.045069, 6.954931, 9.045069, '2.954931 + 4.0k', '5.045069 + 4.0k'])
    
    def test_sinusoidal_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(sinusoidal_model_high['averages']['iqr']['average_value_derivative'], -1.0)
    
    def test_sinusoidal_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(sinusoidal_model_high['averages']['iqr']['mean_values_derivative'], [3.918722, 6.081278, 7.918722, '3.918722 + 4.0k', '6.081278 + 4.0k'])
    
    def test_sinusoidal_model_high_averages_iqr_integral_value(self):
        self.assertEqual(sinusoidal_model_high['averages']['iqr']['average_value_integral'], 2.36338)
    
    def test_sinusoidal_model_high_averages_iqr_integral_points(self):
        self.assertEqual(sinusoidal_model_high['averages']['iqr']['mean_values_integral'], [3.081278, 4.918722, 7.081278, '3.081278 + 4.0k', '4.918722 + 4.0k'])
    
    def test_sinusoidal_model_high_correlation(self):
        self.assertEqual(sinusoidal_model_high['correlation'], 1.0)

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 256 tests in 0.022s ---------- OK ---------- #