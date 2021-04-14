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
    [10, 1.999999]
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

large_set = [[169, 423], [122, 391], [178, 555], [131, 284], [120, 520], [179, 558], [164, 265], [167, 338], [198, 445], [139, 402], [183, 725], [133, 470], [156, 573], [159, 325], [121, 653], [118, 358], [122, 633], [167, 487], [161, 453], [194, 488], [170, 517], [124, 377], [191, 310], [194, 398], [173, 744], [166, 389], [113, 583], [109, 380], [126, 668], [144, 491], [107, 533], [188, 355], [147, 553], [169, 497], [121, 606], [132, 373], [111, 554], [173, 669], [177, 483], [122, 340], [171, 286], [108, 681], [139, 502], [115, 339], [174, 396], [134, 625], [147, 435], [146, 555], [147, 656], [126, 354], [155, 679], [181, 629], [149, 417], [119, 374], [102, 422], [112, 292], [108, 464], [109, 559], [112, 635], [159, 518], [180, 304], [185, 567], [165, 299], [160, 337], [133, 730], [193, 374], [164, 537], [172, 592], [173, 660], [186, 290], [170, 670], [192, 687], [154, 596], [154, 464], [125, 383], [193, 559], [155, 586], [149, 406], [131, 590], [127, 339], [163, 378], [145, 254], [156, 395], [166, 355], [189, 661], [133, 685], [168, 685], [190, 736], [145, 564], [125, 470], [129, 541], [133, 439], [162, 486], [125, 387], [183, 596], [135, 733], [106, 329], [100, 279], [102, 439], [162, 454]]

agnostic_models = run_all(agnostic_set)

