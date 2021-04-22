import unittest

from regressions.errors.positions import argument_position
from regressions.errors.adjustments import no_zeroes
from regressions.errors.scalars import scalar_value, two_scalars, three_scalars, four_scalars, five_scalars, compare_scalars, positive_integer, whole_number, select_integers, allow_none_scalar
from regressions.errors.vectors import confirm_vector, vector_of_scalars, vector_of_strings, compare_vectors, allow_none_vector, length, long_vector
from regressions.errors.matrices import confirm_matrix, matrix_of_scalars, square_matrix, compare_rows, compare_columns, compare_matrices, columns_rows, allow_none_matrix, allow_vector_matrix, level
from regressions.errors.analyses import select_equations, select_points

class TestPosition(unittest.TestCase):
    def test_position_none(self):
        position_none = argument_position()
        self.assertEqual(position_none, 'argument')
    
    def test_position_only(self):
        position_only = argument_position('only')
        self.assertEqual(position_only, 'argument')
    
    def test_position_first(self):
        position_first = argument_position('first')
        self.assertEqual(position_first, 'first argument')
    
    def test_position_second(self):
        position_second = argument_position('second')
        self.assertEqual(position_second, 'second argument')

no_zeroes_list = [1, 2, 3]
all_zeroes_list = [0, 0, 0]
first_zero_list = [0, 1, 2]
last_zero_list = [1, 2, 0]

class TestNoZeroes(unittest.TestCase):
    def test_no_zeroes_no0(self):
        no_zeroes_no0 = no_zeroes(no_zeroes_list)
        self.assertEqual(no_zeroes_no0, [1.0, 2.0, 3.0])
    
    def test_no_zeroes_all0(self):
        no_zeroes_all0 = no_zeroes(all_zeroes_list)
        self.assertEqual(no_zeroes_all0, [0.0001, 0.0001, 0.0001])
    
    def test_no_zeroes_first0(self):
        no_zeroes_first0 = no_zeroes(first_zero_list)
        self.assertEqual(no_zeroes_first0, [0.0001, 1.0, 2.0])
    
    def test_no_zeroes_last0(self):
        no_zeroes_last0 = no_zeroes(last_zero_list)
        self.assertEqual(no_zeroes_last0, [1.0, 2.0, 0.0001])
    
    def test_no_zeroes_all0_precision(self):
        no_zeroes_all0 = no_zeroes(all_zeroes_list, 6)
        self.assertEqual(no_zeroes_all0, [0.000001, 0.000001, 0.000001])

good_positive = 3
good_whole = 0
good_integer = -3
good_float = 3.14
bad_scalar = 'three'
none_scalar = None
choices = [4, 5, 6]

class TestScalarValue(unittest.TestCase):
    def test_scalar_integer(self):
        scalar_integer = scalar_value(good_integer)
        self.assertEqual(scalar_integer, 'Argument is an integer or a float')
    
    def test_scalar_float(self):
        scalar_float = scalar_value(good_float)
        self.assertEqual(scalar_float, 'Argument is an integer or a float')
    
    def test_scalar_position(self):
        scalar_position = scalar_value(good_float, 'second')
        self.assertEqual(scalar_position, 'Second argument is an integer or a float')
    
    def test_scalar_string_raises(self):
        with self.assertRaises(Exception) as context:
            scalar_value(bad_scalar)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be an integer or a float')
    
    def test_scalar_none_raises(self):
        with self.assertRaises(Exception) as context:
            scalar_value(none_scalar)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be an integer or a float')
    
    def test_scalar_array_raises(self):
        with self.assertRaises(Exception) as context:
            scalar_value(choices)
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
        self.assertEqual(none_scalar_none, 'Argument is an integer, a float, or None')
    
    def test_none_scalar_integer(self):
        none_scalar_integer = allow_none_scalar(good_integer)
        self.assertEqual(none_scalar_integer, 'Argument is an integer, a float, or None')
    
    def test_none_scalar_float(self):
        none_scalar_float = allow_none_scalar(good_float)
        self.assertEqual(none_scalar_float, 'Argument is an integer, a float, or None')
    
    def test_none_scalar_string_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_scalar(bad_scalar)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be an integer, a float, or None')
    
    def test_none_scalar_array_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_scalar(choices)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be an integer, a float, or None')

