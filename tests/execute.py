import unittest

from library.execute import run_all

agnostic_set = [
    [1, 32],
    [2, 25],
    [3, 14],
    [4, 23],
    [5, 39],
    [6, 45],
    [7, 42],
    [8, 49],
    [9, 36],
    [10, 33]
]

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

logistic_set = [
    [1, 0.0000122],
    [2, 0.000247],
    [3, 0.004945],
    [4, 0.094852],
    [5, 1.0],
    [6, 1.905148],
    [7, 1.995055],
    [8, 1.999753],
    [9, 1.999988],
    [10, 1.999999],
]

sinusoidal_set = [
    [1, 3], 
    [2, 8], 
    [3, 3], 
    [4, -2], 
    [5, 3], 
    [6, 8], 
    [7, 3], 
    [8, -2], 
    [9, 3], 
    [10, 8]
]

precision = 4

agnostic_models = run_all(agnostic_set, precision)
print(f"AGNOSTIC -> SINUSOIDAL: {agnostic_models['models']['sinusoidal']}")
# {'constants': [14.0875, 0.7119, -3.7531, 34.2915], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d243040>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d2431f0>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d243280>}, 'points': {'roots': [None], 'maxima': [[-1.5466, 48.379], [7.2791, 48.379], [16.1049, 48.379], ['-1.5466 + 8.8258k', 48.379]], 'minima': [[2.8663, 20.204], [11.692, 20.204], ['2.8663 + 8.8258k', 20.204]], 'inflections': [[-3.7531, 34.291], [0.6598, 34.2917], [5.0727, 34.2917], [9.4856, 34.291], [13.8984, 34.2913], ['-3.7531 + 4.4129k', 34.291]]}, 'accumulations': {'range': 307.8889, 'iqr': 183.0544}, 'averages': {'range': {'average_value_derivative': -0.1852, 'mean_values_derivative': [7.2532, 7.3051, '-1.5207 + 8.8257k', '-1.5726 + 8.8257k'], 'average_value_integral': 34.2099, 'mean_values_integral': [5.0645, 9.4937, '-3.7612 + 8.8257k', '0.668 + 8.8257k']}, 'iqr': {'average_value_derivative': 5.2593, 'mean_values_derivative': [6.5037, '-2.322 + 8.8257k', '-0.7712 + 8.8257k'], 'average_value_integral': 36.6109, 'mean_values_integral': [5.305, '-3.5207 + 8.8257k', '0.4275 + 8.8257k']}}, 'correlation': 0.9264}

