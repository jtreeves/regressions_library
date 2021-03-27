def cubic_equation(first_constant, second_constant, third_constant, fourth_constant):
    def cubic_evaluation(variable):
        result = first_constant * variable**3 + second_constant * variable**2 + third_constant * variable + fourth_constant
        return result
    return cubic_evaluation