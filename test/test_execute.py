import unittest

from regressions.execute import run_all
from .data.sets.agnostic import agnostic_set
from .data.sets.linear import linear_set
from .data.sets.quadratic import quadratic_set
from .data.sets.cubic import cubic_set
from .data.sets.hyperbolic import hyperbolic_set
from .data.sets.exponential import exponential_set
from .data.sets.logarithmic import logarithmic_set
from .data.sets.logistic import logistic_set
from .data.sets.sinusoidal import sinusoidal_set
from .data.sets.weather import weather_set
from .data.sets.disease import disease_set
from .data.sets.profits import profits_set
from .data.sets.bad import bad_set_string, bad_set_vector, bad_set_buried_not_list, bad_set_buried_string, bad_set_short, bad_set_zeroes

agnostic_models = run_all(agnostic_set)

class TestAgnosticModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
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
    
    # QUADRATIC MODEL
    def test_agnostic_models_quadratic_constants(self):
        self.assertEqual(agnostic_models['models']['quadratic']['constants'], [-0.3106, 5.3803, 16.1667])
    
    def test_agnostic_models_quadratic_points(self):
        self.assertEqual(agnostic_models['models']['quadratic']['points'], {'roots': [[-2.6112, 0], [19.9335, 0]], 'maxima': [[8.6611, 39.4665]], 'minima': [None], 'inflections': [None]})
    
    def test_agnostic_models_quadratic_accumulations(self):
        self.assertEqual(agnostic_models['models']['quadratic']['accumulations'], {'range': 308.4336, 'iqr': 178.597})
    
    def test_agnostic_models_quadratic_averages(self):
        self.assertEqual(agnostic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 1.9637, 'mean_values_derivative': [5.5], 'average_value_integral': 34.2704, 'mean_values_integral': [4.571]}, 'iqr': {'average_value_derivative': 1.9637, 'mean_values_derivative': [5.5], 'average_value_integral': 35.7194, 'mean_values_integral': [5.1878]}})
    
    def test_agnostic_models_quadratic_correlation(self):
        self.assertEqual(agnostic_models['models']['quadratic']['correlation'], 0.5941)
    
    # CUBIC MODEL
    def test_agnostic_models_cubic_constants(self):
        self.assertEqual(agnostic_models['models']['cubic']['constants'], [-0.3881, 6.0932, -24.155, 49.4667])
    
    def test_agnostic_models_cubic_points(self):
        self.assertEqual(agnostic_models['models']['cubic']['points'], {'roots': [[11.1402, 0]], 'maxima': [[7.8105, 47.5947]], 'minima': [[2.6562, 21.0229]], 'inflections': [[5.2334, 34.3091]]})
    
    def test_agnostic_models_cubic_accumulations(self):
        self.assertEqual(agnostic_models['models']['cubic']['accumulations'], {'range': 308.6937, 'iqr': 178.6995})
    
    def test_agnostic_models_cubic_averages(self):
        self.assertEqual(agnostic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': -0.2089, 'mean_values_derivative': [2.6216, 7.8451], 'average_value_integral': 34.2993, 'mean_values_integral': [5.2321, 9.6977]}, 'iqr': {'average_value_derivative': 5.2245, 'mean_values_derivative': [3.7656, 6.7012], 'average_value_integral': 35.7399, 'mean_values_integral': [5.4187]}})
    
    def test_agnostic_models_cubic_correlation(self):
        self.assertEqual(agnostic_models['models']['cubic']['correlation'], 0.8933)
    
    # HYPERBOLIC MODEL
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
    
    # EXPONENTIAL MODEL
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
    
    # LOGARITHMIC MODEL
    def test_agnostic_models_logarithmic_constants(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['constants'], [7.4791, 22.5032])
    
    def test_agnostic_models_logarithmic_points(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['points'], {'roots': [[0.0494, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_agnostic_models_logarithmic_accumulations(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['accumulations'], {'range': 307.4295, 'iqr': 174.8894})
    
    def test_agnostic_models_logarithmic_averages(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 1.9135, 'mean_values_derivative': [3.9086], 'average_value_integral': 34.1588, 'mean_values_integral': [4.7513]}, 'iqr': {'average_value_derivative': 1.4672, 'mean_values_derivative': [5.0975], 'average_value_integral': 34.9779, 'mean_values_integral': [5.3012]}})
    
    def test_agnostic_models_logarithmic_correlation(self):
        self.assertEqual(agnostic_models['models']['logarithmic']['correlation'], 0.5086)
    
    # LOGISTIC MODEL
    def test_agnostic_models_logistic_constants(self):
        self.assertEqual(agnostic_models['models']['logistic']['constants'], [43.9838, 0.3076, 0.9747])
    
    def test_agnostic_models_logistic_points(self):
        self.assertEqual(agnostic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[0.9747, 21.9919]]})
    
    def test_agnostic_models_logistic_accumulations(self):
        self.assertEqual(agnostic_models['models']['logistic']['accumulations'], {'range': 305.9347, 'iqr': 174.1106})
    
    def test_agnostic_models_logistic_averages(self):
        self.assertEqual(agnostic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 2.1475, 'mean_values_derivative': [5.5247], 'average_value_integral': 33.9927, 'mean_values_integral': [4.9554]}, 'iqr': {'average_value_derivative': 2.1622, 'mean_values_derivative': [5.488], 'average_value_integral': 34.8221, 'mean_values_integral': [5.3155]}})
    
    def test_agnostic_models_logistic_correlation(self):
        self.assertEqual(agnostic_models['models']['logistic']['correlation'], 0.5875)
    
    # SINUSOIDAL MODEL
    def test_agnostic_models_sinusoidal_constants(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['constants'], [14.0875, 0.7119, -3.7531, 34.2915])
    
    def test_agnostic_models_sinusoidal_points(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[7.2794, 48.379], ['7.2794 + 8.826k', 48.379]], 'minima': [[2.8664, 20.204], ['2.8664 + 8.826k', 20.204]], 'inflections': [[5.0729, 34.2915], [9.4859, 34.2915], ['5.0729 + 4.413k', 34.2915]]})
    
    def test_agnostic_models_sinusoidal_accumulations(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['accumulations'], {'range': 307.8897, 'iqr': 183.0504})
    
    def test_agnostic_models_sinusoidal_averages(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': -0.1849, 'mean_values_derivative': [2.8405, 7.3052, '2.8405 + 8.8259k', '7.3052 + 8.8259k'], 'average_value_integral': 34.21, 'mean_values_integral': [5.0647, 9.4939, '5.0647 + 8.8259k', '9.4939 + 8.8259k']}, 'iqr': {'average_value_derivative': 5.2595, 'mean_values_derivative': [3.6418, 6.5038, '3.6418 + 8.8259k', '6.5038 + 8.8259k'], 'average_value_integral': 36.6101, 'mean_values_integral': [5.305, '5.305 + 8.8259k', '9.2535 + 8.8259k']}})
    
    def test_agnostic_models_sinusoidal_correlation(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['correlation'], 0.9264)
    
    # COMPARATIVE ANALYSIS
    def test_agnostic_statistics(self):
        self.assertEqual(agnostic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_agnostic_optimal(self):
        self.assertEqual(agnostic_models['optimal']['option'], 'sinusoidal')

linear_models = run_all(linear_set)

class TestLinearModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
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
    
    # QUADRATIC MODEL
    def test_linear_models_quadratic_constants(self):
        self.assertEqual(linear_models['models']['quadratic']['constants'], [-0.0001, -3.0, 33.0])
    
    def test_linear_models_quadratic_points(self):
        self.assertEqual(linear_models['models']['quadratic']['points'], {'roots': [[-30010.996, 0], [10.996, 0]], 'maxima': [[-15000.0, 22533.0]], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_quadratic_accumulations(self):
        self.assertEqual(linear_models['models']['quadratic']['accumulations'], {'range': 148.4001, 'iqr': 82.4515})
    
    def test_linear_models_quadratic_averages(self):
        self.assertEqual(linear_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': -3.0011, 'mean_values_derivative': [5.5], 'average_value_integral': 16.4889, 'mean_values_integral': [5.5027]}, 'iqr': {'average_value_derivative': -3.0011, 'mean_values_derivative': [5.5], 'average_value_integral': 16.4903, 'mean_values_integral': [5.5022]}})
    
    def test_linear_models_quadratic_correlation(self):
        self.assertEqual(linear_models['models']['quadratic']['correlation'], 1.0)
    
    # CUBIC MODEL
    def test_linear_models_cubic_constants(self):
        self.assertEqual(linear_models['models']['cubic']['constants'], [-0.0001, -0.0001, -3.0, 33.0])
    
    def test_linear_models_cubic_points(self):
        self.assertEqual(linear_models['models']['cubic']['points'], {'roots': [[10.9522, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[-0.3333, 33.9999]]})
    
    def test_linear_models_cubic_accumulations(self):
        self.assertEqual(linear_models['models']['cubic']['accumulations'], {'range': 147.4002, 'iqr': 82.05})
    
    def test_linear_models_cubic_averages(self):
        self.assertEqual(linear_models['models']['cubic']['averages'], {'range': {'average_value_derivative': -3.0122, 'mean_values_derivative': [6.0524], 'average_value_integral': 16.3778, 'mean_values_integral': [5.5341]}, 'iqr': {'average_value_derivative': -3.0108, 'mean_values_derivative': [5.6759], 'average_value_integral': 16.41, 'mean_values_integral': [5.5234]}})
    
    def test_linear_models_cubic_correlation(self):
        self.assertEqual(linear_models['models']['cubic']['correlation'], 1.0)
    
    # HYPERBOLIC MODEL
    def test_linear_models_hyperbolic_constants(self):
        self.assertEqual(linear_models['models']['hyperbolic']['constants'], [26.49, 8.7412])
    
    def test_linear_models_hyperbolic_points(self):
        self.assertEqual(linear_models['models']['hyperbolic']['points'], {'roots': [[-3.0305, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_hyperbolic_accumulations(self):
        self.assertEqual(linear_models['models']['hyperbolic']['accumulations'], {'range': 139.6663, 'iqr': 69.6882})
    
    def test_linear_models_hyperbolic_averages(self):
        self.assertEqual(linear_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': -2.649, 'mean_values_derivative': [3.1623], 'average_value_integral': 15.5185, 'mean_values_integral': [3.9086]}, 'iqr': {'average_value_derivative': -1.1038, 'mean_values_derivative': [4.8989], 'average_value_integral': 13.9376, 'mean_values_integral': [5.0978]}})
    
    def test_linear_models_hyperbolic_correlation(self):
        self.assertEqual(linear_models['models']['hyperbolic']['correlation'], 0.8086)
    
    # EXPONENTIAL MODEL
    def test_linear_models_exponential_constants(self):
        self.assertEqual(linear_models['models']['exponential']['constants'], [48.2454, 0.7942])
    
    def test_linear_models_exponential_points(self):
        self.assertEqual(linear_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_exponential_accumulations(self):
        self.assertEqual(linear_models['models']['exponential']['accumulations'], {'range': 145.3855, 'iqr': 71.7462})
    
    def test_linear_models_exponential_averages(self):
        self.assertEqual(linear_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -3.7222, 'mean_values_derivative': [4.7484], 'average_value_integral': 16.1539, 'mean_values_integral': [4.7485]}, 'iqr': {'average_value_derivative': -3.3064, 'mean_values_derivative': [5.2625], 'average_value_integral': 14.3492, 'mean_values_integral': [5.2626]}})
    
    def test_linear_models_exponential_correlation(self):
        self.assertEqual(linear_models['models']['exponential']['correlation'], 0.9222)
    
    # LOGARITHMIC MODEL
    def test_linear_models_logarithmic_constants(self):
        self.assertEqual(linear_models['models']['logarithmic']['constants'], [-11.7921, 34.3113])
    
    def test_linear_models_logarithmic_points(self):
        self.assertEqual(linear_models['models']['logarithmic']['points'], {'roots': [[18.351, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_logarithmic_accumulations(self):
        self.assertEqual(linear_models['models']['logarithmic']['accumulations'], {'range': 143.4075, 'iqr': 73.2139})
    
    def test_linear_models_logarithmic_averages(self):
        self.assertEqual(linear_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': -3.0169, 'mean_values_derivative': [3.9087], 'average_value_integral': 15.9342, 'mean_values_integral': [4.7513]}, 'iqr': {'average_value_derivative': -2.3132, 'mean_values_derivative': [5.0977], 'average_value_integral': 14.6428, 'mean_values_integral': [5.3012]}})
    
    def test_linear_models_logarithmic_correlation(self):
        self.assertEqual(linear_models['models']['logarithmic']['correlation'], 0.9517)
    
    # LOGISTIC MODEL
    def test_linear_models_logistic_constants(self):
        self.assertEqual(linear_models['models']['logistic']['constants'], [34.8519, -0.402, 5.1709])
    
    def test_linear_models_logistic_points(self):
        self.assertEqual(linear_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[5.1709, 17.426]]})
    
    def test_linear_models_logistic_accumulations(self):
        self.assertEqual(linear_models['models']['logistic']['accumulations'], {'range': 148.5986, 'iqr': 81.8129})
    
    def test_linear_models_logistic_averages(self):
        self.assertEqual(linear_models['models']['logistic']['averages'], {'range': {'average_value_derivative': -2.7764, 'mean_values_derivative': [2.7257, 7.6157], 'average_value_integral': 16.511, 'mean_values_integral': [5.4324]}, 'iqr': {'average_value_derivative': -3.2237, 'mean_values_derivative': [3.7277, 6.6141], 'average_value_integral': 16.3626, 'mean_values_integral': [5.4749]}})
    
    def test_linear_models_logistic_correlation(self):
        self.assertEqual(linear_models['models']['logistic']['correlation'], 0.9974)
    
    # SINUSOIDAL MODEL
    def test_linear_models_sinusoidal_constants(self):
        self.assertEqual(linear_models['models']['sinusoidal']['constants'], [3.6953, 1.8762, 3.8255, 16.5])
    
    def test_linear_models_sinusoidal_points(self):
        self.assertEqual(linear_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[4.6627, 20.1953], [8.0115, 20.1953], ['4.6627 + 3.3488k', 20.1953]], 'minima': [[6.3372, 12.8047], [9.686, 12.8047], ['6.3372 + 3.3488k', 12.8047]], 'inflections': [[3.8255, 16.5], [5.4999, 16.5], [7.1743, 16.5], [8.8487, 16.5], ['3.8255 + 1.6744k', 16.5]]})
    
    def test_linear_models_sinusoidal_accumulations(self):
        self.assertEqual(linear_models['models']['sinusoidal']['accumulations'], {'range': 148.4997, 'iqr': 82.5004})
    
    def test_linear_models_sinusoidal_averages(self):
        self.assertEqual(linear_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': -0.6828, 'mean_values_derivative': [4.7153, 6.2846, 8.0642, 9.6335, '4.7153 + 3.3489k', '6.2846 + 3.3489k'], 'average_value_integral': 16.5, 'mean_values_integral': [3.8255, 5.5, 7.1744, 8.8489, '3.8255 + 3.3489k', '5.5 + 3.3489k']}, 'iqr': {'average_value_derivative': 1.4778, 'mean_values_derivative': [4.5482, 6.4517, 7.8971, '4.5482 + 3.3489k', '6.4517 + 3.3489k'], 'average_value_integral': 16.5001, 'mean_values_integral': [3.8255, 5.4999, 7.1744, '3.8255 + 3.3489k', '5.4999 + 3.3489k']}})
    
    def test_linear_models_sinusoidal_correlation(self):
        self.assertEqual(linear_models['models']['sinusoidal']['correlation'], 0.3046)
    
    # COMPARATIVE ANALYSIS
    def test_linear_statistics(self):
        self.assertEqual(linear_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_linear_optimal(self):
        self.assertEqual(linear_models['optimal']['option'], 'linear')

quadratic_models = run_all(quadratic_set)

class TestQuadraticModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
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
    
    # QUADRATIC MODEL
    def test_quadratic_models_quadratic_constants(self):
        self.assertEqual(quadratic_models['models']['quadratic']['constants'], [-2.0, 23.0, -11.0])
    
    def test_quadratic_models_quadratic_points(self):
        self.assertEqual(quadratic_models['models']['quadratic']['points'], {'roots': [[0.5, 0], [11.0, 0]], 'maxima': [[5.75, 55.125]], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_models_quadratic_accumulations(self):
        self.assertEqual(quadratic_models['models']['quadratic']['accumulations'], {'range': 373.4667, 'iqr': 254.1505})
    
    def test_quadratic_models_quadratic_averages(self):
        self.assertEqual(quadratic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 41.4963, 'mean_values_integral': [3.1396, 8.3604]}, 'iqr': {'average_value_derivative': 1.0, 'mean_values_derivative': [5.5], 'average_value_integral': 50.8301, 'mean_values_integral': [4.2846, 7.2154]}})
    
    def test_quadratic_models_quadratic_correlation(self):
        self.assertEqual(quadratic_models['models']['quadratic']['correlation'], 1.0)
    
    # CUBIC MODEL
    def test_quadratic_models_cubic_constants(self):
        self.assertEqual(quadratic_models['models']['cubic']['constants'], [-0.0001, -2.0, 23.0, -11.0])
    
    def test_quadratic_models_cubic_points(self):
        self.assertEqual(quadratic_models['models']['cubic']['points'], {'roots': [[-20011.4937, 0], [0.5, 0], [10.9937, 0]], 'maxima': [[5.7475, 55.106]], 'minima': [[-13339.0809, -118825262.2912]], 'inflections': [[-6666.6667, -59412604.0378]]})
    
    def test_quadratic_models_cubic_accumulations(self):
        self.assertEqual(quadratic_models['models']['cubic']['accumulations'], {'range': 372.4668, 'iqr': 253.749})
    
    def test_quadratic_models_cubic_averages(self):
        self.assertEqual(quadratic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.9889, 'mean_values_derivative': [5.5005], 'average_value_integral': 41.3852, 'mean_values_integral': [3.1292, 8.3655]}, 'iqr': {'average_value_derivative': 0.9903, 'mean_values_derivative': [5.5002], 'average_value_integral': 50.7498, 'mean_values_integral': [4.2723, 7.2227]}})
    
    def test_quadratic_models_cubic_correlation(self):
        self.assertEqual(quadratic_models['models']['cubic']['correlation'], 1.0)
    
    # HYPERBOLIC MODEL
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
    
    # EXPONENTIAL MODEL
    def test_quadratic_models_exponential_constants(self):
        self.assertEqual(quadratic_models['models']['exponential']['constants'], [26.2561, 1.0509])
    
    def test_quadratic_models_exponential_points(self):
        self.assertEqual(quadratic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_models_exponential_accumulations(self):
        self.assertEqual(quadratic_models['models']['exponential']['accumulations'], {'range': 313.0886, 'iqr': 172.9428})
    
    def test_quadratic_models_exponential_averages(self):
        self.assertEqual(quadratic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 1.7271, 'mean_values_derivative': [5.6673], 'average_value_integral': 34.7876, 'mean_values_integral': [5.6673]}, 'iqr': {'average_value_derivative': 1.7172, 'mean_values_derivative': [5.5515], 'average_value_integral': 34.5886, 'mean_values_integral': [5.5517]}})
    
    def test_quadratic_models_exponential_correlation(self):
        self.assertEqual(quadratic_models['models']['exponential']['correlation'], 0.0)
    
    # LOGARITHMIC MODEL
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
    
    # LOGISTIC MODEL
    def test_quadratic_models_logistic_constants(self):
        self.assertEqual(quadratic_models['models']['logistic']['constants'], [43.9519, 1.9163, 1.7096])
    
    def test_quadratic_models_logistic_points(self):
        self.assertEqual(quadratic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[1.7096, 21.976]]})
    
    def test_quadratic_models_logistic_accumulations(self):
        self.assertEqual(quadratic_models['models']['logistic']['accumulations'], {'range': 359.1378, 'iqr': 217.9022})
    
    def test_quadratic_models_logistic_averages(self):
        self.assertEqual(quadratic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 3.886, 'mean_values_derivative': [3.2626], 'average_value_integral': 39.9042, 'mean_values_integral': [2.9037]}, 'iqr': {'average_value_derivative': 0.6837, 'mean_values_derivative': [4.21], 'average_value_integral': 43.5804, 'mean_values_integral': [4.1961]}})
    
    def test_quadratic_models_logistic_correlation(self):
        self.assertEqual(quadratic_models['models']['logistic']['correlation'], 0.7235)
    
    # SINUSOIDAL MODEL
    def test_quadratic_models_sinusoidal_constants(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['constants'], [-45.0, 0.3267, -8.6568, 10.9862])
    
    def test_quadratic_models_sinusoidal_points(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['points'], {'roots': [['11.3304 + 19.2323k', 0.0], ['19.4367 + 19.2323k', 0.0]], 'maxima': [[5.7674, 55.9862], ['5.7674 + 19.2322k', 55.9862]], 'minima': [['15.3835 + 19.2322k', -34.0138]], 'inflections': [['10.5754 + 9.6161k', 10.9862]]})
    
    def test_quadratic_models_sinusoidal_accumulations(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['accumulations'], {'range': 371.9184, 'iqr': 254.9708})
    
    def test_quadratic_models_sinusoidal_averages(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.8681, 'mean_values_derivative': [5.5866, '5.5866 + 19.2323k', '15.5644 + 19.2323k'], 'average_value_integral': 41.3243, 'mean_values_integral': [3.224, 8.3109, '3.224 + 19.2323k', '8.3109 + 19.2323k']}, 'iqr': {'average_value_derivative': 1.1448, 'mean_values_derivative': [5.5288, '5.5288 + 19.2323k', '15.6222 + 19.2323k'], 'average_value_integral': 50.9942, 'mean_values_integral': [4.312, 7.2229, '4.312 + 19.2323k', '7.2229 + 19.2323k']}})
    
    def test_quadratic_models_sinusoidal_correlation(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['correlation'], 0.9983)
    
    # COMPARATIVE ANALYSIS
    def test_quadratic_statistics(self):
        self.assertEqual(quadratic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_quadratic_optimal(self):
        self.assertEqual(quadratic_models['optimal']['option'], 'quadratic')

cubic_models = run_all(cubic_set)

class TestCubicModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
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
    
    # QUADRATIC MODEL
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
    
    # CUBIC MODEL
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
    
    # HYPERBOLIC MODEL
    def test_cubic_models_hyperbolic_constants(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['constants'], [-28.0701, 72.7217])
    
    def test_cubic_models_hyperbolic_points(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['points'], {'roots': [[0.386, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_cubic_models_hyperbolic_accumulations(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['accumulations'], {'range': 589.8615, 'iqr': 336.0766})
    
    def test_cubic_models_hyperbolic_averages(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 2.807, 'mean_values_derivative': [3.1623], 'average_value_integral': 65.5402, 'mean_values_integral': [3.9087]}, 'iqr': {'average_value_derivative': 1.1696, 'mean_values_derivative': [4.899], 'average_value_integral': 67.2153, 'mean_values_integral': [5.0977]}})
    
    def test_cubic_models_hyperbolic_correlation(self):
        self.assertEqual(cubic_models['models']['hyperbolic']['correlation'], 0.3228)
    
    # EXPONENTIAL MODEL
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
    
    # LOGARITHMIC MODEL
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
    
    # LOGISTIC MODEL
    def test_cubic_models_logistic_constants(self):
        self.assertEqual(cubic_models['models']['logistic']['constants'], [202.5728, 0.0861, 14.5])
    
    def test_cubic_models_logistic_points(self):
        self.assertEqual(cubic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[14.5, 101.2864]]})
    
    def test_cubic_models_logistic_accumulations(self):
        self.assertEqual(cubic_models['models']['logistic']['accumulations'], {'range': 578.6529, 'iqr': 320.0988})
    
    def test_cubic_models_logistic_averages(self):
        self.assertEqual(cubic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 3.7384, 'mean_values_derivative': [5.2699], 'average_value_integral': 64.2948, 'mean_values_integral': [5.6058]}, 'iqr': {'average_value_derivative': 3.7576, 'mean_values_derivative': [5.4289], 'average_value_integral': 64.0198, 'mean_values_integral': [5.533]}})
    
    def test_cubic_models_logistic_correlation(self):
        self.assertEqual(cubic_models['models']['logistic']['correlation'], 0.443)
    
    # SINUSOIDAL MODEL
    def test_cubic_models_sinusoidal_constants(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['constants'], [-26.6739, 0.9479, -1.5548, 62.2016])
    
    def test_cubic_models_sinusoidal_points(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[3.4166, 88.8755], ['3.4166 + 6.6286k', 88.8755]], 'minima': [[6.7309, 35.5277], ['6.7309 + 6.6286k', 35.5277]], 'inflections': [[1.7595, 62.2016], [5.0738, 62.2016], [8.3881, 62.2016], ['1.7595 + 3.3143k', 62.2016]]})
    
    def test_cubic_models_sinusoidal_accumulations(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['accumulations'], {'range': 579.7687, 'iqr': 295.5756})
    
    def test_cubic_models_sinusoidal_averages(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 4.9151, 'mean_values_derivative': [3.2102, 6.9372, 9.8387, '3.2102 + 6.6285k', '6.9372 + 6.6285k'], 'average_value_integral': 64.4187, 'mean_values_integral': [1.8473, 4.9859, 8.4758, '1.8473 + 6.6285k', '4.9859 + 6.6285k']}, 'iqr': {'average_value_derivative': -6.8423, 'mean_values_derivative': [3.7057, 6.4417, '3.7057 + 6.6285k', '6.4417 + 6.6285k'], 'average_value_integral': 59.1151, 'mean_values_integral': [5.196, '5.196 + 6.6285k', '8.2656 + 6.6285k']}})
    
    def test_cubic_models_sinusoidal_correlation(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['correlation'], 0.8205)
    
    # COMPARATIVE ANALYSIS
    def test_cubic_statistics(self):
        self.assertEqual(cubic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_cubic_optimal(self):
        self.assertEqual(cubic_models['optimal']['option'], 'cubic')

hyperbolic_models = run_all(hyperbolic_set)

class TestHyperbolicModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
    def test_hyperbolic_models_linear_constants(self):
        self.assertEqual(hyperbolic_models['models']['linear']['constants'], [-186.6121, 1763.4667])
    
    def test_hyperbolic_models_linear_points(self):
        self.assertEqual(hyperbolic_models['models']['linear']['points'], {'roots': [[9.4499, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hyperbolic_models_linear_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['linear']['accumulations'], {'range': 6633.9063, 'iqr': 3685.5035})
    
    def test_hyperbolic_models_linear_averages(self):
        self.assertEqual(hyperbolic_models['models']['linear']['averages'], {'range': {'average_value_derivative': -186.6121, 'mean_values_derivative': ['All'], 'average_value_integral': 737.1007, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': -186.6121, 'mean_values_derivative': ['All'], 'average_value_integral': 737.1007, 'mean_values_integral': [5.5]}})
    
    def test_hyperbolic_models_linear_correlation(self):
        self.assertEqual(hyperbolic_models['models']['linear']['correlation'], 0.8086)
    
    # QUADRATIC MODEL
    def test_hyperbolic_models_quadratic_constants(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['constants'], [45.0417, -682.0705, 2754.3833])
    
    def test_hyperbolic_models_quadratic_points(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['points'], {'roots': [None], 'maxima': [None], 'minima': [[7.5715, 172.2196]], 'inflections': [None]})
    
    def test_hyperbolic_models_quadratic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['accumulations'], {'range': 6025.8411, 'iqr': 2296.7165})
    
    def test_hyperbolic_models_quadratic_averages(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': -186.6118, 'mean_values_derivative': [5.5], 'average_value_integral': 669.5379, 'mean_values_integral': [4.2487]}, 'iqr': {'average_value_derivative': -186.6118, 'mean_values_derivative': [5.5], 'average_value_integral': 459.3433, 'mean_values_integral': [5.0467]}})
    
    def test_hyperbolic_models_quadratic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['quadratic']['correlation'], 0.9475)
    
    # CUBIC MODEL
    def test_hyperbolic_models_cubic_constants(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['constants'], [-10.4474, 217.4231, -1477.1144, 3650.7667])
    
    def test_hyperbolic_models_cubic_points(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['points'], {'roots': [[10.5478, 0]], 'maxima': [[7.9342, 399.9992]], 'minima': [[5.9399, 358.5629]], 'inflections': [[6.9371, 379.2819]]})
    
    def test_hyperbolic_models_cubic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['accumulations'], {'range': 6025.275, 'iqr': 2296.493})
    
    def test_hyperbolic_models_cubic_averages(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': -245.1217, 'mean_values_derivative': [3.968, 9.9061], 'average_value_integral': 669.475, 'mean_values_integral': [3.5814]}, 'iqr': {'average_value_derivative': -98.8581, 'mean_values_derivative': [4.9003], 'average_value_integral': 459.2986, 'mean_values_integral': [4.4698]}})
    
    def test_hyperbolic_models_cubic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['cubic']['correlation'], 0.9871)
    
    # HYPERBOLIC MODEL
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
    
    # EXPONENTIAL MODEL
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
    
    # LOGARITHMIC MODEL
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
    
    # LOGISTIC MODEL
    def test_hyperbolic_models_logistic_constants(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['constants'], [4787.0, -0.5355, 0.6592])
    
    def test_hyperbolic_models_logistic_points(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[0.6592, 2393.5]]})
    
    def test_hyperbolic_models_logistic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['accumulations'], {'range': 5357.8057, 'iqr': 2071.3903})
    
    def test_hyperbolic_models_logistic_averages(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': -238.1916, 'mean_values_derivative': [4.6875], 'average_value_integral': 595.3117, 'mean_values_integral': [4.304]}, 'iqr': {'average_value_derivative': -194.2074, 'mean_values_derivative': [5.1556], 'average_value_integral': 414.2781, 'mean_values_integral': [5.06]}})
    
    def test_hyperbolic_models_logistic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['correlation'], 0.9428)
    
    # SINUSOIDAL MODEL
    def test_hyperbolic_models_sinusoidal_constants(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['constants'], [448.548, 1.1869, -0.0788, 746.6978])
    
    def test_hyperbolic_models_sinusoidal_points(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[1.2446, 1195.2458], [6.5384, 1195.2458], ['1.2446 + 5.2938k', 1195.2458]], 'minima': [[3.8915, 298.1498], [9.1853, 298.1498], ['3.8915 + 5.2938k', 298.1498]], 'inflections': [[2.5681, 746.6978], [5.215, 746.6978], [7.8619, 746.6978], ['2.5681 + 2.6469k', 746.6978]]})
    
    def test_hyperbolic_models_sinusoidal_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['accumulations'], {'range': 6517.3946, 'iqr': 3777.0004})
    
    def test_hyperbolic_models_sinusoidal_averages(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': -76.0512, 'mean_values_derivative': [1.3654, 3.7708, 6.6592, 9.0646, '1.3654 + 5.2938k', '3.7708 + 5.2938k'], 'average_value_integral': 724.155, 'mean_values_integral': [2.6105, 5.1726, 7.9043, '2.6105 + 5.2938k', '5.1726 + 5.2938k']}, 'iqr': {'average_value_derivative': 29.3583, 'mean_values_derivative': [3.938, 6.492, '3.938 + 5.2938k', '6.492 + 5.2938k'], 'average_value_integral': 755.4001, 'mean_values_integral': [5.2313, 7.8455, '5.2313 + 5.2938k', '7.8455 + 5.2938k']}})
    
    def test_hyperbolic_models_sinusoidal_correlation(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['correlation'], 0.4914)
    
    # COMPARATIVE ANALYSIS
    def test_hyperbolic_statistics(self):
        self.assertEqual(hyperbolic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_hyperbolic_optimal(self):
        self.assertEqual(hyperbolic_models['optimal']['option'], 'hyperbolic')

exponential_models = run_all(exponential_set)

class TestExponentialModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
    def test_exponential_models_linear_constants(self):
        self.assertEqual(exponential_models['models']['linear']['constants'], [261.1273, -822.4])
    
    def test_exponential_models_linear_points(self):
        self.assertEqual(exponential_models['models']['linear']['points'], {'roots': [[3.1494, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_models_linear_accumulations(self):
        self.assertEqual(exponential_models['models']['linear']['accumulations'], {'range': 5524.1964, 'iqr': 3068.998})
    
    def test_exponential_models_linear_averages(self):
        self.assertEqual(exponential_models['models']['linear']['averages'], {'range': {'average_value_derivative': 261.1273, 'mean_values_derivative': ['All'], 'average_value_integral': 613.7996, 'mean_values_integral': [5.5]}, 'iqr': {'average_value_derivative': 261.1273, 'mean_values_derivative': ['All'], 'average_value_integral': 613.7996, 'mean_values_integral': [5.5]}})
    
    def test_exponential_models_linear_correlation(self):
        self.assertEqual(exponential_models['models']['linear']['correlation'], 0.7988)
    
    # QUADRATIC MODEL
    def test_exponential_models_quadratic_constants(self):
        self.assertEqual(exponential_models['models']['quadratic']['constants'], [69.4091, -502.3727, 704.6])
    
    def test_exponential_models_quadratic_points(self):
        self.assertEqual(exponential_models['models']['quadratic']['points'], {'roots': [[1.9028, 0], [5.3351, 0]], 'maxima': [None], 'minima': [[3.6189, -204.4246]], 'inflections': [None]})
    
    def test_exponential_models_quadratic_accumulations(self):
        self.assertEqual(exponential_models['models']['quadratic']['accumulations'], {'range': 4587.21, 'iqr': 928.902})
    
    def test_exponential_models_quadratic_averages(self):
        self.assertEqual(exponential_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 261.1274, 'mean_values_derivative': [5.5], 'average_value_integral': 509.69, 'mean_values_integral': [6.8265]}, 'iqr': {'average_value_derivative': 261.1274, 'mean_values_derivative': [5.5], 'average_value_integral': 185.7804, 'mean_values_integral': [5.99]}})
    
    def test_exponential_models_quadratic_correlation(self):
        self.assertEqual(exponential_models['models']['quadratic']['correlation'], 0.9626)
    
    # CUBIC MODEL
    def test_exponential_models_cubic_constants(self):
        self.assertEqual(exponential_models['models']['cubic']['constants'], [13.5641, -154.3986, 529.8555, -459.2])
    
    def test_exponential_models_cubic_points(self):
        self.assertEqual(exponential_models['models']['cubic']['points'], {'roots': [[1.3077, 0]], 'maxima': [[2.6214, 113.1144]], 'minima': [[4.9672, 25.5731]], 'inflections': [[3.7943, 69.3435]]})
    
    def test_exponential_models_cubic_accumulations(self):
        self.assertEqual(exponential_models['models']['cubic']['accumulations'], {'range': 4586.9274, 'iqr': 928.787})
    
    def test_exponential_models_cubic_averages(self):
        self.assertEqual(exponential_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 337.086, 'mean_values_derivative': [6.9023], 'average_value_integral': 509.6586, 'mean_values_integral': [7.4133]}, 'iqr': {'average_value_derivative': 147.1886, 'mean_values_derivative': [6.0287], 'average_value_integral': 185.7574, 'mean_values_integral': [6.4967]}})
    
    def test_exponential_models_cubic_correlation(self):
        self.assertEqual(exponential_models['models']['cubic']['correlation'], 0.9956)
    
    # HYPERBOLIC MODEL
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
    
    # EXPONENTIAL MODEL
    def test_exponential_models_exponential_constants(self):
        self.assertEqual(exponential_models['models']['exponential']['constants'], [3.0, 1.9999])
    
    def test_exponential_models_exponential_points(self):
        self.assertEqual(exponential_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_models_exponential_accumulations(self):
        self.assertEqual(exponential_models['models']['exponential']['accumulations'], {'range': 4421.4096, 'iqr': 1073.0052})
    
    def test_exponential_models_exponential_averages(self):
        self.assertEqual(exponential_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 340.4961, 'mean_values_derivative': [7.3559], 'average_value_integral': 491.2677, 'mean_values_integral': [7.3559]}, 'iqr': {'average_value_derivative': 148.7393, 'mean_values_derivative': [6.161], 'average_value_integral': 214.601, 'mean_values_integral': [6.161]}})
    
    def test_exponential_models_exponential_correlation(self):
        self.assertEqual(exponential_models['models']['exponential']['correlation'], 1.0)
    
    # LOGARITHMIC MODEL
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
    
    # LOGISTIC MODEL
    def test_exponential_models_logistic_constants(self):
        self.assertEqual(exponential_models['models']['logistic']['constants'], [6138.0, 0.9655, 10.0383])
    
    def test_exponential_models_logistic_points(self):
        self.assertEqual(exponential_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[10.0383, 3069.0]]})
    
    def test_exponential_models_logistic_accumulations(self):
        self.assertEqual(exponential_models['models']['logistic']['accumulations'], {'range': 4289.0764, 'iqr': 824.4254})
    
    def test_exponential_models_logistic_averages(self):
        self.assertEqual(exponential_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 334.5852, 'mean_values_derivative': [7.1897], 'average_value_integral': 476.564, 'mean_values_integral': [7.475]}, 'iqr': {'average_value_derivative': 149.1394, 'mean_values_derivative': [6.2787], 'average_value_integral': 164.8851, 'mean_values_integral': [6.3203]}})
    
    def test_exponential_models_logistic_correlation(self):
        self.assertEqual(exponential_models['models']['logistic']['correlation'], 0.9983)
    
    # SINUSOIDAL MODEL
    def test_exponential_models_sinusoidal_constants(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['constants'], [3065.0, 0.1022, 9.0, 1641.6143])
    
    def test_exponential_models_sinusoidal_points(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['points'], {'roots': [[3.4695, 0.0], ['3.4695 + 61.4793k', 0.0], ['45.2702 + 61.4793k', 0.0]], 'maxima': [['24.3698 + 61.4794k', 4706.6143]], 'minima': [['55.1095 + 61.4794k', -1423.3857]], 'inflections': [[9.0, 1641.6143], ['9.0 + 30.7397k', 1641.6143]]})
    
    def test_exponential_models_sinusoidal_accumulations(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['accumulations'], {'range': 5453.3258, 'iqr': 2900.6588})
    
    def test_exponential_models_sinusoidal_averages(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 283.1817, 'mean_values_derivative': [4.6782, '4.6782 + 61.4793k', '13.3218 + 61.4793k'], 'average_value_integral': 605.9251, 'mean_values_integral': [5.6273, '5.6273 + 61.4793k', '43.1124 + 61.4793k']}, 'iqr': {'average_value_derivative': 290.2342, 'mean_values_derivative': [5.2263, '5.2263 + 61.4793k', '12.7737 + 61.4793k'], 'average_value_integral': 580.1318, 'mean_values_integral': [5.5396, '5.5396 + 61.4793k', '43.2 + 61.4793k']}})
    
    def test_exponential_models_sinusoidal_correlation(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['correlation'], 0.8194)
    
    # COMPARATIVE ANALYSIS
    def test_exponential_statistics(self):
        self.assertEqual(exponential_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_exponential_optimal(self):
        self.assertEqual(exponential_models['optimal']['option'], 'exponential')

logarithmic_models = run_all(logarithmic_set)

class TestLogarithmicModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
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
    
    # QUADRATIC MODEL
    def test_logarithmic_models_quadratic_constants(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['constants'], [-0.0816, 1.5891, 0.9338])
    
    def test_logarithmic_models_quadratic_points(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['points'], {'roots': [[-0.5709, 0], [20.0452, 0]], 'maxima': [[9.7371, 8.6704]], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_models_quadratic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['accumulations'], {'range': 59.8869, 'iqr': 35.1745})
    
    def test_logarithmic_models_quadratic_averages(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 0.6915, 'mean_values_derivative': [5.5], 'average_value_integral': 6.6541, 'mean_values_integral': [4.7662]}, 'iqr': {'average_value_derivative': 0.6915, 'mean_values_derivative': [5.5], 'average_value_integral': 7.0349, 'mean_values_integral': [5.2602]}})
    
    def test_logarithmic_models_quadratic_correlation(self):
        self.assertEqual(logarithmic_models['models']['quadratic']['correlation'], 0.9932)
    
    # CUBIC MODEL
    def test_logarithmic_models_cubic_constants(self):
        self.assertEqual(logarithmic_models['models']['cubic']['constants'], [0.0127, -0.2911, 2.5553, -0.1555])
    
    def test_logarithmic_models_cubic_points(self):
        self.assertEqual(logarithmic_models['models']['cubic']['points'], {'roots': [[0.0613, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[7.6404, 8.0392]]})
    
    def test_logarithmic_models_cubic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['cubic']['accumulations'], {'range': 60.1767, 'iqr': 35.2935})
    
    def test_logarithmic_models_cubic_averages(self):
        self.assertEqual(logarithmic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.7629, 'mean_values_derivative': [4.2742], 'average_value_integral': 6.6863, 'mean_values_integral': [4.616]}, 'iqr': {'average_value_derivative': 0.5851, 'mean_values_derivative': [5.0588], 'average_value_integral': 7.0587, 'mean_values_integral': [5.2221]}})
    
    def test_logarithmic_models_cubic_correlation(self):
        self.assertEqual(logarithmic_models['models']['cubic']['correlation'], 0.999)
    
    # HYPERBOLIC MODEL
    def test_logarithmic_models_hyperbolic_constants(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['constants'], [-7.5094, 8.7308])
    
    def test_logarithmic_models_hyperbolic_points(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['points'], {'roots': [[0.8601, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_models_hyperbolic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['accumulations'], {'range': 61.2862, 'iqr': 36.2885})
    
    def test_logarithmic_models_hyperbolic_averages(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 0.7509, 'mean_values_derivative': [3.1624], 'average_value_integral': 6.8096, 'mean_values_integral': [3.9087]}, 'iqr': {'average_value_derivative': 0.3129, 'mean_values_derivative': [4.8989], 'average_value_integral': 7.2577, 'mean_values_integral': [5.0977]}})
    
    def test_logarithmic_models_hyperbolic_correlation(self):
        self.assertEqual(logarithmic_models['models']['hyperbolic']['correlation'], 0.9468)
    
    # EXPONENTIAL MODEL
    def test_logarithmic_models_exponential_constants(self):
        self.assertEqual(logarithmic_models['models']['exponential']['constants'], [2.9406, 1.1403])
    
    def test_logarithmic_models_exponential_points(self):
        self.assertEqual(logarithmic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_models_exponential_accumulations(self):
        self.assertEqual(logarithmic_models['models']['exponential']['accumulations'], {'range': 57.7114, 'iqr': 30.8163})
    
    def test_logarithmic_models_exponential_averages(self):
        self.assertEqual(logarithmic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 0.8419, 'mean_values_derivative': [5.9382], 'average_value_integral': 6.4124, 'mean_values_integral': [5.9381]}, 'iqr': {'average_value_derivative': 0.8092, 'mean_values_derivative': [5.6364], 'average_value_integral': 6.1633, 'mean_values_integral': [5.6363]}})
    
    def test_logarithmic_models_exponential_correlation(self):
        self.assertEqual(logarithmic_models['models']['exponential']['correlation'], 0.8554)
    
    # LOGARITHMIC MODEL
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
    
    # LOGISTIC MODEL
    def test_logarithmic_models_logistic_constants(self):
        self.assertEqual(logarithmic_models['models']['logistic']['constants'], [8.6893, 0.5704, 2.5092])
    
    def test_logarithmic_models_logistic_points(self):
        self.assertEqual(logarithmic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[2.5092, 4.3446]]})
    
    def test_logarithmic_models_logistic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['logistic']['accumulations'], {'range': 59.929, 'iqr': 35.5215})
    
    def test_logarithmic_models_logistic_averages(self):
        self.assertEqual(logarithmic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.6653, 'mean_values_derivative': [5.4198], 'average_value_integral': 6.6588, 'mean_values_integral': [4.5913]}, 'iqr': {'average_value_derivative': 0.6754, 'mean_values_derivative': [5.3806], 'average_value_integral': 7.1043, 'mean_values_integral': [5.1391]}})
    
    def test_logarithmic_models_logistic_correlation(self):
        self.assertEqual(logarithmic_models['models']['logistic']['correlation'], 0.9898)
    
    # SINUSOIDAL MODEL
    def test_logarithmic_models_sinusoidal_constants(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['constants'], [-1.3224, 1.2013, 0.1451, 6.5218])
    
    def test_logarithmic_models_sinusoidal_points(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[4.0678, 7.8442], [9.2982, 7.8442], ['4.0678 + 5.2304k', 7.8442]], 'minima': [[1.4527, 5.1994], [6.6831, 5.1994], ['1.4527 + 5.2304k', 5.1994]], 'inflections': [[2.7603, 6.5218], [5.3755, 6.5218], [7.9907, 6.5218], ['2.7603 + 2.6152k', 6.5218]]})
    
    def test_logarithmic_models_sinusoidal_accumulations(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['accumulations'], {'range': 58.9487, 'iqr': 32.5638})
    
    def test_logarithmic_models_sinusoidal_averages(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.2235, 'mean_values_derivative': [1.5702, 3.9503, 6.8005, 9.1806, '1.5702 + 5.2303k', '3.9503 + 5.2303k'], 'average_value_integral': 6.5499, 'mean_values_integral': [2.778, 5.3577, 8.0083, '2.778 + 5.2303k', '5.3577 + 5.2303k']}, 'iqr': {'average_value_derivative': -0.0721, 'mean_values_derivative': [4.1056, 6.6452, '4.1056 + 5.2303k', '6.6452 + 5.2303k'], 'average_value_integral': 6.5128, 'mean_values_integral': [5.3811, 7.9849, '5.3811 + 5.2303k', '7.9849 + 5.2303k']}})
    
    def test_logarithmic_models_sinusoidal_correlation(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['correlation'], 0.4601)
    
    # COMPARATIVE ANALYSIS
    def test_logarithmic_statistics(self):
        self.assertEqual(logarithmic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_logarithmic_optimal(self):
        self.assertEqual(logarithmic_models['optimal']['option'], 'logarithmic')

logistic_models = run_all(logistic_set)

class TestLogisticModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
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
    
    # QUADRATIC MODEL
    def test_logistic_models_quadratic_constants(self):
        self.assertEqual(logistic_models['models']['quadratic']['constants'], [-0.0148, 0.4567, -0.8438])
    
    def test_logistic_models_quadratic_points(self):
        self.assertEqual(logistic_models['models']['quadratic']['points'], {'roots': [[1.9739, 0], [28.8842, 0]], 'maxima': [[15.4291, 2.6794]], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_models_quadratic_accumulations(self):
        self.assertEqual(logistic_models['models']['quadratic']['accumulations'], {'range': 10.1124, 'iqr': 5.961})
    
    def test_logistic_models_quadratic_averages(self):
        self.assertEqual(logistic_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 0.2939, 'mean_values_derivative': [5.5], 'average_value_integral': 1.1236, 'mean_values_integral': [5.1761]}, 'iqr': {'average_value_derivative': 0.2939, 'mean_values_derivative': [5.5], 'average_value_integral': 1.1922, 'mean_values_integral': [5.4047]}})
    
    def test_logistic_models_quadratic_correlation(self):
        self.assertEqual(logistic_models['models']['quadratic']['correlation'], 0.9236)
    
    # CUBIC MODEL
    def test_logistic_models_cubic_constants(self):
        self.assertEqual(logistic_models['models']['cubic']['constants'], [-0.0162, 0.2531, -0.7789, 0.5493])
    
    def test_logistic_models_cubic_points(self):
        self.assertEqual(logistic_models['models']['cubic']['points'], {'roots': [[1.0231, 0], [2.8114, 0], [11.789, 0]], 'maxima': [[8.5387, 2.2665]], 'minima': [[1.877, -0.1281]], 'inflections': [[5.2078, 1.0692]]})
    
    def test_logistic_models_cubic_accumulations(self):
        self.assertEqual(logistic_models['models']['cubic']['accumulations'], {'range': 10.7028, 'iqr': 6.198})
    
    def test_logistic_models_cubic_averages(self):
        self.assertEqual(logistic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.207, 'mean_values_derivative': [2.5934, 7.8223], 'average_value_integral': 1.1892, 'mean_values_integral': [5.4307]}, 'iqr': {'average_value_derivative': 0.4338, 'mean_values_derivative': [3.7352, 6.6805], 'average_value_integral': 1.2396, 'mean_values_integral': [5.5248]}})
    
    def test_logistic_models_cubic_correlation(self):
        self.assertEqual(logistic_models['models']['cubic']['correlation'], 0.9739)
    
    # HYPERBOLIC MODEL
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
    
    # EXPONENTIAL MODEL
    def test_logistic_models_exponential_constants(self):
        self.assertEqual(logistic_models['models']['exponential']['constants'], [0.0001, 3.5891])
    
    def test_logistic_models_exponential_points(self):
        self.assertEqual(logistic_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logistic_models_exponential_accumulations(self):
        self.assertEqual(logistic_models['models']['exponential']['accumulations'], {'range': 35.4691, 'iqr': 2.7489})
    
    def test_logistic_models_exponential_averages(self):
        self.assertEqual(logistic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 3.941, 'mean_values_derivative': [8.0887], 'average_value_integral': 3.941, 'mean_values_integral': [8.2806]}, 'iqr': {'average_value_derivative': 0.5498, 'mean_values_derivative': [6.5474], 'average_value_integral': 0.5498, 'mean_values_integral': [6.7393]}})
    
    def test_logistic_models_exponential_correlation(self):
        self.assertEqual(logistic_models['models']['exponential']['correlation'], 0.0)
    
    # LOGARITHMIC MODEL
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
    
    # LOGISTIC MODEL
    def test_logistic_models_logistic_constants(self):
        self.assertEqual(logistic_models['models']['logistic']['constants'], [2.0, 3.0, 5.0])
    
    def test_logistic_models_logistic_points(self):
        self.assertEqual(logistic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[5.0, 1.0]]})
    
    def test_logistic_models_logistic_accumulations(self):
        self.assertEqual(logistic_models['models']['logistic']['accumulations'], {'range': 10.0004, 'iqr': 5.9987})
    
    def test_logistic_models_logistic_averages(self):
        self.assertEqual(logistic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.2222, 'mean_values_derivative': [3.9275, 6.0721], 'average_value_integral': 1.1112, 'mean_values_integral': [5.0744]}, 'iqr': {'average_value_derivative': 0.399, 'mean_values_derivative': [4.146, 5.8538], 'average_value_integral': 1.1997, 'mean_values_integral': [5.1349]}})
    
    def test_logistic_models_logistic_correlation(self):
        self.assertEqual(logistic_models['models']['logistic']['correlation'], 1.0)
    
    # SINUSOIDAL MODEL
    def test_logistic_models_sinusoidal_constants(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['constants'], [-1.1746, 0.5011, -1.1199, 1.0508])
    
    def test_logistic_models_sinusoidal_points(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['points'], {'roots': [[1.0903, 0.0], [2.9393, 0.0], ['1.0903 + 12.5388k', 0.0], ['2.9393 + 12.5388k', 0.0]], 'maxima': [[8.2842, 2.2254], ['8.2842 + 12.5388k', 2.2254]], 'minima': [[2.0148, -0.1238], ['2.0148 + 12.5388k', -0.1238]], 'inflections': [[5.1495, 1.0508], ['5.1495 + 6.2694k', 1.0508]]})
    
    def test_logistic_models_sinusoidal_accumulations(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['accumulations'], {'range': 10.0921, 'iqr': 6.0321})
    
    def test_logistic_models_sinusoidal_averages(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.1992, 'mean_values_derivative': [2.7038, 7.5952, '2.7038 + 12.5388k', '7.5952 + 12.5388k'], 'average_value_integral': 1.1213, 'mean_values_integral': [5.2693, '5.2693 + 12.5388k', '11.2991 + 12.5388k']}, 'iqr': {'average_value_derivative': 0.4394, 'mean_values_derivative': [3.6968, 6.6022, '3.6968 + 12.5388k', '6.6022 + 12.5388k'], 'average_value_integral': 1.2064, 'mean_values_integral': [5.4146, '5.4146 + 12.5388k', '11.1538 + 12.5388k']}})
    
    def test_logistic_models_sinusoidal_correlation(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['correlation'], 0.9789)
    
    # COMPARATIVE ANALYSIS
    def test_logistic_statistics(self):
        self.assertEqual(logistic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_logistic_optimal(self):
        self.assertEqual(logistic_models['optimal']['option'], 'logistic')

sinusoidal_models = run_all(sinusoidal_set)

class TestSinusoidalModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
    def test_sinusoidal_models_linear_constants(self):
        self.assertEqual(sinusoidal_models['models']['linear']['constants'], [0.0303, 3.3333])
    
    def test_sinusoidal_models_linear_points(self):
        self.assertEqual(sinusoidal_models['models']['linear']['points'], {'roots': [[-110.0099, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_sinusoidal_models_linear_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['linear']['accumulations'], {'range': 31.5045, 'iqr': 17.5025})
    
    def test_sinusoidal_models_linear_averages(self):
        self.assertEqual(sinusoidal_models['models']['linear']['averages'], {'range': {'average_value_derivative': 0.0303, 'mean_values_derivative': ['All'], 'average_value_integral': 3.5005, 'mean_values_integral': [5.5182]}, 'iqr': {'average_value_derivative': 0.0303, 'mean_values_derivative': ['All'], 'average_value_integral': 3.5005, 'mean_values_integral': [5.5182]}})
    
    def test_sinusoidal_models_linear_correlation(self):
        self.assertEqual(sinusoidal_models['models']['linear']['correlation'], 0.0249)
    
    # QUADRATIC MODEL
    def test_sinusoidal_models_quadratic_constants(self):
        self.assertEqual(sinusoidal_models['models']['quadratic']['constants'], [0.1515, -1.6364, 6.6667])
    
    def test_sinusoidal_models_quadratic_points(self):
        self.assertEqual(sinusoidal_models['models']['quadratic']['points'], {'roots': [None], 'maxima': [None], 'minima': [[5.4007, 2.2479]], 'inflections': [None]})
    
    def test_sinusoidal_models_quadratic_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['quadratic']['accumulations'], {'range': 29.448, 'iqr': 12.825})
    
    def test_sinusoidal_models_quadratic_averages(self):
        self.assertEqual(sinusoidal_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 0.0301, 'mean_values_derivative': [5.5], 'average_value_integral': 3.272, 'mean_values_integral': [2.8007, 8.0006]}, 'iqr': {'average_value_derivative': 0.0301, 'mean_values_derivative': [5.5], 'average_value_integral': 2.565, 'mean_values_integral': [3.9539, 6.8475]}})
    
    def test_sinusoidal_models_quadratic_correlation(self):
        self.assertEqual(sinusoidal_models['models']['quadratic']['correlation'], 0.3155)
    
    # CUBIC MODEL
    def test_sinusoidal_models_cubic_constants(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['constants'], [0.0466, -0.6177, 1.9114, 2.6667])
    
    def test_sinusoidal_models_cubic_points(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['points'], {'roots': [[-1.0275, 0]], 'maxima': [[1.9997, 4.3915]], 'minima': [[6.8372, 1.7538]], 'inflections': [[4.4185, 3.0726]]})
    
    def test_sinusoidal_models_cubic_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['accumulations'], {'range': 29.9088, 'iqr': 13.011})
    
    def test_sinusoidal_models_cubic_averages(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.2893, 'mean_values_derivative': [1.6043, 7.2327], 'average_value_integral': 3.3232, 'mean_values_integral': [4.1105, 8.7533]}, 'iqr': {'average_value_derivative': -0.3631, 'mean_values_derivative': [6.2221], 'average_value_integral': 2.6022, 'mean_values_integral': [5.0052]}})
    
    def test_sinusoidal_models_cubic_correlation(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['correlation'], 0.3929)
    
    # HYPERBOLIC MODEL
    def test_sinusoidal_models_hyperbolic_constants(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['constants'], [0.7138, 3.2909])
    
    def test_sinusoidal_models_hyperbolic_points(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['points'], {'roots': [[-0.2169, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_sinusoidal_models_hyperbolic_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['accumulations'], {'range': 31.2617, 'iqr': 17.1546})
    
    def test_sinusoidal_models_hyperbolic_averages(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': -0.0714, 'mean_values_derivative': [3.1618], 'average_value_integral': 3.4735, 'mean_values_integral': [3.9091]}, 'iqr': {'average_value_derivative': -0.0297, 'mean_values_derivative': [4.9024], 'average_value_integral': 3.4309, 'mean_values_integral': [5.0986]}})
    
    def test_sinusoidal_models_hyperbolic_correlation(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['correlation'], 0.0537)
    
    # EXPONENTIAL MODEL
    def test_sinusoidal_models_exponential_constants(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['constants'], [0.9234, 0.8984])
    
    def test_sinusoidal_models_exponential_points(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_sinusoidal_models_exponential_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['accumulations'], {'range': 4.7909, 'iqr': 2.5919})
    
    def test_sinusoidal_models_exponential_averages(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -0.057, 'mean_values_derivative': [5.1465], 'average_value_integral': 0.5323, 'mean_values_integral': [5.1415]}, 'iqr': {'average_value_derivative': -0.0555, 'mean_values_derivative': [5.3954], 'average_value_integral': 0.5184, 'mean_values_integral': [5.3884]}})
    
    def test_sinusoidal_models_exponential_correlation(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['correlation'], 0.0)
    
    # LOGARITHMIC MODEL
    def test_sinusoidal_models_logarithmic_constants(self):
        self.assertEqual(sinusoidal_models['models']['logarithmic']['constants'], [-0.1951, 3.7947])
    
    def test_sinusoidal_models_logarithmic_points(self):
        self.assertEqual(sinusoidal_models['models']['logarithmic']['points'], {'roots': [[279923141.2405, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_sinusoidal_models_logarithmic_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['logarithmic']['accumulations'], {'range': 31.4159, 'iqr': 17.3464})
    
    def test_sinusoidal_models_logarithmic_averages(self):
        self.assertEqual(sinusoidal_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': -0.0499, 'mean_values_derivative': [3.9098], 'average_value_integral': 3.4907, 'mean_values_integral': [4.7501]}, 'iqr': {'average_value_derivative': -0.0383, 'mean_values_derivative': [5.094], 'average_value_integral': 3.4693, 'mean_values_integral': [5.3008]}})
    
    def test_sinusoidal_models_logarithmic_correlation(self):
        self.assertEqual(sinusoidal_models['models']['logarithmic']['correlation'], 0.0388)
    
    # LOGISTIC MODEL
    def test_sinusoidal_models_logistic_constants(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['constants'], [7.5777, 0.017, 14.5])
    
    def test_sinusoidal_models_logistic_points(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[14.5, 3.7889]]})
    
    def test_sinusoidal_models_logistic_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['accumulations'], {'range': 31.4974, 'iqr': 17.498})
    
    def test_sinusoidal_models_logistic_averages(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.032, 'mean_values_derivative': [5.2092], 'average_value_integral': 3.4997, 'mean_values_integral': [5.5042]}, 'iqr': {'average_value_derivative': 0.032, 'mean_values_derivative': [5.2092], 'average_value_integral': 3.4996, 'mean_values_integral': [5.501]}})
    
    def test_sinusoidal_models_logistic_correlation(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['correlation'], 0.0254)
    
    # SINUSOIDAL MODEL
    def test_sinusoidal_models_sinusoidal_constants(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['constants'], [-5.0, 1.5708, 3.0, 3.0])
    
    def test_sinusoidal_models_sinusoidal_points(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['points'], {'roots': [[3.4097, 0], [4.5903, 0], [7.4097, 0], [8.5903, 0], ['3.4097 + 4.0k', 0], ['4.5903 + 4.0k', 0]], 'maxima': [[6.0, 8.0], [10.0, 8.0], ['6.0 + 4.0k', 8.0]], 'minima': [[4.0, -2.0], [8.0, -2.0], ['4.0 + 4.0k', -2.0]], 'inflections': [[3.0, 3.0], [5.0, 3.0], [7.0, 3.0], [9.0, 3.0], ['3.0 + 2.0k', 3.0]]})
    
    def test_sinusoidal_models_sinusoidal_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['accumulations'], {'range': 30.1832, 'iqr': 11.8168})
    
    def test_sinusoidal_models_sinusoidal_averages(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.5556, 'mean_values_derivative': [4.0451, 5.9549, 8.0451, 9.9549, '4.0451 + 4.0k', '5.9549 + 4.0k'], 'average_value_integral': 3.3537, 'mean_values_integral': [2.9549, 5.0451, 6.9549, 9.0451, '2.9549 + 4.0k', '5.0451 + 4.0k']}, 'iqr': {'average_value_derivative': -1.0, 'mean_values_derivative': [3.9187, 6.0813, 7.9187, '3.9187 + 4.0k', '6.0813 + 4.0k'], 'average_value_integral': 2.3634, 'mean_values_integral': [3.0813, 4.9187, 7.0813, '3.0813 + 4.0k', '4.9187 + 4.0k']}})
    
    def test_sinusoidal_models_sinusoidal_correlation(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['correlation'], 1.0)
    
    # COMPARATIVE ANALYSIS
    def test_sinusoidal_statistics(self):
        self.assertEqual(sinusoidal_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_sinusoidal_optimal(self):
        self.assertEqual(sinusoidal_models['optimal']['option'], 'sinusoidal')

weather_models = run_all(weather_set)

class TestWeatherModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
    def test_weather_models_linear_constants(self):
        self.assertEqual(weather_models['models']['linear']['constants'], [0.7273, 67.7727])
    
    def test_weather_models_linear_points(self):
        self.assertEqual(weather_models['models']['linear']['points'], {'roots': [[-93.184, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_weather_models_linear_accumulations(self):
        self.assertEqual(weather_models['models']['linear']['accumulations'], {'range': 797.4945, 'iqr': 434.9969})
    
    def test_weather_models_linear_averages(self):
        self.assertEqual(weather_models['models']['linear']['averages'], {'range': {'average_value_derivative': 0.7273, 'mean_values_derivative': ['All'], 'average_value_integral': 72.4995, 'mean_values_integral': [6.4991]}, 'iqr': {'average_value_derivative': 0.7273, 'mean_values_derivative': ['All'], 'average_value_integral': 72.4995, 'mean_values_integral': [6.4991]}})
    
    def test_weather_models_linear_correlation(self):
        self.assertEqual(weather_models['models']['linear']['correlation'], 0.1994)
    
    # QUADRATIC MODEL
    def test_weather_models_quadratic_constants(self):
        self.assertEqual(weather_models['models']['quadratic']['constants'], [-1.1374, 15.513, 33.2727])
    
    def test_weather_models_quadratic_points(self):
        self.assertEqual(weather_models['models']['quadratic']['points'], {'roots': [[-1.8845, 0.0], [15.5235, 0.0]], 'maxima': [[6.8195, 86.1682]], 'minima': [None], 'inflections': [None]})
    
    def test_weather_models_quadratic_accumulations(self):
        self.assertEqual(weather_models['models']['quadratic']['accumulations'], {'range': 820.4735, 'iqr': 495.8662})
    
    def test_weather_models_quadratic_averages(self):
        self.assertEqual(weather_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 0.7268, 'mean_values_derivative': [6.5], 'average_value_integral': 74.5885, 'mean_values_integral': [3.6288, 10.0102]}, 'iqr': {'average_value_derivative': 0.7268, 'mean_values_derivative': [6.5], 'average_value_integral': 82.6444, 'mean_values_integral': [5.0594, 8.5796]}})
    
    def test_weather_models_quadratic_correlation(self):
        self.assertEqual(weather_models['models']['quadratic']['correlation'], 0.9731)
    
    # CUBIC MODEL
    def test_weather_models_cubic_constants(self):
        self.assertEqual(weather_models['models']['cubic']['constants'], [-0.0694, 0.2162, 8.19, 42.7475])
    
    def test_weather_models_cubic_points(self):
        self.assertEqual(weather_models['models']['cubic']['points'], {'roots': [[14.3401, 0]], 'maxima': [[7.3957, 87.0701]], 'minima': [[-5.3189, 15.7451]], 'inflections': [[1.0384, 51.4074]]})
    
    def test_weather_models_cubic_accumulations(self):
        self.assertEqual(weather_models['models']['cubic']['accumulations'], {'range': 819.5352, 'iqr': 495.5075})
    
    def test_weather_models_cubic_averages(self):
        self.assertEqual(weather_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.1048, 'mean_values_derivative': [7.356], 'average_value_integral': 74.5032, 'mean_values_integral': [3.9967, 10.2683]}, 'iqr': {'average_value_derivative': 1.5796, 'mean_values_derivative': [6.768], 'average_value_integral': 82.5846, 'mean_values_integral': [5.4533, 9.1571]}})
    
    def test_weather_models_cubic_correlation(self):
        self.assertEqual(weather_models['models']['cubic']['correlation'], 0.9881)
    
    # HYPERBOLIC MODEL
    def test_weather_models_hyperbolic_constants(self):
        self.assertEqual(weather_models['models']['hyperbolic']['constants'], [-28.1904, 79.7901])
    
    def test_weather_models_hyperbolic_points(self):
        self.assertEqual(weather_models['models']['hyperbolic']['points'], {'roots': [[0.3533, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_weather_models_hyperbolic_accumulations(self):
        self.assertEqual(weather_models['models']['hyperbolic']['accumulations'], {'range': 807.6406, 'iqr': 450.5916})
    
    def test_weather_models_hyperbolic_averages(self):
        self.assertEqual(weather_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 2.3492, 'mean_values_derivative': [3.4641], 'average_value_integral': 73.4219, 'mean_values_integral': [4.4267]}, 'iqr': {'average_value_derivative': 0.8478, 'mean_values_derivative': [5.7664], 'average_value_integral': 75.0986, 'mean_values_integral': [6.0088]}})
    
    def test_weather_models_hyperbolic_correlation(self):
        self.assertEqual(weather_models['models']['hyperbolic']['correlation'], 0.5643)
    
    # EXPONENTIAL MODEL
    def test_weather_models_exponential_constants(self):
        self.assertEqual(weather_models['models']['exponential']['constants'], [66.593, 1.0107])
    
    def test_weather_models_exponential_points(self):
        self.assertEqual(weather_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_weather_models_exponential_accumulations(self):
        self.assertEqual(weather_models['models']['exponential']['accumulations'], {'range': 785.4418, 'iqr': 428.2509})
    
    def test_weather_models_exponential_averages(self):
        self.assertEqual(weather_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 0.76, 'mean_values_derivative': [6.5583], 'average_value_integral': 71.4038, 'mean_values_integral': [6.5537]}, 'iqr': {'average_value_derivative': 0.7597, 'mean_values_derivative': [6.5213], 'average_value_integral': 71.3752, 'mean_values_integral': [6.516]}})
    
    def test_weather_models_exponential_correlation(self):
        self.assertEqual(weather_models['models']['exponential']['correlation'], 0.1604)
    
    # LOGARITHMIC MODEL
    def test_weather_models_logarithmic_constants(self):
        self.assertEqual(weather_models['models']['logarithmic']['constants'], [7.7255, 59.6324])
    
    def test_weather_models_logarithmic_points(self):
        self.assertEqual(weather_models['models']['logarithmic']['points'], {'roots': [[0.0004, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_weather_models_logarithmic_accumulations(self):
        self.assertEqual(weather_models['models']['logarithmic']['accumulations'], {'range': 801.3417, 'iqr': 442.795})
    
    def test_weather_models_logarithmic_averages(self):
        self.assertEqual(weather_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 1.7452, 'mean_values_derivative': [4.4267], 'average_value_integral': 72.8492, 'mean_values_integral': [5.5334]}, 'iqr': {'average_value_derivative': 1.2857, 'mean_values_derivative': [6.0088], 'average_value_integral': 73.7992, 'mean_values_integral': [6.2574]}})
    
    def test_weather_models_logarithmic_correlation(self):
        self.assertEqual(weather_models['models']['logarithmic']['correlation'], 0.4439)
    
    # LOGISTIC MODEL
    def test_weather_models_logistic_constants(self):
        self.assertEqual(weather_models['models']['logistic']['constants'], [77.223, 0.8019, 0.2482])
    
    def test_weather_models_logistic_points(self):
        self.assertEqual(weather_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[0.2482, 38.6115]]})
    
    def test_weather_models_logistic_accumulations(self):
        self.assertEqual(weather_models['models']['logistic']['accumulations'], {'range': 807.4282, 'iqr': 456.5467})
    
    def test_weather_models_logistic_averages(self):
        self.assertEqual(weather_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 2.4824, 'mean_values_derivative': [4.1519], 'average_value_integral': 73.4026, 'mean_values_integral': [3.934]}, 'iqr': {'average_value_derivative': 0.8758, 'mean_values_derivative': [5.5191], 'average_value_integral': 76.0911, 'mean_values_integral': [5.4958]}})
    
    def test_weather_models_logistic_correlation(self):
        self.assertEqual(weather_models['models']['logistic']['correlation'], 0.6298)
    
    # SINUSOIDAL MODEL
    def test_weather_models_sinusoidal_constants(self):
        self.assertEqual(weather_models['models']['sinusoidal']['constants'], [16.722, -0.6093, -11.0, 74.6609])
    
    def test_weather_models_sinusoidal_points(self):
        self.assertEqual(weather_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[7.0464, 91.3829], ['7.0464 + 10.3122k', 91.3829]], 'minima': [[1.8902, 57.9389], ['1.8902 + 10.3122k', 57.9389]], 'inflections': [[4.4683, 74.6609], [9.6244, 74.6609], ['4.4683 + 5.1561k', 74.6609]]})
    
    def test_weather_models_sinusoidal_accumulations(self):
        self.assertEqual(weather_models['models']['sinusoidal']['accumulations'], {'range': 810.4781, 'iqr': 498.1373})
    
    def test_weather_models_sinusoidal_averages(self):
        self.assertEqual(weather_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': -0.2066, 'mean_values_derivative': [1.8568, 7.0794, '1.8568 + 10.3121k', '7.0794 + 10.3121k'], 'average_value_integral': 73.6798, 'mean_values_integral': [4.3718, 9.7205, '4.3718 + 10.3121k', '9.7205 + 10.3121k']}, 'iqr': {'average_value_derivative': 1.7612, 'mean_values_derivative': [6.761, '6.761 + 10.3121k', '12.4873 + 10.3121k'], 'average_value_integral': 83.0229, 'mean_values_integral': [5.3276, 8.7647, '5.3276 + 10.3121k', '8.7647 + 10.3121k']}})
    
    def test_weather_models_sinusoidal_correlation(self):
        self.assertEqual(weather_models['models']['sinusoidal']['correlation'], 0.9689)
    
    # COMPARATIVE ANALYSIS
    def test_weather_statistics(self):
        self.assertEqual(weather_models['statistics'], {'minimum': 1, 'maximum': 12, 'q1': 3.5, 'q3': 9.5, 'mean': 6.5, 'median': 6.5})
    
    def test_weather_optimal(self):
        self.assertEqual(weather_models['optimal']['option'], 'cubic')

disease_models = run_all(disease_set)

class TestDiseaseModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
    def test_disease_models_linear_constants(self):
        self.assertEqual(disease_models['models']['linear']['constants'], [32539.7203, -63428.1818])
    
    def test_disease_models_linear_points(self):
        self.assertEqual(disease_models['models']['linear']['points'], {'roots': [[1.9493, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_disease_models_linear_accumulations(self):
        self.assertEqual(disease_models['models']['linear']['accumulations'], {'range': 1628880.0088, 'iqr': 888480.0047})
    
    def test_disease_models_linear_averages(self):
        self.assertEqual(disease_models['models']['linear']['averages'], {'range': {'average_value_derivative': 32539.7203, 'mean_values_derivative': ['All'], 'average_value_integral': 148080.0008, 'mean_values_integral': [6.5]}, 'iqr': {'average_value_derivative': 32539.7203, 'mean_values_derivative': ['All'], 'average_value_integral': 148080.0008, 'mean_values_integral': [6.5]}})
    
    def test_disease_models_linear_correlation(self):
        self.assertEqual(disease_models['models']['linear']['correlation'], 0.9795)
    
    # QUADRATIC MODEL
    def test_disease_models_quadratic_constants(self):
        self.assertEqual(disease_models['models']['quadratic']['constants'], [1216.7547, 16721.9086, -26519.9545])
    
    def test_disease_models_quadratic_points(self):
        self.assertEqual(disease_models['models']['quadratic']['points'], {'roots': [[-15.179, 0.0], [1.4359, 0.0]], 'maxima': [None], 'minima': [[-6.8715, -83972.4195]], 'inflections': [None]})
    
    def test_disease_models_quadratic_accumulations(self):
        self.assertEqual(disease_models['models']['quadratic']['accumulations'], {'range': 1604342.0877, 'iqr': 823383.6095})
    
    def test_disease_models_quadratic_averages(self):
        self.assertEqual(disease_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 32539.7197, 'mean_values_derivative': [6.5], 'average_value_integral': 145849.2807, 'mean_values_integral': [6.8719]}, 'iqr': {'average_value_derivative': 32539.7197, 'mean_values_derivative': [6.5], 'average_value_integral': 137230.6016, 'mean_values_integral': [6.6117]}})
    
    def test_disease_models_quadratic_correlation(self):
        self.assertEqual(disease_models['models']['quadratic']['correlation'], 0.9859)
    
    # CUBIC MODEL
    def test_disease_models_cubic_constants(self):
        self.assertEqual(disease_models['models']['cubic']['constants'], [247.9681, -3618.624, 42882.5477, -60367.6061])
    
    def test_disease_models_cubic_points(self):
        self.assertEqual(disease_models['models']['cubic']['points'], {'roots': [[1.6001, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[4.8644, 91146.927]]})
    
    def test_disease_models_cubic_accumulations(self):
        self.assertEqual(disease_models['models']['cubic']['accumulations'], {'range': 1604341.4046, 'iqr': 823383.3516})
    
    def test_disease_models_cubic_averages(self):
        self.assertEqual(disease_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 34771.4274, 'mean_values_derivative': [1.2924, 8.4363], 'average_value_integral': 145849.2186, 'mean_values_integral': [6.9405]}, 'iqr': {'average_value_derivative': 29502.1053, 'mean_values_derivative': [7.2467], 'average_value_integral': 137230.5586, 'mean_values_integral': [6.633]}})
    
    def test_disease_models_cubic_correlation(self):
        self.assertEqual(disease_models['models']['cubic']['correlation'], 0.9882)
    
    # HYPERBOLIC MODEL
    def test_disease_models_hyperbolic_constants(self):
        self.assertEqual(disease_models['models']['hyperbolic']['constants'], [-321000.1953, 231090.9361])
    
    def test_disease_models_hyperbolic_points(self):
        self.assertEqual(disease_models['models']['hyperbolic']['points'], {'roots': [[1.3891, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_disease_models_hyperbolic_accumulations(self):
        self.assertEqual(disease_models['models']['hyperbolic']['accumulations'], {'range': 1744344.7772, 'iqr': 1066017.6671})
    
    def test_disease_models_hyperbolic_averages(self):
        self.assertEqual(disease_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 26750.0163, 'mean_values_derivative': [3.4641], 'average_value_integral': 158576.7979, 'mean_values_integral': [4.4267]}, 'iqr': {'average_value_derivative': 9654.1412, 'mean_values_derivative': [5.7663], 'average_value_integral': 177669.6112, 'mean_values_integral': [6.0088]}})
    
    def test_disease_models_hyperbolic_correlation(self):
        self.assertEqual(disease_models['models']['hyperbolic']['correlation'], 0.7056)
    
    # EXPONENTIAL MODEL
    def test_disease_models_exponential_constants(self):
        self.assertEqual(disease_models['models']['exponential']['constants'], [101.8906, 2.3453])
    
    def test_disease_models_exponential_points(self):
        self.assertEqual(disease_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_disease_models_exponential_accumulations(self):
        self.assertEqual(disease_models['models']['exponential']['accumulations'], {'range': 3309999.1694, 'iqr': 390616.9316})
    
    def test_disease_models_exponential_averages(self):
        self.assertEqual(disease_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 256498.8938, 'mean_values_derivative': [9.3742], 'average_value_integral': 300909.0154, 'mean_values_integral': [9.3742]}, 'iqr': {'average_value_derivative': 55494.5215, 'mean_values_derivative': [7.5783], 'average_value_integral': 65102.8219, 'mean_values_integral': [7.5783]}})
    
    def test_disease_models_exponential_correlation(self):
        self.assertEqual(disease_models['models']['exponential']['correlation'], 0.0)
    
    # LOGARITHMIC MODEL
    def test_disease_models_logarithmic_constants(self):
        self.assertEqual(disease_models['models']['logarithmic']['constants'], [141709.0574, -87950.7771])
    
    def test_disease_models_logarithmic_points(self):
        self.assertEqual(disease_models['models']['logarithmic']['points'], {'roots': [[1.8601, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_disease_models_logarithmic_accumulations(self):
        self.assertEqual(disease_models['models']['logarithmic']['accumulations'], {'range': 1699347.1693, 'iqr': 1031463.6528})
    
    def test_disease_models_logarithmic_averages(self):
        self.assertEqual(disease_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 32012.1617, 'mean_values_derivative': [4.4267], 'average_value_integral': 154486.1063, 'mean_values_integral': [5.5334]}, 'iqr': {'average_value_derivative': 23583.4299, 'mean_values_derivative': [6.0088], 'average_value_integral': 171910.6088, 'mean_values_integral': [6.2574]}})
    
    def test_disease_models_logarithmic_correlation(self):
        self.assertEqual(disease_models['models']['logarithmic']['correlation'], 0.8943)
    
    # LOGISTIC MODEL
    def test_disease_models_logistic_constants(self):
        self.assertEqual(disease_models['models']['logistic']['constants'], [564204.8773, 0.3277, 10.4152])
    
    def test_disease_models_logistic_points(self):
        self.assertEqual(disease_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[10.4152, 282102.4387]]})
    
    def test_disease_models_logistic_accumulations(self):
        self.assertEqual(disease_models['models']['logistic']['accumulations'], {'range': 1620921.052, 'iqr': 784603.8887})
    
    def test_disease_models_logistic_averages(self):
        self.assertEqual(disease_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 29917.1189, 'mean_values_derivative': [6.2424], 'average_value_integral': 147356.4593, 'mean_values_integral': [7.242]}, 'iqr': {'average_value_derivative': 31182.7046, 'mean_values_derivative': [6.4595], 'average_value_integral': 130767.3148, 'mean_values_integral': [6.7584]}})
    
    def test_disease_models_logistic_correlation(self):
        self.assertEqual(disease_models['models']['logistic']['correlation'], 0.9756)
    
    # SINUSOIDAL MODEL
    def test_disease_models_sinusoidal_constants(self):
        self.assertEqual(disease_models['models']['sinusoidal']['constants'], [382575.0, 0.098, 11.0, 302192.3729])
    
    def test_disease_models_sinusoidal_points(self):
        self.assertEqual(disease_models['models']['sinusoidal']['points'], {'roots': [[1.7079, 0.0], ['1.7079 + 64.1141k', 0.0], ['52.3492 + 64.1141k', 0.0]], 'maxima': [['27.0285 + 64.1142k', 684767.3729]], 'minima': [['59.0856 + 64.1142k', -80382.6271]], 'inflections': [[11.0, 302192.3729], ['11.0 + 32.0571k', 302192.3729]]})
    
    def test_disease_models_sinusoidal_accumulations(self):
        self.assertEqual(disease_models['models']['sinusoidal']['accumulations'], {'range': 1613540.1441, 'iqr': 847409.2779})
    
    def test_disease_models_sinusoidal_averages(self):
        self.assertEqual(disease_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 32287.2634, 'mean_values_derivative': [5.5589, '5.5589 + 64.1141k', '16.4411 + 64.1141k'], 'average_value_integral': 146685.4676, 'mean_values_integral': [6.7287, '6.7287 + 64.1141k', '47.3284 + 64.1141k']}, 'iqr': {'average_value_derivative': 33418.9467, 'mean_values_derivative': [6.1993, '6.1993 + 64.1141k', '15.8007 + 64.1141k'], 'average_value_integral': 141234.8796, 'mean_values_integral': [6.569, '6.569 + 64.1141k', '47.4881 + 64.1141k']}})
    
    def test_disease_models_sinusoidal_correlation(self):
        self.assertEqual(disease_models['models']['sinusoidal']['correlation'], 0.9839)
    
    # COMPARATIVE ANALYSIS
    def test_disease_statistics(self):
        self.assertEqual(disease_models['statistics'], {'minimum': 1, 'maximum': 12, 'q1': 3.5, 'q3': 9.5, 'mean': 6.5, 'median': 6.5})
    
    def test_disease_optimal(self):
        self.assertEqual(disease_models['optimal']['option'], 'cubic')

