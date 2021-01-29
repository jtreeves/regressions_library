def linear(first_constant, second_constant):
    def linear_equation(variable):
        evaluation = first_constant * variable + second_constant
        return evaluation
    return linear_equation

new_function = linear(2,3)
answer = new_function(5)
print(answer)