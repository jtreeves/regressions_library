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
# {'constants': [-3.0, 33.0], 'evaluations': {'equation': <function linear.<locals>.linear_equation at 0x1036ae9d0>, 'derivative': <function linear.<locals>.first_derivative at 0x10877e820>, 'integral': <function linear.<locals>.linear_integral at 0x10877e940>}, 'points': {'roots': [[11.0, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 148.5, 'iqr': 82.5}, 'averages': {'range': {'average_value_derivative': -3.0, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': -3.0, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.5]}}, 'correlation': 1.0}

print(f'QUADRATIC MODEL LOW: {quadratic_model_low}')
# {'constants': [-2.0, 23.0, -11.0], 'evaluations': {'equation': <function quadratic.<locals>.quadratic_equation at 0x10877e8b0>, 'derivative': <function quadratic.<locals>.first_derivative at 0x10877e9d0>, 'integral': <function quadratic.<locals>.quadratic_integral at 0x10877eaf0>}, 'points': {'roots': [[0.5, 0], [11.0, 0]], 'maxima': [[5.75, 55.125]], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 373.50000000000006, 'iqr': 254.16666666666669}, 'averages': {'range': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 41.50000000000001, 'mean_values_integral': [3.139923372772363, 8.360076627227636]}, 'iqr': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 50.833333333333336, 'mean_values_integral': [4.285133680729421, 7.214866319270579]}}, 'correlation': 1.0}

print(f'CUBIC MODEL LOW: {cubic_model_low}')
# {'constants': [1.0, -15.0, 63.0, -7.0], 'evaluations': {'equation': <function cubic.<locals>.cubic_equation at 0x10877ea60>, 'derivative': <function cubic.<locals>.first_derivative at 0x10877eb80>, 'integral': <function cubic.<locals>.cubic_integral at 0x10877eca0>}, 'points': {'roots': [[0.11419220382428004, 0]], 'maxima': [[3.0, 74.0]], 'minima': [[7.0, 42.0]], 'inflections': [[5.0, 58.0]]}, 'accumulations': {'range': 560.25, 'iqr': 276.25}, 'averages': {'range': {'average_value_derivative': 9.0, 'mean_values_derivative': [2.3542486889354093, 7.645751311064591], 'average_value_integral': 62.25, 'mean_values_integral': [1.7287946059970638, 4.642010097525695, 8.62919529647724]}, 'iqr': {'average_value_derivative': -5.0, 'mean_values_derivative': [3.4724747683480537, 6.527525231651946], 'average_value_integral': 55.25, 'mean_values_integral': [5.230183005507413]}}, 'correlation': 1.0}

print(f'HYPERBOLIC MODEL LOW: {hyperbolic_model_low}')
# {'constants': [2519.999999999999, -0.9999999999995097], 'evaluations': {'equation': <function hyperbolic.<locals>.hyperbolic_equation at 0x11789fb80>, 'derivative': <function hyperbolic.<locals>.first_derivative at 0x11789fd30>, 'integral': <function hyperbolic.<locals>.hyperbolic_integral at 0x11789fdc0>}, 'points': {'roots': [[2520.0000000012346, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 5793.514434344997, 'iqr': 2466.6897175895506}, 'averages': {'range': {'average_value_derivative': -251.9999999999999, 'mean_values_derivative': [3.1622776601683795], 'average_value_integral': 643.7238260383331, 'mean_values_integral': [3.908650337129266]}, 'iqr': {'average_value_derivative': -104.99999999999996, 'mean_values_derivative': [4.898979485566356], 'average_value_integral': 493.3379435179101, 'mean_values_integral': [5.097727239116333]}}, 'correlation': 1.0}

