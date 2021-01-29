def cubic(first_constant, second_constant, third_constant, fourth_constant):
    constants = [3 * first_constant, 2 * second_constant, third_constant]
    def cubic_derivative(variable):
        evaluation = constants[0] * variable**2 + constants[1] * variable + constants[2]
        return evaluation
    results = {
        'constants': constants,
        'derivative': cubic_derivative
    }
    return results