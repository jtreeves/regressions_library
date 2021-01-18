from matrices.addition import addition
from matrices.scalar import scalar
from matrices.multiplication import multiplication
from matrices.magnitude import magnitude

def error(independent, dependent, solution):
    product = multiplication(independent, solution)
    negation = scalar(dependent, -1)
    array = addition(product, negation)
    norm = magnitude(array)
    result = norm**(1/2)
    return result