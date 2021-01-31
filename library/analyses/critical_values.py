from .equations.linear import linear
from .equations.quadratic import quadratic
from .equations.cubic import cubic
from .equations.hyperbolic import hyperbolic
from .equations.exponential import exponential
from .equations.logarithmic import logarithmic

def critical_values(equation_type, critical_points, coefficients):
    result = []
    if critical_points[0] == None:
        result = [None]
    else:
        for i in range(len(critical_points)):
            if equation_type == 'linear':
                lineq = linear(coefficients[0], coefficients[1])
                result.append(lineq(critical_points[i]))
            elif equation_type == 'quadratic':
                quadeq = quadratic(coefficients[0], coefficients[1], coefficients[2])
                result.append(quadeq(critical_points[i]))
            elif equation_type == 'cubic':
                cubeq = cubic(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
                result.append(cubeq(critical_points[i]))
            elif equation_type == 'hyperbolic':
                hypeq = hyperbolic(coefficients[0], coefficients[1])
                result.append(hypeq(critical_points[i]))
            elif equation_type == 'exponential':
                expeq = exponential(coefficients[0], coefficients[1])
                result.append(expeq(critical_points[i]))
            elif equation_type == 'logarithmic':
                logeq = logarithmic(coefficients[0], coefficients[1])
                result.append(logeq(critical_points[i]))
    return result