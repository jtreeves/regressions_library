def hyperbolic(first_constant, second_constant):
    first_constants = [-1 * first_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] / variable**2
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [-2 * first_constants[0]]
    def second_derivative(variable):
        evaluation = second_constants[0] / variable**3
        return evaluation
    second_object = {
        'constants': second_constants,
        'evaluation': second_derivative
    }
    results = {
        'first': first_object,
        'second': second_object
    }
    return results