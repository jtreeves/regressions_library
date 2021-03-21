from library.models.linear import linear
from library.models.quadratic import quadratic
from library.models.cubic import cubic
from library.models.hyperbolic import hyperbolic
from library.models.exponential import exponential
from library.models.logarithmic import logarithmic

linear_set = [
    [1, 30],
    [2, 27],
    [3, 24],
    [4, 21],
    [5, 18],
    [6, 15],
    [7, 12],
    [8, 9],
    [9, 6],
    [10, 3]
]

quadratic_set = [
    [1, 10],
    [2, 27],
    [3, 40],
    [4, 49],
    [5, 54],
    [6, 55],
    [7, 52],
    [8, 45],
    [9, 34],
    [10, 19]
]

cubic_set = [
    [1, 42],
    [2, 67],
    [3, 74],
    [4, 69],
    [5, 58],
    [6, 47],
    [7, 42],
    [8, 49],
    [9, 74],
    [10, 123]
]

hyperbolic_set = [
    [1, 2519],
    [2, 1259],
    [3, 839],
    [4, 629],
    [5, 503],
    [6, 419],
    [7, 359],
    [8, 314],
    [9, 279],
    [10, 251]
]

exponential_set = [
    [1, 6],
    [2, 12],
    [3, 24],
    [4, 48],
    [5, 96],
    [6, 192],
    [7, 384],
    [8, 768],
    [9, 1536],
    [10, 3072]
]

logarithmic_set = [
    [1, 2],
    [2, 4.0794],
    [3, 5.2958],
    [4, 6.1589],
    [5, 6.8283],
    [6, 7.3753],
    [7, 7.8377],
    [8, 8.2383],
    [9, 8.5917],
    [10, 8.9078]
]

low_precision = 2
high_precision = 6

linear_model_low = linear(linear_set, low_precision)
quadratic_model_low = quadratic(quadratic_set, low_precision)
cubic_model_low = cubic(cubic_set, low_precision)
hyperbolic_model_low = hyperbolic(hyperbolic_set, low_precision)
exponential_model_low = exponential(exponential_set, low_precision)
logarithmic_model_low = logarithmic(logarithmic_set, low_precision)

linear_model_high = linear(linear_set, high_precision)
quadratic_model_high = quadratic(quadratic_set, high_precision)
cubic_model_high = cubic(cubic_set, high_precision)
hyperbolic_model_high = hyperbolic(hyperbolic_set, high_precision)
exponential_model_high = exponential(exponential_set, high_precision)
logarithmic_model_high = logarithmic(logarithmic_set, high_precision)

print(f'LINEAR MODEL LOW: {linear_model_low}')
# {'constants': [-3.0, 33.0], 'evaluations': {'equation': <function linear.<locals>.linear_equation at 0x10cec4ca0>, 'derivative': <function linear.<locals>.first_derivative at 0x10e37d9d0>, 'integral': <function linear.<locals>.linear_integral at 0x10e37daf0>}, 'points': {'roots': [[11.0, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 148.5, 'iqr': 82.5}, 'averages': {'range': {'average_value_derivative': -3.0, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': -3.0, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.5]}}, 'correlation': 1.0}

print(f'QUADRATIC MODEL LOW: {quadratic_model_low}')
# {'constants': [-2.0, 23.0, -11.0], 'evaluations': {'equation': <function quadratic.<locals>.quadratic_equation at 0x10e37da60>, 'derivative': <function quadratic.<locals>.first_derivative at 0x10e37db80>, 'integral': <function quadratic.<locals>.quadratic_integral at 0x10e37dca0>}, 'points': {'roots': [[0.5, 0], [11.0, 0]], 'maxima': [[5.75, 55.12]], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 373.5, 'iqr': 254.17}, 'averages': {'range': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 41.5, 'mean_values_integral': [3.14, 8.36]}, 'iqr': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 50.83, 'mean_values_integral': [4.28, 7.22]}}, 'correlation': 1.0}

