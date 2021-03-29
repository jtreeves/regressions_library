from library.errors.vectors import vector_of_scalars
from library.statistics.summation import sum_value

def vector_magnitude(vector):
    vector_of_scalars(vector, 'only')
    squares = []
    for element in vector:
        squares.append(element**2)
    sum_squares = sum_value(squares)
    result = sum_squares**(1/2)
    return result