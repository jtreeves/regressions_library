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

linear_model = linear(linear_set)
quadratic_model = quadratic(quadratic_set)
cubic_model = cubic(cubic_set)
hyperbolic_model = hyperbolic(hyperbolic_set)
exponential_model = exponential(exponential_set)
logarithmic_model = logarithmic(logarithmic_set)

print(f'LINEAR MODEL: {linear_model}')
# {'constants': [-2.999999999999999, 32.99999999999999], 'evaluations': {'equation': <function linear.<locals>.linear_equation at 0x10ebb99d0>, 'derivative': <function linear.<locals>.first_derivative at 0x10ff13790>, 'integral': <function linear.<locals>.linear_integral at 0x10ff138b0>}, 'points': {'roots': [[11.000000000000002, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 148.5, 'iqr': 94.87499999999999}, 'averages': {'range': {'average_value_derivative': -2.999999999999999, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.499999999999999]}, 'iqr': {'average_value_derivative': -2.9999999999999987, 'mean_values_derivative': ['All'], 'average_value_integral': 17.249999999999996, 'mean_values_integral': [5.25]}}, 'correlation': 1.0}

print(f'QUADRATIC MODEL: {quadratic_model}')
# {'constants': [-2.000000000000003, 23.0000000000001, -11.000000000000238], 'evaluations': {'equation': <function quadratic.<locals>.quadratic_equation at 0x10ff13820>, 'derivative': <function quadratic.<locals>.first_derivative at 0x10ff13940>, 'integral': <function quadratic.<locals>.quadratic_integral at 0x10ff13a60>}, 'points': {'roots': [[0.500000000000009, 0], [11.000000000000021, 0]], 'maxima': [[5.750000000000016, 55.12500000000023]], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 373.5000000000018, 'iqr': 272.7083333333344}, 'averages': {'range': {'average_value_derivative': 1.000000000000065, 'mean_values_derivative': [5.5], 'average_value_integral': 41.5000000000002, 'mean_values_integral': [3.139923372772378, 8.360076627227654]}, 'iqr': {'average_value_derivative': 2.000000000000067, 'mean_values_derivative': [5.25], 'average_value_integral': 49.58333333333353, 'mean_values_integral': [4.085417970380164, 7.414582029619868]}}, 'correlation': 1.0}

print(f'CUBIC MODEL: {cubic_model}')
# {'constants': [1.0000000000000635, -15.00000000000084, 63.000000000002764, -7.000000000003915], 'evaluations': {'equation': <function cubic.<locals>.cubic_equation at 0x10ff139d0>, 'derivative': <function cubic.<locals>.first_derivative at 0x10ff13af0>, 'integral': <function cubic.<locals>.cubic_integral at 0x10ff13c10>}, 'points': {'roots': [[0.1141922038243403, 0]], 'maxima': [[2.999999999999953, 73.99999999999852]], 'minima': [[6.9999999999999725, 41.99999999999597]], 'inflections': [[4.999999999999963, 57.99999999999731]]}, 'accumulations': {'range': 560.2499999999806, 'iqr': 312.9843749999838}, 'averages': {'range': {'average_value_derivative': 9.000000000000561, 'mean_values_derivative': [2.3542486889353653, 7.6457513110645605], 'average_value_integral': 62.24999999999784, 'mean_values_integral': [1.7287946059970212, 4.642010097525637, 8.629195296477228]}, 'iqr': {'average_value_derivative': -4.250000000000324, 'mean_values_derivative': [3.3927248731677966, 6.607275126832128], 'average_value_integral': 56.90624999999705, 'mean_values_integral': [5.091209064728017]}}, 'correlation': 1.0}

print(f'HYPERBOLIC MODEL: {hyperbolic_model}')
# {'constants': [2519.999999999999, -0.9999999999995097], 'evaluations': {'equation': <function hyperbolic.<locals>.hyperbolic_equation at 0x10ff13b80>, 'derivative': <function hyperbolic.<locals>.first_derivative at 0x10ff13d30>, 'integral': <function hyperbolic.<locals>.hyperbolic_integral at 0x10ff13dc0>}, 'points': {'roots': [[2520.0000000012346, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 5793.514434344997, 'iqr': 2925.640040710316}, 'averages': {'range': {'average_value_derivative': -251.9999999999999, 'mean_values_derivative': [3.1622776601683795], 'average_value_integral': 643.7238260383331, 'mean_values_integral': [3.908650337129266]}, 'iqr': {'average_value_derivative': -125.99999999999996, 'mean_values_derivative': [4.47213595499958], 'average_value_integral': 531.9345528564211, 'mean_values_integral': [4.728535589395194]}}, 'correlation': 1.0}

print(f'EXPONENTIAL MODEL: {exponential_model}')
# {'constants': [2.999999999999999, 2.0], 'evaluations': {'equation': <function exponential.<locals>.exponential_equation at 0x10ff13ca0>, 'derivative': <function exponential.<locals>.first_derivative at 0x10ff13e50>, 'integral': <function exponential.<locals>.exponential_integral at 0x10ff13f70>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 4423.3029953655605, 'iqr': 1083.5064446844005}, 'averages': {'range': {'average_value_derivative': 340.6666666666666, 'mean_values_derivative': [7.356020852440207], 'average_value_integral': 491.4781105961734, 'mean_values_integral': [7.356020852440207]}, 'iqr': {'average_value_derivative': 136.5508067730041, 'mean_values_derivative': [6.037097899894957], 'average_value_integral': 197.0011717608001, 'mean_values_integral': [6.037097899894957]}}, 'correlation': 1.0}

print(f'LOGARITHMIC MODEL: {logarithmic_model}')
# {'constants': [3.0000161177167617, 1.9999718832129783], 'evaluations': {'equation': <function logarithmic.<locals>.logarithmic_equation at 0x10ff13ee0>, 'derivative': <function logarithmic.<locals>.first_derivative at 0x10ff2a040>, 'integral': <function logarithmic.<locals>.logarithmic_integral at 0x10ff2a160>}, 'points': {'roots': [[0.5134237698335792, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 60.07752580343081, 'iqr': 37.5344044270012}, 'averages': {'range': {'average_value_derivative': 0.7675324879329428, 'mean_values_derivative': [3.9086503371292665], 'average_value_integral': 6.675280644825645, 'mean_values_integral': [4.751345690108391]}, 'iqr': {'average_value_derivative': 0.6344493048640629, 'mean_values_derivative': [4.728535589395192], 'average_value_integral': 6.824437168545672, 'mean_values_integral': [4.9935468818287525]}}, 'correlation': 0.9999999999212983}