print(f'EXPONENTIAL MODEL LOW: {exponential_model_low}')
# {'constants': [2.999999999999999, 2.0], 'evaluations': {'equation': <function exponential.<locals>.exponential_equation at 0x11789fca0>, 'derivative': <function exponential.<locals>.first_derivative at 0x11789fe50>, 'integral': <function exponential.<locals>.exponential_integral at 0x11789ff70>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 4423.3029953655605, 'iqr': 1073.3651104213884}, 'averages': {'range': {'average_value_derivative': 340.6666666666666, 'mean_values_derivative': [7.356020852440207], 'average_value_integral': 491.4781105961734, 'mean_values_integral': [7.356020852440207]}, 'iqr': {'average_value_derivative': 148.79999999999995, 'mean_values_derivative': [6.161034588444411], 'average_value_integral': 214.67302208427768, 'mean_values_integral': [6.161034588444411]}}, 'correlation': 1.0}

print(f'LOGARITHMIC MODEL LOW: {logarithmic_model_low}')
# {'constants': [3.0000161177167617, 1.9999718832129783], 'evaluations': {'equation': <function logarithmic.<locals>.logarithmic_equation at 0x11789fee0>, 'derivative': <function logarithmic.<locals>.first_derivative at 0x1178b2040>, 'integral': <function logarithmic.<locals>.logarithmic_integral at 0x1178b2160>}, 'points': {'roots': [[0.5134237698335792, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 60.07752580343081, 'iqr': 35.01908023521739}, 'averages': {'range': {'average_value_derivative': 0.7675324879329428, 'mean_values_derivative': [3.9086503371292665], 'average_value_integral': 6.675280644825645, 'mean_values_integral': [4.751345690108391]}, 'iqr': {'average_value_derivative': 0.5885007135526539, 'mean_values_derivative': [5.097727239116332], 'average_value_integral': 7.003816047043477, 'mean_values_integral': [5.301231189503074]}}, 'correlation': 0.9999999999212983}

print(f'LINEAR MODEL HIGH: {linear_model_high}')
# {'constants': [-2.999999999999999, 32.99999999999999], 'evaluations': {'equation': <function linear.<locals>.linear_equation at 0x1027ec9d0>, 'derivative': <function linear.<locals>.first_derivative at 0x11789f790>, 'integral': <function linear.<locals>.linear_integral at 0x11789f8b0>}, 'points': {'roots': [[11.000000000000002, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 148.5, 'iqr': 82.5}, 'averages': {'range': {'average_value_derivative': -2.999999999999999, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.499999999999999]}, 'iqr': {'average_value_derivative': -2.999999999999999, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.499999999999999]}}, 'correlation': 1.0}

print(f'QUADRATIC MODEL HIGH: {quadratic_model_high}')
# {'constants': [-2.000000000000003, 23.0000000000001, -11.000000000000238], 'evaluations': {'equation': <function quadratic.<locals>.quadratic_equation at 0x11789f820>, 'derivative': <function quadratic.<locals>.first_derivative at 0x11789f940>, 'integral': <function quadratic.<locals>.quadratic_integral at 0x11789fa60>}, 'points': {'roots': [[0.500000000000009, 0], [11.000000000000021, 0]], 'maxima': [[5.750000000000016, 55.12500000000023]], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 373.5000000000018, 'iqr': 254.1666666666677}, 'averages': {'range': {'average_value_derivative': 1.000000000000065, 'mean_values_derivative': [5.5], 'average_value_integral': 41.5000000000002, 'mean_values_integral': [3.139923372772378, 8.360076627227654]}, 'iqr': {'average_value_derivative': 1.0000000000000653, 'mean_values_derivative': [5.5], 'average_value_integral': 50.83333333333354, 'mean_values_integral': [4.2851336807294365, 7.2148663192705955]}}, 'correlation': 1.0}

