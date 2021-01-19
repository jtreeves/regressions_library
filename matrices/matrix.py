from numpy import array, matrix
from numpy.linalg import inv

a = [[1, 2], [3, 4]]
a_array = array(a)
a_matrix = matrix(a)
a_inv_array = inv(a_array)
a_inv_matrix = inv(a_matrix)
a_inv_matrix_list = matrix.tolist(a_inv_matrix)
print(f'a: {a}')
print(f'a_array: {a_array}')
print(f'a_matrix: {a_matrix}')
print(f'a_inv_array: {a_inv_array}')
print(f'a_inv_matrix: {a_inv_matrix}')
print(f'a_inv_matrix_list: {a_inv_matrix_list}')