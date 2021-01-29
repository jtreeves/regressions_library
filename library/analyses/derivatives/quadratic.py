def quadratic(first_constant, second_constant):
    def quadratic_derivative(variable):
        evaluation = 2 * first_constant * variable + second_constant
        return evaluation
    return quadratic_derivative