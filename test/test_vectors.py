import unittest

from regressions.vectors.components import component_form
from regressions.vectors.direction import vector_direction
from regressions.vectors.magnitude import vector_magnitude
from regressions.vectors.unit import unit_vector
from regressions.vectors.column import column_conversion
from regressions.vectors.dimension import single_dimension
from regressions.vectors.separate import separate_elements
from regressions.vectors.generate import generate_elements
from regressions.vectors.unify import unite_vectors
from regressions.vectors.addition import vector_sum
from regressions.vectors.multiplication import scalar_product_vector, dot_product

first_point = [2, -3]
second_point = [5, 7]

first_vector = [2, 5, 9, 13]
second_vector = [1, -7, 23, -2]

nested_vector = [
    [3, 4], 
    [5, 9], 
    [2, 8]
]

string_vector = ['one', 'two', 'three']

mixed_vector = [1, 'two', 3, 'four', 5]

scalar_number = -3

component_vector = component_form(first_point, second_point)

class TestComponent(unittest.TestCase):
    def test_component(self):
        self.assertEqual(component_vector, [3, 10])
    
    def test_component_long(self):
        component_long = component_form(first_vector, second_vector)
        self.assertEqual(component_long, [-1, -12, 14, -15])

class TestDirection(unittest.TestCase):
    def test_direction(self):
        direction = vector_direction(component_vector)
        self.assertEqual(direction['degree'], 73.30075576600639)

    def test_direction_zero(self):
        direction_zero = vector_direction([0, 1])
        self.assertEqual(direction_zero['degree'], 89.99427042206779)

class TestMagnitude(unittest.TestCase):    
    def test_magnitude_short(self):
        magnitude_short = vector_magnitude(component_vector)
        self.assertEqual(magnitude_short, 10.44030650891055)
    
    def test_magnitude_long(self):
        magnitude_long = vector_magnitude(first_vector)
        self.assertEqual(magnitude_long, 16.703293088490067)

class TestUnit(unittest.TestCase):    
    def test_unit(self):
        unit = unit_vector(component_vector)
        self.assertEqual(unit, [0.2873478855663454, 0.9578262852211514])

    def test_unit_zero(self):
        unit_zero = unit_vector([0, 0])
        self.assertEqual(unit_zero, [0.0, 0.0])

class TestColumn(unittest.TestCase):
    def test_column_first(self):
        column_first = column_conversion(first_vector)
        self.assertEqual(column_first, [[2], [5], [9], [13]])

    def test_column_second(self):
        column_second = column_conversion(second_vector)
        self.assertEqual(column_second, [[1], [-7], [23], [-2]])

class TestDimension(unittest.TestCase):
    def test_dimension_first(self):
        dimension_first = single_dimension(nested_vector, 1)
        self.assertEqual(dimension_first, [3, 5, 2])

    def test_dimension_second(self):
        dimension_second = single_dimension(nested_vector, 2)
        self.assertEqual(dimension_second, [4, 9, 8])

class TestSeparate(unittest.TestCase):
    def test_separate_all_numbers(self):
        separate_all_numbers = separate_elements(first_vector)
        self.assertEqual(separate_all_numbers, {'numerical': first_vector, 'other': []})
    
    def test_separate_all_strings(self):
        separate_all_strings = separate_elements(string_vector)
        self.assertEqual(separate_all_strings, {'numerical': [], 'other': string_vector})
    
    def test_separate_mixed(self):
        separate_mixed = separate_elements(mixed_vector)
        self.assertEqual(separate_mixed, {'numerical': [1, 3, 5], 'other': ['two', 'four']})
    
    def test_separate_none(self):
        separate_none = separate_elements([None])
        self.assertEqual(separate_none, {'numerical': [], 'other': [None]})

class TestGenerate(unittest.TestCase):
    def test_generate_ints(self):
        generate_ints = generate_elements(2, 3)
        self.assertEqual(generate_ints, [2.0, 5.0, 8.0, 11.0, 14.0, '2.0 + 3.0k'])
    
    def test_generate_floats(self):
        generate_floats = generate_elements(7.81259217, 3.12748261)
        self.assertEqual(generate_floats, [7.8126, 10.9401, 14.0676, 17.195, 20.3225, '7.8126 + 3.1275k'])

class TestUnify(unittest.TestCase):
    def test_unify_first(self):
        unify_first = unite_vectors(first_vector, second_vector)
        self.assertEqual(unify_first, [[2, 1], [5, -7], [9, 23], [13, -2]])

    def test_unify_second(self):
        unify_second = unite_vectors(second_vector, first_vector)
        self.assertEqual(unify_second, [[1, 2], [-7, 5], [23, 9], [-2, 13]])

class TestAddition(unittest.TestCase):
    def test_addition_first(self):
        addition_first = vector_sum(first_point, second_point)
        self.assertEqual(addition_first, [7, 4])

    def test_addition_second(self):
        addition_second = vector_sum(first_vector, second_vector)
        self.assertEqual(addition_second, [3, -2, 32, 11])

class TestScalarProduct(unittest.TestCase):
    def test_scalar_first(self):
        scalar_first = scalar_product_vector(first_vector, scalar_number)
        self.assertEqual(scalar_first, [-6, -15, -27, -39])

    def test_scalar_second(self):
        scalar_second = scalar_product_vector(second_vector, scalar_number)
        self.assertEqual(scalar_second, [-3, 21, -69, 6])

class TestDotProduct(unittest.TestCase):
    def test_dot_product_first(self):
        dot_product_first = dot_product(first_point, second_point)
        self.assertEqual(dot_product_first, -11)

    def test_dot_product_second(self):
        dot_product_second = dot_product(first_vector, second_vector)
        self.assertEqual(dot_product_second, 148)

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 26 tests in 0.002s ---------- OK ---------- #