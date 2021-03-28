from library.statistics.summation import sum_value
from library.errors.vectors import first_vector
from .check import check_first_vector

def vector_magnitude(vector):
    first_vector(vector)
    squares = []
    for i in range(len(vector)):
        squares.append(vector[i]**2)
    sum_squares = sum_value(squares)
    result = sum_squares**(1/2)
    return result