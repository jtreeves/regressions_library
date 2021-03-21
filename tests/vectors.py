import unittest

from library.vectors.component_form import component_form
from library.vectors.direction import direction
from library.vectors.magnitude import magnitude
from library.vectors.unit import unit
from library.vectors.column import column
from library.vectors.dimension import dimension
from library.vectors.unify import unify
from library.vectors.addition import addition
from library.vectors.scalar import scalar
from library.vectors.dot_product import dot_product

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
direction_vector = direction(component_vector)
magnitude_vector = magnitude(component_vector)
unit_vector = unit(component_vector)

class TestSimpleVector(unittest.TestCase):
    def test_component_vector(self):
        self.assertEqual(component_vector, [3, 10])

    def test_direction_vector(self):
        self.assertAlmostEqual(direction_vector['degree'], 73.3008, 4)
    
    def test_magnitude_vector(self):
        self.assertAlmostEqual(magnitude_vector, 10.4403, 4)
    
    def test_unit_vector(self):
        self.assertAlmostEqual(unit_vector[0], 0.2873, 4)

column_first = column(first_vector)
column_second = column(second_vector)

class TestColumn(unittest.TestCase):
    def test_column_first(self):
        self.assertEqual(column_first, [[2], [5], [9], [13]])

    def test_column_second(self):
        self.assertEqual(column_second, [[1], [-7], [23], [-2]])

dimension_first = dimension(nested_vector, 1)
dimension_second = dimension(nested_vector, 2)

class TestDimension(unittest.TestCase):
    def test_dimension_first(self):
        self.assertEqual(dimension_first, [3, 5, 2])

    def test_dimension_second(self):
        self.assertEqual(dimension_second, [4, 9, 8])

unify_first = unify(first_vector, second_vector)
unify_second = unify(second_vector, first_vector)

class TestUnify(unittest.TestCase):
    def test_unify_first(self):
        self.assertEqual(unify_first, [[2, 1], [5, -7], [9, 23], [13, -2]])

    def test_unify_second(self):
        self.assertEqual(unify_second, [[1, 2], [-7, 5], [23, 9], [-2, 13]])

addition_first = addition(first_point, second_point)
addition_second = addition(first_vector, second_vector)

class TestAddition(unittest.TestCase):
    def test_addition_first(self):
        self.assertEqual(addition_first, [7, 4])

    def test_addition_second(self):
        self.assertEqual(addition_second, [3, -2, 32, 11])

scalar_first = scalar(first_vector, scalar_number)
scalar_second = scalar(second_vector, scalar_number)

class TestScalar(unittest.TestCase):
    def test_scalar_first(self):
        self.assertEqual(scalar_first, [-6, -15, -27, -39])

    def test_scalar_second(self):
        self.assertEqual(scalar_second, [-3, 21, -69, 6])

dot_product_first = dot_product(first_point, second_point)
dot_product_second = dot_product(first_vector, second_vector)

class TestDotProduct(unittest.TestCase):
    def test_dot_product_first(self):
        self.assertEqual(dot_product_first, -11)

    def test_dot_product_second(self):
        self.assertEqual(dot_product_second, 148)

if __name__ == '__main__':
    unittest.main()