from library.statistics.summation import summation

def magnitude(vector):
    squares = []
    for i in range(len(vector)):
        squares.append(vector[i]**2)
    sum_squares = summation(squares)
    result = sum_squares**(1/2)
    return result