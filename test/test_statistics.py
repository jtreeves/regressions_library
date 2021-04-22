import unittest

from regressions.statistics.rounding import rounded_value, rounded_list
from regressions.statistics.summation import sum_value
from regressions.statistics.sort import sorted_list, sorted_dimension, sorted_strings
from regressions.statistics.halve import half, half_dimension
from regressions.statistics.minimum import minimum_value
from regressions.statistics.maximum import maximum_value
from regressions.statistics.quartiles import quartile_value
from regressions.statistics.median import median_value
from regressions.statistics.mean import mean_value
from regressions.statistics.summary import five_number_summary
from regressions.statistics.ranges import range_value, shift_into_range
from regressions.statistics.deviations import multiple_deviations
from regressions.statistics.residuals import multiple_residuals
from regressions.statistics.correlation import correlation_coefficient

even_set = [8, 2, 5, 9, 1, 3, 22, 11, 9, 13]
odd_set = [7, 4, 6, 8, 2, 5, 25, 14, 8]
compare_set = [5, 5, 5, 10, 1, 7, 22, 13, 8]
counting_set = [1, 2, 3, 4, 5]
identical_set = [1, 1, 1, 1, 1]
approximate_set = [1.0001, 1.0001, 1.0001, 1.0001, 1.0001]
extreme_set = [1, 13, 59, 134, 2892]
dimension_set = [[2, 7], [1, 9], [5, 2], [3, 4], [4, 3], [8, 1], [2, 3], [7, 7], [1, 1], [5, 3]]
strings_ordered = ['2 + 3k', '4 + 3k']
strings_unordered = ['4 + 3k', '2 + 3k']

normal_decimal = 6.817239833721
extreme_decimal = 0.000000000000000000005782016894

low_precision = 2
high_precision = 8

class TestRounding(unittest.TestCase):
    def test_round_missing(self):
        round_missing = rounded_value(normal_decimal)
        self.assertEqual(round_missing, 6.8172)
    
    def test_round_normal_low(self):
        round_normal_low = rounded_value(normal_decimal, low_precision)
        self.assertEqual(round_normal_low, 6.82)

    def test_round_normal_high(self):
        round_normal_high = rounded_value(normal_decimal, high_precision)
        self.assertEqual(round_normal_high, 6.81723983)
    
    def test_round_extreme_low(self):
        round_extreme_low = rounded_value(extreme_decimal, low_precision)
        self.assertEqual(round_extreme_low, 0.01)
    
    def test_round_extreme_high(self):
        round_extreme_high = rounded_value(extreme_decimal, high_precision) 
        self.assertEqual(round_extreme_high, 1e-08)
    
    def test_rounded_list(self):
        rounded_list_main = rounded_list([3.12718492, 2.17729, 54.21, 8.9999222222, 3.9274826, 115.28191], 6)
        self.assertEqual(rounded_list_main, [3.127185, 2.17729, 54.21, 8.999922, 3.927483, 115.28191])

class TestSummation(unittest.TestCase):
    def test_sum_even(self):
        sum_even = sum_value(even_set)
        self.assertEqual(sum_even, 83)

    def test_sum_odd(self):
        sum_odd = sum_value(odd_set)
        self.assertEqual(sum_odd, 79)

class TestSort(unittest.TestCase):
    def test_sort_even(self):
        sort_even = sorted_list(even_set)
        self.assertEqual(sort_even, [1, 2, 3, 5, 8, 9, 9, 11, 13, 22])

    def test_sort_odd(self):
        sort_odd = sorted_list(odd_set)
        self.assertEqual(sort_odd, [2, 4, 5, 6, 7, 8, 8, 14, 25])
    
    def test_sort_dimension(self):
        dimension_sort = sorted_dimension(dimension_set, 1)
        self.assertEqual(dimension_sort, [[1, 9], [1, 1], [2, 7], [2, 3], [3, 4], [4, 3], [5, 2], [5, 3], [7, 7], [8, 1]])
    
    def test_sort_strings_ordered(self):
        sort_strings_ordered = sorted_strings(strings_ordered)
        self.assertEqual(sort_strings_ordered, strings_ordered)
    
    def test_sort_strings_unordered(self):
        sort_strings_unordered = sorted_strings(strings_unordered)
        self.assertEqual(sort_strings_unordered, strings_ordered)

