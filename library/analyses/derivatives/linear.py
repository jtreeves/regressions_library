def linear(first_constant, second_constant):
    constants = [first_constant]
    def linear_derivative(variable):
        evaluation = constants[0]
        return evaluation
    results = {
        'constants': constants,
        'derivative': linear_derivative
    }
    return results