class TestCompareScalars(unittest.TestCase):
    def test_compare_scalars_less(self):
        compare_scalars_less = compare_scalars(good_integer, good_float, 'second', 'third')
        self.assertEqual(compare_scalars_less, 'Second argument is less than or equal to third argument')
    
    def test_compare_scalars_equal(self):
        compare_scalars_equal = compare_scalars(good_integer, good_integer, 'second', 'third')
        self.assertEqual(compare_scalars_equal, 'Second argument is less than or equal to third argument')
    
    def test_compare_scalars_more_raises(self):
        with self.assertRaises(Exception) as context:
            compare_scalars(good_float, good_integer, 'second', 'third')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Second argument must be less than or equal to third argument')

class TestSelectIntegers(unittest.TestCase):
    def test_select_integers_included(self):
        select_integers_included = select_integers(5, choices)
        self.assertEqual(select_integers_included, 'Argument is one of the following integers: [4, 5, 6]')
    
    def test_select_integers_excluded_raises(self):
        with self.assertRaises(Exception) as context:
            select_integers(1, choices)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Argument must be one of the following integers: [4, 5, 6]')

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

class TestFiveScalars(unittest.TestCase):
    def test_five_scalars_integer_float_whole_positive(self):
        five_scalars_integer_float_whole_positive = five_scalars(good_integer, good_float, good_whole, good_positive, good_integer)
        self.assertEqual(five_scalars_integer_float_whole_positive, 'First, second, third, fourth, and fifth arguments are all integers or floats')
    
    def test_five_scalars_integer_float_whole_string_raises(self):
        with self.assertRaises(Exception) as context:
            five_scalars(good_integer, good_float, good_whole, good_positive, bad_scalar)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Fifth argument must be an integer or a float')

first_vector = [2, 3, 5]
second_vector = [7, 11, 13]
longer_vector = [1, 2, 3, 4]
none_vector = [None]
vector_strings = ['1 + 2k', '2 + 2k']
good_multitype = ['positive', 1, 'negative']
bad_multitype = ['positive', 'negative', 1]
bad_vector_string = 'vector'
bad_vector_buried_string = [1, 'two', 3]
bad_vector_final_string = [1, 2, 3, 4, 5, 'six']
bad_vector_nested =[[2], 3, 5]
good_long_vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
better_long_vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

