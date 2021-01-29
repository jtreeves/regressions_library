def quadratic(first_constant, second_constant, third_constant):
    constants = [2 * first_constant, second_constant]
    def quadratic_derivative(variable):
        evaluation = constants[0] * variable + constants[1]
        return evaluation
    results = {
        'constants': constants,
        'derivative': quadratic_derivative
    }
    return results