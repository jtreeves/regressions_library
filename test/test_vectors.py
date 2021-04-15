import unittest

from library.vectors.components import component_form
from library.vectors.direction import vector_direction
from library.vectors.magnitude import vector_magnitude
from library.vectors.unit import unit_vector
from library.vectors.column import column_conversion
from library.vectors.dimension import single_dimension
from library.vectors.unify import unite_vectors
from library.vectors.addition import vector_sum
from library.vectors.multiplication import scalar_product_vector, dot_product

first_point = [2, -3]
second_point = [5, 7]

first_vector = [2, 5, 9, 13]
second_vector = [1, -7, 23, -2]

nested_vector = [
    [3, 4], 
    [5, 9], 
    [2, 8]
]

scalar_number = -3

component_vector = component_form(first_point, second_point)

class TestSimpleVector(unittest.TestCase):
    def test_component_vector(self):
        self.assertEqual(component_vector, [3, 10])

    def test_direction_vector(self):
        direction_vector = vector_direction(component_vector)
        self.assertEqual(direction_vector['degree'], 73.30075576600639)
    
    def test_magnitude_vector(self):
        magnitude_vector = vector_magnitude(component_vector)
        self.assertEqual(magnitude_vector, 10.44030650891055)
    
    def test_unit_vector(self):
        unit = unit_vector(component_vector)
        self.assertEqual(unit, [0.2873478855663454, 0.9578262852211514])

class TestZeroes(unittest.TestCase):
    def test_direction_zero(self):
        direction_zero = vector_direction([0, 1])
        self.assertEqual(direction_zero['degree'], 89.99427042206779)
    
    def test_unit_vector(self):
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

# ---------- Ran 18 tests in 0.002s ---------- OK ---------- #