class TestConfirmVector(unittest.TestCase):
    def test_confirm_vector_scalars(self):
        confirm_vector_scalars = confirm_vector(first_vector)
        self.assertEqual(confirm_vector_scalars, 'Argument is a 1-dimensional list')
    
    def test_confirm_vector_multitype(self):
        confirm_vector_multitype = confirm_vector(good_multitype)
        self.assertEqual(confirm_vector_multitype, 'Argument is a 1-dimensional list')
    
    def test_confirm_vector_string_raises(self):
        with self.assertRaises(Exception) as context:
            confirm_vector(bad_vector_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 1-dimensional list')

    def test_confirm_vector_nested_raises(self):
        with self.assertRaises(Exception) as context:
            confirm_vector(bad_vector_nested)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 1-dimensional list')

class TestVectorScalars(unittest.TestCase):
    def test_vector_scalars_3long(self):
        vector_scalars_3long = vector_of_scalars(first_vector)
        self.assertEqual(vector_scalars_3long, 'Argument is a 1-dimensional list containing elements that are integers or floats')
    
    def test_vector_scalars_4long(self):
        vector_scalars_4long = vector_of_scalars(longer_vector)
        self.assertEqual(vector_scalars_4long, 'Argument is a 1-dimensional list containing elements that are integers or floats')
    
    def test_vector_scalars_none_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_scalars(none_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements of argument must be integers or floats')
    
    def test_vector_scalars_multitype_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_scalars(good_multitype)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements of argument must be integers or floats')
    
    def test_vector_scalars_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_scalars(bad_vector_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements of argument must be integers or floats')
    
    def test_vector_scalars_final_string_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_scalars(bad_vector_final_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements of argument must be integers or floats')

class TestVectorStrings(unittest.TestCase):
    def test_vector_strings_normal(self):
        vector_strings_normal = vector_of_strings(vector_strings)
        self.assertEqual(vector_strings_normal, 'Argument is a 1-dimensional list containing elements that are strings or None')
    
    def test_vector_strings_none(self):
        vector_strings_none = vector_of_strings(none_vector)
        self.assertEqual(vector_strings_none, 'Argument is a 1-dimensional list containing elements that are strings or None')
    
    def test_vector_strings_nested_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_vector(bad_vector_nested)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements of argument must be integers, floats, strings, or None')

class TestLength(unittest.TestCase):
    def test_length_4_4_integers(self):
        length_4_4_integers = length(longer_vector, 4)
        self.assertEqual(length_4_4_integers, 'Argument contains exactly 4 elements')
    
    def test_length_3_3_integers(self):
        length_3_3_integers = length(first_vector, 3)
        self.assertEqual(length_3_3_integers, 'Argument contains exactly 3 elements')
    
    def test_length_3_3_mix(self):
        length_3_3_mix = length(good_multitype, 3)
        self.assertEqual(length_3_3_mix, 'Argument contains exactly 3 elements')
    
    def test_length_2_3_raises(self):
        with self.assertRaises(Exception) as context:
            length(first_vector, 2)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Argument must contain exactly 2 elements')
    
    def test_length_5_4_raises(self):
        with self.assertRaises(Exception) as context:
            length(longer_vector, 5)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Argument must contain exactly 5 elements')

class TestCompareVectors(unittest.TestCase):
    def test_compare_vectors_3_3(self):
        compare_vectors_3_3 = compare_vectors(first_vector, second_vector)
        self.assertEqual(compare_vectors_3_3, 'Both arguments contain the same number of elements')
    
    def test_compare_vectors_3_4_raises(self):
        with self.assertRaises(Exception) as context:
            compare_vectors(first_vector, longer_vector)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Both arguments must contain the same number of elements')

class TestAllowNoneVector(unittest.TestCase):
    def test_allow_none_vector_scalars(self):
        allow_none_vector_scalars = allow_none_vector(first_vector)
        self.assertEqual(allow_none_vector_scalars, 'Elements of argument are integers, floats, strings, or None')
    
    def test_allow_none_vector_strings(self):
        allow_none_vector_strings = allow_none_vector(vector_strings)
        self.assertEqual(allow_none_vector_strings, 'Elements of argument are integers, floats, strings, or None')
    
    def test_allow_none_vector_none(self):
        allow_none_vector_none = allow_none_vector(none_vector)
        self.assertEqual(allow_none_vector_none, 'Elements of argument are integers, floats, strings, or None')
    
    def test_allow_none_vector_scalars_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_strings(first_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements of argument must be strings or None')

class TestLongVector(unittest.TestCase):
    def test_long_vector_10(self):
        long_vector_10 = long_vector(good_long_vector)
        self.assertEqual(long_vector_10, 'First argument contains at least 10 elements')
    
    def test_long_vector_11(self):
        long_vector_11 = long_vector(better_long_vector)
        self.assertEqual(long_vector_11, 'First argument contains at least 10 elements')
    
    def test_long_vector_3_raises(self):
        with self.assertRaises(Exception) as context:
            long_vector(first_vector)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

first_matrix = [[1, 2, 3], [4, 5, 6]]
second_matrix = [[7, 8, 9], [10, 11, 12]]
small_square = [[1, 2], [3, 4]]
large_square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_points = [[1, 2], [3, 2], [5, 2], ['1 + 2k', 2]]
bad_matrix_string = 'matrix'
bad_matrix_buried_string = [['one', 2, 3], [4, 5, 6]]
bad_matrix_last_string = [[1, 2, 3], [4, 5, 6], [7, 8, 'nine']]
bad_matrix_vector = [1, 2, 3]
bad_matrix_buried_not_vector = [[1, 2, 3], [4, 5, 6], 7, [8, 9]]
bad_matrix_last_not_vector = [[1, 2, 3], [4, 5, 6], [7, 8], 9]
bad_matrix_nested = [[[1], 2, 3], [4, 5, 6]]

class TestConfirmMatrix(unittest.TestCase):
    def test_confirm_matrix_scalars(self):
        confirm_matrix_scalars = confirm_matrix(first_matrix)
        self.assertEqual(confirm_matrix_scalars, 'Argument is a 2-dimensional list')
    
    def test_confirm_matrix_string(self):
        confirm_matrix_string = confirm_matrix(bad_matrix_buried_string)
        self.assertEqual(confirm_matrix_string, 'Argument is a 2-dimensional list')
    
    def test_confirm_matrix_string_raises(self):
        with self.assertRaises(Exception) as context:
            confirm_matrix(bad_matrix_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 2-dimensional list')
    
    def test_confirm_matrix_vector_raises(self):
        with self.assertRaises(Exception) as context:
            confirm_matrix(bad_matrix_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 2-dimensional list')

    def test_confirm_matrix_nested_raises(self):
        with self.assertRaises(Exception) as context:
            confirm_matrix(bad_matrix_nested)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 2-dimensional list')

class TestMatrixScalars(unittest.TestCase):
    def test_matrix_scalars_2x3(self):
        matrix_scalars_2x3 = matrix_of_scalars(first_matrix)
        self.assertEqual(matrix_scalars_2x3, 'Argument is a 2-dimensional list containing nested elements that are integers or floats')
    
    def test_matrix_scalars_2x2(self):
        matrix_scalars_2x2 = matrix_of_scalars(small_square)
        self.assertEqual(matrix_scalars_2x2, 'Argument is a 2-dimensional list containing nested elements that are integers or floats')

    def test_matrix_scalars_buried_not_vector_raises(self):
        with self.assertRaises(Exception) as context:
            matrix_of_scalars(bad_matrix_buried_not_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within argument must be lists')
    
    def test_matrix_scalars_last_not_vector_raises(self):
        with self.assertRaises(Exception) as context:
            matrix_of_scalars(bad_matrix_last_not_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within argument must be lists')
    
    def test_matrix_scalars_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            matrix_of_scalars(bad_matrix_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within argument must be integers or floats')
    
    def test_matrix_scalars_last_string_raises(self):
        with self.assertRaises(Exception) as context:
            matrix_of_scalars(bad_matrix_last_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within argument must be integers or floats')

class TestSquareMatrix(unittest.TestCase):
    def test_square_matrix_2x2(self):
        square_matrix_2x2 = square_matrix(small_square)
        self.assertEqual(square_matrix_2x2, 'First argument contains the same amount of lists as the amount of elements contained within its first list')
    
    def test_square_matrix_3x3(self):
        square_matrix_3x3 = square_matrix(large_square)
        self.assertEqual(square_matrix_3x3, 'First argument contains the same amount of lists as the amount of elements contained within its first list')
    
    def test_square_matrix_2x3_raises(self):
        with self.assertRaises(Exception) as context:
            square_matrix(first_matrix)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain the same amount of lists as the amount of elements contained within its first list')

class TestCompareRows(unittest.TestCase):
    def test_compare_rows_2x2_2x3(self):
        compare_rows_2x2_2x3 = compare_rows(small_square, first_matrix)
        self.assertEqual(compare_rows_2x2_2x3, 'First argument and second argument contain the same amount of lists')
    
    def test_compare_rows_3x3_2x3_raises(self):
        with self.assertRaises(Exception) as context:
            compare_rows(large_square, first_matrix)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument and second argument must contain the same amount of lists')

class TestCompareColumns(unittest.TestCase):
    def test_compare_columns_3x3_2x3(self):
        compare_columns_3x3_2x3 = compare_columns(large_square, first_matrix)
        self.assertEqual(compare_columns_3x3_2x3, 'First list within first argument and first list within second argument contain the same amount of elements')
    
    def test_compare_columns_2x2_2x3_raises(self):
        with self.assertRaises(Exception) as context:
            compare_columns(small_square, first_matrix)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First list within first argument and first list within second argument must contain the same amount of elements')

class TestCompareMatrices(unittest.TestCase):
    def test_compare_matrices_2x3_2x3(self):
        compare_matrices_2x3_2x3 = compare_matrices(first_matrix, second_matrix)
        self.assertEqual(compare_matrices_2x3_2x3, 'First argument and second argument contain the same amount of lists; first list within first argument and first list within second argument contain the same amount of elements')
    
    def test_compare_matrices_3x3_2x3_raises(self):
        with self.assertRaises(Exception) as context:
            compare_matrices(large_square, first_matrix)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument and second argument must contain the same amount of lists')

    def test_compare_matrices_2x2_2x3_raises(self):
        with self.assertRaises(Exception) as context:
            compare_matrices(small_square, first_matrix)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First list within first argument and first list within second argument must contain the same amount of elements')

class TestColumnsRows(unittest.TestCase):
    def test_columns_rows_2x2_2x3(self):
        columns_rows_2x2_2x3 = columns_rows(small_square, first_matrix)
        self.assertEqual(columns_rows_2x2_2x3, 'First list within first argument contains the same amount of elements as the amount of lists contained within second argument')
    
    def test_columns_rows_2x2_3x3_raises(self):
        with self.assertRaises(Exception) as context:
            columns_rows(small_square, large_square)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First list within first argument must contain the same amount of elements as the amount of lists contained within second argument')

class TestAllowNoneMatrix(unittest.TestCase):
    def test_none_matrix_none(self):
        none_matrix_none = allow_none_matrix(none_vector)
        self.assertEqual(none_matrix_none, 'Argument is either a 1-dimensional list that contains None or a 2-dimensional list containing lists in which the first nested list contains integers or floats and the last nested list begins with a string')
    
    def test_none_matrix_lists(self):
        none_matrix_lists = allow_none_matrix(matrix_points)
        self.assertEqual(none_matrix_lists, 'Argument is either a 1-dimensional list that contains None or a 2-dimensional list containing lists in which the first nested list contains integers or floats and the last nested list begins with a string')

    def test_none_matrix_no_string_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_matrix(first_matrix)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'If the first element of argument is not None, then the last element must be a list with a first element that is a string')

class TestAllowVectorMatrix(unittest.TestCase):
    def test_allow_vector_matrix_matrix(self):
        allow_vector_matrix_matrix = allow_vector_matrix(first_matrix)
        self.assertEqual(allow_vector_matrix_matrix, 'Argument is a list containing lists, integers, floats, strings, or None')
    
    def test_allow_vector_matrix_vector(self):
        allow_vector_matrix_vector = allow_vector_matrix(good_long_vector)
        self.assertEqual(allow_vector_matrix_vector, 'Argument is a list containing lists, integers, floats, strings, or None')
    
    def test_allow_vector_matrix_none(self):
        allow_vector_matrix_none = allow_vector_matrix(none_vector)
        self.assertEqual(allow_vector_matrix_none, 'Argument is a list containing lists, integers, floats, strings, or None')

    def test_allow_vector_matrix_nested_raises(self):
        with self.assertRaises(Exception) as context:
            allow_vector_matrix(bad_matrix_nested)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument cannot be more than a 2-dimensional list')

class TestLevel(unittest.TestCase):
    def test_level_2x3_2(self):
        level_2x2_2 = level(first_matrix, 2)
        self.assertEqual(level_2x2_2, 'Last argument is less than or equal to the length of the nested lists within the first argument')
    
    def test_level_2x3_4_raises(self):
        with self.assertRaises(Exception) as context:
            level(first_matrix, 4)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Last argument must be less than or equal to the length of the nested lists within the first argument')

good_equation = 'hyperbolic'
bad_equation = 'rational'

class TestSelectEquations(unittest.TestCase):
    def test_select_equations_included(self):
        select_equations_multiple = select_equations(good_equation)
        self.assertEqual(select_equations_multiple, "First argument is either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")
    
    def test_select_equations_excluded_raises(self):
        with self.assertRaises(Exception) as context:
            select_equations(bad_equation)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), "First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")

good_points = 'intercepts'
bad_points = 'criticals'

class TestSelectPoints(unittest.TestCase):
    def test_select_points_included(self):
        select_points_multiple = select_points(good_points)
        self.assertEqual(select_points_multiple, "Argument is either 'point', 'intercepts', 'maxima', 'minima', or 'inflections'")
    
    def test_select_points_excluded_raises(self):
        with self.assertRaises(Exception) as context:
            select_points(bad_points)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), "Argument must be either 'point', 'intercepts', 'maxima', 'minima', or 'inflections'")

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 111 tests in 0.007s ---------- OK ---------- #