class TestHalve(unittest.TestCase):
    def test_halve_even(self):
        halve_even = half(even_set)
        self.assertEqual(halve_even, {'upper': [9, 9, 11, 13, 22], 'lower': [1, 2, 3, 5, 8]})

    def test_halve_odd(self):
        halve_odd = half(odd_set)
        self.assertEqual(halve_odd, {'upper': [8, 8, 14, 25], 'lower': [2, 4, 5, 6]})
    
    def test_halve_dimension(self):
        dimension_halve = half_dimension(dimension_set, 1)
        self.assertEqual(dimension_halve, {'upper': [[4, 3], [5, 2], [5, 3], [7, 7], [8, 1]], 'lower': [[1, 9], [1, 1], [2, 7], [2, 3], [3, 4]]})

class TestMinimum(unittest.TestCase):
    def test_min_even(self):
        min_even = minimum_value(even_set)
        self.assertEqual(min_even, 1)

    def test_min_odd(self):
        min_odd = minimum_value(odd_set)
        self.assertEqual(min_odd, 2)

class TestMaximum(unittest.TestCase):
    def test_max_even(self):
        max_even = maximum_value(even_set)
        self.assertEqual(max_even, 22)

    def test_max_odd(self):
        max_odd = maximum_value(odd_set)
        self.assertEqual(max_odd, 25)

class TestQuartiles(unittest.TestCase):
    def test_q1_even(self):
        q1_even = quartile_value(even_set, 1)
        self.assertEqual(q1_even, 3)
    
    def test_q1_odd(self):
        q1_odd = quartile_value(odd_set, 1)
        self.assertEqual(q1_odd, 4.5)
    
    def test_q3_even(self):
        q3_even = quartile_value(even_set, 3)
        self.assertEqual(q3_even, 11)
    
    def test_q3_odd(self):
        q3_odd = quartile_value(odd_set, 3)
        self.assertEqual(q3_odd, 11)

class TestMedian(unittest.TestCase):
    def test_median_even(self):
        median_even = median_value(even_set)
        self.assertEqual(median_even, 8.5)
    
    def test_median_odd(self):
        median_odd = median_value(odd_set)
        self.assertEqual(median_odd, 7)

class TestMean(unittest.TestCase):
    def test_mean_even(self):
        mean_even = mean_value(even_set)
        self.assertEqual(mean_even, 8.3)
    
    def test_mean_odd(self):
        mean_odd = mean_value(odd_set)
        self.assertEqual(mean_odd, 8.777777777777779)

class TestFiveNumberSummary(unittest.TestCase):
    def test_five_even(self):
        five_even = five_number_summary(even_set)
        self.assertEqual(five_even, {'minimum': 1, 'q1': 3, 'median': 8.5, 'q3': 11, 'maximum': 22})
    
    def test_five_odd(self):
        five_odd = five_number_summary(odd_set)
        self.assertEqual(five_odd, {'minimum': 2, 'q1': 4.5, 'median': 7, 'q3': 11.0, 'maximum': 25})

class TestRange(unittest.TestCase):
    def test_range_even(self):
        range_even = range_value(even_set)
        self.assertEqual(range_even, 21)
    
    def test_range_odd(self):
        range_odd = range_value(odd_set)
        self.assertEqual(range_odd, 23)

