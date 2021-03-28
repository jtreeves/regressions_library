import unittest

from library.errors.scalars import scalar_value, two_scalars, three_scalars, four_scalars, compare_scalars, positive_integer, whole_number, select_integers, allow_none_scalar
from library.errors.vectors import vector_of_scalars, compare_vectors, multitype_vector, allow_none_vector, length
from library.errors.matrices import matrix_of_scalars, square_matrix, compare_rows, compare_columns, compare_matrices, columns_rows, level
from library.errors.analyses import callable_function, select_equations

good_positive = 3
good_whole = 0
good_integer = -3
good_float = 3.14
bad_scalar = 'three'
none_scalar = None
choices = [4, 5, 6]

class TestScalarValue(unittest.TestCase):
    def test_scalar_integer(self):
        scalar_integer = scalar_value(good_integer, 'only')
        self.assertEqual(scalar_integer, 'Argument is an integer or a float')
    
    def test_scalar_float(self):
        scalar_float = scalar_value(good_float, 'only')
        self.assertEqual(scalar_float, 'Argument is an integer or a float')
    
    def test_scalar_position(self):
        scalar_position = scalar_value(good_float, 'second')
        self.assertEqual(scalar_position, 'Second argument is an integer or a float')
    
    def test_scalar_string_raises(self):
        with self.assertRaises(Exception) as context:
            scalar_value(bad_scalar, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be an integer or a float')
    
    def test_scalar_none_raises(self):
        with self.assertRaises(Exception) as context:
            scalar_value(none_scalar, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be an integer or a float')
    
    def test_scalar_array_raises(self):
        with self.assertRaises(Exception) as context:
            scalar_value(choices, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be an integer or a float')

class TestWholeNumber(unittest.TestCase):
    def test_whole_zero(self):
        whole_zero = whole_number(good_whole, 'second')
        self.assertEqual(whole_zero, 'Second argument is a whole number')
    
    def test_whole_natural(self):
        whole_natural = whole_number(good_positive, 'third')
        self.assertEqual(whole_natural, 'Third argument is a whole number')
    
    def test_whole_negative_raises(self):
        with self.assertRaises(Exception) as context:
            whole_number(good_integer, 'second')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Second argument must be a whole number')
    
    def test_whole_float_raises(self):
        with self.assertRaises(Exception) as context:
            whole_number(good_float, 'second')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Second argument must be a whole number')
    
    def test_whole_string_raises(self):
        with self.assertRaises(Exception) as context:
            whole_number(bad_scalar, 'second')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Second argument must be a whole number')
    
    def test_whole_none_raises(self):
        with self.assertRaises(Exception) as context:
            whole_number(none_scalar, 'second')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Second argument must be a whole number')
    
    def test_whole_array_raises(self):
        with self.assertRaises(Exception) as context:
            whole_number(choices, 'second')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Second argument must be a whole number')

class TestPositiveInteger(unittest.TestCase):
    def test_positive_natural(self):
        positive_natural = positive_integer(good_positive)
        self.assertEqual(positive_natural, 'Last argument is a positive integer')
    
    def test_positive_whole_raises(self):
        with self.assertRaises(Exception) as context:
            positive_integer(good_whole)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Last argument must be a positive integer')
    
    def test_positive_negative_raises(self):
        with self.assertRaises(Exception) as context:
            positive_integer(good_integer)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Last argument must be a positive integer')
    
    def test_positive_float_raises(self):
        with self.assertRaises(Exception) as context:
            positive_integer(good_float)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Last argument must be a positive integer')
    
    def test_positive_string_raises(self):
        with self.assertRaises(Exception) as context:
            positive_integer(bad_scalar)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Last argument must be a positive integer')
    
    def test_positive_none_raises(self):
        with self.assertRaises(Exception) as context:
            positive_integer(none_scalar)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Last argument must be a positive integer')
    
    def test_positive_array_raises(self):
        with self.assertRaises(Exception) as context:
            positive_integer(choices)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Last argument must be a positive integer')

class TestAllowNoneScalar(unittest.TestCase):
    def test_none_scalar_none(self):
        none_scalar_none = allow_none_scalar(none_scalar)
        self.assertEqual(none_scalar_none, 'First argument is an integer, a float, or None')
    
    def test_none_scalar_integer(self):
        none_scalar_integer = allow_none_scalar(good_integer)
        self.assertEqual(none_scalar_integer, 'First argument is an integer, a float, or None')
    
    def test_none_scalar_float(self):
        none_scalar_float = allow_none_scalar(good_float)
        self.assertEqual(none_scalar_float, 'First argument is an integer, a float, or None')
    
    def test_none_scalar_string_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_scalar(bad_scalar)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be an integer, a float, or None')
    
    def test_none_sclar_array_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_scalar(choices)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be an integer, a float, or None')

class TestCompareScalars(unittest.TestCase):
    def test_compare_scalars_less(self):
        compare_scalars_less = compare_scalars(good_integer, good_float, 'second', 'third')
        self.assertEqual(compare_scalars_less, 'Second argument is less than third argument')
    
    def test_compare_scalars_more_raises(self):
        with self.assertRaises(Exception) as context:
            compare_scalars(good_float, good_integer, 'second', 'third')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Second argument must be less than third argument')

class TestSelectIntegers(unittest.TestCase):
    def test_select_integers_included(self):
        select_integers_included = select_integers(5, choices)
        self.assertEqual(select_integers_included, 'Second argument is one of the following integers: [4, 5, 6]')
    
    def test_select_integers_excluded_raises(self):
        with self.assertRaises(Exception) as context:
            select_integers(1, choices)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Second argument must be one of the following integers: [4, 5, 6]')

class TestTwoScalars(unittest.TestCase):
    def test_two_scalars_integer_float(self):
        two_scalars_integer_float = two_scalars(good_integer, good_float)
        self.assertEqual(two_scalars_integer_float, 'Both first and second arguments are integers or floats')
    
    def test_two_scalars_string_integer_raises(self):
        with self.assertRaises(Exception) as context:
            two_scalars(bad_scalar, good_integer)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be an integer or a float')
    
    def test_two_scalars_integer_string_raises(self):
        with self.assertRaises(Exception) as context:
            two_scalars(good_integer, bad_scalar)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Second argument must be an integer or a float')

class TestThreeScalars(unittest.TestCase):
    def test_three_scalars_integer_float_whole(self):
        three_scalars_integer_float_whole = three_scalars(good_integer, good_float, good_whole)
        self.assertEqual(three_scalars_integer_float_whole, 'First, second, and third arguments are all integers or floats')
    
    def test_three_scalars_integer_float_string_raises(self):
        with self.assertRaises(Exception) as context:
            three_scalars(good_integer, good_float, bad_scalar)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Third argument must be an integer or a float')

class TestFourScalars(unittest.TestCase):
    def test_four_scalars_integer_float_whole_positive(self):
        four_scalars_integer_float_whole_positive = four_scalars(good_integer, good_float, good_whole, good_positive)
        self.assertEqual(four_scalars_integer_float_whole_positive, 'First, second, third, and fourth arguments are all integers or floats')
    
    def test_four_scalars_integer_float_whole_string_raises(self):
        with self.assertRaises(Exception) as context:
            four_scalars(good_integer, good_float, good_whole, bad_scalar)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Fourth argument must be an integer or a float')

first_vector = [2, 3, 5]
second_vector = [7, 11, 13]
long_vector = [1, 2, 3, 4]
none_vector = [None]
good_multitype = ['positive', 1, 'negative']
bad_multitype = ['positive', 'negative', 1]
bad_vector_string = 'vector'
bad_vector_nested =[[2], 3, 5]

first_matrix = [[1, 2, 3], [4, 5, 6]]
second_matrix = [[7, 8, 9], [10, 11, 12]]
small_square = [[1, 2], [3, 4]]
large_square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
bad_matrix_string = 'matrix'
bad_matrix_vector = [1, 2, 3]
bad_matrix_nested = [[[1], 2, 3], [4, 5, 6]]

def good_function(x):
    return 2 * x

bad_function = 'function'

good_equation = 'hyperbolic'
bad_equation = 'rational'

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 36 tests in 0.003s ---------- OK ---------- #