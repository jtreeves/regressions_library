def cubic(first_constant, second_constant, third_constant, fourth_constant):
    def cubic_equation(variable):
        evaluation = first_constant * variable**3 + second_constant * variable**2 + third_constant * variable + fourth_constant
        return evaluation
    return cubic_equation