print(f'CUBIC MODEL HIGH: {cubic_model_high}')
# {'constants': [1.0000000000000635, -15.00000000000084, 63.000000000002764, -7.000000000003915], 'evaluations': {'equation': <function cubic.<locals>.cubic_equation at 0x11789f9d0>, 'derivative': <function cubic.<locals>.first_derivative at 0x11789faf0>, 'integral': <function cubic.<locals>.cubic_integral at 0x11789fc10>}, 'points': {'roots': [[0.1141922038243403, 0]], 'maxima': [[2.999999999999953, 73.99999999999852]], 'minima': [[6.9999999999999725, 41.99999999999597]], 'inflections': [[4.999999999999963, 57.99999999999731]]}, 'accumulations': {'range': 560.2499999999806, 'iqr': 276.2499999999845}, 'averages': {'range': {'average_value_derivative': 9.000000000000561, 'mean_values_derivative': [2.3542486889353653, 7.6457513110645605], 'average_value_integral': 62.24999999999784, 'mean_values_integral': [1.7287946059970212, 4.642010097525637, 8.629195296477228]}, 'iqr': {'average_value_derivative': -5.000000000000322, 'mean_values_derivative': [3.4724747683480035, 6.5275252316519214], 'average_value_integral': 55.249999999996895, 'mean_values_integral': [5.230183005507392]}}, 'correlation': 1.0}

print(f'HYPERBOLIC MODEL HIGH: {hyperbolic_model_high}')
# {'constants': [2519.999999999999, -0.9999999999995097], 'evaluations': {'equation': <function hyperbolic.<locals>.hyperbolic_equation at 0x11789fb80>, 'derivative': <function hyperbolic.<locals>.first_derivative at 0x11789fd30>, 'integral': <function hyperbolic.<locals>.hyperbolic_integral at 0x11789fdc0>}, 'points': {'roots': [[2520.0000000012346, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 5793.514434344997, 'iqr': 2466.6897175895506}, 'averages': {'range': {'average_value_derivative': -251.9999999999999, 'mean_values_derivative': [3.1622776601683795], 'average_value_integral': 643.7238260383331, 'mean_values_integral': [3.908650337129266]}, 'iqr': {'average_value_derivative': -104.99999999999996, 'mean_values_derivative': [4.898979485566356], 'average_value_integral': 493.3379435179101, 'mean_values_integral': [5.097727239116333]}}, 'correlation': 1.0}

print(f'EXPONENTIAL MODEL HIGH: {exponential_model_high}')
# {'constants': [2.999999999999999, 2.0], 'evaluations': {'equation': <function exponential.<locals>.exponential_equation at 0x11789fca0>, 'derivative': <function exponential.<locals>.first_derivative at 0x11789fe50>, 'integral': <function exponential.<locals>.exponential_integral at 0x11789ff70>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 4423.3029953655605, 'iqr': 1073.3651104213884}, 'averages': {'range': {'average_value_derivative': 340.6666666666666, 'mean_values_derivative': [7.356020852440207], 'average_value_integral': 491.4781105961734, 'mean_values_integral': [7.356020852440207]}, 'iqr': {'average_value_derivative': 148.79999999999995, 'mean_values_derivative': [6.161034588444411], 'average_value_integral': 214.67302208427768, 'mean_values_integral': [6.161034588444411]}}, 'correlation': 1.0}

print(f'LOGARITHMIC MODEL HIGH: {logarithmic_model_high}')
# {'constants': [3.0000161177167617, 1.9999718832129783], 'evaluations': {'equation': <function logarithmic.<locals>.logarithmic_equation at 0x11789fee0>, 'derivative': <function logarithmic.<locals>.first_derivative at 0x1178b2040>, 'integral': <function logarithmic.<locals>.logarithmic_integral at 0x1178b2160>}, 'points': {'roots': [[0.5134237698335792, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 60.07752580343081, 'iqr': 35.01908023521739}, 'averages': {'range': {'average_value_derivative': 0.7675324879329428, 'mean_values_derivative': [3.9086503371292665], 'average_value_integral': 6.675280644825645, 'mean_values_integral': [4.751345690108391]}, 'iqr': {'average_value_derivative': 0.5885007135526539, 'mean_values_derivative': [5.097727239116332], 'average_value_integral': 7.003816047043477, 'mean_values_integral': [5.301231189503074]}}, 'correlation': 0.9999999999212983}