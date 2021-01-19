from matrices.addition import addition
from matrices.scalar import scalar
from matrices.multiplication import multiplication
from matrices.magnitude import magnitude

def error_new(data, equation):
    summation = 0
    for i in range(len(data)):
        summation += (data[i][1] - equation(data[i][0]))**2
    result = summation**(1/4)
    return result

def error(independent, dependent, solution):
    product = multiplication(independent, solution)
    negation = scalar(dependent, -1)
    array = addition(product, negation)
    norm = magnitude(array)
    result = norm**(1/2)
    return result