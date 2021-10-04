import unittest

from regressions.execute import run_all
from .data.sets.hundred import hundred_set
from .data.sets.thousand import thousand_set

hundred_models = run_all(hundred_set)

class TestHundredModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
    def test_hundred_models_linear_constants(self):
        self.assertEqual(hundred_models['models']['linear']['constants'], [0.4934, 414.5401])
    
    def test_hundred_models_linear_points(self):
        self.assertEqual(hundred_models['models']['linear']['points'], {'roots': [[-840.1704, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hundred_models_linear_accumulations(self):
        self.assertEqual(hundred_models['models']['linear']['accumulations'], {'range': 47829.5566, 'iqr': 22178.5177})
    
    def test_hundred_models_linear_averages(self):
        self.assertEqual(hundred_models['models']['linear']['averages'], {'range': {'average_value_derivative': 0.4934, 'mean_values_derivative': ['All'], 'average_value_integral': 488.0567, 'mean_values_integral': [149.0]}, 'iqr': {'average_value_derivative': 0.4934, 'mean_values_derivative': ['All'], 'average_value_integral': 487.4399, 'mean_values_integral': [147.7499]}})
    
    def test_hundred_models_linear_correlation(self):
        self.assertEqual(hundred_models['models']['linear']['correlation'], 0.1013)
    
    # QUADRATIC MODEL
    def test_hundred_models_quadratic_constants(self):
        self.assertEqual(hundred_models['models']['quadratic']['constants'], [-0.007, 2.5668, 265.4919])
    
    def test_hundred_models_quadratic_points(self):
        self.assertEqual(hundred_models['models']['quadratic']['points'], {'roots': [[-84.1305, 0], [450.8163, 0]], 'maxima': [[183.3429, 500.7941]], 'minima': [None], 'inflections': [None]})
    
    def test_hundred_models_quadratic_accumulations(self):
        self.assertEqual(hundred_models['models']['quadratic']['accumulations'], {'range': 47945.1182, 'iqr': 22427.8043})
    
    def test_hundred_models_quadratic_averages(self):
        self.assertEqual(hundred_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 0.4808, 'mean_values_derivative': [149.0], 'average_value_integral': 489.2359, 'mean_values_integral': [142.7082]}, 'iqr': {'average_value_derivative': 0.4983, 'mean_values_derivative': [147.75], 'average_value_integral': 492.9188, 'mean_values_integral': [149.8011]}})
    
    def test_hundred_models_quadratic_correlation(self):
        self.assertEqual(hundred_models['models']['quadratic']['correlation'], 0.1071)
    
    # CUBIC MODEL
    def test_hundred_models_cubic_constants(self):
        self.assertEqual(hundred_models['models']['cubic']['constants'], [0.0005, -0.2204, 33.8099, -1226.1398])
    
    def test_hundred_models_cubic_points(self):
        self.assertEqual(hundred_models['models']['cubic']['points'], {'roots': [[51.579, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[146.9333, 569.4583]]})
    
    def test_hundred_models_cubic_accumulations(self):
        self.assertEqual(hundred_models['models']['cubic']['accumulations'], {'range': 20188.5488, 'iqr': 10848.7089})
    
    def test_hundred_models_cubic_averages(self):
        self.assertEqual(hundred_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 2.6327, 'mean_values_derivative': [118.5678, 175.2989], 'average_value_integral': 206.0056, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': 1.6856, 'mean_values_derivative': [133.7726, 160.094], 'average_value_integral': 238.4332, 'mean_values_integral': [None]}})
    
    def test_hundred_models_cubic_correlation(self):
        self.assertEqual(hundred_models['models']['cubic']['correlation'], 0.0)
    
    # HYPERBOLIC MODEL
    def test_hundred_models_hyperbolic_constants(self):
        self.assertEqual(hundred_models['models']['hyperbolic']['constants'], [-10786.2465, 563.019])
    
    def test_hundred_models_hyperbolic_points(self):
        self.assertEqual(hundred_models['models']['hyperbolic']['points'], {'roots': [[19.1579, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hundred_models_hyperbolic_accumulations(self):
        self.assertEqual(hundred_models['models']['hyperbolic']['accumulations'], {'range': 47807.811, 'iqr': 22269.081})
    
    def test_hundred_models_hyperbolic_averages(self):
        self.assertEqual(hundred_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 0.5448, 'mean_values_derivative': [140.7073], 'average_value_integral': 487.8348, 'mean_values_integral': [143.4643]}, 'iqr': {'average_value_derivative': 0.5061, 'mean_values_derivative': [145.9879], 'average_value_integral': 489.4304, 'mean_values_integral': [146.575]}})
    
    def test_hundred_models_hyperbolic_correlation(self):
        self.assertEqual(hundred_models['models']['hyperbolic']['correlation'], 0.1082)
    
    # EXPONENTIAL MODEL
    def test_hundred_models_exponential_constants(self):
        self.assertEqual(hundred_models['models']['exponential']['constants'], [407.8094, 1.0009])
    
    def test_hundred_models_exponential_points(self):
        self.assertEqual(hundred_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hundred_models_exponential_accumulations(self):
        self.assertEqual(hundred_models['models']['exponential']['accumulations'], {'range': 45712.6755, 'iqr': 21194.5052})
    
    def test_hundred_models_exponential_averages(self):
        self.assertEqual(hundred_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 0.4196, 'mean_values_derivative': [149.3031], 'average_value_integral': 466.4559, 'mean_values_integral': [149.36]}, 'iqr': {'average_value_derivative': 0.419, 'mean_values_derivative': [147.7124], 'average_value_integral': 465.8133, 'mean_values_integral': [147.8276]}})
    
    def test_hundred_models_exponential_correlation(self):
        self.assertEqual(hundred_models['models']['exponential']['correlation'], 0.0)
    
    # LOGARITHMIC MODEL
    def test_hundred_models_logarithmic_constants(self):
        self.assertEqual(hundred_models['models']['logarithmic']['constants'], [74.0076, 118.997])
    
    def test_hundred_models_logarithmic_points(self):
        self.assertEqual(hundred_models['models']['logarithmic']['points'], {'roots': [[0.2003, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_hundred_models_logarithmic_accumulations(self):
        self.assertEqual(hundred_models['models']['logarithmic']['accumulations'], {'range': 47818.8482, 'iqr': 22222.6107})
    
    def test_hundred_models_logarithmic_averages(self):
        self.assertEqual(hundred_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 0.5159, 'mean_values_derivative': [143.4534], 'average_value_integral': 487.9474, 'mean_values_integral': [146.2481]}, 'iqr': {'average_value_derivative': 0.5049, 'mean_values_derivative': [146.5787], 'average_value_integral': 488.409, 'mean_values_integral': [147.1631]}})
    
    def test_hundred_models_logarithmic_correlation(self):
        self.assertEqual(hundred_models['models']['logarithmic']['correlation'], 0.1047)
    
    # LOGISTIC MODEL
    def test_hundred_models_logistic_constants(self):
        self.assertEqual(hundred_models['models']['logistic']['constants'], [878.3475, 0.0023, 51.0002])
    
    def test_hundred_models_logistic_points(self):
        self.assertEqual(hundred_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[51.0002, 439.1737]]})
    
    def test_hundred_models_logistic_accumulations(self):
        self.assertEqual(hundred_models['models']['logistic']['accumulations'], {'range': 47864.0424, 'iqr': 22196.0656})
    
    def test_hundred_models_logistic_averages(self):
        self.assertEqual(hundred_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.4982, 'mean_values_derivative': [152.7184], 'average_value_integral': 488.4086, 'mean_values_integral': [148.8968]}, 'iqr': {'average_value_derivative': 0.4987, 'mean_values_derivative': [148.8896], 'average_value_integral': 487.8256, 'mean_values_integral': [147.728]}})
    
    def test_hundred_models_logistic_correlation(self):
        self.assertEqual(hundred_models['models']['logistic']['correlation'], 0.1013)
    
    # SINUSOIDAL MODEL
    def test_hundred_models_sinusoidal_constants(self):
        self.assertEqual(hundred_models['models']['sinusoidal']['constants'], [32.3199, 1.0085, 1.8848, 488.9635])
    
    def test_hundred_models_sinusoidal_points(self):
        self.assertEqual(hundred_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[103.1256, 521.2834], [109.3558, 521.2834], [115.586, 521.2834], [121.8162, 521.2834], [128.0464, 521.2834], ['103.1256 + 6.2302k', 521.2834]], 'minima': [[100.0105, 456.6436], [106.2407, 456.6436], [112.4709, 456.6436], [118.7011, 456.6436], [124.9313, 456.6436], ['100.0105 + 6.2302k', 456.6436]], 'inflections': [[101.568, 488.9635], [104.6831, 488.9635], [107.7982, 488.9635], [110.9133, 488.9635], [114.0284, 488.9635], ['101.568 + 3.1151k', 488.9635]]})
    
    def test_hundred_models_sinusoidal_accumulations(self):
        self.assertEqual(hundred_models['models']['sinusoidal']['accumulations'], {'range': 47949.8129, 'iqr': 22220.5541})
    
    def test_hundred_models_sinusoidal_averages(self):
        self.assertEqual(hundred_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.3752, 'mean_values_derivative': [100.0219, 103.1141, 106.2521, 109.3443, 112.4823, 115.5745, 118.7125, 121.8047, 124.9427, 128.0349, '100.0219 + 6.2302k', '103.1141 + 6.2302k'], 'average_value_integral': 489.2838, 'mean_values_integral': [101.5778, 104.6733, 107.808, 110.9035, 114.0382, 117.1337, 120.2684, 123.3639, 126.4986, 129.5941, '101.5778 + 6.2302k', '104.6733 + 6.2302k']}, 'iqr': {'average_value_derivative': 0.9868, 'mean_values_derivative': [128.0163, 131.1915, 134.2465, 137.4217, 140.4767, 143.6519, 146.7069, 149.8821, 152.9371, 156.1123, '128.0163 + 6.2302k', '131.1915 + 6.2302k'], 'average_value_integral': 488.3638, 'mean_values_integral': [126.4704, 129.6223, 132.7006, 135.8525, 138.9308, 142.0827, 145.161, 148.3129, 151.3912, 154.5431, '126.4704 + 6.2302k', '129.6223 + 6.2302k']}})
    
    def test_hundred_models_sinusoidal_correlation(self):
        self.assertEqual(hundred_models['models']['sinusoidal']['correlation'], 0.1727)
    
    # COMPARATIVE ANALYSIS
    def test_hundred_statistics(self):
        self.assertEqual(hundred_models['statistics'], {'minimum': 100, 'maximum': 198, 'q1': 125.0, 'q3': 170.5, 'mean': 149.29, 'median': 151.5})
    
    def test_hundred_optimal(self):
        self.assertEqual(hundred_models['optimal']['option'], 'sinusoidal')

