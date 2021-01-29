def hyperbolic(first_constant, second_constant):
    def hyperbolic_equation(variable):
        evaluation = first_constant / variable + second_constant
        return evaluation
    return hyperbolic_equation