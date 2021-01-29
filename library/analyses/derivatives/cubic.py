def cubic(first_constant, second_constant, third_constant, fourth_constant):
    def cubic_derivative(variable):
        evaluation = 3 * first_constant * variable**2 + 2 * second_constant * variable + third_constant
        return evaluation
    return cubic_derivative