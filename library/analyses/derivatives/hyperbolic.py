def hyperbolic(first_constant, second_constant):
    def hyperbolic_derivative(variable):
        evaluation = -1 * first_constant / variable**2
        return evaluation
    return hyperbolic_derivative