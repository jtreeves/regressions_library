from library.statistics.summation import sum_value

def vector_magnitude(vector):
    squares = []
    for i in range(len(vector)):
        squares.append(vector[i]**2)
    sum_squares = sum_value(squares)
    result = sum_squares**(1/2)
    return result