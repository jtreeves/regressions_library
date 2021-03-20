from library.vectors.unify import unify
from .intercepts import intercepts
from .extrema import extrema
from .inflections import inflections

def key_points(equation_type, coefficients, equation, first_derivative, second_derivative):
    intercepts_inputs = intercepts(equation_type, coefficients)
    extrema_inputs = extrema(equation_type, coefficients, first_derivative)
    maxima_inputs = extrema_inputs['maxima']
    minima_inputs = extrema_inputs['minima']
    inflections_inputs = inflections(equation_type, coefficients, second_derivative)
    intercepts_outputs = []
    maxima_outputs = []
    minima_outputs = []
    inflections_outputs = []
    intercepts_coordinates = []
    maxima_coordinates = []
    minima_coordinates = []
    inflections_coordinates = []
    if intercepts_inputs[0] == None:
        intercepts_coordinates = [None]
    else:
        for i in range(len(intercepts_inputs)):
            intercepts_outputs.append(0)
        intercepts_coordinates = unify(intercepts_inputs, intercepts_outputs)
    if maxima_inputs[0] == None:
        maxima_coordinates = [None]
    else:
        for i in range(len(maxima_inputs)):
            maxima_outputs.append(equation(maxima_inputs[i]))
        maxima_coordinates = unify(maxima_inputs, maxima_outputs)
    if minima_inputs[0] == None:
        minima_coordinates = [None]
    else:
        for i in range(len(minima_inputs)):
            minima_outputs.append(equation(minima_inputs[i]))
        minima_coordinates = unify(minima_inputs, minima_outputs)
    if inflections_inputs[0] == None:
        inflections_coordinates = [None]
    else:
        for i in range(len(inflections_inputs)):
            inflections_outputs.append(equation(inflections_inputs[i]))
        inflections_coordinates = unify(inflections_inputs, inflections_outputs)
    result = {
        'roots': intercepts_coordinates,
        'maxima': maxima_coordinates,
        'minima': minima_coordinates,
        'inflections': inflections_coordinates
    }
    return result