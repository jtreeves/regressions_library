from matrices.addition import addition
from matrices.scalar import scalar
from matrices.multiplication import multiplication

def error(independent, dependent, solution):
    product = multiplication(independent, solution)
    negation = scalar(product, -1)
    result = addition(dependent, negation)
    return result