class TestAgnosticModels(unittest.TestCase):
    maxDiff = None

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
        self.assertEqual(agnostic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 2.1695, 'mean_values_derivative': [5.7254], 'average_value_integral': 32.4232, 'mean_values_integral': [3.0875]}, 'iqr': {'average_value_derivative': 2.147, 'mean_values_derivative': [5.5696], 'average_value_integral': 32.0875, 'mean_values_integral': [3.0771]}})
    
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
        self.assertEqual(agnostic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[0.9746, 21.9915]]})
    
    def test_agnostic_models_logistic_accumulations(self):
        self.assertEqual(agnostic_models['models']['logistic']['accumulations'], {'range': 305.9311, 'iqr': 174.1085})
    
    def test_agnostic_models_logistic_averages(self):
        self.assertEqual(agnostic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 2.1475, 'mean_values_derivative': [5.5246], 'average_value_integral': 33.9923, 'mean_values_integral': [4.9554]}, 'iqr': {'average_value_derivative': 2.1621, 'mean_values_derivative': [5.4879], 'average_value_integral': 34.8217, 'mean_values_integral': [5.3155]}})
    
    def test_agnostic_models_logistic_correlation(self):
        self.assertEqual(agnostic_models['models']['logistic']['correlation'], 0.5875)
    
    def test_agnostic_models_sinusoidal_constants(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['constants'], [14.0875, 0.7119, -3.7531, 34.2915])
    
    def test_agnostic_models_sinusoidal_points(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[7.2794, 48.379], [16.1054, 48.379], ['7.2794 + 8.826k', 48.379]], 'minima': [[2.8664, 20.204], [11.6924, 20.204], ['2.8664 + 8.826k', 20.204]], 'inflections': [[5.0729, 34.2915], [9.4859, 34.2915], [13.8989, 34.2915], [18.3119, 34.2915], ['5.0729 + 4.413k', 34.2915]]})
    
    def test_agnostic_models_sinusoidal_accumulations(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['accumulations'], {'range': 307.8897, 'iqr': 183.0504})
    
    def test_agnostic_models_sinusoidal_averages(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': -0.1849, 'mean_values_derivative': [2.8405, 7.3052, '2.8405 + 8.8259k', '7.3052 + 8.8259k'], 'average_value_integral': 34.21, 'mean_values_integral': [5.0647, 9.4939, '5.0647 + 8.8259k', '9.4939 + 8.8259k']}, 'iqr': {'average_value_derivative': 5.2595, 'mean_values_derivative': [3.6418, 6.5039, '3.6418 + 8.8259k', '6.5039 + 8.8259k'], 'average_value_integral': 36.6101, 'mean_values_integral': [5.305, '5.305 + 8.8259k', '9.2535 + 8.8259k']}})
    
    def test_agnostic_models_sinusoidal_correlation(self):
        self.assertEqual(agnostic_models['models']['sinusoidal']['correlation'], 0.9264)
    
    def test_agnostic_statistics(self):
        self.assertEqual(agnostic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_agnostic_optimal(self):
        self.assertEqual(agnostic_models['optimal']['option'], 'sinusoidal')

linear_models = run_all(linear_set)

class TestLinearModels(unittest.TestCase):
    maxDiff = None

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
        self.assertEqual(linear_models['models']['quadratic']['constants'], [-0.0001, -3.0, 33.0])
    
    def test_linear_models_quadratic_points(self):
        self.assertEqual(linear_models['models']['quadratic']['points'], {'roots': [[-30010.996, 0], [10.996, 0]], 'maxima': [[-15000.0, 22533.0]], 'minima': [None], 'inflections': [None]})
    
    def test_linear_models_quadratic_accumulations(self):
        self.assertEqual(linear_models['models']['quadratic']['accumulations'], {'range': 148.4667, 'iqr': 82.4838})
    
    def test_linear_models_quadratic_averages(self):
        self.assertEqual(linear_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': -3.0011, 'mean_values_derivative': [5.5], 'average_value_integral': 16.4963, 'mean_values_integral': [5.5002]}, 'iqr': {'average_value_derivative': -3.0011, 'mean_values_derivative': [5.5], 'average_value_integral': 16.4968, 'mean_values_integral': [5.5001]}})
    
    def test_linear_models_quadratic_correlation(self):
        self.assertEqual(linear_models['models']['quadratic']['correlation'], 1.0)
    
    def test_linear_models_cubic_constants(self):
        self.assertEqual(linear_models['models']['cubic']['constants'], [-0.0001, -0.0001, -3.0, 33.0])
    
    def test_linear_models_cubic_points(self):
        self.assertEqual(linear_models['models']['cubic']['points'], {'roots': [[10.9522, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[-0.3333, 33.9999]]})
    
    def test_linear_models_cubic_accumulations(self):
        self.assertEqual(linear_models['models']['cubic']['accumulations'], {'range': 148.2167, 'iqr': 82.3835})
    
    def test_linear_models_cubic_averages(self):
        self.assertEqual(linear_models['models']['cubic']['averages'], {'range': {'average_value_derivative': -3.0122, 'mean_values_derivative': [6.0524], 'average_value_integral': 16.4685, 'mean_values_integral': [5.5039]}, 'iqr': {'average_value_derivative': -3.0108, 'mean_values_derivative': [5.6759], 'average_value_integral': 16.4767, 'mean_values_integral': [5.5012]}})
    
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
        self.assertEqual(linear_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -3.7222, 'mean_values_derivative': [4.7484], 'average_value_integral': 16.154, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': -3.3064, 'mean_values_derivative': [5.2625], 'average_value_integral': 14.3492, 'mean_values_integral': [None]}})
    
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
        self.assertEqual(linear_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[5.1708, 17.426]]})
    
    def test_linear_models_logistic_accumulations(self):
        self.assertEqual(linear_models['models']['logistic']['accumulations'], {'range': 148.596, 'iqr': 81.8113})
    
    def test_linear_models_logistic_averages(self):
        self.assertEqual(linear_models['models']['logistic']['averages'], {'range': {'average_value_derivative': -2.7764, 'mean_values_derivative': [2.7256, 7.6156], 'average_value_integral': 16.5107, 'mean_values_integral': [5.4323]}, 'iqr': {'average_value_derivative': -3.2237, 'mean_values_derivative': [3.7276, 6.614], 'average_value_integral': 16.3623, 'mean_values_integral': [5.4749]}})
    
    def test_linear_models_logistic_correlation(self):
        self.assertEqual(linear_models['models']['logistic']['correlation'], 0.9974)
    
    def test_linear_models_sinusoidal_constants(self):
        self.assertEqual(linear_models['models']['sinusoidal']['constants'], [3.6953, 1.8762, 3.8255, 16.5])
    
    def test_linear_models_sinusoidal_points(self):
        self.assertEqual(linear_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[4.6627, 20.1953], [8.0115, 20.1953], [11.3603, 20.1953], ['4.6627 + 3.3488k', 20.1953]], 'minima': [[6.3372, 12.8047], [9.686, 12.8047], [13.0348, 12.8047], ['6.3372 + 3.3488k', 12.8047]], 'inflections': [[3.8255, 16.5], [5.4999, 16.5], [7.1743, 16.5], [8.8487, 16.5], [10.5231, 16.5], ['3.8255 + 1.6744k', 16.5]]})
    
    def test_linear_models_sinusoidal_accumulations(self):
        self.assertEqual(linear_models['models']['sinusoidal']['accumulations'], {'range': 148.4997, 'iqr': 82.5004})
    
    def test_linear_models_sinusoidal_averages(self):
        self.assertEqual(linear_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': -0.6828, 'mean_values_derivative': [4.7153, 6.2846, 8.0642, 9.6335, '4.7153 + 3.3489k', '6.2846 + 3.3489k'], 'average_value_integral': 16.5, 'mean_values_integral': [3.8255, 5.5, 7.1744, 8.8489, '3.8255 + 3.3489k', '5.5 + 3.3489k']}, 'iqr': {'average_value_derivative': 1.4778, 'mean_values_derivative': [4.5482, 6.4517, 7.8971, '4.5482 + 3.3489k', '6.4517 + 3.3489k'], 'average_value_integral': 16.5001, 'mean_values_integral': [3.8255, 5.4999, 7.1744, '3.8255 + 3.3489k', '5.4999 + 3.3489k']}})
    
    def test_linear_models_sinusoidal_correlation(self):
        self.assertEqual(linear_models['models']['sinusoidal']['correlation'], 0.3046)
    
    def test_linear_statistics(self):
        self.assertEqual(linear_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_linear_optimal(self):
        self.assertEqual(linear_models['optimal']['option'], 'linear')

quadratic_models = run_all(quadratic_set)

class TestQuadraticModels(unittest.TestCase):
    maxDiff = None

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
        self.assertEqual(quadratic_models['models']['cubic']['constants'], [-0.0001, -2.0, 23.0, -11.0])
    
    def test_quadratic_models_cubic_points(self):
        self.assertEqual(quadratic_models['models']['cubic']['points'], {'roots': [[-20011.4937, 0], [0.5, 0], [10.9937, 0]], 'maxima': [[5.7475, 55.106]], 'minima': [[-13339.0809, -118825262.2912]], 'inflections': [[-6666.6667, -59412604.0378]]})
    
    def test_quadratic_models_cubic_accumulations(self):
        self.assertEqual(quadratic_models['models']['cubic']['accumulations'], {'range': 373.25, 'iqr': 254.0663})
    
    def test_quadratic_models_cubic_averages(self):
        self.assertEqual(quadratic_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.9889, 'mean_values_derivative': [5.5005], 'average_value_integral': 41.4722, 'mean_values_integral': [3.1376, 8.3571]}, 'iqr': {'average_value_derivative': 0.9903, 'mean_values_derivative': [5.5002], 'average_value_integral': 50.8133, 'mean_values_integral': [4.2831, 7.2119]}})
    
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
        self.assertEqual(quadratic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 1.7271, 'mean_values_derivative': [5.6673], 'average_value_integral': 34.7876, 'mean_values_integral': [3.2842]}, 'iqr': {'average_value_derivative': 1.7172, 'mean_values_derivative': [5.5515], 'average_value_integral': 34.5886, 'mean_values_integral': [3.2784]}})
    
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
        self.assertEqual(quadratic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[1.7096, 21.976]]})
    
    def test_quadratic_models_logistic_accumulations(self):
        self.assertEqual(quadratic_models['models']['logistic']['accumulations'], {'range': 359.1381, 'iqr': 217.9023})
    
    def test_quadratic_models_logistic_averages(self):
        self.assertEqual(quadratic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 3.886, 'mean_values_derivative': [3.2626], 'average_value_integral': 39.9042, 'mean_values_integral': [2.9037]}, 'iqr': {'average_value_derivative': 0.6837, 'mean_values_derivative': [4.21], 'average_value_integral': 43.5805, 'mean_values_integral': [4.1962]}})
    
    def test_quadratic_models_logistic_correlation(self):
        self.assertEqual(quadratic_models['models']['logistic']['correlation'], 0.7235)
    
    def test_quadratic_models_sinusoidal_constants(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['constants'], [-45.0, 0.3267, -8.6568, 10.9862])
    
    def test_quadratic_models_sinusoidal_points(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['points'], {'roots': [[11.3304, 0.0], [19.4367, 0.0], [30.5627, 0.0], [38.669, 0.0], ['11.3304 + 19.2323k', 0.0], ['19.4367 + 19.2323k', 0.0]], 'maxima': [[5.7674, 55.9862], [24.9996, 55.9862], [44.2318, 55.9862], ['5.7674 + 19.2322k', 55.9862]], 'minima': [[15.3835, -34.0138], [34.6157, -34.0138], [53.8479, -34.0138], ['15.3835 + 19.2322k', -34.0138]], 'inflections': [[10.5754, 10.9862], [20.1915, 10.9862], [29.8076, 10.9862], [39.4237, 10.9862], [49.0398, 10.9862], ['10.5754 + 9.6161k', 10.9862]]})
    
    def test_quadratic_models_sinusoidal_accumulations(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['accumulations'], {'range': 371.9185, 'iqr': 254.9709})
    
    def test_quadratic_models_sinusoidal_averages(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.8681, 'mean_values_derivative': [5.5866, '5.5866 + 19.2323k', '15.5644 + 19.2323k'], 'average_value_integral': 41.3243, 'mean_values_integral': [3.224, 8.3109, '3.224 + 19.2323k', '8.3109 + 19.2323k']}, 'iqr': {'average_value_derivative': 1.1448, 'mean_values_derivative': [5.5288, '5.5288 + 19.2323k', '15.6221 + 19.2323k'], 'average_value_integral': 50.9942, 'mean_values_integral': [4.312, 7.2229, '4.312 + 19.2323k', '7.2229 + 19.2323k']}})
    
    def test_quadratic_models_sinusoidal_correlation(self):
        self.assertEqual(quadratic_models['models']['sinusoidal']['correlation'], 0.9983)
    
    def test_quadratic_statistics(self):
        self.assertEqual(quadratic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_quadratic_optimal(self):
        self.assertEqual(quadratic_models['optimal']['option'], 'quadratic')

cubic_models = run_all(cubic_set)

class TestCubicModels(unittest.TestCase):
    maxDiff = None

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
        self.assertEqual(cubic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 2.4589, 'mean_values_derivative': [5.6352], 'average_value_integral': 61.4876, 'mean_values_integral': [3.4445]}, 'iqr': {'average_value_derivative': 2.4497, 'mean_values_derivative': [5.5414], 'average_value_integral': 61.2589, 'mean_values_integral': [3.4407]}})
    
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
        self.assertEqual(cubic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[14.9001, 102.0]]})
    
    def test_cubic_models_logistic_accumulations(self):
        self.assertEqual(cubic_models['models']['logistic']['accumulations'], {'range': 578.2231, 'iqr': 319.917})
    
    def test_cubic_models_logistic_averages(self):
        self.assertEqual(cubic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 3.6426, 'mean_values_derivative': [5.2832], 'average_value_integral': 64.247, 'mean_values_integral': [5.6041]}, 'iqr': {'average_value_derivative': 3.6599, 'mean_values_derivative': [5.433], 'average_value_integral': 63.9834, 'mean_values_integral': [5.5324]}})
    
    def test_cubic_models_logistic_correlation(self):
        self.assertEqual(cubic_models['models']['logistic']['correlation'], 0.4433)
    
    def test_cubic_models_sinusoidal_constants(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['constants'], [-26.6739, 0.9479, -1.5548, 62.2016])
    
    def test_cubic_models_sinusoidal_points(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[3.4166, 88.8755], [10.0452, 88.8755], ['3.4166 + 6.6286k', 88.8755]], 'minima': [[6.7309, 35.5277], [13.3595, 35.5277], ['6.7309 + 6.6286k', 35.5277]], 'inflections': [[1.7595, 62.2016], [5.0738, 62.2016], [8.3881, 62.2016], [11.7024, 62.2016], ['1.7595 + 3.3143k', 62.2016]]})
    
    def test_cubic_models_sinusoidal_accumulations(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['accumulations'], {'range': 579.7687, 'iqr': 295.5756})
    
    def test_cubic_models_sinusoidal_averages(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 4.9151, 'mean_values_derivative': [3.2102, 6.9373, 9.8387, '3.2102 + 6.6285k', '6.9373 + 6.6285k'], 'average_value_integral': 64.4187, 'mean_values_integral': [1.8473, 4.9859, 8.4758, '1.8473 + 6.6285k', '4.9859 + 6.6285k']}, 'iqr': {'average_value_derivative': -6.8423, 'mean_values_derivative': [3.7057, 6.4418, '3.7057 + 6.6285k', '6.4418 + 6.6285k'], 'average_value_integral': 59.1151, 'mean_values_integral': [5.196, '5.196 + 6.6285k', '8.2656 + 6.6285k']}})
    
    def test_cubic_models_sinusoidal_correlation(self):
        self.assertEqual(cubic_models['models']['sinusoidal']['correlation'], 0.8205)
    
    def test_cubic_statistics(self):
        self.assertEqual(cubic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_cubic_optimal(self):
        self.assertEqual(cubic_models['optimal']['option'], 'cubic')

hyperbolic_models = run_all(hyperbolic_set)

class TestHyperbolicModels(unittest.TestCase):
    maxDiff = None

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
        self.assertEqual(hyperbolic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -152.4631, 'mean_values_derivative': [4.7473], 'average_value_integral': 660.5919, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': -135.3796, 'mean_values_derivative': [5.2622], 'average_value_integral': 586.5725, 'mean_values_integral': [None]}})
    
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
        self.assertEqual(hyperbolic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[0.6592, 2393.5]]})
    
    def test_hyperbolic_models_logistic_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['accumulations'], {'range': 5357.8056, 'iqr': 2071.3903})
    
    def test_hyperbolic_models_logistic_averages(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': -238.1916, 'mean_values_derivative': [4.6875], 'average_value_integral': 595.3117, 'mean_values_integral': [4.304]}, 'iqr': {'average_value_derivative': -194.2074, 'mean_values_derivative': [5.1556], 'average_value_integral': 414.2781, 'mean_values_integral': [5.06]}})
    
    def test_hyperbolic_models_logistic_correlation(self):
        self.assertEqual(hyperbolic_models['models']['logistic']['correlation'], 0.9428)
    
    def test_hyperbolic_models_sinusoidal_constants(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['constants'], [448.548, 1.1869, -0.0788, 746.6978])
    
    def test_hyperbolic_models_sinusoidal_points(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[1.2446, 1195.2458], [6.5384, 1195.2458], ['1.2446 + 5.2938k', 1195.2458]], 'minima': [[3.8915, 298.1498], [9.1853, 298.1498], ['3.8915 + 5.2938k', 298.1498]], 'inflections': [[2.5681, 746.6978], [5.215, 746.6978], [7.8619, 746.6978], [10.5088, 746.6978], ['2.5681 + 2.6469k', 746.6978]]})
    
    def test_hyperbolic_models_sinusoidal_accumulations(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['accumulations'], {'range': 6517.3946, 'iqr': 3777.0004})
    
    def test_hyperbolic_models_sinusoidal_averages(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': -76.0512, 'mean_values_derivative': [1.3654, 3.7708, 6.6592, 9.0645, '1.3654 + 5.2938k', '3.7708 + 5.2938k'], 'average_value_integral': 724.155, 'mean_values_integral': [2.6105, 5.1726, 7.9043, '2.6105 + 5.2938k', '5.1726 + 5.2938k']}, 'iqr': {'average_value_derivative': 29.3583, 'mean_values_derivative': [3.938, 6.4919, '3.938 + 5.2938k', '6.4919 + 5.2938k'], 'average_value_integral': 755.4001, 'mean_values_integral': [5.2313, 7.8455, '5.2313 + 5.2938k', '7.8455 + 5.2938k']}})
    
    def test_hyperbolic_models_sinusoidal_correlation(self):
        self.assertEqual(hyperbolic_models['models']['sinusoidal']['correlation'], 0.4914)
    
    def test_hyperbolic_statistics(self):
        self.assertEqual(hyperbolic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_hyperbolic_optimal(self):
        self.assertEqual(hyperbolic_models['optimal']['option'], 'hyperbolic')

exponential_models = run_all(exponential_set)

class TestExponentialModels(unittest.TestCase):
    maxDiff = None

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
        self.assertEqual(exponential_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 340.4961, 'mean_values_derivative': [7.3559], 'average_value_integral': 491.2674, 'mean_values_integral': [5.465]}, 'iqr': {'average_value_derivative': 148.7393, 'mean_values_derivative': [6.161], 'average_value_integral': 214.6009, 'mean_values_integral': [4.6368]}})
    
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
        self.assertEqual(exponential_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[10.0383, 3069.0]]})
    
    def test_exponential_models_logistic_accumulations(self):
        self.assertEqual(exponential_models['models']['logistic']['accumulations'], {'range': 4289.0764, 'iqr': 824.4254})
    
    def test_exponential_models_logistic_averages(self):
        self.assertEqual(exponential_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 334.5852, 'mean_values_derivative': [7.1897], 'average_value_integral': 476.564, 'mean_values_integral': [7.475]}, 'iqr': {'average_value_derivative': 149.1394, 'mean_values_derivative': [6.2787], 'average_value_integral': 164.8851, 'mean_values_integral': [6.3203]}})
    
    def test_exponential_models_logistic_correlation(self):
        self.assertEqual(exponential_models['models']['logistic']['correlation'], 0.9983)
    
    def test_exponential_models_sinusoidal_constants(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['constants'], [3065.0, 0.1022, 9.0, 1641.6143])
    
    def test_exponential_models_sinusoidal_points(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['points'], {'roots': [[3.4695, 0.0], [45.2702, 0.0], [64.9488, 0.0], [106.7495, 0.0], [126.4281, 0.0], ['3.4695 + 61.4793k', 0.0], ['45.2702 + 61.4793k', 0.0]], 'maxima': [[24.3698, 4706.6143], [85.8492, 4706.6143], ['24.3698 + 61.4794k', 4706.6143]], 'minima': [[55.1095, -1423.3857], [116.5889, -1423.3857], ['55.1095 + 61.4794k', -1423.3857]], 'inflections': [[9.0, 1641.6143], [39.7397, 1641.6143], [70.4794, 1641.6143], [101.2191, 1641.6143], ['9.0 + 30.7397k', 1641.6143]]})
    
    def test_exponential_models_sinusoidal_accumulations(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['accumulations'], {'range': 5453.3259, 'iqr': 2900.6589})
    
    def test_exponential_models_sinusoidal_averages(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 283.1817, 'mean_values_derivative': [4.6782, '4.6782 + 61.4793k', '13.3218 + 61.4793k'], 'average_value_integral': 605.9251, 'mean_values_integral': [5.6273, '5.6273 + 61.4793k', '43.1124 + 61.4793k']}, 'iqr': {'average_value_derivative': 290.2342, 'mean_values_derivative': [5.2263, '5.2263 + 61.4793k', '12.7737 + 61.4793k'], 'average_value_integral': 580.1318, 'mean_values_integral': [5.5396, '5.5396 + 61.4793k', '43.2 + 61.4793k']}})
    
    def test_exponential_models_sinusoidal_correlation(self):
        self.assertEqual(exponential_models['models']['sinusoidal']['correlation'], 0.8194)
    
    def test_exponential_statistics(self):
        self.assertEqual(exponential_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_exponential_optimal(self):
        self.assertEqual(exponential_models['optimal']['option'], 'exponential')

logarithmic_models = run_all(logarithmic_set)

class TestLogarithmicModels(unittest.TestCase):
    maxDiff = None

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
        self.assertEqual(logarithmic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 0.8419, 'mean_values_derivative': [5.9382], 'average_value_integral': 6.4124, 'mean_values_integral': [2.81]}, 'iqr': {'average_value_derivative': 0.8092, 'mean_values_derivative': [5.6364], 'average_value_integral': 6.1633, 'mean_values_integral': [None]}})
    
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
        self.assertEqual(logarithmic_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[2.5092, 4.3446]]})
    
    def test_logarithmic_models_logistic_accumulations(self):
        self.assertEqual(logarithmic_models['models']['logistic']['accumulations'], {'range': 59.9282, 'iqr': 35.5211})
    
    def test_logarithmic_models_logistic_averages(self):
        self.assertEqual(logarithmic_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.6653, 'mean_values_derivative': [5.4198], 'average_value_integral': 6.6587, 'mean_values_integral': [4.5913]}, 'iqr': {'average_value_derivative': 0.6754, 'mean_values_derivative': [5.3806], 'average_value_integral': 7.1042, 'mean_values_integral': [5.1391]}})
    
    def test_logarithmic_models_logistic_correlation(self):
        self.assertEqual(logarithmic_models['models']['logistic']['correlation'], 0.9898)
    
    def test_logarithmic_models_sinusoidal_constants(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['constants'], [-1.3224, 1.2013, 0.1451, 6.5218])
    
    def test_logarithmic_models_sinusoidal_points(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[4.0678, 7.8442], [9.2982, 7.8442], ['4.0678 + 5.2304k', 7.8442]], 'minima': [[1.4527, 5.1994], [6.6831, 5.1994], ['1.4527 + 5.2304k', 5.1994]], 'inflections': [[2.7603, 6.5218], [5.3755, 6.5218], [7.9907, 6.5218], [10.6059, 6.5218], ['2.7603 + 2.6152k', 6.5218]]})
    
    def test_logarithmic_models_sinusoidal_accumulations(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['accumulations'], {'range': 58.9486, 'iqr': 32.5637})
    
    def test_logarithmic_models_sinusoidal_averages(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.2235, 'mean_values_derivative': [1.5702, 3.9503, 6.8005, 9.1807, '1.5702 + 5.2303k', '3.9503 + 5.2303k'], 'average_value_integral': 6.5498, 'mean_values_integral': [2.7779, 5.3578, 8.0082, '2.7779 + 5.2303k', '5.3578 + 5.2303k']}, 'iqr': {'average_value_derivative': -0.0721, 'mean_values_derivative': [4.1056, 6.6452, '4.1056 + 5.2303k', '6.6452 + 5.2303k'], 'average_value_integral': 6.5127, 'mean_values_integral': [5.3811, 7.9848, '5.3811 + 5.2303k', '7.9848 + 5.2303k']}})
    
    def test_logarithmic_models_sinusoidal_correlation(self):
        self.assertEqual(logarithmic_models['models']['sinusoidal']['correlation'], 0.4601)
    
    def test_logarithmic_statistics(self):
        self.assertEqual(logarithmic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_logarithmic_optimal(self):
        self.assertEqual(logarithmic_models['optimal']['option'], 'logarithmic')

logistic_models = run_all(logistic_set)

class TestLogisticModels(unittest.TestCase):
    maxDiff = None

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
        self.assertEqual(logistic_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 3.941, 'mean_values_derivative': [8.0887], 'average_value_integral': 3.084, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': 0.5498, 'mean_values_derivative': [6.5474], 'average_value_integral': 0.4302, 'mean_values_integral': [None]}})
    
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
    
    def test_logistic_models_sinusoidal_constants(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['constants'], [-1.1746, 0.5011, -1.1199, 1.0508])
    
    def test_logistic_models_sinusoidal_points(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['points'], {'roots': [[1.0903, 0.0], [2.9393, 0.0], [13.6291, 0.0], [15.4781, 0.0], ['1.0903 + 12.5388k', 0.0], ['2.9393 + 12.5388k', 0.0]], 'maxima': [[8.2842, 2.2254], [20.823, 2.2254], ['8.2842 + 12.5388k', 2.2254]], 'minima': [[2.0148, -0.1238], [14.5536, -0.1238], ['2.0148 + 12.5388k', -0.1238]], 'inflections': [[5.1495, 1.0508], [11.4189, 1.0508], [17.6883, 1.0508], [23.9577, 1.0508], ['5.1495 + 6.2694k', 1.0508]]})
    
    def test_logistic_models_sinusoidal_accumulations(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['accumulations'], {'range': 10.092, 'iqr': 6.0321})
    
    def test_logistic_models_sinusoidal_averages(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.1992, 'mean_values_derivative': [2.7038, 7.5952, '2.7038 + 12.5388k', '7.5952 + 12.5388k'], 'average_value_integral': 1.1213, 'mean_values_integral': [5.2693, '5.2693 + 12.5388k', '11.2991 + 12.5388k']}, 'iqr': {'average_value_derivative': 0.4394, 'mean_values_derivative': [3.6968, 6.6022, '3.6968 + 12.5388k', '6.6022 + 12.5388k'], 'average_value_integral': 1.2064, 'mean_values_integral': [5.4146, '5.4146 + 12.5388k', '11.1538 + 12.5388k']}})
    
    def test_logistic_models_sinusoidal_correlation(self):
        self.assertEqual(logistic_models['models']['sinusoidal']['correlation'], 0.9789)
    
    def test_logistic_statistics(self):
        self.assertEqual(logistic_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_logistic_optimal(self):
        self.assertEqual(logistic_models['optimal']['option'], 'logistic')

sinusoidal_models = run_all(sinusoidal_set)

class TestSinusoidalModels(unittest.TestCase):
    maxDiff = None

    def test_sinusoidal_models_linear_constants(self):
        self.assertEqual(sinusoidal_models['models']['linear']['constants'], [0.0303, 3.3333])
    
    def test_sinusoidal_models_linear_points(self):
        self.assertEqual(sinusoidal_models['models']['linear']['points'], {'roots': [[-110.0099, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_sinusoidal_models_linear_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['linear']['accumulations'], {'range': 31.4995, 'iqr': 17.4997})
    
    def test_sinusoidal_models_linear_averages(self):
        self.assertEqual(sinusoidal_models['models']['linear']['averages'], {'range': {'average_value_derivative': 0.0303, 'mean_values_derivative': ['All'], 'average_value_integral': 3.4999, 'mean_values_integral': [5.4983]}, 'iqr': {'average_value_derivative': 0.0303, 'mean_values_derivative': ['All'], 'average_value_integral': 3.4999, 'mean_values_integral': [5.4983]}})
    
    def test_sinusoidal_models_linear_correlation(self):
        self.assertEqual(sinusoidal_models['models']['linear']['correlation'], 0.0249)
    
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
    
    def test_sinusoidal_models_cubic_constants(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['constants'], [0.0466, -0.6177, 1.9114, 2.6667])
    
    def test_sinusoidal_models_cubic_points(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['points'], {'roots': [[-1.0275, 0]], 'maxima': [[1.9997, 4.3915]], 'minima': [[6.8372, 1.7538]], 'inflections': [[4.4185, 3.0726]]})
    
    def test_sinusoidal_models_cubic_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['accumulations'], {'range': 29.4088, 'iqr': 12.8103})
    
    def test_sinusoidal_models_cubic_averages(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 0.2893, 'mean_values_derivative': [1.6043, 7.2327], 'average_value_integral': 3.2676, 'mean_values_integral': [4.1793, 8.7223]}, 'iqr': {'average_value_derivative': -0.3631, 'mean_values_derivative': [6.2221], 'average_value_integral': 2.5621, 'mean_values_integral': [5.0576]}})
    
    def test_sinusoidal_models_cubic_correlation(self):
        self.assertEqual(sinusoidal_models['models']['cubic']['correlation'], 0.3929)
    
    def test_sinusoidal_models_hyperbolic_constants(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['constants'], [0.7138, 3.2909])
    
    def test_sinusoidal_models_hyperbolic_points(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['points'], {'roots': [[-0.2169, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_sinusoidal_models_hyperbolic_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['accumulations'], {'range': 31.2617, 'iqr': 17.1546})
    
    def test_sinusoidal_models_hyperbolic_averages(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': -0.0714, 'mean_values_derivative': [3.1618], 'average_value_integral': 3.4735, 'mean_values_integral': [3.9091]}, 'iqr': {'average_value_derivative': -0.0297, 'mean_values_derivative': [4.9024], 'average_value_integral': 3.4309, 'mean_values_integral': [5.0986]}})
    
    def test_sinusoidal_models_hyperbolic_correlation(self):
        self.assertEqual(sinusoidal_models['models']['hyperbolic']['correlation'], 0.0536)
    
    def test_sinusoidal_models_exponential_constants(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['constants'], [0.9234, 0.8984])
    
    def test_sinusoidal_models_exponential_points(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_sinusoidal_models_exponential_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['accumulations'], {'range': 4.7909, 'iqr': 2.5919})
    
    def test_sinusoidal_models_exponential_averages(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['averages'], {'range': {'average_value_derivative': -0.057, 'mean_values_derivative': [5.1465], 'average_value_integral': 0.5323, 'mean_values_integral': [1.6828]}, 'iqr': {'average_value_derivative': -0.0555, 'mean_values_derivative': [5.3954], 'average_value_integral': 0.5184, 'mean_values_integral': [None]}})
    
    def test_sinusoidal_models_exponential_correlation(self):
        self.assertEqual(sinusoidal_models['models']['exponential']['correlation'], 0.0)
    
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
    
    def test_sinusoidal_models_logistic_constants(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['constants'], [3.5, 6.2649, -14.3299])
    
    def test_sinusoidal_models_logistic_points(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[-14.3299, 1.75]]})
    
    def test_sinusoidal_models_logistic_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['accumulations'], {'range': 31.5, 'iqr': 17.5})
    
    def test_sinusoidal_models_logistic_averages(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 3.5, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 3.5, 'mean_values_integral': [None]}})
    
    def test_sinusoidal_models_logistic_correlation(self):
        self.assertEqual(sinusoidal_models['models']['logistic']['correlation'], 0.0)
    
    def test_sinusoidal_models_sinusoidal_constants(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['constants'], [-5.0, 1.5708, 3.0, 3.0])
    
    def test_sinusoidal_models_sinusoidal_points(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['points'], {'roots': [[3.4097, 0], [4.5903, 0], [7.4097, 0], [8.5903, 0], ['3.4097 + 4.0k', 0], ['4.5903 + 4.0k', 0]], 'maxima': [[6.0, 8.0], [10.0, 8.0], ['6.0 + 4.0k', 8.0]], 'minima': [[4.0, -2.0], [8.0, -2.0], ['4.0 + 4.0k', -2.0]], 'inflections': [[3.0, 3.0], [5.0, 3.0], [7.0, 3.0], [9.0, 3.0], ['3.0 + 2.0k', 3.0]]})
    
    def test_sinusoidal_models_sinusoidal_accumulations(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['accumulations'], {'range': 30.1832, 'iqr': 11.8169})
    
    def test_sinusoidal_models_sinusoidal_averages(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.5556, 'mean_values_derivative': [4.0451, 5.9549, 8.0451, 9.9549, '4.0451 + 4.0k', '5.9549 + 4.0k'], 'average_value_integral': 3.3537, 'mean_values_integral': [2.9549, 5.0451, 6.9549, 9.0451, '2.9549 + 4.0k', '5.0451 + 4.0k']}, 'iqr': {'average_value_derivative': -1.0, 'mean_values_derivative': [3.9187, 6.0813, 7.9187, '3.9187 + 4.0k', '6.0813 + 4.0k'], 'average_value_integral': 2.3634, 'mean_values_integral': [3.0813, 4.9187, 7.0813, '3.0813 + 4.0k', '4.9187 + 4.0k']}})
    
    def test_sinusoidal_models_sinusoidal_correlation(self):
        self.assertEqual(sinusoidal_models['models']['sinusoidal']['correlation'], 1.0)
    
    def test_sinusoidal_statistics(self):
        self.assertEqual(sinusoidal_models['statistics'], {'minimum': 1, 'maximum': 10, 'q1': 3, 'q3': 8, 'mean': 5.5, 'median': 5.5})
    
    def test_sinusoidal_optimal(self):
        self.assertEqual(sinusoidal_models['optimal']['option'], 'sinusoidal')

