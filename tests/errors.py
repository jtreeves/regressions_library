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
bad_vector_buried_string = [1, 'two', 3]
bad_vector_nested =[[2], 3, 5]

class TestVectorScalars(unittest.TestCase):
    def test_vector_scalars_3long(self):
        vector_scalars_3long = vector_of_scalars(first_vector, 'only')
        self.assertEqual(vector_scalars_3long, 'Argument is a 1-dimensional list or tuple containing elements that are integers or floats')
    
    def test_vector_scalars_4long(self):
        vector_scalars_4long = vector_of_scalars(long_vector, 'only')
        self.assertEqual(vector_scalars_4long, 'Argument is a 1-dimensional list or tuple containing elements that are integers or floats')
    
    def test_vector_scalars_nested_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_scalars(bad_vector_nested, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 1-dimensional list or tuple')
    
    def test_vector_scalars_string_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_scalars(bad_vector_string, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 1-dimensional list or tuple')
    
    def test_vector_scalars_none_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_scalars(none_vector, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements of argument must be integers or floats')
    
    def test_vector_scalars_multitype_raises(self):
        with self.assertRaises(Exception) as context:
            vector_of_scalars(good_multitype, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements of argument must be integers or floats')

class TestAllowNoneVector(unittest.TestCase):
    def test_none_vector_none(self):
        none_vector_none = allow_none_vector(none_vector, 'only')
        self.assertEqual(none_vector_none, 'Argument is a 1-dimensional list or tuple that only contains integers, floats, or None; if it contains a second element, then its second element is an integer or a float')
    
    def test_none_vector_scalars(self):
        none_vector_scalars = allow_none_vector(first_vector, 'only')
        self.assertEqual(none_vector_scalars, 'Argument is a 1-dimensional list or tuple that only contains integers, floats, or None; if it contains a second element, then its second element is an integer or a float')
    
    def test_none_vector_multitype_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_vector(good_multitype, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument can only contain integers, floats, or None')
    
    def test_none_vector_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_vector(bad_vector_buried_string, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Second element of argument must be an integer or a float')
    
    def test_none_vector_string_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_vector(bad_vector_string, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 1-dimensional list or tuple')
    
    def test_none_vector_nested_raises(self):
        with self.assertRaises(Exception) as context:
            allow_none_vector(bad_vector_nested, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 1-dimensional list or tuple')

class TestMultitypeVector(unittest.TestCase):
    def test_multitype_vector_string_integer(self):
        multitype_vector_string_integer = multitype_vector(good_multitype)
        self.assertEqual(multitype_vector_string_integer, "Argument is a 1-dimensional list or tuple with an initial element of either 'constant', 'positive', or 'negative'; if it contains a second element, then its second element is an integer or a float")
    
    def test_multitype_vector_string_string_raises(self):
        with self.assertRaises(Exception) as context:
            multitype_vector(bad_multitype)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Second element of argument must be an integer or a float')
    
    def test_multitype_vector_integer_raises(self):
        with self.assertRaises(Exception) as context:
            multitype_vector(first_vector)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), "First element of argument must be either 'constant', 'positive', or 'negative'")
    
    def test_multitype_vector_string_raises(self):
        with self.assertRaises(Exception) as context:
            multitype_vector(bad_vector_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 1-dimensional list or tuple')
    
    def test_multitype_vector_nested_raises(self):
        with self.assertRaises(Exception) as context:
            multitype_vector(bad_vector_nested)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 1-dimensional list or tuple')

class TestLength(unittest.TestCase):
    def test_length_4_4_integers(self):
        length_4_4_integers = length(long_vector, 4)
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
            length(long_vector, 5)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Argument must contain exactly 5 elements')

class TestCompareVectors(unittest.TestCase):
    def test_compare_vectors_3_3(self):
        compare_vectors_3_3 = compare_vectors(first_vector, second_vector)
        self.assertEqual(compare_vectors_3_3, 'Both arguments contain the same number of elements')
    
    def test_compare_vectors_3_4_raises(self):
        with self.assertRaises(Exception) as context:
            compare_vectors(first_vector, long_vector)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Both arguments must contain the same number of elements')

first_matrix = [[1, 2, 3], [4, 5, 6]]
second_matrix = [[7, 8, 9], [10, 11, 12]]
small_square = [[1, 2], [3, 4]]
large_square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
bad_matrix_string = 'matrix'
bad_matrix_buried_string = [['one', 2, 3], [4, 5, 6]]
bad_matrix_vector = [1, 2, 3]
bad_matrix_nested = [[[1], 2, 3], [4, 5, 6]]

class TestMatrixScalars(unittest.TestCase):
    def test_matrix_scalars_2x3(self):
        matrix_scalars_2x3 = matrix_of_scalars(first_matrix, 'only')
        self.assertEqual(matrix_scalars_2x3, 'Argument is a 2-dimensional list or tuple containing elements that are integers or floats')
    
    def test_matrix_scalars_2x2(self):
        matrix_scalars_2x2 = matrix_of_scalars(small_square, 'only')
        self.assertEqual(matrix_scalars_2x2, 'Argument is a 2-dimensional list or tuple containing elements that are integers or floats')
    
    def test_matrix_scalars_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            matrix_of_scalars(bad_matrix_buried_string, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements nested within argument must be integers or floats')
    
    def test_matrix_scalars_string_raises(self):
        with self.assertRaises(Exception) as context:
            matrix_of_scalars(bad_matrix_string, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 2-dimensional list or tuple')
    
    def test_matrix_scalars_vector_raises(self):
        with self.assertRaises(Exception) as context:
            matrix_of_scalars(bad_matrix_vector, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 2-dimensional list or tuple')
    
    def test_matrix_scalars_nested_raises(self):
        with self.assertRaises(Exception) as context:
            matrix_of_scalars(bad_matrix_nested, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a 2-dimensional list or tuple')

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

class TestLevel(unittest.TestCase):
    def test_level_2x3_2(self):
        level_2x2_2 = level(first_matrix, 2)
        self.assertEqual(level_2x2_2, 'Last argument is less than or equal to the length of the nested lists within the first argument')
    
    def test_level_2x3_4_raises(self):
        with self.assertRaises(Exception) as context:
            level(first_matrix, 4)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'Last argument must be less than or equal to the length of the nested lists within the first argument')

def good_function(x):
    return 2 * x

bad_function = 'function'

class TestCallableFunction(unittest.TestCase):
    def test_callable_function_multiply(self):
        callable_function_multiply = callable_function(good_function, 'only')
        self.assertEqual(callable_function_multiply, 'Argument is a callable function')
    
    def test_callable_string_raises(self):
        with self.assertRaises(Exception) as context:
            callable_function(bad_function, 'only')
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Argument must be a callable function')

good_equation = 'hyperbolic'
bad_equation = 'rational'

class TestSelectEquations(unittest.TestCase):
    def test_select_equations_included(self):
        select_equations_multiply = select_equations(good_equation)
        self.assertEqual(select_equations_multiply, "First argument is either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")
    
    def test_select_equations_excluded_raises(self):
        with self.assertRaises(Exception) as context:
            select_equations(bad_equation)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), "First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 84 tests in 0.010s ---------- OK ---------- #