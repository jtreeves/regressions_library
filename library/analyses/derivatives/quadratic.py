def quadratic_derivatives(first_constant, second_constant, third_constant):
    first_constants = [2 * first_constant, second_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] * variable + first_constants[1]
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [first_constants[0]]
    def second_derivative(variable):
        evaluation = second_constants[0]
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