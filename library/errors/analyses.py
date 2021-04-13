def select_equations(string):
    choices = ['linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', 'sinusoidal']
    if string not in choices:
        raise ValueError("First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'")
    else:
        return "First argument is either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'"