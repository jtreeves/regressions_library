def cubic(first_constant, second_constant, third_constant, fourth_constant):
    first_constants = [3 * first_constant, 2 * second_constant, third_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] * variable**2 + first_constants[1] * variable + first_constants[2]
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [2 * first_constants[0], first_constants[1]]
    def second_derivative(variable):
        evaluation = second_constants[0] * variable + second_constants[1]
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