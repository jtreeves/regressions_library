def hyperbolic(first_constant, second_constant):
    constants = [-1 * first_constant]
    def hyperbolic_derivative(variable):
        evaluation = constants[0] / variable**2
        return evaluation
    results = {
        'constants': constants,
        'derivative': hyperbolic_derivative
    }
    return results