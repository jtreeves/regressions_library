import unittest

from regressions.matrices.addition import matrix_sum
from regressions.matrices.multiplication import scalar_product_matrix, matrix_product
from regressions.matrices.transpose import transposed_matrix
from regressions.matrices.cofactors import matrix_of_cofactors
from regressions.matrices.determinant import linear_determinant
from regressions.matrices.minors import matrix_of_minors
from regressions.matrices.inverse import inverse_matrix
from regressions.matrices.solve import system_solution

first_2d = [
    [5, 8],
    [2, 3]
]

second_2d = [
    [4, 1],
    [7, 3]
]

zero_2d = [
    [0, 0],
    [0, 0]
]

first_3d = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]

second_3d = [
    [3, 0, 2],
    [2, 0, -2],
    [0, 1, 1]
]

first_4d = [
    [5, 2, -6, 2],
    [3, 4, 1, -5],
    [9, -8, 7, 1],
    [-2, 5, 0, 11]
]

second_4d = [
    [13, -7, 1, -12],
    [5, -16, 14, 5],
    [-8, 6, 2, 11],
    [3, 0, 8, -2]
]

first_2x3 = [
    [2, 6, -9],
    [4, 5, 1]
]

second_2x3 = [
    [7, 1, 3],
    [-8, 2, 5]
]

column_2d = [
    [3],
    [-4]
]

column_3d = [
    [5],
    [-1],
    [7]
]

scalar_number = -7

class TestAddition(unittest.TestCase):
    def test_addition_2d(self):
        addition_2d = matrix_sum(first_2d, second_2d)
        self.assertEqual(addition_2d, [[9, 9], [9, 6]])
    
    def test_addition_3d(self):
        addition_3d = matrix_sum(first_3d, second_3d)
        self.assertEqual(addition_3d, [[9, 1, 3], [6, -2, 3], [2, 9, 8]])
    
    def test_addition_4d(self):
        addition_4d = matrix_sum(first_4d, second_4d)
        self.assertEqual(addition_4d, [[18, -5, -5, -10], [8, -12, 15, 0], [1, -2, 9, 12], [1, 5, 8, 9]])
    
    def test_addition_2x3(self):
        addition_2x3 = matrix_sum(first_2x3, second_2x3)
        self.assertEqual(addition_2x3, [[9, 7, -6], [-4, 7, 6]])

class TestScalarProduct(unittest.TestCase):
    def test_scalar_2d(self):
        scalar_2d = scalar_product_matrix(first_2d, scalar_number)
        self.assertEqual(scalar_2d, [[-35, -56], [-14, -21]])
    
    def test_scalar_3d(self):
        scalar_3d = scalar_product_matrix(first_3d, scalar_number)
        self.assertEqual(scalar_3d, [[-42, -7, -7], [-28, 14, -35], [-14, -56, -49]])
    
    def test_scalar_4d(self):
        scalar_4d = scalar_product_matrix(first_4d, scalar_number)
        self.assertEqual(scalar_4d, [[-35, -14, 42, -14], [-21, -28, -7, 35], [-63, 56, -49, -7], [14, -35, 0, -77]])
    
    def test_scalar_2x3(self):
        scalar_2x3 = scalar_product_matrix(first_2x3, scalar_number)
        self.assertEqual(scalar_2x3, [[-14, -42, 63], [-28, -35, -7]])

class TestMatrixProduct(unittest.TestCase):
    def test_multiplication_2d_first(self):
        multiplication_2d_first = matrix_product(first_2d, second_2d)
        self.assertEqual(multiplication_2d_first, [[76, 29], [29, 11]])
    
    def test_multiplication_2d_second(self):
        multiplication_2d_second = matrix_product(second_2d, first_2d)
        self.assertEqual(multiplication_2d_second, [[22, 35], [41, 65]])
    
    def test_multiplication_3d_first(self):
        multiplication_3d_first = matrix_product(first_3d, second_3d)
        self.assertEqual(multiplication_3d_first, [[20, 1, 11], [8, 5, 17], [22, 7, -5]])
    
    def test_multiplication_3d_second(self):
        multiplication_3d_second = matrix_product(second_3d, first_3d)
        self.assertEqual(multiplication_3d_second, [[22, 19, 17], [8, -14, -12], [6, 6, 12]])
    
    def test_multiplication_4d_first(self):
        multiplication_4d_first = matrix_product(first_4d, second_4d)
        self.assertEqual(multiplication_4d_first, [[129, -103, 37, -120], [36, -79, 21, 5], [24, 107, -81, -73], [32, -66, 156, 27]])
    
    def test_multiplication_4d_second(self):
        multiplication_4d_second = matrix_product(second_4d, first_4d)
        self.assertEqual(multiplication_4d_second, [[77, -70, -78, -70], [93, -141, 52, 159], [-26, 47, 68, 77], [91, -68, 38, -8]])

