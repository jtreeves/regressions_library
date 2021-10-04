import unittest

from regressions.models.linear import linear_model
from regressions.models.quadratic import quadratic_model
from regressions.models.cubic import cubic_model
from regressions.models.hyperbolic import hyperbolic_model
from regressions.models.exponential import exponential_model
from regressions.models.logarithmic import logarithmic_model
from regressions.models.logistic import logistic_model
from regressions.models.sinusoidal import sinusoidal_model
from .data.sets.linear import linear_set
from .data.sets.quadratic import quadratic_set
from .data.sets.cubic import cubic_set
from .data.sets.hyperbolic import hyperbolic_set
from .data.sets.exponential import exponential_set
from .data.sets.logarithmic import logarithmic_set
from .data.sets.logistic import logistic_set
from .data.sets.sinusoidal import sinusoidal_set
from .data.sets.bad import bad_set_string, bad_set_vector, bad_set_buried_not_list, bad_set_buried_string, bad_set_short, bad_set_zeroes

low_precision = 2
high_precision = 6

linear_model_low = linear_model(linear_set, low_precision)
linear_model_high = linear_model(linear_set, high_precision)

class TestLinearModel(unittest.TestCase):
    # LOW PRECISION
    def test_linear_model_low_constants(self):
        self.assertEqual(linear_model_low['constants'], [-3.0, 33.0])
    
    def test_linear_model_low_roots(self):
        self.assertEqual(linear_model_low['points']['roots'], [[11.0, 0.0]])
    
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
    
    # HIGH PRECISION
    def test_linear_model_high_constants(self):
        self.assertEqual(linear_model_high['constants'], [-3.0, 33.0])
    
    def test_linear_model_high_roots(self):
        self.assertEqual(linear_model_high['points']['roots'], [[11.0, 0.0]])
    
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
    
    # EDGE CASES
    def test_linear_model_zeroes(self):
        linear_model_zeroes = linear_model(bad_set_zeroes)
        self.assertEqual(linear_model_zeroes['constants'], [0.0001, 0.0001])

    def test_linear_model_string_raises(self):
        with self.assertRaises(Exception) as context:
            linear_model(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_linear_model_vector_raises(self):
        with self.assertRaises(Exception) as context:
            linear_model(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_linear_model_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            linear_model(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_linear_model_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            linear_model(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_linear_model_short_raises(self):
        with self.assertRaises(Exception) as context:
            linear_model(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

quadratic_model_low = quadratic_model(quadratic_set, low_precision)
quadratic_model_high = quadratic_model(quadratic_set, high_precision)

class TestQuadraticModel(unittest.TestCase):
    # LOW PRECISION
    def test_quadratic_model_low_constants(self):
        self.assertEqual(quadratic_model_low['constants'], [-2.0, 23.0, -11.0])
    
    def test_quadratic_model_low_roots(self):
        self.assertEqual(quadratic_model_low['points']['roots'], [[0.5, 0.0], [11.0, 0.0]])
    
    def test_quadratic_model_low_maxima(self):
        self.assertEqual(quadratic_model_low['points']['maxima'], [[5.75, 55.12]])
    
    def test_quadratic_model_low_minima(self):
        self.assertEqual(quadratic_model_low['points']['minima'], [None])
    
    def test_quadratic_model_low_inflections(self):
        self.assertEqual(quadratic_model_low['points']['inflections'], [None])
    
    def test_quadratic_model_low_accumulations_range(self):
        self.assertEqual(quadratic_model_low['accumulations']['range'], 370.17)
    
    def test_quadratic_model_low_accumulations_iqr(self):
        self.assertEqual(quadratic_model_low['accumulations']['iqr'], 252.55)
    
    def test_quadratic_model_low_averages_range_derivative_value(self):
        self.assertEqual(quadratic_model_low['averages']['range']['average_value_derivative'], 1.0)
    
    def test_quadratic_model_low_averages_range_derivative_points(self):
        self.assertEqual(quadratic_model_low['averages']['range']['mean_values_derivative'], [5.5])
    
    def test_quadratic_model_low_averages_range_integral_value(self):
        self.assertEqual(quadratic_model_low['averages']['range']['average_value_integral'], 41.13)
    
    def test_quadratic_model_low_averages_range_integral_points(self):
        self.assertEqual(quadratic_model_low['averages']['range']['mean_values_integral'], [3.1, 8.4])
    
    def test_quadratic_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(quadratic_model_low['averages']['iqr']['average_value_derivative'], 1.0)
    
    def test_quadratic_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(quadratic_model_low['averages']['iqr']['mean_values_derivative'], [5.5])
    
    def test_quadratic_model_low_averages_iqr_integral_value(self):
        self.assertEqual(quadratic_model_low['averages']['iqr']['average_value_integral'], 50.51)
    
    def test_quadratic_model_low_averages_iqr_integral_points(self):
        self.assertEqual(quadratic_model_low['averages']['iqr']['mean_values_integral'], [4.23, 7.27])
    
    def test_quadratic_model_low_correlation(self):
        self.assertEqual(quadratic_model_low['correlation'], 1.0)
    
    # HIGH PRECISION
    def test_quadratic_model_high_constants(self):
        self.assertEqual(quadratic_model_high['constants'], [-2.0, 23.0, -11.0])
    
    def test_quadratic_model_high_roots(self):
        self.assertEqual(quadratic_model_high['points']['roots'], [[0.5, 0.0], [11.0, 0.0]])
    
    def test_quadratic_model_high_maxima(self):
        self.assertEqual(quadratic_model_high['points']['maxima'], [[5.75, 55.125]])
    
    def test_quadratic_model_high_minima(self):
        self.assertEqual(quadratic_model_high['points']['minima'], [None])
    
    def test_quadratic_model_high_inflections(self):
        self.assertEqual(quadratic_model_high['points']['inflections'], [None])
    
    def test_quadratic_model_high_accumulations_range(self):
        self.assertEqual(quadratic_model_high['accumulations']['range'], 373.499667)
    
    def test_quadratic_model_high_accumulations_iqr(self):
        self.assertEqual(quadratic_model_high['accumulations']['iqr'], 254.166505)
    
    def test_quadratic_model_high_averages_range_derivative_value(self):
        self.assertEqual(quadratic_model_high['averages']['range']['average_value_derivative'], 1.0)
    
    def test_quadratic_model_high_averages_range_derivative_points(self):
        self.assertEqual(quadratic_model_high['averages']['range']['mean_values_derivative'], [5.5])
    
    def test_quadratic_model_high_averages_range_integral_value(self):
        self.assertEqual(quadratic_model_high['averages']['range']['average_value_integral'], 41.499963)
    
    def test_quadratic_model_high_averages_range_integral_points(self):
        self.assertEqual(quadratic_model_high['averages']['range']['mean_values_integral'], [3.13992, 8.36008])
    
    def test_quadratic_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(quadratic_model_high['averages']['iqr']['average_value_derivative'], 1.0)
    
    def test_quadratic_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(quadratic_model_high['averages']['iqr']['mean_values_derivative'], [5.5])
    
    def test_quadratic_model_high_averages_iqr_integral_value(self):
        self.assertEqual(quadratic_model_high['averages']['iqr']['average_value_integral'], 50.833301)
    
    def test_quadratic_model_high_averages_iqr_integral_points(self):
        self.assertEqual(quadratic_model_high['averages']['iqr']['mean_values_integral'], [4.285128, 7.214872])
    
    def test_quadratic_model_high_correlation(self):
        self.assertEqual(quadratic_model_high['correlation'], 1.0)
    
    # EDGE CASES
    def test_quadratic_model_zeroes(self):
        quadratic_model_zeroes = quadratic_model(bad_set_zeroes)
        self.assertEqual(quadratic_model_zeroes['constants'], [0.0001, 0.0001, 0.0001])

    def test_quadratic_model_string_raises(self):
        with self.assertRaises(Exception) as context:
            quadratic_model(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_quadratic_model_vector_raises(self):
        with self.assertRaises(Exception) as context:
            quadratic_model(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_quadratic_model_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            quadratic_model(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_quadratic_model_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            quadratic_model(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_quadratic_model_short_raises(self):
        with self.assertRaises(Exception) as context:
            quadratic_model(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

cubic_model_low = cubic_model(cubic_set, low_precision)
cubic_model_high = cubic_model(cubic_set, high_precision)

class TestCubicModel(unittest.TestCase):
    # LOW PRECISION
    def test_cubic_model_low_constants(self):
        self.assertEqual(cubic_model_low['constants'], [1.0, -15.0, 63.0, -7.0])
    
    def test_cubic_model_low_roots(self):
        self.assertEqual(cubic_model_low['points']['roots'], [[0.11, 0.0]])
    
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
    
    # HIGH PRECISION
    def test_cubic_model_high_constants(self):
        self.assertEqual(cubic_model_high['constants'], [1.0, -15.0, 63.0, -7.0])
    
    def test_cubic_model_high_roots(self):
        self.assertEqual(cubic_model_high['points']['roots'], [[0.114192, 0.0]])
    
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
    
    # EDGE CASES
    def test_cubic_model_zeroes(self):
        cubic_model_zeroes = cubic_model(bad_set_zeroes)
        self.assertEqual(cubic_model_zeroes['constants'], [0.0001, 0.0001, 0.0001, 0.0001])

    def test_cubic_model_string_raises(self):
        with self.assertRaises(Exception) as context:
            cubic_model(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_cubic_model_vector_raises(self):
        with self.assertRaises(Exception) as context:
            cubic_model(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_cubic_model_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            cubic_model(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_cubic_model_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            cubic_model(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_cubic_model_short_raises(self):
        with self.assertRaises(Exception) as context:
            cubic_model(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

hyperbolic_model_low = hyperbolic_model(hyperbolic_set, low_precision)
hyperbolic_model_high = hyperbolic_model(hyperbolic_set, high_precision)

class TestHyperbolicModel(unittest.TestCase):
    # LOW PRECISION
    def test_hyperbolic_model_low_constants(self):
        self.assertEqual(hyperbolic_model_low['constants'], [2520.0, -1.0])
    
    def test_hyperbolic_model_low_roots(self):
        self.assertEqual(hyperbolic_model_low['points']['roots'], [[2520.0, 0.0]])
    
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
    
    # HIGH PRECISION
    def test_hyperbolic_model_high_constants(self):
        self.assertEqual(hyperbolic_model_high['constants'], [2520.0, -1.0])
    
    def test_hyperbolic_model_high_roots(self):
        self.assertEqual(hyperbolic_model_high['points']['roots'], [[2520.0, 0.0]])
    
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
    
    # EDGE CASES
    def test_hyperbolic_model_zeroes(self):
        hyperbolic_model_zeroes = hyperbolic_model(bad_set_zeroes)
        self.assertEqual(hyperbolic_model_zeroes['constants'], [0.0001, 0.0001])

    def test_hyperbolic_model_string_raises(self):
        with self.assertRaises(Exception) as context:
            hyperbolic_model(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_hyperbolic_model_vector_raises(self):
        with self.assertRaises(Exception) as context:
            hyperbolic_model(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_hyperbolic_model_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            hyperbolic_model(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_hyperbolic_model_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            hyperbolic_model(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_hyperbolic_model_short_raises(self):
        with self.assertRaises(Exception) as context:
            hyperbolic_model(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

exponential_model_low = exponential_model(exponential_set, low_precision)
exponential_model_high = exponential_model(exponential_set, high_precision)

class TestExponentialModel(unittest.TestCase):
    # LOW PRECISION
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
        self.assertEqual(exponential_model_low['accumulations']['range'], 4237.68)
    
    def test_exponential_model_low_accumulations_iqr(self):
        self.assertEqual(exponential_model_low['accumulations']['iqr'], 1037.93)
    
    def test_exponential_model_low_averages_range_derivative_value(self):
        self.assertEqual(exponential_model_low['averages']['range']['average_value_derivative'], 323.98)
    
    def test_exponential_model_low_averages_range_derivative_points(self):
        self.assertEqual(exponential_model_low['averages']['range']['mean_values_derivative'], [7.35])
    
    def test_exponential_model_low_averages_range_integral_value(self):
        self.assertEqual(exponential_model_low['averages']['range']['average_value_integral'], 470.85)
    
    def test_exponential_model_low_averages_range_integral_points(self):
        self.assertEqual(exponential_model_low['averages']['range']['mean_values_integral'], [7.35])
    
    def test_exponential_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(exponential_model_low['averages']['iqr']['average_value_derivative'], 142.83)
    
    def test_exponential_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(exponential_model_low['averages']['iqr']['mean_values_derivative'], [6.16])
    
    def test_exponential_model_low_averages_iqr_integral_value(self):
        self.assertEqual(exponential_model_low['averages']['iqr']['average_value_integral'], 207.59)
    
    def test_exponential_model_low_averages_iqr_integral_points(self):
        self.assertEqual(exponential_model_low['averages']['iqr']['mean_values_integral'], [6.16])
    
    def test_exponential_model_low_correlation(self):
        self.assertEqual(exponential_model_low['correlation'], 1.0)
    
    # HIGH PRECISION
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
        self.assertEqual(exponential_model_high['accumulations']['range'], 4423.301848)
    
    def test_exponential_model_high_accumulations_iqr(self):
        self.assertEqual(exponential_model_high['accumulations']['iqr'], 1073.364832)
    
    def test_exponential_model_high_averages_range_derivative_value(self):
        self.assertEqual(exponential_model_high['averages']['range']['average_value_derivative'], 340.666553)
    
    def test_exponential_model_high_averages_range_derivative_points(self):
        self.assertEqual(exponential_model_high['averages']['range']['mean_values_derivative'], [7.356021])
    
    def test_exponential_model_high_averages_range_integral_value(self):
        self.assertEqual(exponential_model_high['averages']['range']['average_value_integral'], 491.477983)
    
    def test_exponential_model_high_averages_range_integral_points(self):
        self.assertEqual(exponential_model_high['averages']['range']['mean_values_integral'], [7.356021])
    
    def test_exponential_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(exponential_model_high['averages']['iqr']['average_value_derivative'], 148.79995)
    
    def test_exponential_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(exponential_model_high['averages']['iqr']['mean_values_derivative'], [6.161035])
    
    def test_exponential_model_high_averages_iqr_integral_value(self):
        self.assertEqual(exponential_model_high['averages']['iqr']['average_value_integral'], 214.672966)
    
    def test_exponential_model_high_averages_iqr_integral_points(self):
        self.assertEqual(exponential_model_high['averages']['iqr']['mean_values_integral'], [6.161035])
    
    def test_exponential_model_high_correlation(self):
        self.assertEqual(exponential_model_high['correlation'], 1.0)
    
    # EDGE CASES
    def test_exponential_model_zeroes(self):
        exponential_model_zeroes = exponential_model(bad_set_zeroes)
        self.assertEqual(exponential_model_zeroes['constants'], [1.0, 1.0])

    def test_exponential_model_string_raises(self):
        with self.assertRaises(Exception) as context:
            exponential_model(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_exponential_model_vector_raises(self):
        with self.assertRaises(Exception) as context:
            exponential_model(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_exponential_model_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            exponential_model(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_exponential_model_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            exponential_model(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_exponential_model_short_raises(self):
        with self.assertRaises(Exception) as context:
            exponential_model(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

logarithmic_model_low = logarithmic_model(logarithmic_set, low_precision)
logarithmic_model_high = logarithmic_model(logarithmic_set, high_precision)

class TestLogarithmicModel(unittest.TestCase):
    # LOW PRECISION
    def test_logarithmic_model_low_constants(self):
        self.assertEqual(logarithmic_model_low['constants'], [3.0, 2.0])
    
    def test_logarithmic_model_low_roots(self):
        self.assertEqual(logarithmic_model_low['points']['roots'], [[0.51, 0.0]])
    
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
    
    # HIGH PRECISION
    def test_logarithmic_model_high_constants(self):
        self.assertEqual(logarithmic_model_high['constants'], [3.000016, 1.999972])
    
    def test_logarithmic_model_high_roots(self):
        self.assertEqual(logarithmic_model_high['points']['roots'], [[0.513424, 0.0]])
    
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
    
    # EDGE CASES
    def test_logarithmic_model_zeroes(self):
        logarithmic_model_zeroes = logarithmic_model(bad_set_zeroes)
        self.assertEqual(logarithmic_model_zeroes['constants'], [0.0001, 0.0001])

    def test_linear_model_string_raises(self):
        with self.assertRaises(Exception) as context:
            linear_model(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_logarithmic_model_vector_raises(self):
        with self.assertRaises(Exception) as context:
            logarithmic_model(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_logarithmic_model_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            logarithmic_model(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_logarithmic_model_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            logarithmic_model(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_logarithmic_model_short_raises(self):
        with self.assertRaises(Exception) as context:
            logarithmic_model(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

logistic_model_low = logistic_model(logistic_set, low_precision)
logistic_model_high = logistic_model(logistic_set, high_precision)

class TestLogisticModel(unittest.TestCase):
    # LOW PRECISION
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
        self.assertEqual(logistic_model_low['accumulations']['range'], 10.04)
    
    def test_logistic_model_low_accumulations_iqr(self):
        self.assertEqual(logistic_model_low['accumulations']['iqr'], 6.02)
    
    def test_logistic_model_low_averages_range_derivative_value(self):
        self.assertEqual(logistic_model_low['averages']['range']['average_value_derivative'], 0.22)
    
    def test_logistic_model_low_averages_range_derivative_points(self):
        self.assertEqual(logistic_model_low['averages']['range']['mean_values_derivative'], [3.92, 6.07])
    
    def test_logistic_model_low_averages_range_integral_value(self):
        self.assertEqual(logistic_model_low['averages']['range']['average_value_integral'], 1.12)
    
    def test_logistic_model_low_averages_range_integral_points(self):
        self.assertEqual(logistic_model_low['averages']['range']['mean_values_integral'], [5.08])
    
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
    
    # HIGH PRECISION
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
        self.assertEqual(logistic_model_high['accumulations']['range'], 9.999995)
    
    def test_logistic_model_high_accumulations_iqr(self):
        self.assertEqual(logistic_model_high['accumulations']['iqr'], 5.998431)
    
    def test_logistic_model_high_averages_range_derivative_value(self):
        self.assertEqual(logistic_model_high['averages']['range']['average_value_derivative'], 0.222221)
    
    def test_logistic_model_high_averages_range_derivative_points(self):
        self.assertEqual(logistic_model_high['averages']['range']['mean_values_derivative'], [3.927574, 6.072426])
    
    def test_logistic_model_high_averages_range_integral_value(self):
        self.assertEqual(logistic_model_high['averages']['range']['average_value_integral'], 1.111111)
    
    def test_logistic_model_high_averages_range_integral_points(self):
        self.assertEqual(logistic_model_high['averages']['range']['mean_values_integral'], [5.074381])
    
    def test_logistic_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(logistic_model_high['averages']['iqr']['average_value_derivative'], 0.398962)
    
    def test_logistic_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(logistic_model_high['averages']['iqr']['mean_values_derivative'], [4.145996, 5.854006])
    
    def test_logistic_model_high_averages_iqr_integral_value(self):
        self.assertEqual(logistic_model_high['averages']['iqr']['average_value_integral'], 1.199686)
    
    def test_logistic_model_high_averages_iqr_integral_points(self):
        self.assertEqual(logistic_model_high['averages']['iqr']['mean_values_integral'], [5.134937])
    
    def test_logistic_model_high_correlation(self):
        self.assertEqual(logistic_model_high['correlation'], 1.0)

    # EDGE CASES
    def test_logistic_model_zeroes(self):
        logistic_model_zeroes = logistic_model(bad_set_zeroes)
        self.assertEqual(logistic_model_zeroes['constants'], [0.0001, 1.0, 0.0001])

    def test_logistic_model_string_raises(self):
        with self.assertRaises(Exception) as context:
            logistic_model(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_logistic_model_vector_raises(self):
        with self.assertRaises(Exception) as context:
            logistic_model(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_logistic_model_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            logistic_model(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_logistic_model_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            logistic_model(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_logistic_model_short_raises(self):
        with self.assertRaises(Exception) as context:
            logistic_model(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

sinusoidal_model_low = sinusoidal_model(sinusoidal_set, low_precision)
sinusoidal_model_high = sinusoidal_model(sinusoidal_set, high_precision)

class TestSinusoidalModel(unittest.TestCase):
    # LOW PRECISION
    def test_sinusoidal_model_low_constants(self):
        self.assertEqual(sinusoidal_model_low['constants'], [-5.0, 1.57, 3.0, 3.0])
    
    def test_sinusoidal_model_low_roots(self):
        self.assertEqual(sinusoidal_model_low['points']['roots'], [[3.41, 0.0], [4.59, 0.0], [7.41, 0.0], [8.59, 0.0], ['3.41 + 4.0k', 0.0], ['4.59 + 4.0k', 0.0]])
    
    def test_sinusoidal_model_low_maxima(self):
        self.assertEqual(sinusoidal_model_low['points']['maxima'], [[6.0, 8.0], [10.0, 8.0], ['6.0 + 4.0k', 8.0]])
    
    def test_sinusoidal_model_low_minima(self):
        self.assertEqual(sinusoidal_model_low['points']['minima'], [[4.0, -2.0], [8.0, -2.0], ['4.0 + 4.0k', -2.0]])
    
    def test_sinusoidal_model_low_inflections(self):
        self.assertEqual(sinusoidal_model_low['points']['inflections'], [[3.0, 3.0], [5.0, 3.0], [7.0, 3.0], [9.0, 3.0], ['3.0 + 2.0k', 3.0]])
    
    def test_sinusoidal_model_low_accumulations_range(self):
        self.assertEqual(sinusoidal_model_low['accumulations']['range'], 30.16)
    
    def test_sinusoidal_model_low_accumulations_iqr(self):
        self.assertEqual(sinusoidal_model_low['accumulations']['iqr'], 11.83)
    
    def test_sinusoidal_model_low_averages_range_derivative_value(self):
        self.assertEqual(sinusoidal_model_low['averages']['range']['average_value_derivative'], 0.55)
    
    def test_sinusoidal_model_low_averages_range_derivative_points(self):
        self.assertEqual(sinusoidal_model_low['averages']['range']['mean_values_derivative'], [4.05, 5.96, 8.05, 9.96, '4.05 + 4.0k', '5.96 + 4.0k'])
    
    def test_sinusoidal_model_low_averages_range_integral_value(self):
        self.assertEqual(sinusoidal_model_low['averages']['range']['average_value_integral'], 3.35)
    
    def test_sinusoidal_model_low_averages_range_integral_points(self):
        self.assertEqual(sinusoidal_model_low['averages']['range']['mean_values_integral'], [2.96, 5.05, 6.96, 9.05, '2.96 + 4.0k', '5.05 + 4.0k'])
    
    def test_sinusoidal_model_low_averages_iqr_derivative_value(self):
        self.assertEqual(sinusoidal_model_low['averages']['iqr']['average_value_derivative'], -1.0)
    
    def test_sinusoidal_model_low_averages_iqr_derivative_points(self):
        self.assertEqual(sinusoidal_model_low['averages']['iqr']['mean_values_derivative'], [3.92, 6.08, 7.92, '3.92 + 4.0k', '6.08 + 4.0k'])
    
    def test_sinusoidal_model_low_averages_iqr_integral_value(self):
        self.assertEqual(sinusoidal_model_low['averages']['iqr']['average_value_integral'], 2.37)
    
    def test_sinusoidal_model_low_averages_iqr_integral_points(self):
        self.assertEqual(sinusoidal_model_low['averages']['iqr']['mean_values_integral'], [3.08, 4.92, 7.08, '3.08 + 4.0k', '4.92 + 4.0k'])
    
    def test_sinusoidal_model_low_correlation(self):
        self.assertEqual(sinusoidal_model_low['correlation'], 1.0)
    
    # HIGH PRECISION
    def test_sinusoidal_model_high_constants(self):
        self.assertEqual(sinusoidal_model_high['constants'], [-5.0, 1.570796, 3.0, 3.0])
    
    def test_sinusoidal_model_high_roots(self):
        self.assertEqual(sinusoidal_model_high['points']['roots'], [[3.409666, 0.0], [4.590335, 0.0], [7.409667, 0.0], [8.590336, 0.0], ['3.409666 + 4.000001k', 0.0], ['4.590335 + 4.000001k', 0.0]])
    
    def test_sinusoidal_model_high_maxima(self):
        self.assertEqual(sinusoidal_model_high['points']['maxima'], [[5.999993, 8.0], [9.999983, 8.0], ['5.999993 + 3.99999k', 8.0]])
    
    def test_sinusoidal_model_high_minima(self):
        self.assertEqual(sinusoidal_model_high['points']['minima'], [[3.999998, -2.0], [7.999988, -2.0], ['3.999998 + 3.99999k', -2.0]])
    
    def test_sinusoidal_model_high_inflections(self):
        self.assertEqual(sinusoidal_model_high['points']['inflections'], [[3.0, 3.0], [4.999995, 3.0], [6.99999, 3.0], [8.999985, 3.0], ['3.0 + 1.999995k', 3.0]])
    
    def test_sinusoidal_model_high_accumulations_range(self):
        self.assertEqual(sinusoidal_model_high['accumulations']['range'], 30.183093)
    
    def test_sinusoidal_model_high_accumulations_iqr(self):
        self.assertEqual(sinusoidal_model_high['accumulations']['iqr'], 11.816905)
    
    def test_sinusoidal_model_high_averages_range_derivative_value(self):
        self.assertEqual(sinusoidal_model_high['averages']['range']['average_value_derivative'], 0.555555)
    
    def test_sinusoidal_model_high_averages_range_derivative_points(self):
        self.assertEqual(sinusoidal_model_high['averages']['range']['mean_values_derivative'], [4.045069, 5.954931, 8.04507, 9.954932, '4.045069 + 4.000001k', '5.954931 + 4.000001k'])
    
    def test_sinusoidal_model_high_averages_range_integral_value(self):
        self.assertEqual(sinusoidal_model_high['averages']['range']['average_value_integral'], 3.353677)
    
    def test_sinusoidal_model_high_averages_range_integral_points(self):
        self.assertEqual(sinusoidal_model_high['averages']['range']['mean_values_integral'], [2.954931, 5.04507, 6.954932, 9.045071, '2.954931 + 4.000001k', '5.04507 + 4.000001k'])
    
    def test_sinusoidal_model_high_averages_iqr_derivative_value(self):
        self.assertEqual(sinusoidal_model_high['averages']['iqr']['average_value_derivative'], -1.0)
    
    def test_sinusoidal_model_high_averages_iqr_derivative_points(self):
        self.assertEqual(sinusoidal_model_high['averages']['iqr']['mean_values_derivative'], [3.918723, 6.081278, 7.918724, '3.918723 + 4.000001k', '6.081278 + 4.000001k'])
    
    def test_sinusoidal_model_high_averages_iqr_integral_value(self):
        self.assertEqual(sinusoidal_model_high['averages']['iqr']['average_value_integral'], 2.363381)
    
    def test_sinusoidal_model_high_averages_iqr_integral_points(self):
        self.assertEqual(sinusoidal_model_high['averages']['iqr']['mean_values_integral'], [3.081277, 4.918723, 7.081278, '3.081277 + 4.000001k', '4.918723 + 4.000001k'])
    
    def test_sinusoidal_model_high_correlation(self):
        self.assertEqual(sinusoidal_model_high['correlation'], 1.0)
    
    # EDGE CASES
    def test_sinusoidal_model_zeroes(self):
        sinusoidal_model_zeroes = sinusoidal_model(bad_set_zeroes)
        self.assertEqual(sinusoidal_model_zeroes['constants'], [0.0001, 1.0, 0.0001, 0.0001])

    def test_sinusoidal_model_string_raises(self):
        with self.assertRaises(Exception) as context:
            sinusoidal_model(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_sinusoidal_model_vector_raises(self):
        with self.assertRaises(Exception) as context:
            sinusoidal_model(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_sinusoidal_model_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            sinusoidal_model(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_sinusoidal_model_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            sinusoidal_model(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_sinusoidal_model_short_raises(self):
        with self.assertRaises(Exception) as context:
            sinusoidal_model(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

if __name__ == '__main__':
    unittest.main()

# ----- Ran 304 tests in 0.108s ----- OK ----- #