def hyperbolic_equation(first_constant, second_constant):
    def hyperbolic_evaluation(variable):
        result = first_constant / variable + second_constant
        return result
    return hyperbolic_evaluation