print(f'CUBIC MODEL LOW: {cubic_model_low}')
# {'constants': [1.0, -15.0, 63.0, -7.0], 'evaluations': {'equation': <function cubic.<locals>.cubic_equation at 0x10e37dc10>, 'derivative': <function cubic.<locals>.first_derivative at 0x10e37dd30>, 'integral': <function cubic.<locals>.cubic_integral at 0x10e37de50>}, 'points': {'roots': [[0.11, 0]], 'maxima': [[3.0, 74.0]], 'minima': [[7.0, 42.0]], 'inflections': [[5.0, 58.0]]}, 'accumulations': {'range': 560.25, 'iqr': 276.25}, 'averages': {'range': {'average_value_derivative': 9.0, 'mean_values_derivative': [2.35, 7.65], 'average_value_integral': 62.25, 'mean_values_integral': [1.73, 4.64, 8.63]}, 'iqr': {'average_value_derivative': -5.0, 'mean_values_derivative': [3.47, 6.53], 'average_value_integral': 55.25, 'mean_values_integral': [5.23]}}, 'correlation': 1.0}

print(f'HYPERBOLIC MODEL LOW: {hyperbolic_model_low}')
# {'constants': [2520.0, -1.0], 'evaluations': {'equation': <function hyperbolic.<locals>.hyperbolic_equation at 0x10e37ddc0>, 'derivative': <function hyperbolic.<locals>.first_derivative at 0x10e37df70>, 'integral': <function hyperbolic.<locals>.hyperbolic_integral at 0x10e38b040>}, 'points': {'roots': [[2520.0, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 5793.51, 'iqr': 2466.69}, 'averages': {'range': {'average_value_derivative': -252.0, 'mean_values_derivative': [3.16], 'average_value_integral': 643.72, 'mean_values_integral': [3.91]}, 'iqr': {'average_value_derivative': -105.0, 'mean_values_derivative': [4.9], 'average_value_integral': 493.34, 'mean_values_integral': [5.1]}}, 'correlation': 1.0}

print(f'EXPONENTIAL MODEL LOW: {exponential_model_low}')
# {'constants': [3.0, 1.99], 'evaluations': {'equation': <function exponential.<locals>.exponential_equation at 0x11d137e50>, 'derivative': <function exponential.<locals>.first_derivative at 0x11d148040>, 'integral': <function exponential.<locals>.exponential_integral at 0x11d148160>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 4237.31, 'iqr': 1037.84}, 'averages': {'range': {'average_value_derivative': 323.98, 'mean_values_derivative': [7.35], 'average_value_integral': 470.81, 'mean_values_integral': [7.35]}, 'iqr': {'average_value_derivative': 142.83, 'mean_values_derivative': [6.16], 'average_value_integral': 207.57, 'mean_values_integral': [6.16]}}, 'correlation': 1.0}

print(f'LOGARITHMIC MODEL LOW: {logarithmic_model_low}')
# {'constants': [3.0, 2.0], 'evaluations': {'equation': <function logarithmic.<locals>.logarithmic_equation at 0x10e38b160>, 'derivative': <function logarithmic.<locals>.first_derivative at 0x10e38b280>, 'integral': <function logarithmic.<locals>.logarithmic_integral at 0x10e38b3a0>}, 'points': {'roots': [[0.51, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 60.08, 'iqr': 35.02}, 'averages': {'range': {'average_value_derivative': 0.77, 'mean_values_derivative': [3.9], 'average_value_integral': 6.68, 'mean_values_integral': [4.76]}, 'iqr': {'average_value_derivative': 0.59, 'mean_values_derivative': [5.08], 'average_value_integral': 7.0, 'mean_values_integral': [5.29]}}, 'correlation': 1.0}

print(f'LINEAR MODEL HIGH: {linear_model_high}')
# {'constants': [-3.0, 33.0], 'evaluations': {'equation': <function linear.<locals>.linear_equation at 0x10e38b310>, 'derivative': <function linear.<locals>.first_derivative at 0x10e38b430>, 'integral': <function linear.<locals>.linear_integral at 0x10e38b550>}, 'points': {'roots': [[11.0, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 148.5, 'iqr': 82.5}, 'averages': {'range': {'average_value_derivative': -3.0, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': -3.0, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.5]}}, 'correlation': 1.0}