class TestShiftIntoRange(unittest.TestCase):
    def test_shift_range_within_positive(self):
        shift_range_within_positive = shift_into_range(11, 2, 10, 20)
        self.assertEqual(shift_range_within_positive, 11)
    
    def test_shift_range_at_min_positive(self):
        shift_range_at_min_positive = shift_into_range(10, 2, 10, 20)
        self.assertEqual(shift_range_at_min_positive, 10)
    
    def test_shift_range_at_max_positive(self):
        shift_range_at_max_positive = shift_into_range(20, 2, 10, 20)
        self.assertEqual(shift_range_at_max_positive, 20)
    
    def test_shift_range_below_positive(self):
        shift_range_below_positive = shift_into_range(1, 2, 10, 20)
        self.assertEqual(shift_range_below_positive, 11)
    
    def test_shift_range_above_positive(self):
        shift_range_above_positive = shift_into_range(31, 2, 10, 20)
        self.assertEqual(shift_range_above_positive, 19)
    
    def test_shift_range_unfit_above_positive(self):
        shift_range_unfit_above_positive = shift_into_range(31, 30, 10, 20)
        self.assertEqual(shift_range_unfit_above_positive, 31)
    
    def test_shift_range_unfit_below_positive(self):
        shift_range_unfit_below_positive = shift_into_range(1, 30, 10, 20)
        self.assertEqual(shift_range_unfit_below_positive, 31)
    
    def test_shift_range_within_negative(self):
        shift_range_within_negative = shift_into_range(11, -2, 10, 20)
        self.assertEqual(shift_range_within_negative, 11)
    
    def test_shift_range_at_min_negative(self):
        shift_range_at_min_negative = shift_into_range(10, -2, 10, 20)
        self.assertEqual(shift_range_at_min_negative, 10)
    
    def test_shift_range_at_max_negative(self):
        shift_range_at_max_negative = shift_into_range(20, -2, 10, 20)
        self.assertEqual(shift_range_at_max_negative, 20)
    
    def test_shift_range_below_negative(self):
        shift_range_below_negative = shift_into_range(1, -2, 10, 20)
        self.assertEqual(shift_range_below_negative, 11)
    
    def test_shift_range_above_negative(self):
        shift_range_above_negative = shift_into_range(31, -2, 10, 20)
        self.assertEqual(shift_range_above_negative, 19)
    
    def test_shift_range_unfit_above_negative(self):
        shift_range_unfit_above_negative = shift_into_range(31, -30, 10, 20)
        self.assertEqual(shift_range_unfit_above_negative, 31)
    
    def test_shift_range_unfit_below_negative(self):
        shift_range_unfit_below_negative = shift_into_range(1, -30, 10, 20)
        self.assertEqual(shift_range_unfit_below_negative, 31)

class TestDeviations(unittest.TestCase):
    def test_deviations_even(self):
        deviations_even = multiple_deviations(even_set)
        self.assertEqual(deviations_even, [-0.3000000000000007, -6.300000000000001, -3.3000000000000007, 0.6999999999999993, -7.300000000000001, -5.300000000000001, 13.7, 2.6999999999999993, 0.6999999999999993, 4.699999999999999])
    
    def test_deviations_odd(self):
        deviations_odd = multiple_deviations(odd_set)
        self.assertEqual(deviations_odd, [-1.7777777777777786, -4.777777777777779, -2.7777777777777786, -0.7777777777777786, -6.777777777777779, -3.7777777777777786, 16.22222222222222, 5.222222222222221, -0.7777777777777786])
    
    def test_deviations_extreme(self):
        deviations_extreme = multiple_deviations(extreme_set)
        self.assertEqual(deviations_extreme, [-618.8, -606.8, -560.8, -485.79999999999995, 2272.2])

class TestResiduals(unittest.TestCase):
    def test_residuals_compare(self):
        residuals_compare = multiple_residuals(odd_set, compare_set)
        self.assertEqual(residuals_compare, [2, -1, 1, -2, 1, -2, 3, 1, 0])
    
    def test_residuals_extreme(self):
        residuals_extreme = multiple_residuals(extreme_set, counting_set)
        self.assertEqual(residuals_extreme, [0.0, 11.0, 56.0, 130.0, 2887.0])

class TestCorrelation(unittest.TestCase):    
    def test_correlation_compare(self):
        correlation_compare = correlation_coefficient(odd_set, compare_set)
        self.assertEqual(correlation_compare, 0.967)
    
    def test_correlation_deviation_zero(self):
        correlation_deviation_zero = correlation_coefficient(identical_set, approximate_set)
        self.assertEqual(correlation_deviation_zero, 0.9997)
    
    def test_correlation_ratio_over(self):
        correlation_ratio_over = correlation_coefficient(extreme_set, identical_set)
        self.assertEqual(correlation_ratio_over, 0.0)

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 54 tests in 0.005s ---------- OK ---------- #