class TestAgnosticModels(unittest.TestCase):
    def test_agnostic_models_linear_constants(self):
        self.assertEqual(agnostic_models['models']['linear']['constants'], [1.9636, 23.0])
    
    def test_agnostic_models_linear_points(self):
        self.assertEqual(agnostic_models['models']['linear']['points'], {'roots': [[-11.7132, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_agnostic_models_linear_accumulations(self):
        self.assertEqual(agnostic_models['models']['linear']['accumulations'], {'range': 304.1982, 'iqr': 168.999})
    
    def test_agnostic_models_linear_averages(self):
        self.assertEqual(agnostic_models['models']['linear']['averages'], {'range': {'average_value_derivative': 1.9636, 'mean_values_derivative': ['All'], 'average_value_integral': 33.7998, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': 1.9636, 'mean_values_derivative': ['All'], 'average_value_integral': 33.7998, 'mean_values_integral': [5.5]}})
    
    def test_agnostic_models_linear_correlation(self):
        self.assertEqual(agnostic_models['models']['linear']['correlation'], 0.5516)
    
    def test_agnostic_models_quadratic_constants(self):
        self.assertEqual(agnostic_models['models']['quadratic']['constants'], [-0.3106, 5.3803, 16.1667])
    
    def test_agnostic_models_quadratic_points(self):
        self.assertEqual(agnostic_models['models']['quadratic']['points'], {'roots': [[-2.6112, 0], [19.9335, 0]], 'maxima': [[8.6611, 39.4665]], 'minima': [None], 'inflections': [None]})
    
    def test_agnostic_models_quadratic_accumulations(self):
        self.assertEqual(agnostic_models['models']['quadratic']['accumulations'], {'range': 308.3953, 'iqr': 178.5781})
    
    def test_agnostic_models_quadratic_averages(self):
        self.assertEqual(agnostic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 1.9637, 'mean_values_derivative': [5.5], 'average_value_integral': 34.2661, 'mean_values_integral': [4.5693]}, 'iqr': {'average_value_derivative': 1.9637, 'mean_values_derivative': [5.5], 'average_value_integral': 35.7156, 'mean_values_integral': [5.1861]}})
    
    def test_agnostic_models_quadratic_correlation(self):
        self.assertEqual(agnostic_models['models']['quadratic']['correlation'], 0.5941)
    
    def test_agnostic_models_cubic_constants(self):
        self.assertEqual(agnostic_models['models']['cubic']['constants'], [-0.3881, 6.0932, -24.155, 49.4667])
    
    def test_agnostic_models_cubic_points(self):
        self.assertEqual(agnostic_models['models']['cubic']['points'], {'roots': [[11.1402, 0]], 'maxima': [[7.8105, 47.5947]], 'minima': [[2.6562, 21.0229]], 'inflections': [[5.2334, 34.3091]]})
    
    def test_agnostic_models_cubic_accumulations(self):
        self.assertEqual(agnostic_models['models']['cubic']['accumulations'], {'range': 308.4104, 'iqr': 178.583})
    
    def test_agnostic_models_cubic_averages(self):
        self.assertEqual(agnostic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': -0.2089, 'mean_values_derivative': [2.6216, 7.8451], 'average_value_integral': 34.2678, 'mean_values_integral': [5.2281, 9.6998]}, 'iqr': {'average_value_derivative': 5.2245, 'mean_values_derivative': [3.7656, 6.7012], 'average_value_integral': 35.7166, 'mean_values_integral': [5.4157]}})
    
    def test_agnostic_models_cubic_correlation(self):
        self.assertEqual(agnostic_models['models']['cubic']['correlation'], 0.8933)
    
    def test_agnostic_models_hyperbolic_constants(self):
        self.assertEqual(agnostic_models['models']['hyperbolic']['constants'], [-13.5246, 37.7613])
    
    def test_agnostic_models_hyperbolic_points(self):
        self.assertEqual(agnostic_models['models']['hyperbolic']['points'], {'roots': [[0.3582, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_agnostic_models_hyperbolic_accumulations(self):
        self.assertEqual(agnostic_models['models']['hyperbolic']['accumulations'], {'range': 308.7102, 'iqr': 175.5412})
    
    def test_agnostic_models_hyperbolic_averages(self):
        self.assertEqual(agnostic_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 1.3525, 'mean_values_derivative': [3.1622], 'average_value_integral': 34.3011, 'mean_values_integral': [3.9086]}, 'iqr': {'average_value_derivative': 0.5635, 'mean_values_derivative': [4.8991], 'average_value_integral': 35.1082, 'mean_values_integral': [5.0977]}})
    
    def test_agnostic_models_hyperbolic_correlation(self):
        self.assertEqual(agnostic_models['models']['hyperbolic']['correlation'], 0.3479)
    
    def test_agnostic_models_exponential_constants(self):
        self.assertEqual(agnostic_models['models']['exponential']['constants'], [22.1049, 1.0692])
    
    def test_agnostic_models_exponential_points(self):
        self.assertEqual(agnostic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_agnostic_models_exponential_accumulations(self):
        self.assertEqual(agnostic_models['models']['exponential']['accumulations'], {'range': 291.8084, 'iqr': 160.4376})
    
    def test_agnostic_models_exponential_averages(self):
        self.assertEqual(agnostic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 2.1695, 'mean_values_derivative': [5.7254], 'average_value_integral': 32.4232, 'mean_values_integral': [5.7252]}, 'iqr': {'average_value_derivative': 2.147, 'mean_values_derivative': [5.5696], 'average_value_integral': 32.0875, 'mean_values_integral': [5.5696]}})
    
    def test_agnostic_models_exponential_correlation(self):
        self.assertEqual(agnostic_models['models']['exponential']['correlation'], 0.5069)
    
    def test_agnostic_models_logarithmic_constants(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['constants'], [7.4791, 22.5032])
    
    def test_agnostic_models_logarithmic_points(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['points'], {'roots': [[0.0494, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_agnostic_models_logarithmic_accumulations(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['accumulations'], {'range': 307.4295, 'iqr': 174.8894})
    
    def test_agnostic_models_logarithmic_averages(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 1.9135, 'mean_values_derivative': [3.9086], 'average_value_integral': 34.1588, 'mean_values_integral': [4.7513]}, 'iqr': {'average_value_derivative': 1.4671, 'mean_values_derivative': [5.0979], 'average_value_integral': 34.9779, 'mean_values_integral': [5.3012]}})
    
    def test_agnostic_models_logarithmic_correlation(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['correlation'], 0.5086)
    
    def test_agnostic_models_logistic_constants(self):
        self.assertEqual(agnostic_models['models']['logistic']['constants'], [43.983, 0.3076, 0.9746])
    
    def test_agnostic_models_logistic_points(self):
        self.assertEqual(agnostic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[0.9746, 21.9914]]})
    
    def test_agnostic_models_logistic_accumulations(self):
        self.assertEqual(agnostic_models['models']['logistic']['accumulations'], {'range': 305.924, 'iqr': 174.1038})
    
    def test_agnostic_models_logistic_averages(self):
        self.assertEqual(agnostic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 2.1474, 'mean_values_derivative': [5.5251], 'average_value_integral': 33.9916, 'mean_values_integral': [4.9555]}, 'iqr': {'average_value_derivative': 2.1621, 'mean_values_derivative': [5.4884], 'average_value_integral': 34.8208, 'mean_values_integral': [5.3155]}})
    
    def test_agnostic_models_logistic_correlation(self):
        self.assertEqual(agnostic_models['models']['logistic']['correlation'], 0.5875)
    
    def test_agnostic_statistics(self):
        self.assertEqual(agnostic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_agnostic_optimal(self):
        self.assertEqual(agnostic_models['optimal']['option'], 'sinusoidal')

linear_models = run_all(linear_set, precision)
print(f"LINEAR -> SINUSOIDAL: {linear_models['models']['sinusoidal']}")
# {'constants': [3.6953, 1.8762, 3.8255, 16.5], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d2520d0>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d2524c0>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d252550>}, 'points': {'roots': [None], 'maxima': [[4.6627, 20.1953], [8.0117, 20.1953], [11.3607, 20.1953], ['4.6627 + 3.349k', 20.1953]], 'minima': [[6.3372, 12.8047], [9.6862, 12.8047], ['6.3372 + 3.349k', 12.8047]], 'inflections': [[3.8255, 16.5], [5.5, 16.4999], [7.1745, 16.5002], [8.849, 16.4998], [10.5235, 16.5003], ['3.8255 + 1.6745k', 16.5]]}, 'accumulations': {'range': 148.4999, 'iqr': 82.5001}, 'averages': {'range': {'average_value_derivative': -0.6829, 'mean_values_derivative': [4.6102, 4.7153, 7.9591, 8.0643, '4.7153 + 3.349k', '4.6102 + 3.349k'], 'average_value_integral': 16.5, 'mean_values_integral': [3.8255, 5.5, 7.1745, 8.849, '3.8255 + 3.349k', '5.5 + 3.349k']}, 'iqr': {'average_value_derivative': 1.4778, 'mean_values_derivative': [4.5483, 4.7772, 7.8972, '4.5483 + 3.349k', '4.7772 + 3.349k'], 'average_value_integral': 16.5, 'mean_values_integral': [3.8255, 5.5, 7.1745, '3.8255 + 3.349k', '5.5 + 3.349k']}}, 'correlation': 0.3046}

class TestLinearModels(unittest.TestCase):
    def test_linear_models_linear_constants(self):
        self.assertEqual(linear_models['models']['linear']['constants'], [-3.0, 33.0])
    
    def test_linear_models_linear_points(self):
        self.assertEqual(linear_models['models']['linear']['points'], {'roots': [[11.0, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_linear_accumulations(self):
        self.assertEqual(linear_models['models']['linear']['accumulations'], {'range': 148.5, 'iqr': 82.5})
    
    def test_linear_models_linear_averages(self):
        self.assertEqual(linear_models['models']['linear']['averages'], {'range': {'average_value_derivative': -3.0, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': -3.0, 'mean_values_derivative': ['All'], 'average_value_integral': 16.5, 'mean_values_integral': [5.5]}})
    
    def test_linear_models_linear_correlation(self):
        self.assertEqual(linear_models['models']['linear']['correlation'], 1.0)
    
    def test_linear_models_quadratic_constants(self):
        self.assertEqual(linear_models['models']['quadratic']['constants'], [0.0001, -3.0, 33.0])
    
    def test_linear_models_quadratic_points(self):
        self.assertEqual(linear_models['models']['quadratic']['points'], {'roots': [[11.004, 0], [29988.996, 0]], 'maxima': [None], 'minima': [[15000.0, -22467.0]], 'inflections': [None]})
    
    def test_linear_models_quadratic_accumulations(self):
        self.assertEqual(linear_models['models']['quadratic']['accumulations'], {'range': 148.5333, 'iqr': 82.5162})
    
    def test_linear_models_quadratic_averages(self):
        self.assertEqual(linear_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': -2.9989, 'mean_values_derivative': [5.5], 'average_value_integral': 16.5037, 'mean_values_integral': [5.4998]}, 'iqr': {'average_value_derivative': -2.9989, 'mean_values_derivative': [5.5], 'average_value_integral': 16.5032, 'mean_values_integral': [5.4999]}})
    
    def test_linear_models_quadratic_correlation(self):
        self.assertEqual(linear_models['models']['quadratic']['correlation'], 1.0)
    
    def test_linear_models_cubic_constants(self):
        self.assertEqual(linear_models['models']['cubic']['constants'], [0.0001, -0.0001, -3.0, 33.0])
    
    def test_linear_models_cubic_points(self):
        self.assertEqual(linear_models['models']['cubic']['points'], {'roots': [[-177.978, 0], [11.0408, 0], [167.9372, 0]], 'maxima': [[-99.6672, 232.0033]], 'minima': [[100.3339, -168.0033]], 'inflections': [[0.3333, 32.0001]]})
    
    def test_linear_models_cubic_accumulations(self):
        self.assertEqual(linear_models['models']['cubic']['accumulations'], {'range': 148.7167, 'iqr': 82.5842})
    
    def test_linear_models_cubic_averages(self):
        self.assertEqual(linear_models['models']['cubic']['averages'], {'range': {'average_value_derivative': -2.99, 'mean_values_derivative': [6.1165], 'average_value_integral': 16.5241, 'mean_values_integral': [5.4965]}, 'iqr': {'average_value_derivative': -2.9914, 'mean_values_derivative': [5.6978], 'average_value_integral': 16.5168, 'mean_values_integral': [5.4989]}})
    
    def test_linear_models_cubic_correlation(self):
        self.assertEqual(linear_models['models']['cubic']['correlation'], 1.0)
    
    def test_linear_models_hyperbolic_constants(self):
        self.assertEqual(linear_models['models']['hyperbolic']['constants'], [26.49, 8.7412])
    
    def test_linear_models_hyperbolic_points(self):
        self.assertEqual(linear_models['models']['hyperbolic']['points'], {'roots': [[-3.0305, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_hyperbolic_accumulations(self):
        self.assertEqual(linear_models['models']['hyperbolic']['accumulations'], {'range': 139.6663, 'iqr': 69.6882})
    
    def test_linear_models_hyperbolic_averages(self):
        self.assertEqual(linear_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': -2.649, 'mean_values_derivative': [3.1623], 'average_value_integral': 15.5185, 'mean_values_integral': [3.9086]}, 'iqr': {'average_value_derivative': -1.1037, 'mean_values_derivative': [4.8991], 'average_value_integral': 13.9376, 'mean_values_integral': [5.0978]}})
    
    def test_linear_models_hyperbolic_correlation(self):
        self.assertEqual(linear_models['models']['hyperbolic']['correlation'], 0.8086)
    
    def test_linear_models_exponential_constants(self):
        self.assertEqual(linear_models['models']['exponential']['constants'], [48.2454, 0.7942])
    
    def test_linear_models_exponential_points(self):
        self.assertEqual(linear_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_exponential_accumulations(self):
        self.assertEqual(linear_models['models']['exponential']['accumulations'], {'range': 145.3856, 'iqr': 71.7462})
    
    def test_linear_models_exponential_averages(self):
        self.assertEqual(linear_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -3.7222, 'mean_values_derivative': [4.7484], 'average_value_integral': 16.154, 'mean_values_integral': [4.7484]}, 'iqr': {'average_value_derivative': -3.3064, 'mean_values_derivative': [5.2625], 'average_value_integral': 14.3492, 'mean_values_integral': [5.2626]}})
    
    def test_linear_models_exponential_correlation(self):
        self.assertEqual(linear_models['models']['exponential']['correlation'], 0.9222)
    
    def test_linear_models_logarithmic_constants(self):
        self.assertEqual(linear_models['models']['logarithmic']['constants'], [-11.7921, 34.3113])
    
    def test_linear_models_logarithmic_points(self):
        self.assertEqual(linear_models['models']['logarithmic']['points'], {'roots': [[18.351, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_logarithmic_accumulations(self):
        self.assertEqual(linear_models['models']['logarithmic']['accumulations'], {'range': 143.4075, 'iqr': 73.214})
    
    def test_linear_models_logarithmic_averages(self):
        self.assertEqual(linear_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': -3.0169, 'mean_values_derivative': [3.9087], 'average_value_integral': 15.9342, 'mean_values_integral': [4.7513]}, 'iqr': {'average_value_derivative': -2.3132, 'mean_values_derivative': [5.0977], 'average_value_integral': 14.6428, 'mean_values_integral': [5.3012]}})
    
    def test_linear_models_logarithmic_correlation(self):
        self.assertEqual(linear_models['models']['logarithmic']['correlation'], 0.9517)
    
    def test_linear_models_logistic_constants(self):
        self.assertEqual(linear_models['models']['logistic']['constants'], [34.8519, -0.402, 5.1708])
    
    def test_linear_models_logistic_points(self):
        self.assertEqual(linear_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[5.1708, 17.4261]]})
    
    def test_linear_models_logistic_accumulations(self):
        self.assertEqual(linear_models['models']['logistic']['accumulations'], {'range': 148.5979, 'iqr': 81.8126})
    
    def test_linear_models_logistic_averages(self):
        self.assertEqual(linear_models['models']['logistic']['averages'], {'range': {'average_value_derivative': -2.7762, 'mean_values_derivative': [2.7261, 7.6158], 'average_value_integral': 16.5109, 'mean_values_integral': [5.4324]}, 'iqr': {'average_value_derivative': -3.2234, 'mean_values_derivative': [3.7279, 6.614], 'average_value_integral': 16.3625, 'mean_values_integral': [5.4749]}})
    
    def test_linear_models_logistic_correlation(self):
        self.assertEqual(linear_models['models']['logistic']['correlation'], 0.9974)
    
    def test_linear_statistics(self):
        self.assertEqual(linear_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_linear_optimal(self):
        self.assertEqual(linear_models['optimal']['option'], 'linear')

quadratic_models = run_all(quadratic_set, precision)
print(f"QUADRATIC -> SINUSOIDAL: {quadratic_models['models']['sinusoidal']}")
# {'constants': [-45.0, 0.3267, -8.6568, 10.9862], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d2593a0>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d259790>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d259820>}, 'points': {'roots': [[-7.9018, 0], [0.2055, 0], [11.3328, 0], [19.4401, 0], [30.5675, 0], [38.6748, 0], ['-7.9018 + 19.2346k', 0], ['0.2055 + 19.2346k', 0]], 'maxima': [[5.7691, 55.9862], [25.0038, 55.9862], ['5.7691 + 19.2346k', 55.9862]], 'minima': [[-3.8482, -34.0138], [15.3865, -34.0138], [34.6211, -34.0138], ['-3.8482 + 19.2346k', -34.0138]], 'inflections': [[-8.6568, 10.9857], [0.9605, 10.9865], [10.5778, 10.9864], [20.1951, 10.9858], [29.8125, 10.9856], ['-8.6568 + 9.6173k', 10.9857]]}, 'accumulations': {'range': 371.9341, 'iqr': 254.9671}, 'averages': {'range': {'average_value_derivative': 0.8736, 'mean_values_derivative': [None], 'average_value_integral': 41.326, 'mean_values_integral': [3.2255, 8.3127, '-10.9219 + 19.2346k', '3.2255 + 19.2346k']}, 'iqr': {'average_value_derivative': 1.152, 'mean_values_derivative': [None], 'average_value_integral': 50.9934, 'mean_values_integral': [4.3134, 7.2249, '-12.0097 + 19.2346k', '4.3134 + 19.2346k']}}, 'correlation': 0.9983}

class TestQuadraticModels(unittest.TestCase):
    def test_quadratic_models_linear_constants(self):
        self.assertEqual(quadratic_models['models']['linear']['constants'], [1.0, 33.0])
    
    def test_quadratic_models_linear_points(self):
        self.assertEqual(quadratic_models['models']['linear']['points'], {'roots': [[-33.0, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_models_linear_accumulations(self):
        self.assertEqual(quadratic_models['models']['linear']['accumulations'], {'range': 346.5, 'iqr': 192.5})
    
    def test_quadratic_models_linear_averages(self):
        self.assertEqual(quadratic_models['models']['linear']['averages'], {'range': {'average_value_derivative': 1.0, 'mean_values_derivative': ['All'], 'average_value_integral': 38.5, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': 1.0, 'mean_values_derivative': ['All'], 'average_value_integral': 38.5, 'mean_values_integral': [5.5]}})
    
    def test_quadratic_models_linear_correlation(self):
        self.assertEqual(quadratic_models['models']['linear']['correlation'], 0.1939)
    
    def test_quadratic_models_quadratic_constants(self):
        self.assertEqual(quadratic_models['models']['quadratic']['constants'], [-2.0, 23.0, -11.0])
    
    def test_quadratic_models_quadratic_points(self):
        self.assertEqual(quadratic_models['models']['quadratic']['points'], {'roots': [[0.5, 0], [11.0, 0]], 'maxima': [[5.75, 55.125]], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_models_quadratic_accumulations(self):
        self.assertEqual(quadratic_models['models']['quadratic']['accumulations'], {'range': 373.5, 'iqr': 254.1667})
    
    def test_quadratic_models_quadratic_averages(self):
        self.assertEqual(quadratic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 41.5, 'mean_values_integral': [3.1399, 8.3601]}, 'iqr': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 50.8333, 'mean_values_integral': [4.2851, 7.2149]}})
    
    def test_quadratic_models_quadratic_correlation(self):
        self.assertEqual(quadratic_models['models']['quadratic']['correlation'], 1.0)
    
    def test_quadratic_models_cubic_constants(self):
        self.assertEqual(quadratic_models['models']['cubic']['constants'], [0.0001, -2.0, 23.0, -11.0])
    
    def test_quadratic_models_cubic_points(self):
        self.assertEqual(quadratic_models['models']['cubic']['points'], {'roots': [[0.5, 0], [11.0063, 0], [19988.4937, 0]], 'maxima': [[5.7525, 55.144]], 'minima': [[13327.5809, -118211928.9959]], 'inflections': [[6666.6667, -59105937.3696]]})
    
    def test_quadratic_models_cubic_accumulations(self):
        self.assertEqual(quadratic_models['models']['cubic']['accumulations'], {'range': 373.75, 'iqr': 254.267})
    
    def test_quadratic_models_cubic_averages(self):
        self.assertEqual(quadratic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 1.0111, 'mean_values_derivative': [5.4995], 'average_value_integral': 41.5278, 'mean_values_integral': [3.1423, 8.363]}, 'iqr': {'average_value_derivative': 1.0097, 'mean_values_derivative': [5.4998], 'average_value_integral': 50.8534, 'mean_values_integral': [4.2872, 7.2179]}})
    
    def test_quadratic_models_cubic_correlation(self):
        self.assertEqual(quadratic_models['models']['cubic']['correlation'], 1.0)
    
    def test_quadratic_models_hyperbolic_constants(self):
        self.assertEqual(quadratic_models['models']['hyperbolic']['constants'], [-36.1101, 49.0765])
    
    def test_quadratic_models_hyperbolic_points(self):
        self.assertEqual(quadratic_models['models']['hyperbolic']['points'], {'roots': [[0.7358, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_models_hyperbolic_accumulations(self):
        self.assertEqual(quadratic_models['models']['hyperbolic']['accumulations'], {'range': 358.5419, 'iqr': 209.9647})
    
    def test_quadratic_models_hyperbolic_averages(self):
        self.assertEqual(quadratic_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 3.611, 'mean_values_derivative': [3.1623], 'average_value_integral': 39.838, 'mean_values_integral': [3.9087]}, 'iqr': {'average_value_derivative': 1.5046, 'mean_values_derivative': [4.899], 'average_value_integral': 41.9929, 'mean_values_integral': [5.0977]}})
    
    def test_quadratic_models_hyperbolic_correlation(self):
        self.assertEqual(quadratic_models['models']['hyperbolic']['correlation'], 0.6412)
    
    def test_quadratic_models_exponential_constants(self):
        self.assertEqual(quadratic_models['models']['exponential']['constants'], [26.2561, 1.0509])
    
    def test_quadratic_models_exponential_points(self):
        self.assertEqual(quadratic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_models_exponential_accumulations(self):
        self.assertEqual(quadratic_models['models']['exponential']['accumulations'], {'range': 313.0885, 'iqr': 172.9428})
    
    def test_quadratic_models_exponential_averages(self):
        self.assertEqual(quadratic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 1.7271, 'mean_values_derivative': [5.6673], 'average_value_integral': 34.7876, 'mean_values_integral': [5.6673]}, 'iqr': {'average_value_derivative': 1.7172, 'mean_values_derivative': [5.5515], 'average_value_integral': 34.5886, 'mean_values_integral': [5.5517]}})
    
    def test_quadratic_models_exponential_correlation(self):
        self.assertEqual(quadratic_models['models']['exponential']['correlation'], 0.0)
    
    def test_quadratic_models_logarithmic_constants(self):
        self.assertEqual(quadratic_models['models']['logarithmic']['constants'], [9.8723, 23.5885])
    
    def test_quadratic_models_logarithmic_points(self):
        self.assertEqual(quadratic_models['models']['logarithmic']['points'], {'roots': [[0.0917, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_models_logarithmic_accumulations(self):
        self.assertEqual(quadratic_models['models']['logarithmic']['accumulations'], {'range': 350.7639, 'iqr': 200.2745})
    
    def test_quadratic_models_logarithmic_averages(self):
        self.assertEqual(quadratic_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 2.5258, 'mean_values_derivative': [3.9086], 'average_value_integral': 38.9738, 'mean_values_integral': [4.7514]}, 'iqr': {'average_value_derivative': 1.9366, 'mean_values_derivative': [5.0977], 'average_value_integral': 40.0549, 'mean_values_integral': [5.3012]}})
    
    def test_quadratic_models_logarithmic_correlation(self):
        self.assertEqual(quadratic_models['models']['logarithmic']['correlation'], 0.4634)
    
    def test_quadratic_models_logistic_constants(self):
        self.assertEqual(quadratic_models['models']['logistic']['constants'], [43.9519, 1.9163, 1.7096])
    
    def test_quadratic_models_logistic_points(self):
        self.assertEqual(quadratic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[1.7096, 21.9765]]})
    
    def test_quadratic_models_logistic_accumulations(self):
        self.assertEqual(quadratic_models['models']['logistic']['accumulations'], {'range': 359.1389, 'iqr': 217.9023})
    
    def test_quadratic_models_logistic_averages(self):
        self.assertEqual(quadratic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 3.8859, 'mean_values_derivative': [3.2626], 'average_value_integral': 39.9043, 'mean_values_integral': [2.9038]}, 'iqr': {'average_value_derivative': 0.6837, 'mean_values_derivative': [4.21], 'average_value_integral': 43.5805, 'mean_values_integral': [4.1962]}})
    
    def test_quadratic_models_logistic_correlation(self):
        self.assertEqual(quadratic_models['models']['logistic']['correlation'], 0.7235)
    
    def test_quadratic_statistics(self):
        self.assertEqual(quadratic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_quadratic_optimal(self):
        self.assertEqual(quadratic_models['optimal']['option'], 'quadratic')

cubic_models = run_all(cubic_set, precision)
print(f"CUBIC -> SINUSOIDAL: {cubic_models['models']['sinusoidal']}")
# {'constants': [-26.6739, 0.9479, -1.5548, 62.2016], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d263670>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d263a60>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d263af0>}, 'points': {'roots': [None], 'maxima': [[3.4164, 88.8755], [10.0446, 88.8755], ['3.4164 + 6.6282k', 88.8755]], 'minima': [[0.1023, 35.5276], [6.7305, 35.5276], [13.3586, 35.5276], ['0.1023 + 6.6282k', 35.5276]], 'inflections': [[-1.5548, 62.2026], [1.7593, 62.2008], [5.0734, 62.2021], [8.3875, 62.2013], [11.7016, 62.2017], ['-1.5548 + 3.3141k', 62.2026]]}, 'accumulations': {'range': 579.7843, 'iqr': 295.5669}, 'averages': {'range': {'average_value_derivative': 4.915, 'mean_values_derivative': [6.5241, 6.9368, '0.3087 + 6.6282k', '-0.1041 + 6.6282k'], 'average_value_integral': 64.4205, 'mean_values_integral': [1.8472, 4.9856, 8.4754, '-1.6426 + 6.6282k', '1.8472 + 6.6282k']}, 'iqr': {'average_value_derivative': -6.8405, 'mean_values_derivative': [6.4415, 7.0195, '-0.1867 + 6.6282k', '0.3913 + 6.6282k'], 'average_value_integral': 59.1134, 'mean_values_integral': [5.1958, '-1.4324 + 6.6282k', '1.6369 + 6.6282k']}}, 'correlation': 0.8205}

class TestCubicModels(unittest.TestCase):
    def test_cubic_models_linear_constants(self):
        self.assertEqual(cubic_models['models']['linear']['constants'], [3.4, 45.8])
    
    def test_cubic_models_linear_points(self):
        self.assertEqual(cubic_models['models']['linear']['points'], {'roots': [[-13.4706, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_cubic_models_linear_accumulations(self):
        self.assertEqual(cubic_models['models']['linear']['accumulations'], {'range': 580.5, 'iqr': 322.5})
    
    def test_cubic_models_linear_averages(self):
        self.assertEqual(cubic_models['models']['linear']['averages'], {'range': {'average_value_derivative': 3.4, 'mean_values_derivative': ['All'], 'average_value_integral': 64.5, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': 3.4, 'mean_values_derivative': ['All'], 'average_value_integral': 64.5, 'mean_values_integral': [5.5]}})
    
    def test_cubic_models_linear_correlation(self):
        self.assertEqual(cubic_models['models']['linear']['correlation'], 0.427)
    
    def test_cubic_models_quadratic_constants(self):
        self.assertEqual(cubic_models['models']['quadratic']['constants'], [1.5, -13.1, 78.8])
    
    def test_cubic_models_quadratic_points(self):
        self.assertEqual(cubic_models['models']['quadratic']['points'], {'roots': [None], 'maxima': [None], 'minima': [[4.3667, 50.1983]], 'inflections': [None]})
    
    def test_cubic_models_quadratic_accumulations(self):
        self.assertEqual(cubic_models['models']['quadratic']['accumulations'], {'range': 560.25, 'iqr': 276.25})
    
    def test_cubic_models_quadratic_averages(self):
        self.assertEqual(cubic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 3.4, 'mean_values_derivative': [5.5], 'average_value_integral': 62.25, 'mean_values_integral': [1.5322, 7.2012]}, 'iqr': {'average_value_derivative': 3.4, 'mean_values_derivative': [5.5], 'average_value_integral': 55.25, 'mean_values_integral': [6.2018]}})
    
    def test_cubic_models_quadratic_correlation(self):
        self.assertEqual(cubic_models['models']['quadratic']['correlation'], 0.6399)
    
    def test_cubic_models_cubic_constants(self):
        self.assertEqual(cubic_models['models']['cubic']['constants'], [1.0, -15.0, 63.0, -7.0])
    
    def test_cubic_models_cubic_points(self):
        self.assertEqual(cubic_models['models']['cubic']['points'], {'roots': [[0.1142, 0]], 'maxima': [[3.0, 74.0]], 'minima': [[7.0, 42.0]], 'inflections': [[5.0, 58.0]]})
    
    def test_cubic_models_cubic_accumulations(self):
        self.assertEqual(cubic_models['models']['cubic']['accumulations'], {'range': 560.25, 'iqr': 276.25})
    
    def test_cubic_models_cubic_averages(self):
        self.assertEqual(cubic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 9.0, 'mean_values_derivative': [2.3542, 7.6458], 'average_value_integral': 62.25, 'mean_values_integral': [1.7288, 4.642, 8.6292]}, 'iqr': {'average_value_derivative': -5.0, 'mean_values_derivative': [3.4725, 6.5275], 'average_value_integral': 55.25, 'mean_values_integral': [5.2302]}})
    
    def test_cubic_models_cubic_correlation(self):
        self.assertEqual(cubic_models['models']['cubic']['correlation'], 1.0)
    
    def test_cubic_models_hyperbolic_constants(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['constants'], [-28.0701, 72.7217])
    
    def test_cubic_models_hyperbolic_points(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['points'], {'roots': [[0.386, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_cubic_models_hyperbolic_accumulations(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['accumulations'], {'range': 589.8615, 'iqr': 336.0765})
    
    def test_cubic_models_hyperbolic_averages(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 2.807, 'mean_values_derivative': [3.1623], 'average_value_integral': 65.5402, 'mean_values_integral': [3.9087]}, 'iqr': {'average_value_derivative': 1.1696, 'mean_values_derivative': [4.899], 'average_value_integral': 67.2153, 'mean_values_integral': [5.0977]}})
    
    def test_cubic_models_hyperbolic_correlation(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['correlation'], 0.3228)
    
    def test_cubic_models_exponential_constants(self):
        self.assertEqual(cubic_models['models']['exponential']['constants'], [49.0824, 1.0408])
    
    def test_cubic_models_exponential_points(self):
        self.assertEqual(cubic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_cubic_models_exponential_accumulations(self):
        self.assertEqual(cubic_models['models']['exponential']['accumulations'], {'range': 553.3881, 'iqr': 306.2944})
    
    def test_cubic_models_exponential_averages(self):
        self.assertEqual(cubic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 2.4589, 'mean_values_derivative': [5.6352], 'average_value_integral': 61.4876, 'mean_values_integral': [5.6348]}, 'iqr': {'average_value_derivative': 2.4497, 'mean_values_derivative': [5.5414], 'average_value_integral': 61.2589, 'mean_values_integral': [5.5416]}})
    
    def test_cubic_models_exponential_correlation(self):
        self.assertEqual(cubic_models['models']['exponential']['correlation'], 0.4088)
    
    def test_cubic_models_logarithmic_constants(self):
        self.assertEqual(cubic_models['models']['logarithmic']['constants'], [11.6113, 46.9618])
    
    def test_cubic_models_logarithmic_points(self):
        self.assertEqual(cubic_models['models']['logarithmic']['points'], {'roots': [[0.0175, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_cubic_models_logarithmic_accumulations(self):
        self.assertEqual(cubic_models['models']['logarithmic']['accumulations'], {'range': 585.5146, 'iqr': 331.6437})
    
    def test_cubic_models_logarithmic_averages(self):
        self.assertEqual(cubic_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 2.9707, 'mean_values_derivative': [3.9086], 'average_value_integral': 65.0572, 'mean_values_integral': [4.7514]}, 'iqr': {'average_value_derivative': 2.2777, 'mean_values_derivative': [5.0978], 'average_value_integral': 66.3287, 'mean_values_integral': [5.3012]}})
    
    def test_cubic_models_logarithmic_correlation(self):
        self.assertEqual(cubic_models['models']['logarithmic']['correlation'], 0.3531)
    
    def test_cubic_models_logistic_constants(self):
        self.assertEqual(cubic_models['models']['logistic']['constants'], [204.0, 0.0836, 14.9001])
    
    def test_cubic_models_logistic_points(self):
        self.assertEqual(cubic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[14.9001, 102.0001]]})
    
    def test_cubic_models_logistic_accumulations(self):
        self.assertEqual(cubic_models['models']['logistic']['accumulations'], {'range': 578.3231, 'iqr': 319.9737})
    
    def test_cubic_models_logistic_averages(self):
        self.assertEqual(cubic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 3.6417, 'mean_values_derivative': [5.2827], 'average_value_integral': 64.2581, 'mean_values_integral': [5.6041]}, 'iqr': {'average_value_derivative': 3.659, 'mean_values_derivative': [5.4325], 'average_value_integral': 63.9947, 'mean_values_integral': [5.5324]}})
    
    def test_cubic_models_logistic_correlation(self):
        self.assertEqual(cubic_models['models']['logistic']['correlation'], 0.4433)
    
    def test_cubic_statistics(self):
        self.assertEqual(cubic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_cubic_optimal(self):
        self.assertEqual(cubic_models['optimal']['option'], 'cubic')

hyperbolic_models = run_all(hyperbolic_set, precision)
print(f"HYPERBOLIC -> SINUSOIDAL: {hyperbolic_models['models']['sinusoidal']}")
# {'constants': [448.548, 1.1869, -0.0788, 746.6978], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d26d940>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d26dd30>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d26ddc0>}, 'points': {'roots': [None], 'maxima': [[1.2446, 1195.2458], [6.5382, 1195.2458], [11.8317, 1195.2458], ['1.2446 + 5.2936k', 1195.2458]], 'minima': [[3.8914, 298.1497], [9.185, 298.1497], ['3.8914 + 5.2936k', 298.1497]], 'inflections': [[-0.0788, 746.6851], [2.568, 746.7], [5.2148, 746.706], [7.8616, 746.6791], [10.5083, 746.6737], ['-0.0788 + 2.6468k', 746.6851]]}, 'accumulations': {'range': 6517.2945, 'iqr': 3776.9985}, 'averages': {'range': {'average_value_derivative': -76.0326, 'mean_values_derivative': [1.1239, 1.3653, 6.4174, 6.6589, '1.3653 + 5.2936k', '1.1239 + 5.2936k'], 'average_value_integral': 724.1438, 'mean_values_integral': [2.6104, 5.1724, 7.9039, '-0.1212 + 5.2936k', '2.6104 + 5.2936k']}, 'iqr': {'average_value_derivative': 29.3354, 'mean_values_derivative': [6.4917, 6.5846, '1.1982 + 5.2936k', '1.2911 + 5.2936k'], 'average_value_integral': 755.3997, 'mean_values_integral': [5.2311, 7.8452, '-0.0624 + 5.2936k', '2.5517 + 5.2936k']}}, 'correlation': 0.4914}

class TestHyperbolicModels(unittest.TestCase):
    def test_hyperbolic_models_linear_constants(self):
        self.assertEqual(hyperbolic_models['models']['linear']['constants'], [-186.6121, 1763.4667])
    
    def test_hyperbolic_models_linear_points(self):
        self.assertEqual(hyperbolic_models['models']['linear']['points'], {'roots': [[9.4499, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hyperbolic_models_linear_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['linear']['accumulations'], {'range': 6633.9014, 'iqr': 3685.5008})
    
    def test_hyperbolic_models_linear_averages(self):
        self.assertEqual(hyperbolic_models['models']['linear']['averages'], {'range': {'average_value_derivative': -186.6121, 'mean_values_derivative': ['All'], 'average_value_integral': 737.1002, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': -186.6121, 'mean_values_derivative': ['All'], 'average_value_integral': 737.1002, 'mean_values_integral': [5.5]}})
    
    def test_hyperbolic_models_linear_correlation(self):
        self.assertEqual(hyperbolic_models['models']['linear']['correlation'], 0.8086)
    
    def test_hyperbolic_models_quadratic_constants(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['constants'], [45.0417, -682.0705, 2754.3833])
    
    def test_hyperbolic_models_quadratic_points(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['points'], {'roots': [None], 'maxima': [None], 'minima': [[7.5715, 172.2196]], 'inflections': [None]})
    
    def test_hyperbolic_models_quadratic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['accumulations'], {'range': 6025.846, 'iqr': 2296.7192})
    
    def test_hyperbolic_models_quadratic_averages(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': -186.6118, 'mean_values_derivative': [5.5], 'average_value_integral': 669.5384, 'mean_values_integral': [4.2487]}, 'iqr': {'average_value_derivative': -186.6118, 'mean_values_derivative': [5.5], 'average_value_integral': 459.3438, 'mean_values_integral': [5.0467]}})
    
    def test_hyperbolic_models_quadratic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['correlation'], 0.9475)
    
    def test_hyperbolic_models_cubic_constants(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['constants'], [-10.4474, 217.4231, -1477.1144, 3650.7667])
    
    def test_hyperbolic_models_cubic_points(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['points'], {'roots': [[10.5478, 0]], 'maxima': [[7.9342, 399.9992]], 'minima': [[5.9399, 358.5629]], 'inflections': [[6.9371, 379.2819]]})
    
    def test_hyperbolic_models_cubic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['accumulations'], {'range': 6025.7417, 'iqr': 2296.6776})
    
    def test_hyperbolic_models_cubic_averages(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': -245.1217, 'mean_values_derivative': [3.968, 9.9061], 'average_value_integral': 669.5269, 'mean_values_integral': [3.5812]}, 'iqr': {'average_value_derivative': -98.8581, 'mean_values_derivative': [4.9003], 'average_value_integral': 459.3355, 'mean_values_integral': [4.4696]}})
    
    def test_hyperbolic_models_cubic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['correlation'], 0.9871)
    
    def test_hyperbolic_models_hyperbolic_constants(self):
        self.assertEqual(hyperbolic_models['models']['hyperbolic']['constants'], [2520.0, -1.0])
    
    def test_hyperbolic_models_hyperbolic_points(self):
        self.assertEqual(hyperbolic_models['models']['hyperbolic']['points'], {'roots': [[2520.0, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hyperbolic_models_hyperbolic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['hyperbolic']['accumulations'], {'range': 5793.5144, 'iqr': 2466.6897})
    
    def test_hyperbolic_models_hyperbolic_averages(self):
        self.assertEqual(hyperbolic_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': -252.0, 'mean_values_derivative': [3.1623], 'average_value_integral': 643.7238, 'mean_values_integral': [3.9087]}, 'iqr': {'average_value_derivative': -105.0, 'mean_values_derivative': [4.899], 'average_value_integral': 493.3379, 'mean_values_integral': [5.0977]}})
    
    def test_hyperbolic_models_hyperbolic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['hyperbolic']['correlation'], 1.0)
    
    def test_hyperbolic_models_exponential_constants(self):
        self.assertEqual(hyperbolic_models['models']['exponential']['constants'], [1975.941, 0.7939])
    
    def test_hyperbolic_models_exponential_points(self):
        self.assertEqual(hyperbolic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hyperbolic_models_exponential_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['exponential']['accumulations'], {'range': 5945.3267, 'iqr': 2932.8626})
    
    def test_hyperbolic_models_exponential_averages(self):
        self.assertEqual(hyperbolic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -152.4631, 'mean_values_derivative': [4.7473], 'average_value_integral': 660.5919, 'mean_values_integral': [4.7473]}, 'iqr': {'average_value_derivative': -135.3796, 'mean_values_derivative': [5.2622], 'average_value_integral': 586.5725, 'mean_values_integral': [5.2622]}})
    
    def test_hyperbolic_models_exponential_correlation(self):
        self.assertEqual(hyperbolic_models['models']['exponential']['correlation'], 0.8821)
    
    def test_hyperbolic_models_logarithmic_constants(self):
        self.assertEqual(hyperbolic_models['models']['logarithmic']['constants'], [-902.4723, 2100.2313])
    
    def test_hyperbolic_models_logarithmic_points(self):
        self.assertEqual(hyperbolic_models['models']['logarithmic']['points'], {'roots': [[10.2492, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hyperbolic_models_logarithmic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['logarithmic']['accumulations'], {'range': 6244.1398, 'iqr': 2974.8124})
    
    def test_hyperbolic_models_logarithmic_averages(self):
        self.assertEqual(hyperbolic_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': -230.891, 'mean_values_derivative': [3.9087], 'average_value_integral': 693.7933, 'mean_values_integral': [4.7513]}, 'iqr': {'average_value_derivative': -177.0342, 'mean_values_derivative': [5.0977], 'average_value_integral': 594.9625, 'mean_values_integral': [5.3012]}})
    
    def test_hyperbolic_models_logarithmic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['logarithmic']['correlation'], 0.9468)
    
    def test_hyperbolic_models_logistic_constants(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['constants'], [4787.0, -0.5355, 0.6592])
    
    def test_hyperbolic_models_logistic_points(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[0.6592, 2393.475]]})
    
    def test_hyperbolic_models_logistic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['accumulations'], {'range': 5357.9935, 'iqr': 2071.5342})
    
    def test_hyperbolic_models_logistic_averages(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': -238.1892, 'mean_values_derivative': [4.6875], 'average_value_integral': 595.3326, 'mean_values_integral': [4.304]}, 'iqr': {'average_value_derivative': -194.2107, 'mean_values_derivative': [5.1556], 'average_value_integral': 414.3068, 'mean_values_integral': [5.06]}})
    
    def test_hyperbolic_models_logistic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['correlation'], 0.9428)
    
    def test_hyperbolic_statistics(self):
        self.assertEqual(hyperbolic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_hyperbolic_optimal(self):
        self.assertEqual(hyperbolic_models['optimal']['option'], 'hyperbolic')

exponential_models = run_all(exponential_set, precision)
print(f"EXPONENTIAL -> SINUSOIDAL: {exponential_models['models']['sinusoidal']}")
# {'constants': [3065.0, 0.1022, 9.0, 1641.6143], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d278c10>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d278f70>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d280160>}, 'points': {'roots': [[3.4716, 0], [45.2562, 0], [64.9273, 0], [106.7119, 0], [126.383, 0], [168.1676, 0], ['3.4716 + 61.4557k', 0], ['45.2562 + 61.4557k', 0]], 'maxima': [[24.3639, 4706.6143], [85.8196, 4706.6143], [147.2753, 4706.6143], ['24.3639 + 61.4556k', 4706.6143]], 'minima': [[55.0918, -1423.3857], [116.5474, -1423.3857], ['55.0918 + 61.4556k', -1423.3857]], 'inflections': [[9.0, 1641.6143], [39.7278, 1641.6254], [70.4557, 1641.6233], [101.1835, 1641.6164], [131.9113, 1641.601], ['9.0 + 30.7278k', 1641.6143]]}, 'accumulations': {'range': 5450.1513, 'iqr': 2898.7499}, 'averages': {'range': {'average_value_derivative': 283.2682, 'mean_values_derivative': [None], 'average_value_integral': 605.5724, 'mean_values_integral': [5.6274, '5.6274 + 61.4557k', '43.1005 + 61.4557k']}, 'iqr': {'average_value_derivative': 290.3284, 'mean_values_derivative': [None], 'average_value_integral': 579.75, 'mean_values_integral': [5.5397, '5.5397 + 61.4557k', '43.1882 + 61.4557k']}}, 'correlation': 0.8194}

class TestExponentialModels(unittest.TestCase):
    def test_exponential_models_linear_constants(self):
        self.assertEqual(exponential_models['models']['linear']['constants'], [261.1273, -822.4])
    
    def test_exponential_models_linear_points(self):
        self.assertEqual(exponential_models['models']['linear']['points'], {'roots': [[3.1494, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_models_linear_accumulations(self):
        self.assertEqual(exponential_models['models']['linear']['accumulations'], {'range': 5524.2013, 'iqr': 3069.0007})
    
    def test_exponential_models_linear_averages(self):
        self.assertEqual(exponential_models['models']['linear']['averages'], {'range': {'average_value_derivative': 261.1273, 'mean_values_derivative': ['All'], 'average_value_integral': 613.8001, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': 261.1273, 'mean_values_derivative': ['All'], 'average_value_integral': 613.8001, 'mean_values_integral': [5.5]}})
    
    def test_exponential_models_linear_correlation(self):
        self.assertEqual(exponential_models['models']['linear']['correlation'], 0.7988)
    
    def test_exponential_models_quadratic_constants(self):
        self.assertEqual(exponential_models['models']['quadratic']['constants'], [69.4091, -502.3727, 704.6])
    
    def test_exponential_models_quadratic_points(self):
        self.assertEqual(exponential_models['models']['quadratic']['points'], {'roots': [[1.9028, 0], [5.3351, 0]], 'maxima': [None], 'minima': [[3.6189, -204.4246]], 'inflections': [None]})
    
    def test_exponential_models_quadratic_accumulations(self):
        self.assertEqual(exponential_models['models']['quadratic']['accumulations'], {'range': 4587.1816, 'iqr': 928.8886})
    
    def test_exponential_models_quadratic_averages(self):
        self.assertEqual(exponential_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 261.1274, 'mean_values_derivative': [5.5], 'average_value_integral': 509.6868, 'mean_values_integral': [6.8265]}, 'iqr': {'average_value_derivative': 261.1274, 'mean_values_derivative': [5.5], 'average_value_integral': 185.7777, 'mean_values_integral': [5.99]}})
    
    def test_exponential_models_quadratic_correlation(self):
        self.assertEqual(exponential_models['models']['quadratic']['correlation'], 0.9626)
    
    def test_exponential_models_cubic_constants(self):
        self.assertEqual(exponential_models['models']['cubic']['constants'], [13.5641, -154.3986, 529.8555, -459.2])
    
    def test_exponential_models_cubic_points(self):
        self.assertEqual(exponential_models['models']['cubic']['points'], {'roots': [[1.3077, 0]], 'maxima': [[2.6214, 113.1144]], 'minima': [[4.9672, 25.5731]], 'inflections': [[3.7943, 69.3435]]})
    
    def test_exponential_models_cubic_accumulations(self):
        self.assertEqual(exponential_models['models']['cubic']['accumulations'], {'range': 4587.1724, 'iqr': 928.8846})
    
    def test_exponential_models_cubic_averages(self):
        self.assertEqual(exponential_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 337.086, 'mean_values_derivative': [6.9023], 'average_value_integral': 509.6858, 'mean_values_integral': [7.4133]}, 'iqr': {'average_value_derivative': 147.1886, 'mean_values_derivative': [6.0287], 'average_value_integral': 185.7769, 'mean_values_integral': [6.4968]}})
    
    def test_exponential_models_cubic_correlation(self):
        self.assertEqual(exponential_models['models']['cubic']['correlation'], 0.9956)
    
    def test_exponential_models_hyperbolic_constants(self):
        self.assertEqual(exponential_models['models']['hyperbolic']['constants'], [-1569.4534, 1073.4879])
    
    def test_exponential_models_hyperbolic_points(self):
        self.assertEqual(exponential_models['models']['hyperbolic']['points'], {'roots': [[1.462, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_models_hyperbolic_accumulations(self):
        self.assertEqual(exponential_models['models']['hyperbolic']['accumulations'], {'range': 6047.5911, 'iqr': 3828.0737})
    
    def test_exponential_models_hyperbolic_averages(self):
        self.assertEqual(exponential_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 156.9453, 'mean_values_derivative': [3.1623], 'average_value_integral': 671.9546, 'mean_values_integral': [3.9087]}, 'iqr': {'average_value_derivative': 65.3939, 'mean_values_derivative': [4.899], 'average_value_integral': 765.6147, 'mean_values_integral': [5.0977]}})
    
    def test_exponential_models_hyperbolic_correlation(self):
        self.assertEqual(exponential_models['models']['hyperbolic']['correlation'], 0.4397)
    
    def test_exponential_models_exponential_constants(self):
        self.assertEqual(exponential_models['models']['exponential']['constants'], [3.0, 1.9999])
    
    def test_exponential_models_exponential_points(self):
        self.assertEqual(exponential_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_models_exponential_accumulations(self):
        self.assertEqual(exponential_models['models']['exponential']['accumulations'], {'range': 4421.4069, 'iqr': 1073.0046})
    
    def test_exponential_models_exponential_averages(self):
        self.assertEqual(exponential_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 340.4961, 'mean_values_derivative': [7.3559], 'average_value_integral': 491.2674, 'mean_values_integral': [7.3559]}, 'iqr': {'average_value_derivative': 148.7393, 'mean_values_derivative': [6.161], 'average_value_integral': 214.6009, 'mean_values_integral': [6.161]}})
    
    def test_exponential_models_exponential_correlation(self):
        self.assertEqual(exponential_models['models']['exponential']['correlation'], 1.0)
    
    def test_exponential_models_logarithmic_constants(self):
        self.assertEqual(exponential_models['models']['logarithmic']['constants'], [852.2441, -673.4647])
    
    def test_exponential_models_logarithmic_points(self):
        self.assertEqual(exponential_models['models']['logarithmic']['points'], {'roots': [[2.2039, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_models_logarithmic_accumulations(self):
        self.assertEqual(exponential_models['models']['logarithmic']['accumulations'], {'range': 5892.2664, 'iqr': 3740.1328})
    
    def test_exponential_models_logarithmic_averages(self):
        self.assertEqual(exponential_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 218.0405, 'mean_values_derivative': [3.9087], 'average_value_integral': 654.6963, 'mean_values_integral': [4.7513]}, 'iqr': {'average_value_derivative': 167.1812, 'mean_values_derivative': [5.0977], 'average_value_integral': 748.0266, 'mean_values_integral': [5.3012]}})
    
    def test_exponential_models_logarithmic_correlation(self):
        self.assertEqual(exponential_models['models']['logarithmic']['correlation'], 0.6312)
    
    def test_exponential_models_logistic_constants(self):
        self.assertEqual(exponential_models['models']['logistic']['constants'], [6138.0, 0.9655, 10.0383])
    
    def test_exponential_models_logistic_points(self):
        self.assertEqual(exponential_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[10.0383, 3069.0584]]})
    
    def test_exponential_models_logistic_accumulations(self):
        self.assertEqual(exponential_models['models']['logistic']['accumulations'], {'range': 4289.2526, 'iqr': 824.485})
    
    def test_exponential_models_logistic_averages(self):
        self.assertEqual(exponential_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 334.5918, 'mean_values_derivative': [7.1896], 'average_value_integral': 476.5836, 'mean_values_integral': [7.475]}, 'iqr': {'average_value_derivative': 149.1477, 'mean_values_derivative': [6.2787], 'average_value_integral': 164.897, 'mean_values_integral': [6.3202]}})
    
    def test_exponential_models_logistic_correlation(self):
        self.assertEqual(exponential_models['models']['logistic']['correlation'], 0.9983)
    
    def test_exponential_statistics(self):
        self.assertEqual(exponential_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_exponential_optimal(self):
        self.assertEqual(exponential_models['optimal']['option'], 'exponential')

logarithmic_models = run_all(logarithmic_set, precision)
print(f"LOGARITHMIC -> SINUSOIDAL: {logarithmic_models['models']['sinusoidal']}")
# {'constants': [-1.3224, 1.2013, 0.1451, 6.5218], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d2890d0>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d289310>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d2893a0>}, 'points': {'roots': [None], 'maxima': [[4.0677, 7.8441], [9.2979, 7.8441], ['4.0677 + 5.2302k', 7.8441]], 'minima': [[1.4526, 5.1994], [6.6828, 5.1994], [11.913, 5.1994], ['1.4526 + 5.2302k', 5.1994]], 'inflections': [[0.1451, 6.5218], [2.7602, 6.5218], [5.3753, 6.5217], [7.9903, 6.5217], [10.6054, 6.5218], ['0.1451 + 2.6151k', 6.5218]]}, 'accumulations': {'range': 58.9487, 'iqr': 32.5636}, 'averages': {'range': {'average_value_derivative': 0.2234, 'mean_values_derivative': [1.3352, 1.5701, 6.5654, 6.8002, '1.5701 + 5.2302k', '1.3352 + 5.2302k'], 'average_value_integral': 6.5499, 'mean_values_integral': [2.7779, 5.3576, 8.008, '0.1274 + 5.2302k', '2.7779 + 5.2302k']}, 'iqr': {'average_value_derivative': -0.0721, 'mean_values_derivative': [6.645, 6.7206, '1.4148 + 5.2302k', '1.4904 + 5.2302k'], 'average_value_integral': 6.5127, 'mean_values_integral': [5.381, 7.9846, '0.1508 + 5.2302k', '2.7545 + 5.2302k']}}, 'correlation': 0.4601}

class TestLogarithmicModels(unittest.TestCase):
    def test_logarithmic_models_linear_constants(self):
        self.assertEqual(logarithmic_models['models']['linear']['constants'], [0.6912, 2.7296])
    
    def test_logarithmic_models_linear_points(self):
        self.assertEqual(logarithmic_models['models']['linear']['points'], {'roots': [[-3.9491, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_models_linear_accumulations(self):
        self.assertEqual(logarithmic_models['models']['linear']['accumulations'], {'range': 58.7808, 'iqr': 32.656})
    
    def test_logarithmic_models_linear_averages(self):
        self.assertEqual(logarithmic_models['models']['linear']['averages'], {'range': {'average_value_derivative': 0.6912, 'mean_values_derivative': ['All'], 'average_value_integral': 6.5312, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': 0.6912, 'mean_values_derivative': ['All'], 'average_value_integral': 6.5312, 'mean_values_integral': [5.5]}})
    
    def test_logarithmic_models_linear_correlation(self):
        self.assertEqual(logarithmic_models['models']['linear']['correlation'], 0.9517)
    
    def test_logarithmic_models_quadratic_constants(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['constants'], [-0.0816, 1.5891, 0.9338])
    
    def test_logarithmic_models_quadratic_points(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['points'], {'roots': [[-0.5709, 0], [20.0452, 0]], 'maxima': [[9.7371, 8.6704]], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_models_quadratic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['accumulations'], {'range': 59.8918, 'iqr': 35.1772})
    
    def test_logarithmic_models_quadratic_averages(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 0.6915, 'mean_values_derivative': [5.5], 'average_value_integral': 6.6546, 'mean_values_integral': [4.7668]}, 'iqr': {'average_value_derivative': 0.6915, 'mean_values_derivative': [5.5], 'average_value_integral': 7.0354, 'mean_values_integral': [5.2608]}})
    
    def test_logarithmic_models_quadratic_correlation(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['correlation'], 0.9932)
    
    def test_logarithmic_models_cubic_constants(self):
        self.assertEqual(logarithmic_models['models']['cubic']['constants'], [0.0127, -0.2911, 2.5553, -0.1555])
    
    def test_logarithmic_models_cubic_points(self):
        self.assertEqual(logarithmic_models['models']['cubic']['points'], {'roots': [[0.0613, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[7.6404, 8.0392]]})
    
    def test_logarithmic_models_cubic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['cubic']['accumulations'], {'range': 59.8984, 'iqr': 35.1797})
    
    def test_logarithmic_models_cubic_averages(self):
        self.assertEqual(logarithmic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.7629, 'mean_values_derivative': [4.2742], 'average_value_integral': 6.6554, 'mean_values_integral': [4.5709]}, 'iqr': {'average_value_derivative': 0.5851, 'mean_values_derivative': [5.0588], 'average_value_integral': 7.0359, 'mean_values_integral': [5.1812]}})
    
    def test_logarithmic_models_cubic_correlation(self):
        self.assertEqual(logarithmic_models['models']['cubic']['correlation'], 0.999)
    
    def test_logarithmic_models_hyperbolic_constants(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['constants'], [-7.5094, 8.7308])
    
    def test_logarithmic_models_hyperbolic_points(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['points'], {'roots': [[0.8601, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_models_hyperbolic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['accumulations'], {'range': 61.2862, 'iqr': 36.2886})
    
    def test_logarithmic_models_hyperbolic_averages(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 0.7509, 'mean_values_derivative': [3.1624], 'average_value_integral': 6.8096, 'mean_values_integral': [3.9087]}, 'iqr': {'average_value_derivative': 0.3129, 'mean_values_derivative': [4.8989], 'average_value_integral': 7.2577, 'mean_values_integral': [5.0977]}})
    
    def test_logarithmic_models_hyperbolic_correlation(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['correlation'], 0.9468)
    
    def test_logarithmic_models_exponential_constants(self):
        self.assertEqual(logarithmic_models['models']['exponential']['constants'], [2.9406, 1.1403])
    
    def test_logarithmic_models_exponential_points(self):
        self.assertEqual(logarithmic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_models_exponential_accumulations(self):
        self.assertEqual(logarithmic_models['models']['exponential']['accumulations'], {'range': 57.7114, 'iqr': 30.8164})
    
    def test_logarithmic_models_exponential_averages(self):
        self.assertEqual(logarithmic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 0.8419, 'mean_values_derivative': [5.9382], 'average_value_integral': 6.4124, 'mean_values_integral': [5.9381]}, 'iqr': {'average_value_derivative': 0.8092, 'mean_values_derivative': [5.6364], 'average_value_integral': 6.1633, 'mean_values_integral': [5.6363]}})
    
    def test_logarithmic_models_exponential_correlation(self):
        self.assertEqual(logarithmic_models['models']['exponential']['correlation'], 0.8554)
    
    def test_logarithmic_models_logarithmic_constants(self):
        self.assertEqual(logarithmic_models['models']['logarithmic']['constants'], [3.0, 2.0])
    
    def test_logarithmic_models_logarithmic_points(self):
        self.assertEqual(logarithmic_models['models']['logarithmic']['points'], {'roots': [[0.5134, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_models_logarithmic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['logarithmic']['accumulations'], {'range': 60.0776, 'iqr': 35.0191})
    
    def test_logarithmic_models_logarithmic_averages(self):
        self.assertEqual(logarithmic_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 0.7675, 'mean_values_derivative': [3.9088], 'average_value_integral': 6.6753, 'mean_values_integral': [4.7514]}, 'iqr': {'average_value_derivative': 0.5885, 'mean_values_derivative': [5.0977], 'average_value_integral': 7.0038, 'mean_values_integral': [5.3012]}})
    
    def test_logarithmic_models_logarithmic_correlation(self):
        self.assertEqual(logarithmic_models['models']['logarithmic']['correlation'], 1.0)
    
    def test_logarithmic_models_logistic_constants(self):
        self.assertEqual(logarithmic_models['models']['logistic']['constants'], [8.6892, 0.5704, 2.5092])
    
    def test_logarithmic_models_logistic_points(self):
        self.assertEqual(logarithmic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[2.5092, 4.3447]]})
    
    def test_logarithmic_models_logistic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['logistic']['accumulations'], {'range': 59.9283, 'iqr': 35.521})
    
    def test_logarithmic_models_logistic_averages(self):
        self.assertEqual(logarithmic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.6653, 'mean_values_derivative': [5.4199], 'average_value_integral': 6.6587, 'mean_values_integral': [4.5914]}, 'iqr': {'average_value_derivative': 0.6754, 'mean_values_derivative': [5.3807], 'average_value_integral': 7.1042, 'mean_values_integral': [5.1392]}})
    
    def test_logarithmic_models_logistic_correlation(self):
        self.assertEqual(logarithmic_models['models']['logistic']['correlation'], 0.9898)
    
    def test_logarithmic_statistics(self):
        self.assertEqual(logarithmic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_logarithmic_optimal(self):
        self.assertEqual(logarithmic_models['optimal']['option'], 'logarithmic')

logistic_models = run_all(logistic_set, precision)
print(f"LOGISTIC -> SINUSOIDAL: {logistic_models['models']['sinusoidal']}")
# {'constants': [-1.1746, 0.5011, -1.1199, 1.0508], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d2941f0>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d2945e0>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d294670>}, 'points': {'roots': [[1.0904, 0], [2.9391, 0], [13.629, 0], [15.4777, 0], [26.1676, 0], [28.0164, 0], ['1.0904 + 12.5386k', 0], ['2.9391 + 12.5386k', 0]], 'maxima': [[8.2841, 2.2254], [20.8227, 2.2254], ['8.2841 + 12.5386k', 2.2254]], 'minima': [[2.0148, -0.1238], [14.5534, -0.1238], [27.092, -0.1238], ['2.0148 + 12.5386k', -0.1238]], 'inflections': [[-1.1199, 1.0508], [5.1494, 1.0508], [11.4187, 1.0508], [17.688, 1.0508], [23.9573, 1.0508], ['-1.1199 + 6.2693k', 1.0508]]}, 'accumulations': {'range': 10.0923, 'iqr': 6.0323}, 'averages': {'range': {'average_value_derivative': 0.1992, 'mean_values_derivative': [1.3258, 2.7037, '2.7037 + 12.5386k', '1.3258 + 12.5386k'], 'average_value_integral': 1.1214, 'mean_values_integral': [5.2694, '-1.2399 + 12.5386k', '5.2694 + 12.5386k']}, 'iqr': {'average_value_derivative': 0.4394, 'mean_values_derivative': [3.6967, '3.6967 + 12.5386k', '0.3328 + 12.5386k'], 'average_value_integral': 1.2065, 'mean_values_integral': [5.4147, '-1.3852 + 12.5386k', '5.4147 + 12.5386k']}}, 'correlation': 0.9789}

class TestLogisticModels(unittest.TestCase):
    def test_logistic_models_linear_constants(self):
        self.assertEqual(logistic_models['models']['linear']['constants'], [0.2944, -0.5193])
    
    def test_logistic_models_linear_points(self):
        self.assertEqual(logistic_models['models']['linear']['points'], {'roots': [[1.7639, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_models_linear_accumulations(self):
        self.assertEqual(logistic_models['models']['linear']['accumulations'], {'range': 9.8991, 'iqr': 5.4995})
    
    def test_logistic_models_linear_averages(self):
        self.assertEqual(logistic_models['models']['linear']['averages'], {'range': {'average_value_derivative': 0.2944, 'mean_values_derivative': ['All'], 'average_value_integral': 1.0999, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': 0.2944, 'mean_values_derivative': ['All'], 'average_value_integral': 1.0999, 'mean_values_integral': [5.5]}})
    
    def test_logistic_models_linear_correlation(self):
        self.assertEqual(logistic_models['models']['linear']['correlation'], 0.9163)
    
    def test_logistic_models_quadratic_constants(self):
        self.assertEqual(logistic_models['models']['quadratic']['constants'], [-0.0148, 0.4567, -0.8438])
    
    def test_logistic_models_quadratic_points(self):
        self.assertEqual(logistic_models['models']['quadratic']['points'], {'roots': [[1.9739, 0], [28.8842, 0]], 'maxima': [[15.4291, 2.6794]], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_models_quadratic_accumulations(self):
        self.assertEqual(logistic_models['models']['quadratic']['accumulations'], {'range': 10.084, 'iqr': 5.9476})
    
    def test_logistic_models_quadratic_averages(self):
        self.assertEqual(logistic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 0.2939, 'mean_values_derivative': [5.5], 'average_value_integral': 1.1204, 'mean_values_integral': [5.1656]}, 'iqr': {'average_value_derivative': 0.2939, 'mean_values_derivative': [5.5], 'average_value_integral': 1.1895, 'mean_values_integral': [5.3956]}})
    
    def test_logistic_models_quadratic_correlation(self):
        self.assertEqual(logistic_models['models']['quadratic']['correlation'], 0.9236)
    
    def test_logistic_models_cubic_constants(self):
        self.assertEqual(logistic_models['models']['cubic']['constants'], [-0.0162, 0.2531, -0.7789, 0.5493])
    
    def test_logistic_models_cubic_points(self):
        self.assertEqual(logistic_models['models']['cubic']['points'], {'roots': [[1.0231, 0], [2.8114, 0], [11.789, 0]], 'maxima': [[8.5387, 2.2665]], 'minima': [[1.877, -0.1281]], 'inflections': [[5.2078, 1.0692]]})
    
    def test_logistic_models_cubic_accumulations(self):
        self.assertEqual(logistic_models['models']['cubic']['accumulations'], {'range': 10.1745, 'iqr': 5.9838})
    
    def test_logistic_models_cubic_averages(self):
        self.assertEqual(logistic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.207, 'mean_values_derivative': [2.5934, 7.8223], 'average_value_integral': 1.1305, 'mean_values_integral': [5.3215]}, 'iqr': {'average_value_derivative': 0.4338, 'mean_values_derivative': [3.7352, 6.6805], 'average_value_integral': 1.1968, 'mean_values_integral': [5.4448]}})
    
    def test_logistic_models_cubic_correlation(self):
        self.assertEqual(logistic_models['models']['cubic']['correlation'], 0.9739)
    
    def test_logistic_models_hyperbolic_constants(self):
        self.assertEqual(logistic_models['models']['hyperbolic']['constants'], [-2.4884, 1.8288])
    
    def test_logistic_models_hyperbolic_points(self):
        self.assertEqual(logistic_models['models']['hyperbolic']['points'], {'roots': [[1.3607, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_models_hyperbolic_accumulations(self):
        self.assertEqual(logistic_models['models']['hyperbolic']['accumulations'], {'range': 10.7294, 'iqr': 6.7033})
    
    def test_logistic_models_hyperbolic_averages(self):
        self.assertEqual(logistic_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 0.2488, 'mean_values_derivative': [3.1625], 'average_value_integral': 1.1922, 'mean_values_integral': [3.9089]}, 'iqr': {'average_value_derivative': 0.1037, 'mean_values_derivative': [4.8986], 'average_value_integral': 1.3407, 'mean_values_integral': [5.0981]}})
    
    def test_logistic_models_hyperbolic_correlation(self):
        self.assertEqual(logistic_models['models']['hyperbolic']['correlation'], 0.7092)
    
    def test_logistic_models_exponential_constants(self):
        self.assertEqual(logistic_models['models']['exponential']['constants'], [0.0001, 3.5891])
    
    def test_logistic_models_exponential_points(self):
        self.assertEqual(logistic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_models_exponential_accumulations(self):
        self.assertEqual(logistic_models['models']['exponential']['accumulations'], {'range': 27.7558, 'iqr': 2.1511})
    
    def test_logistic_models_exponential_averages(self):
        self.assertEqual(logistic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 3.941, 'mean_values_derivative': [8.0887], 'average_value_integral': 3.084, 'mean_values_integral': [8.0887]}, 'iqr': {'average_value_derivative': 0.5498, 'mean_values_derivative': [6.5474], 'average_value_integral': 0.4302, 'mean_values_integral': [6.5473]}})
    
    def test_logistic_models_exponential_correlation(self):
        self.assertEqual(logistic_models['models']['exponential']['correlation'], 0.0)
    
    def test_logistic_models_logarithmic_constants(self):
        self.assertEqual(logistic_models['models']['logarithmic']['constants'], [1.155, -0.6445])
    
    def test_logistic_models_logarithmic_points(self):
        self.assertEqual(logistic_models['models']['logarithmic']['points'], {'roots': [[1.7472, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_models_logarithmic_accumulations(self):
        self.assertEqual(logistic_models['models']['logarithmic']['accumulations'], {'range': 10.3994, 'iqr': 6.4098})
    
    def test_logistic_models_logarithmic_averages(self):
        self.assertEqual(logistic_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 0.2955, 'mean_values_derivative': [3.9086], 'average_value_integral': 1.1555, 'mean_values_integral': [4.7514]}, 'iqr': {'average_value_derivative': 0.2266, 'mean_values_derivative': [5.0971], 'average_value_integral': 1.282, 'mean_values_integral': [5.3014]}})
    
    def test_logistic_models_logarithmic_correlation(self):
        self.assertEqual(logistic_models['models']['logarithmic']['correlation'], 0.8703)
    
    def test_logistic_models_logistic_constants(self):
        self.assertEqual(logistic_models['models']['logistic']['constants'], [2.0, 3.0, 5.0])
    
    def test_logistic_models_logistic_points(self):
        self.assertEqual(logistic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[5.0, 1.0]]})
    
    def test_logistic_models_logistic_accumulations(self):
        self.assertEqual(logistic_models['models']['logistic']['accumulations'], {'range': 10.0, 'iqr': 5.9984})
    
    def test_logistic_models_logistic_averages(self):
        self.assertEqual(logistic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.2222, 'mean_values_derivative': [3.9275, 6.0721], 'average_value_integral': 1.1111, 'mean_values_integral': [5.0744]}, 'iqr': {'average_value_derivative': 0.399, 'mean_values_derivative': [4.146, 5.8538], 'average_value_integral': 1.1997, 'mean_values_integral': [5.1349]}})
    
    def test_logistic_models_logistic_correlation(self):
        self.assertEqual(logistic_models['models']['logistic']['correlation'], 1.0)
    
    def test_logistic_statistics(self):
        self.assertEqual(logistic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_logistic_optimal(self):
        self.assertEqual(logistic_models['optimal']['option'], 'logistic')

sinusoidal_models = run_all(sinusoidal_set, precision)
print(f"SINUSOIDAL MODELS: {sinusoidal_models}")
# {'models': {'linear': {'constants': [0.0303, 3.3333], 'evaluations': {'equation': <function linear.<locals>.linear_equation at 0x10d294550>, 'derivative': <function linear.<locals>.first_derivative at 0x10d298b80>, 'integral': <function linear.<locals>.linear_integral at 0x10d298ca0>}, 'points': {'roots': [[-110.0099, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 31.4995, 'iqr': 17.4997}, 'averages': {'range': {'average_value_derivative': 0.0303, 'mean_values_derivative': ['All'], 'average_value_integral': 3.4999, 'mean_values_integral': [5.4983]}, 'iqr': {'average_value_derivative': 0.0303, 'mean_values_derivative': ['All'], 'average_value_integral': 3.4999, 'mean_values_integral': [5.4983]}}, 'correlation': 0.0249}, 'quadratic': {'constants': [0.1515, -1.6364, 6.6667], 'evaluations': {'equation': <function quadratic.<locals>.quadratic_equation at 0x10d298c10>, 'derivative': <function quadratic.<locals>.first_derivative at 0x10d298d30>, 'integral': <function quadratic.<locals>.quadratic_integral at 0x10d298e50>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [[5.4007, 2.2479]], 'inflections': [None]}, 'accumulations': {'range': 29.448, 'iqr': 12.825}, 'averages': {'range': {'average_value_derivative': 0.0301, 'mean_values_derivative': [5.5], 'average_value_integral': 3.272, 'mean_values_integral': [2.8007, 8.0006]}, 'iqr': {'average_value_derivative': 0.0301, 'mean_values_derivative': [5.5], 'average_value_integral': 2.565, 'mean_values_integral': [3.9539, 6.8475]}}, 'correlation': 0.3155}, 'cubic': {'constants': [0.0466, -0.6177, 1.9114, 2.6667], 'evaluations': {'equation': <function cubic.<locals>.cubic_equation at 0x10d298dc0>, 'derivative': <function cubic.<locals>.first_derivative at 0x10d298ee0>, 'integral': <function cubic.<locals>.cubic_integral at 0x10d29b040>}, 'points': {'roots': [[-1.0275, 0]], 'maxima': [[1.9997, 4.3915]], 'minima': [[6.8372, 1.7538]], 'inflections': [[4.4185, 3.0726]]}, 'accumulations': {'range': 29.4088, 'iqr': 12.8103}, 'averages': {'range': {'average_value_derivative': 0.2893, 'mean_values_derivative': [1.6043, 7.2327], 'average_value_integral': 3.2676, 'mean_values_integral': [4.1793, 8.7223]}, 'iqr': {'average_value_derivative': -0.3631, 'mean_values_derivative': [6.2221], 'average_value_integral': 2.5621, 'mean_values_integral': [5.0576]}}, 'correlation': 0.3929}, 'hyperbolic': {'constants': [0.7138, 3.2909], 'evaluations': {'equation': <function hyperbolic.<locals>.hyperbolic_equation at 0x10d298f70>, 'derivative': <function hyperbolic.<locals>.first_derivative at 0x10d29b160>, 'integral': <function hyperbolic.<locals>.hyperbolic_integral at 0x10d29b1f0>}, 'points': {'roots': [[-0.2169, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 31.2617, 'iqr': 17.1546}, 'averages': {'range': {'average_value_derivative': -0.0714, 'mean_values_derivative': [3.1618], 'average_value_integral': 3.4735, 'mean_values_integral': [3.9091]}, 'iqr': {'average_value_derivative': -0.0297, 'mean_values_derivative': [4.9024], 'average_value_integral': 3.4309, 'mean_values_integral': [5.0986]}}, 'correlation': 0.0536}, 'exponential': {'constants': [0.9234, 0.8984], 'evaluations': {'equation': <function exponential.<locals>.exponential_equation at 0x10d29b0d0>, 'derivative': <function exponential.<locals>.first_derivative at 0x10d29b280>, 'integral': <function exponential.<locals>.exponential_integral at 0x10d29b3a0>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 4.7909, 'iqr': 2.5919}, 'averages': {'range': {'average_value_derivative': -0.057, 'mean_values_derivative': [5.1465], 'average_value_integral': 0.5323, 'mean_values_integral': [5.1415]}, 'iqr': {'average_value_derivative': -0.0555, 'mean_values_derivative': [5.3954], 'average_value_integral': 0.5184, 'mean_values_integral': [5.3884]}}, 'correlation': 0.0}, 'logarithmic': {'constants': [-0.1951, 3.7947], 'evaluations': {'equation': <function logarithmic.<locals>.logarithmic_equation at 0x10d29b310>, 'derivative': <function logarithmic.<locals>.first_derivative at 0x10d29b430>, 'integral': <function logarithmic.<locals>.logarithmic_integral at 0x10d29b550>}, 'points': {'roots': [[279923141.2405, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}, 'accumulations': {'range': 31.4159, 'iqr': 17.3464}, 'averages': {'range': {'average_value_derivative': -0.0499, 'mean_values_derivative': [3.9098], 'average_value_integral': 3.4907, 'mean_values_integral': [4.7501]}, 'iqr': {'average_value_derivative': -0.0383, 'mean_values_derivative': [5.094], 'average_value_integral': 3.4693, 'mean_values_integral': [5.3008]}}, 'correlation': 0.0388}, 'logistic': {'constants': [3.5, 6.2649, -14.3299], 'evaluations': {'equation': <function logistic.<locals>.logistic_equation at 0x10d29b5e0>, 'derivative': <function logistic.<locals>.first_derivative at 0x10d29b700>, 'integral': <function logistic.<locals>.logistic_integral at 0x10d29b790>}, 'points': {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[-14.3299, 1.7499]]}, 'accumulations': {'range': 31.5, 'iqr': 17.5}, 'averages': {'range': {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 3.5, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 3.5, 'mean_values_integral': [None]}}, 'correlation': 0.0}, 'sinusoidal': {'constants': [-5.0, 1.5708, 3.0, 3.0], 'evaluations': {'equation': <function sinusoidal.<locals>.sinusoidal_equation at 0x10d29b4c0>, 'derivative': <function sinusoidal.<locals>.first_derivative at 0x10d29b9d0>, 'integral': <function sinusoidal.<locals>.sinusoidal_integral at 0x10d29ba60>}, 'points': {'roots': [[3.4097, 0], [4.5903, 0], [7.4097, 0], [8.5903, 0], [11.4097, 0], [12.5903, 0], ['3.4097 + 4.0k', 0], ['4.5903 + 4.0k', 0]], 'maxima': [[6.0, 8.0], [10.0, 8.0], ['6.0 + 4.0k', 8.0]], 'minima': [[4.0, -2.0], [8.0, -2.0], [12.0, -2.0], ['4.0 + 4.0k', -2.0]], 'inflections': [[3.0, 3.0], [5.0, 3.0], [7.0, 3.0], [9.0, 3.0], [11.0, 3.0], ['3.0 + 2.0k', 3.0]]}, 'accumulations': {'range': 30.1831, 'iqr': 11.8169}, 'averages': {'range': {'average_value_derivative': 0.5556, 'mean_values_derivative': [3.9549, 4.0451, 7.9549, 8.0451, '4.0451 + 4.0k', '3.9549 + 4.0k'], 'average_value_integral': 3.3537, 'mean_values_integral': [2.9549, 5.0451, 6.9549, 9.0451, '2.9549 + 4.0k', '5.0451 + 4.0k']}, 'iqr': {'average_value_derivative': -1.0, 'mean_values_derivative': [3.9187, 4.0813, 7.9187, '3.9187 + 4.0k', '4.0813 + 4.0k'], 'average_value_integral': 2.3634, 'mean_values_integral': [3.0813, 4.9187, 7.0813, '3.0813 + 4.0k', '4.9187 + 4.0k']}}, 'correlation': 1.0}}, 'statistics': {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5}, 'optimal': {'option': 'sinusoidal', 'correlation': 1.0}}

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 296 tests in 0.022s ---------- OK ---------- #