class TestTranspose(unittest.TestCase):
    def test_transpose_2d(self):
        transpose_2d = transposed_matrix(first_2d)
        self.assertEqual(transpose_2d, [[5, 2], [8, 3]])
    
    def test_transpose_3d(self):
        transpose_3d = transposed_matrix(first_3d)
        self.assertEqual(transpose_3d, [[6, 4, 2], [1, -2, 8], [1, 5, 7]])
    
    def test_transpose_4d(self):
        transpose_4d = transposed_matrix(first_4d)
        self.assertEqual(transpose_4d, [[5, 3, 9, -2], [2, 4, -8, 5], [-6, 1, 7, 0], [2, -5, 1, 11]])
    
    def test_transpose_2x3(self):
        transpose_2x3 = transposed_matrix(first_2x3)
        self.assertEqual(transpose_2x3, [[2, 4], [6, 5], [-9, 1]])

class TestCofactors(unittest.TestCase):
    def test_cofactors_2d(self):
        cofactors_2d = matrix_of_cofactors(first_2d)
        self.assertEqual(cofactors_2d, [[5, -8], [-2, 3]])
    
    def test_cofactors_3d(self):
        cofactors_3d = matrix_of_cofactors(first_3d)
        self.assertEqual(cofactors_3d, [[6, -1, 1], [-4, -2, -5], [2, -8, 7]])
    
    def test_cofactors_4d(self):
        cofactors_4d = matrix_of_cofactors(first_4d)
        self.assertEqual(cofactors_4d, [[5, -2, -6, -2], [-3, 4, -1, -5], [9, 8, 7, -1], [2, 5, 0, 11]])

class TestDeterminant(unittest.TestCase):
    def test_determinant_2d(self):
        determinant_2d = linear_determinant(first_2d)
        self.assertEqual(determinant_2d, -1)
    
    def test_determinant_3d(self):
        determinant_3d = linear_determinant(first_3d)
        self.assertEqual(determinant_3d, -306)
    
    def test_determinant_4d(self):
        determinant_4d = linear_determinant(first_4d)
        self.assertEqual(determinant_4d, 7992)

class TestMinors(unittest.TestCase):
    def test_minors_2d(self):
        minors_2d = matrix_of_minors(first_2d)
        self.assertEqual(minors_2d, [[3, 2], [8, 5]])
    
    def test_minors_3d(self):
        minors_3d = matrix_of_minors(first_3d)
        self.assertEqual(minors_3d, [[-54, 18, 36], [-1, 40, 46], [7, 26, -16]])
    
    def test_minors_4d(self):
        minors_4d = matrix_of_minors(first_4d)
        self.assertEqual(minors_4d, [[576, 60, -828, -132], [-474, 1019, -609, -377], [426, 197, 345, -167], [-72, 492, -396, 516]])

class TestInverse(unittest.TestCase):
    def test_inverse_2d(self):
        inverse_2d = inverse_matrix(first_2d)
        self.assertEqual(inverse_2d, [[-3.0, 8.0], [2.0, -5.0]])
    
    def test_inverse_3d(self):
        inverse_3d = inverse_matrix(first_3d)
        self.assertEqual(inverse_3d, [[0.17647058823529413, -0.0032679738562091504, -0.022875816993464054], [0.058823529411764705, -0.13071895424836602, 0.08496732026143791], [-0.11764705882352941, 0.1503267973856209, 0.05228758169934641]])
    
    def test_inverse_4d(self):
        inverse_4d = inverse_matrix(first_4d)
        self.assertEqual(inverse_4d, [[0.07207207207207207, 0.05930930930930931, 0.0533033033033033, 0.009009009009009009], [-0.0075075075075075074, 0.1275025025025025, -0.02464964964964965, 0.06156156156156156], [-0.1036036036036036, 0.0762012012012012, 0.04316816816816817, 0.04954954954954955], [0.016516516516516516, -0.04717217217217217, 0.020895895895895897, 0.06456456456456457]])
    
    def test_inverse_zero(self):
        inverse_zero = inverse_matrix(zero_2d)
        self.assertEqual(inverse_zero, zero_2d)

class TestSolveSystems(unittest.TestCase):
    def test_solve_2d(self):
        solve_2d = system_solution(first_2d, column_2d)
        self.assertEqual(solve_2d, [-41.0, 26.0])
    
    def test_solve_3d(self):
        solve_3d = system_solution(first_3d, column_3d)
        self.assertEqual(solve_3d, [0.7255, 1.0196, -0.3725])

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 33 tests in 0.012s ---------- OK ---------- #