print(f'QUADRATIC MODEL HIGH: {quadratic_model_high}')
# {'constants': [-2.0, 23.0, -11.0], 'evaluations': {'equation': <function quadratic.<locals>.quadratic_equation at 0x10e38b4c0>, 'derivative': <function quadratic.<locals>.first_derivative at 0x10e38b5e0>, 'integral': <function quadratic.<locals>.quadratic_integral at 0x10e38b700>}, 'points': {'roots': [[0.5, 0], [11.0, 0]], 'maxima': [[5.75, 55.125]], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 373.5, 'iqr': 254.166667}, 'averages': {'range': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 41.5, 'mean_values_integral': [3.139923, 8.360077]}, 'iqr': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 50.833333, 'mean_values_integral': [4.285134, 7.214866]}}, 'correlation': 1.0}

print(f'CUBIC MODEL HIGH: {cubic_model_high}')
# {'constants': [1.0, -15.0, 63.0, -7.0], 'evaluations': {'equation': <function cubic.<locals>.cubic_equation at 0x10e38b670>, 'derivative': <function cubic.<locals>.first_derivative at 0x10e38b790>, 'integral': <function cubic.<locals>.cubic_integral at 0x10e38b8b0>}, 'points': {'roots': [[0.114192, 0]], 'maxima': [[3.0, 74.0]], 'minima': [[7.0, 42.0]], 'inflections': [[5.0, 58.0]]}, 'accumulations': {'range': 560.25, 'iqr': 276.25}, 'averages': {'range': {'average_value_derivative': 9.0, 'mean_values_derivative': [2.354249, 7.645751], 'average_value_integral': 62.25, 'mean_values_integral': [1.728795, 4.64201, 8.629195]}, 'iqr': {'average_value_derivative': -5.0, 'mean_values_derivative': [3.472475, 6.527525], 'average_value_integral': 55.25, 'mean_values_integral': [5.230183]}}, 'correlation': 1.0}

print(f'HYPERBOLIC MODEL HIGH: {hyperbolic_model_high}')
# {'constants': [2520.0, -1.0], 'evaluations': {'equation': <function hyperbolic.<locals>.hyperbolic_equation at 0x10e38b820>, 'derivative': <function hyperbolic.<locals>.first_derivative at 0x10e38b9d0>, 'integral': <function hyperbolic.<locals>.hyperbolic_integral at 0x10e38ba60>}, 'points': {'roots': [[2520.0, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 5793.514434, 'iqr': 2466.689718}, 'averages': {'range': {'average_value_derivative': -252.0, 'mean_values_derivative': [3.162278], 'average_value_integral': 643.723826, 'mean_values_integral': [3.90865]}, 'iqr': {'average_value_derivative': -105.0, 'mean_values_derivative': [4.898979], 'average_value_integral': 493.337944, 'mean_values_integral': [5.097727]}}, 'correlation': 1.0}

print(f'EXPONENTIAL MODEL HIGH: {exponential_model_high}')
# {'constants': [2.999999, 2.0], 'evaluations': {'equation': <function exponential.<locals>.exponential_equation at 0x11d1488b0>, 'derivative': <function exponential.<locals>.first_derivative at 0x11d148a60>, 'integral': <function exponential.<locals>.exponential_integral at 0x11d148b80>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 4423.301521, 'iqr': 1073.364753}, 'averages': {'range': {'average_value_derivative': 340.666553, 'mean_values_derivative': [7.356021], 'average_value_integral': 491.477947, 'mean_values_integral': [7.356021]}, 'iqr': {'average_value_derivative': 148.79995, 'mean_values_derivative': [6.161035], 'average_value_integral': 214.672951, 'mean_values_integral': [6.161035]}}, 'correlation': 1.0}

print(f'LOGARITHMIC MODEL HIGH: {logarithmic_model_high}')
# {'constants': [3.000016, 1.999972], 'evaluations': {'equation': <function logarithmic.<locals>.logarithmic_equation at 0x10e38bb80>, 'derivative': <function logarithmic.<locals>.first_derivative at 0x10e38bca0>, 'integral': <function logarithmic.<locals>.logarithmic_integral at 0x10e38bdc0>}, 'points': {'roots': [[0.513424, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 60.077525, 'iqr': 35.01908}, 'averages': {'range': {'average_value_derivative': 0.767532, 'mean_values_derivative': [3.908653], 'average_value_integral': 6.675281, 'mean_values_integral': [4.751346]}, 'iqr': {'average_value_derivative': 0.588501, 'mean_values_derivative': [5.097725], 'average_value_integral': 7.003816, 'mean_values_integral': [5.301231]}}, 'correlation': 1.0}