profits_models = run_all(profits_set)

class TestProfitsModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
    def test_profits_models_linear_constants(self):
        self.assertEqual(profits_models['models']['linear']['constants'], [-14.9826, 23791.1699])
    
    def test_profits_models_linear_points(self):
        self.assertEqual(profits_models['models']['linear']['points'], {'roots': [[1587.92, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_profits_models_linear_accumulations(self):
        self.assertEqual(profits_models['models']['linear']['accumulations'], {'range': 2196292.1114, 'iqr': 1200006.7586})
    
    def test_profits_models_linear_averages(self):
        self.assertEqual(profits_models['models']['linear']['averages'], {'range': {'average_value_derivative': -14.9826, 'mean_values_derivative': ['All'], 'average_value_integral': 20719.7369, 'mean_values_integral': [205.0]}, 'iqr': {'average_value_derivative': -14.9826, 'mean_values_derivative': ['All'], 'average_value_integral': 20689.7717, 'mean_values_integral': [207.0]}})
    
    def test_profits_models_linear_correlation(self):
        self.assertEqual(profits_models['models']['linear']['correlation'], 0.1767)
    
    # QUADRATIC MODEL
    def test_profits_models_quadratic_constants(self):
        self.assertEqual(profits_models['models']['quadratic']['constants'], [-2.6043, 1055.9536, -83362.0271])
    
    def test_profits_models_quadratic_points(self):
        self.assertEqual(profits_models['models']['quadratic']['points'], {'roots': [[107.3851, 0.0], [298.0804, 0.0]], 'maxima': [[202.7327, 23676.1411]], 'minima': [None], 'inflections': [None]})
    
    def test_profits_models_quadratic_accumulations(self):
        self.assertEqual(profits_models['models']['quadratic']['accumulations'], {'range': 2249771.613, 'iqr': 1328121.4274})
    
    def test_profits_models_quadratic_averages(self):
        self.assertEqual(profits_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': -11.8094, 'mean_values_derivative': [205.0], 'average_value_integral': 21224.2605, 'mean_values_integral': [172.0493, 233.4162]}, 'iqr': {'average_value_derivative': -22.2266, 'mean_values_derivative': [207.0], 'average_value_integral': 22898.6453, 'mean_values_integral': [185.4543, 220.0111]}})
    
    def test_profits_models_quadratic_correlation(self):
        self.assertEqual(profits_models['models']['quadratic']['correlation'], 0.9285)
    
    # CUBIC MODEL
    def test_profits_models_cubic_constants(self):
        self.assertEqual(profits_models['models']['cubic']['constants'], [0.0017, -3.6712, 1271.1194, -97581.8495])
    
    def test_profits_models_cubic_points(self):
        self.assertEqual(profits_models['models']['cubic']['points'], {'roots': [[109.8431, 0.0], [298.3928, 0.0], [1751.2935, 0.0]], 'maxima': [[201.2537, 23398.1906]], 'minima': [[1238.4326, -924976.6175]], 'inflections': [[719.8431, -450789.1624]]})
    
    def test_profits_models_cubic_accumulations(self):
        self.assertEqual(profits_models['models']['cubic']['accumulations'], {'range': 2118709.8422, 'iqr': 1257318.1246})
    
    def test_profits_models_cubic_averages(self):
        self.assertEqual(profits_models['models']['cubic']['averages'], {'range': {'average_value_derivative': -14.9698, 'mean_values_derivative': [204.0915], 'average_value_integral': 19987.8287, 'mean_values_integral': [165.7475, 237.5895]}, 'iqr': {'average_value_derivative': -28.7978, 'mean_values_derivative': [206.7268], 'average_value_integral': 21677.8987, 'mean_values_integral': [226.9709]}})
    
    def test_profits_models_cubic_correlation(self):
        self.assertEqual(profits_models['models']['cubic']['correlation'], 0.9194)
    
    # HYPERBOLIC MODEL
    def test_profits_models_hyperbolic_constants(self):
        self.assertEqual(profits_models['models']['hyperbolic']['constants'], [138413.9218, 19996.5303])
    
    def test_profits_models_hyperbolic_points(self):
        self.assertEqual(profits_models['models']['hyperbolic']['points'], {'roots': [[-6.9219, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_profits_models_hyperbolic_accumulations(self):
        self.assertEqual(profits_models['models']['hyperbolic']['accumulations'], {'range': 2192864.12, 'iqr': 1198838.1625})
    
    def test_profits_models_hyperbolic_averages(self):
        self.assertEqual(profits_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': -3.5295, 'mean_values_derivative': [198.0311], 'average_value_integral': 20687.3974, 'mean_values_integral': [200.3481]}, 'iqr': {'average_value_derivative': -3.2949, 'mean_values_derivative': [204.9598], 'average_value_integral':  20669.6235, 'mean_values_integral': [205.6386]}})
    
    def test_profits_models_hyperbolic_correlation(self):
        self.assertEqual(profits_models['models']['hyperbolic']['correlation'], 0.041)
    
    # EXPONENTIAL MODEL
    def test_profits_models_exponential_constants(self):
        self.assertEqual(profits_models['models']['exponential']['constants'], [24035.8081, 0.9992])
    
    def test_profits_models_exponential_points(self):
        self.assertEqual(profits_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_profits_models_exponential_accumulations(self):
        self.assertEqual(profits_models['models']['exponential']['accumulations'], {'range': 2162927.7663, 'iqr': 1181347.7594})
    
    def test_profits_models_exponential_averages(self):
        self.assertEqual(profits_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -16.3305, 'mean_values_derivative': [204.6266], 'average_value_integral': 20404.9789, 'mean_values_integral': [204.6253]}, 'iqr': {'average_value_derivative': -16.301, 'mean_values_derivative': [206.8858], 'average_value_integral': 20368.0648, 'mean_values_integral': [206.8878]}})
    
    def test_profits_models_exponential_correlation(self):
        self.assertEqual(profits_models['models']['exponential']['correlation'], 0.12)
    
    # LOGARITHMIC MODEL
    def test_profits_models_logarithmic_constants(self):
        self.assertEqual(profits_models['models']['logarithmic']['constants'], [-1864.227, 30602.8572])
    
    def test_profits_models_logarithmic_points(self):
        self.assertEqual(profits_models['models']['logarithmic']['points'], {'roots': [[13468210.7299, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_profits_models_logarithmic_accumulations(self):
        self.assertEqual(profits_models['models']['logarithmic']['accumulations'], {'range': 2194280.1749, 'iqr': 1198720.4117})
    
    def test_profits_models_logarithmic_averages(self):
        self.assertEqual(profits_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': -9.3049, 'mean_values_derivative': [200.349], 'average_value_integral': 20700.7564, 'mean_values_integral': [202.6821]}, 'iqr': {'average_value_derivative': -9.0656, 'mean_values_derivative': [205.6375], 'average_value_integral': 20667.5933, 'mean_values_integral': [206.32]}})
    
    def test_profits_models_logarithmic_correlation(self):
        self.assertEqual(profits_models['models']['logarithmic']['correlation'], 0.109)
    
    # LOGISTIC MODEL
    def test_profits_models_logistic_constants(self):
        self.assertEqual(profits_models['models']['logistic']['constants'], [21721.3181, -0.0865, 269.7954])
    
    def test_profits_models_logistic_points(self):
        self.assertEqual(profits_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[269.7954, 10860.6591]]})
    
    def test_profits_models_logistic_accumulations(self):
        self.assertEqual(profits_models['models']['logistic']['accumulations'], {'range': 2225165.868, 'iqr': 1246777.3468})
    
    def test_profits_models_logistic_averages(self):
        self.assertEqual(profits_models['models']['logistic']['averages'], {'range': {'average_value_derivative': -54.2892, 'mean_values_derivative': [229.5238], 'average_value_integral': 20992.1308, 'mean_values_integral': [230.9518]}, 'iqr': {'average_value_derivative': -18.9716, 'mean_values_derivative': [216.8982], 'average_value_integral': 21496.1612, 'mean_values_integral': [217.0921]}})
    
    def test_profits_models_logistic_correlation(self):
        self.assertEqual(profits_models['models']['logistic']['correlation'], 0.6133)
    
    # SINUSOIDAL MODEL
    def test_profits_models_sinusoidal_constants(self):
        self.assertEqual(profits_models['models']['sinusoidal']['constants'], [-2317.8178, 1.0496, 10.9914, 20658.4641])
    
    def test_profits_models_sinusoidal_points(self):
        self.assertEqual(profits_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[153.1637, 22976.2819], [159.1499, 22976.2819], [165.1361, 22976.2819], [171.1223, 22976.2819], [177.1085, 22976.2819], ['153.1637 + 5.9862k', 22976.2819]], 'minima': [[156.1568, 18340.6463], [162.143, 18340.6463], [168.1292, 18340.6463], [174.1154, 18340.6463], [180.1016, 18340.6463], ['156.1568 + 5.9862k', 18340.6463]], 'inflections': [[154.6602, 20658.4641], [157.6533, 20658.4641], [160.6464, 20658.4641], [163.6395, 20658.4641], [166.6326, 20658.4641], ['154.6602 + 2.9931k', 20658.4641]]})
    
    def test_profits_models_sinusoidal_accumulations(self):
        self.assertEqual(profits_models['models']['sinusoidal']['accumulations'], {'range': 2191699.3762, 'iqr': 1194532.556})
    
    def test_profits_models_sinusoidal_averages(self):
        self.assertEqual(profits_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': -29.2504, 'mean_values_derivative': [153.1775, 156.1477, 159.1638, 162.134, 165.1501, 168.1203, 171.1364, 174.1066, 177.1227, 180.0929, '153.1775 + 5.9863k', '156.1477 + 5.9863k'], 'average_value_integral': 20676.4092, 'mean_values_integral': [154.6552, 157.6631, 160.6415, 163.6494, 166.6278, 169.6357, 172.6141, 175.622, 178.6004, 181.6083, '154.6552 + 5.9863k', '157.6631 + 5.9863k']}, 'iqr': {'average_value_derivative': -2.8944, 'mean_values_derivative': [180.1032, 183.0986, 186.0895, 189.0849, 192.0758, 195.0712, 198.0621, 201.0575, 204.0484, 207.0438, '180.1032 + 5.9863k', '183.0986 + 5.9863k'], 'average_value_integral': 20595.3889, 'mean_values_integral': [178.6337, 181.575, 184.62, 187.5613, 190.6063, 193.5476, 196.5926, 199.5339, 202.5789, 205.5202, '178.6337 + 5.9863k', '181.575 + 5.9863k']}})
    
    def test_profits_models_sinusoidal_correlation(self):
        self.assertEqual(profits_models['models']['sinusoidal']['correlation'], 0.5088)
    
    # COMPARATIVE ANALYSIS
    def test_profits_statistics(self):
        self.assertEqual(profits_models['statistics'], {'minimum': 152, 'maximum': 258, 'q1': 178, 'q3': 236, 'mean': 207.5, 'median': 207.5})
    
    def test_profits_optimal(self):
        self.assertEqual(profits_models['optimal']['option'], 'quadratic')

class TestEdgeCases(unittest.TestCase):
    def test_run_all_zeroes(self):
        run_all_zeroes = run_all(bad_set_zeroes)
        self.assertEqual(run_all_zeroes['optimal']['option'], 'linear')

    def test_run_all_string_raises(self):
        with self.assertRaises(Exception) as context:
            run_all(bad_set_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_run_all_vector_raises(self):
        with self.assertRaises(Exception) as context:
            run_all(bad_set_vector)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'First argument must be a 2-dimensional list')
    
    def test_run_all_buried_not_list_raises(self):
        with self.assertRaises(Exception) as context:
            run_all(bad_set_buried_not_list)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within first argument must be lists')
    
    def test_run_all_buried_string_raises(self):
        with self.assertRaises(Exception) as context:
            run_all(bad_set_buried_string)
        self.assertEqual(type(context.exception), TypeError)
        self.assertEqual(str(context.exception), 'Elements within lists within first argument must be integers or floats')
    
    def test_run_all_short_raises(self):
        with self.assertRaises(Exception) as context:
            run_all(bad_set_short)
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), 'First argument must contain at least 10 elements')

if __name__ == '__main__':
    unittest.main()

# ----- Ran 510 tests in 0.101s ----- OK ----- #