thousand_models = run_all(thousand_set)

class TestThousandModels(unittest.TestCase):
    maxDiff = None

    # LINEAR MODEL
    def test_thousand_models_linear_constants(self):
        self.assertEqual(thousand_models['models']['linear']['constants'], [-0.077, 276.4791])
    
    def test_thousand_models_linear_points(self):
        self.assertEqual(thousand_models['models']['linear']['points'], {'roots': [[3590.6377, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_thousand_models_linear_accumulations(self):
        self.assertEqual(thousand_models['models']['linear']['accumulations'], {'range': 128338.1094, 'iqr': 63564.1504})
    
    def test_thousand_models_linear_averages(self):
        self.assertEqual(thousand_models['models']['linear']['averages'], {'range': {'average_value_derivative': -0.077, 'mean_values_derivative': ['All'], 'average_value_integral': 257.1906, 'mean_values_integral': [250.5]}, 'iqr': {'average_value_derivative': -0.077, 'mean_values_derivative': ['All'], 'average_value_integral': 256.8249, 'mean_values_integral': [255.2494]}})
    
    def test_thousand_models_linear_correlation(self):
        self.assertEqual(thousand_models['models']['linear']['correlation'], 0.077)
    
    # QUADRATIC MODEL
    def test_thousand_models_quadratic_constants(self):
        self.assertEqual(thousand_models['models']['quadratic']['constants'], [-0.0001, -0.0574, 274.8526])
    
    def test_thousand_models_quadratic_points(self):
        self.assertEqual(thousand_models['models']['quadratic']['points'], {'roots': [[-1969.5264, 0.0], [1395.5264, 0.0]], 'maxima': [[-287.0, 283.0895]], 'minima': [None], 'inflections': [None]})
    
    def test_thousand_models_quadratic_accumulations(self):
        self.assertEqual(thousand_models['models']['quadratic']['accumulations'], {'range': 117476.4762, 'iqr': 59183.2086})
    
    def test_thousand_models_quadratic_averages(self):
        self.assertEqual(thousand_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': -0.1075, 'mean_values_derivative': [250.5], 'average_value_integral': 235.4238, 'mean_values_integral': [403.4035]}, 'iqr': {'average_value_derivative': -0.1085, 'mean_values_derivative': [255.5], 'average_value_integral': 239.1241, 'mean_values_integral': [376.0641]}})
    
    def test_thousand_models_quadratic_correlation(self):
        self.assertEqual(thousand_models['models']['quadratic']['correlation'], 0.0609)
    
    # CUBIC MODEL
    def test_thousand_models_cubic_constants(self):
        self.assertEqual(thousand_models['models']['cubic']['constants'], [0.0001, -0.0013, 0.1879, 265.0801])
    
    def test_thousand_models_cubic_points(self):
        self.assertEqual(thousand_models['models']['cubic']['points'], {'roots': [[-129.818, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [[4.3333, 265.8781]]})
    
    def test_thousand_models_cubic_accumulations(self):
        self.assertEqual(thousand_models['models']['cubic']['accumulations'], {'range': 6355774.8762, 'iqr': 2089989.2011})
    
    def test_thousand_models_cubic_averages(self):
        self.assertEqual(thousand_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 24.5867, 'mean_values_derivative': [289.5492], 'average_value_integral': 12737.0238, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': 20.6014, 'mean_values_derivative': [265.2237], 'average_value_integral': 8444.4008, 'mean_values_integral': [None]}})
    
    def test_thousand_models_cubic_correlation(self):
        self.assertEqual(thousand_models['models']['cubic']['correlation'], 0.0)
    
    # HYPERBOLIC MODEL
    def test_thousand_models_hyperbolic_constants(self):
        self.assertEqual(thousand_models['models']['hyperbolic']['constants'], [-32.989, 257.7945])
    
    def test_thousand_models_hyperbolic_points(self):
        self.assertEqual(thousand_models['models']['hyperbolic']['points'], {'roots': [[0.128, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_thousand_models_hyperbolic_accumulations(self):
        self.assertEqual(thousand_models['models']['hyperbolic']['accumulations'], {'range': 128434.4418, 'iqr': 63769.2189})
    
    def test_thousand_models_hyperbolic_averages(self):
        self.assertEqual(thousand_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 0.066, 'mean_values_derivative': [22.357], 'average_value_integral': 257.3837, 'mean_values_integral': [80.3043]}, 'iqr': {'average_value_derivative': 0.0007, 'mean_values_derivative': [217.0879], 'average_value_integral': 257.6534, 'mean_values_integral': [233.7987]}})
    
    def test_thousand_models_hyperbolic_correlation(self):
        self.assertEqual(thousand_models['models']['hyperbolic']['correlation'], 0.0211)
    
    # EXPONENTIAL MODEL
    def test_thousand_models_exponential_constants(self):
        self.assertEqual(thousand_models['models']['exponential']['constants'], [214.8414, 0.9995])
    
    def test_thousand_models_exponential_points(self):
        self.assertEqual(thousand_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_thousand_models_exponential_accumulations(self):
        self.assertEqual(thousand_models['models']['exponential']['accumulations'], {'range': 94827.8637, 'iqr': 46830.598})
    
    def test_thousand_models_exponential_averages(self):
        self.assertEqual(thousand_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -0.095, 'mean_values_derivative': [246.1906], 'average_value_integral': 190.0358, 'mean_values_integral': [245.3139]}, 'iqr': {'average_value_derivative': -0.0946, 'mean_values_derivative': [254.6273], 'average_value_integral': 189.2145, 'mean_values_integral': [253.9741]}})
    
    def test_thousand_models_exponential_correlation(self):
        self.assertEqual(thousand_models['models']['exponential']['correlation'], 0.0)
    
    # LOGARITHMIC MODEL
    def test_thousand_models_logarithmic_constants(self):
        self.assertEqual(thousand_models['models']['logarithmic']['constants'], [-5.8812, 287.718])
    
    def test_thousand_models_logarithmic_points(self):
        self.assertEqual(thousand_models['models']['logarithmic']['points'], {'roots': [[1.7636079640078343e+21, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_thousand_models_logarithmic_accumulations(self):
        self.assertEqual(thousand_models['models']['logarithmic']['accumulations'], {'range': 128231.3242, 'iqr': 63204.499})
    
    def test_thousand_models_logarithmic_averages(self):
        self.assertEqual(thousand_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': -0.0732, 'mean_values_derivative': [80.3443], 'average_value_integral': 256.9766, 'mean_values_integral': [186.2449]}, 'iqr': {'average_value_derivative': -0.0252, 'mean_values_derivative': [233.381], 'average_value_integral': 255.3717, 'mean_values_integral': [244.6795]}})
    
    def test_thousand_models_logarithmic_correlation(self):
        self.assertEqual(thousand_models['models']['logarithmic']['correlation'], 0.0433)
    
    # LOGISTIC MODEL
    def test_thousand_models_logistic_constants(self):
        self.assertEqual(thousand_models['models']['logistic']['constants'], [435.7515, -0.0007, 749.4225])
    
    def test_thousand_models_logistic_points(self):
        self.assertEqual(thousand_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[749.4225, 217.8758]]})
    
    def test_thousand_models_logistic_accumulations(self):
        self.assertEqual(thousand_models['models']['logistic']['accumulations'], {'range': 127468.1415, 'iqr': 63153.5003})
    
    def test_thousand_models_logistic_averages(self):
        self.assertEqual(thousand_models['models']['logistic']['averages'], {'range': {'average_value_derivative': -0.0738, 'mean_values_derivative': [231.7002], 'average_value_integral': 255.4472, 'mean_values_integral': [251.7514]}, 'iqr': {'average_value_derivative': -0.074, 'mean_values_derivative': [253.6974], 'average_value_integral': 255.1657, 'mean_values_integral': [255.5552]}})
    
    def test_thousand_models_logistic_correlation(self):
        self.assertEqual(thousand_models['models']['logistic']['correlation'], 0.076)
    
    # SINUSOIDAL MODEL
    def test_thousand_models_sinusoidal_constants(self):
        self.assertEqual(thousand_models['models']['sinusoidal']['constants'], [499.0, 0.0001, 0.0001, 250.5])
    
    def test_thousand_models_sinusoidal_points(self):
        self.assertEqual(thousand_models['models']['sinusoidal']['points'], {'roots': [['36675.0702 + 62831.8531k', 0.0], ['57572.7097 + 62831.8531k', 0.0]], 'maxima': [['15707.9634 + 62831.853k', 749.5]], 'minima': [['47123.8899 + 62831.853k', -248.5]], 'inflections': [['31415.9266 + 31415.9265k', 250.5]]})
    
    def test_thousand_models_sinusoidal_accumulations(self):
        self.assertEqual(thousand_models['models']['sinusoidal']['accumulations'], {'range': 131235.6732, 'iqr': 65150.7273})
    
    def test_thousand_models_sinusoidal_averages(self):
        self.assertEqual(thousand_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.0499, 'mean_values_derivative': ['62831.8532 + 62831.8531k'], 'average_value_integral': 262.9973, 'mean_values_integral': [250.4732, '250.4732 + 62831.8531k', '31165.4536 + 62831.8531k']}, 'iqr': {'average_value_derivative': 0.0499, 'mean_values_derivative': ['62831.8532 + 62831.8531k'], 'average_value_integral': 263.2353, 'mean_values_integral': [255.2442, '255.2442 + 62831.8531k', '31160.6825 + 62831.8531k']}})
    
    def test_thousand_models_sinusoidal_correlation(self):
        self.assertEqual(thousand_models['models']['sinusoidal']['correlation'], 0.0)
    
    # COMPARATIVE ANALYSIS
    def test_thousand_statistics(self):
        self.assertEqual(thousand_models['statistics'], {'minimum': 1, 'maximum': 500, 'q1': 131.5, 'q3': 379.0, 'mean': 251.255, 'median': 249.5})
    
    def test_thousand_optimal(self):
        self.assertEqual(thousand_models['optimal']['option'], 'linear')

if __name__ == '__main__':
    unittest.main()

# ----- Ran 84 tests in 0.008s ----- OK ----- #