large_models = run_all(large_set)

class TestLargeModels(unittest.TestCase):
    maxDiff = None

    def test_large_models_linear_constants(self):
        self.assertEqual(large_models['models']['linear']['constants'], [0.4934, 414.5401])
    
    def test_large_models_linear_points(self):
        self.assertEqual(large_models['models']['linear']['points'], {'roots': [[-840.1704, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_large_models_linear_accumulations(self):
        self.assertEqual(large_models['models']['linear']['accumulations'], {'range': 47829.5566, 'iqr': 22178.5177})
    
    def test_large_models_linear_averages(self):
        self.assertEqual(large_models['models']['linear']['averages'], {'range': {'average_value_derivative': 0.4934, 'mean_values_derivative': ['All'], 'average_value_integral': 488.0567, 'mean_values_integral': [149.0]}, 'iqr': {'average_value_derivative': 0.4934, 'mean_values_derivative': ['All'], 'average_value_integral': 487.4399, 'mean_values_integral': [147.7499]}})
    
    def test_large_models_linear_correlation(self):
        self.assertEqual(large_models['models']['linear']['correlation'], 0.1013)
    
    def test_large_models_quadratic_constants(self):
        self.assertEqual(large_models['models']['quadratic']['constants'], [-0.007, 2.5668, 265.4919])
    
    def test_large_models_quadratic_points(self):
        self.assertEqual(large_models['models']['quadratic']['points'], {'roots': [[-84.1305, 0], [450.8163, 0]], 'maxima': [[183.3429, 500.7941]], 'minima': [None], 'inflections': [None]})
    
    def test_large_models_quadratic_accumulations(self):
        self.assertEqual(large_models['models']['quadratic']['accumulations'], {'range': 47719.7051, 'iqr': 22327.6925})
    
    def test_large_models_quadratic_averages(self):
        self.assertEqual(large_models['models']['quadratic']['averages'], {'range': {'average_value_derivative': 0.4808, 'mean_values_derivative': [149.0], 'average_value_integral': 486.9358, 'mean_values_integral': [138.8484]}, 'iqr': {'average_value_derivative': 0.4983, 'mean_values_derivative': [147.75], 'average_value_integral': 490.7185, 'mean_values_integral': [145.4038]}})
    
    def test_large_models_quadratic_correlation(self):
        self.assertEqual(large_models['models']['quadratic']['correlation'], 0.1071)
    
    def test_large_models_cubic_constants(self):
        self.assertEqual(large_models['models']['cubic']['constants'], [0.0005, -0.2204, 33.8099, -1226.1398])
    
    def test_large_models_cubic_points(self):
        self.assertEqual(large_models['models']['cubic']['points'], {'roots': [[51.579, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[146.9333, 569.4583]]})
    
    def test_large_models_cubic_accumulations(self):
        self.assertEqual(large_models['models']['cubic']['accumulations'], {'range': 56339.2625, 'iqr': 25972.9632})
    
    def test_large_models_cubic_averages(self):
        self.assertEqual(large_models['models']['cubic']['averages'], {'range': {'average_value_derivative': 2.6327, 'mean_values_derivative': [118.5678, 175.2989], 'average_value_integral': 574.8904, 'mean_values_integral': [150.7241]}, 'iqr': {'average_value_derivative': 1.6856, 'mean_values_derivative': [133.7726, 160.094], 'average_value_integral': 570.8344, 'mean_values_integral': [147.8981]}})
    
    def test_large_models_cubic_correlation(self):
        self.assertEqual(large_models['models']['cubic']['correlation'], 0.0)
    
    def test_large_models_hyperbolic_constants(self):
        self.assertEqual(large_models['models']['hyperbolic']['constants'], [-10786.2465, 563.019])
    
    def test_large_models_hyperbolic_points(self):
        self.assertEqual(large_models['models']['hyperbolic']['points'], {'roots': [[19.1579, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_large_models_hyperbolic_accumulations(self):
        self.assertEqual(large_models['models']['hyperbolic']['accumulations'], {'range': 47807.811, 'iqr': 22269.081})
    
    def test_large_models_hyperbolic_averages(self):
        self.assertEqual(large_models['models']['hyperbolic']['averages'], {'range': {'average_value_derivative': 0.5448, 'mean_values_derivative': [140.7073], 'average_value_integral': 487.8348, 'mean_values_integral': [143.4643]}, 'iqr': {'average_value_derivative': 0.5061, 'mean_values_derivative': [145.9879], 'average_value_integral': 489.4304, 'mean_values_integral': [146.575]}})
    
    def test_large_models_hyperbolic_correlation(self):
        self.assertEqual(large_models['models']['hyperbolic']['correlation'], 0.1082)
    
    def test_large_models_exponential_constants(self):
        self.assertEqual(large_models['models']['exponential']['constants'], [407.8094, 1.0009])
    
    def test_large_models_exponential_points(self):
        self.assertEqual(large_models['models']['exponential']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_large_models_exponential_accumulations(self):
        self.assertEqual(large_models['models']['exponential']['accumulations'], {'range': 45712.6755, 'iqr': 21194.5052})
    
    def test_large_models_exponential_averages(self):
        self.assertEqual(large_models['models']['exponential']['averages'], {'range': {'average_value_derivative': 0.4196, 'mean_values_derivative': [149.3031], 'average_value_integral': 466.4559, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': 0.419, 'mean_values_derivative': [147.7124], 'average_value_integral': 465.8133, 'mean_values_integral': [None]}})
    
    def test_large_models_exponential_correlation(self):
        self.assertEqual(large_models['models']['exponential']['correlation'], 0.0)
    
    def test_large_models_logarithmic_constants(self):
        self.assertEqual(large_models['models']['logarithmic']['constants'], [74.0076, 118.997])
    
    def test_large_models_logarithmic_points(self):
        self.assertEqual(large_models['models']['logarithmic']['points'], {'roots': [[0.2003, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_large_models_logarithmic_accumulations(self):
        self.assertEqual(large_models['models']['logarithmic']['accumulations'], {'range': 47818.8482, 'iqr': 22222.6107})
    
    def test_large_models_logarithmic_averages(self):
        self.assertEqual(large_models['models']['logarithmic']['averages'], {'range': {'average_value_derivative': 0.5159, 'mean_values_derivative': [143.4534], 'average_value_integral': 487.9474, 'mean_values_integral': [146.2481]}, 'iqr': {'average_value_derivative': 0.5049, 'mean_values_derivative': [146.5787], 'average_value_integral': 488.409, 'mean_values_integral': [147.1631]}})
    
    def test_large_models_logarithmic_correlation(self):
        self.assertEqual(large_models['models']['logarithmic']['correlation'], 0.1047)
    
    def test_large_models_logistic_constants(self):
        self.assertEqual(large_models['models']['logistic']['constants'], [488.2, 1.0, 1.0])
    
    def test_large_models_logistic_points(self):
        self.assertEqual(large_models['models']['logistic']['points'], {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[1.0, 244.1]]})
    
    def test_large_models_logistic_accumulations(self):
        self.assertEqual(large_models['models']['logistic']['accumulations'], {'range': 47843.6, 'iqr': 22213.1})
    
    def test_large_models_logistic_averages(self):
        self.assertEqual(large_models['models']['logistic']['averages'], {'range': {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 488.2, 'mean_values_integral': [None]}, 'iqr': {'average_value_derivative': 0.0, 'mean_values_derivative': [None], 'average_value_integral': 488.2, 'mean_values_integral': [None]}})
    
    def test_large_models_logistic_correlation(self):
        self.assertEqual(large_models['models']['logistic']['correlation'], 0.0)
    
    def test_large_models_sinusoidal_constants(self):
        self.assertEqual(large_models['models']['sinusoidal']['constants'], [32.3199, 1.0085, 1.8848, 488.9635])
    
    def test_large_models_sinusoidal_points(self):
        self.assertEqual(large_models['models']['sinusoidal']['points'], {'roots': [None], 'maxima': [[103.1256, 521.2834], [109.3558, 521.2834], [115.586, 521.2834], ['103.1256 + 6.2302k', 521.2834]], 'minima': [[100.0105, 456.6436], [106.2407, 456.6436], [112.4709, 456.6436], ['100.0105 + 6.2302k', 456.6436]], 'inflections': [[101.568, 488.9635], [104.6831, 488.9635], [107.7982, 488.9635], [110.9133, 488.9635], [114.0284, 488.9635], ['101.568 + 3.1151k', 488.9635]]})
    
    def test_large_models_sinusoidal_accumulations(self):
        self.assertEqual(large_models['models']['sinusoidal']['accumulations'], {'range': 47949.813, 'iqr': 22220.5541})
    
    def test_large_models_sinusoidal_averages(self):
        self.assertEqual(large_models['models']['sinusoidal']['averages'], {'range': {'average_value_derivative': 0.3752, 'mean_values_derivative': [100.0223, 103.1146, 106.2525, 109.3448, 112.4828, 115.5751, '100.0223 + 6.2302k', '103.1146 + 6.2302k'], 'average_value_integral': 489.2838, 'mean_values_integral': [101.5778, 104.6733, 107.808, 110.9035, 114.0382, 117.1337, 120.2684, 123.3639, 126.4986, 129.5941, '101.5778 + 6.2302k', '104.6733 + 6.2302k']}, 'iqr': {'average_value_derivative': 0.9868, 'mean_values_derivative': [128.0169, 131.1921, 134.2471, 137.4223, 140.4774, 143.6525, '128.0169 + 6.2302k', '131.1921 + 6.2302k'], 'average_value_integral': 488.3638, 'mean_values_integral': [126.4704, 129.6223, 132.7006, 135.8525, 138.9308, 142.0827, 145.161, 148.3129, 151.3912, 154.5431, '126.4704 + 6.2302k', '129.6223 + 6.2302k']}})
    
    def test_large_models_sinusoidal_correlation(self):
        self.assertEqual(large_models['models']['sinusoidal']['correlation'], 0.1727)
    
    def test_large_statistics(self):
        self.assertEqual(large_models['statistics'], {'minimum': 100, 'maximum': 198, 'q1': 125.0, 'q3': 170.5, 'mean': 149.29, 'median': 151.5})
    
    def test_large_optimal(self):
        self.assertEqual(large_models['optimal']['option'], 'sinusoidal')

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 420 tests in 0.028s ---------- OK ---------- #