from .errors.matrices import matrix_of_scalars
from .errors.scalars import positive_integer
from .models.linear import linear_model
from .models.quadratic import quadratic_model
from .models.cubic import cubic_model
from .models.hyperbolic import hyperbolic_model
from .models.exponential import exponential_model
from .models.logarithmic import logarithmic_model
from .models.logistic import logistic_model
from .models.sinusoidal import sinusoidal_model
from .vectors.dimension import single_dimension
from .statistics.minimum import minimum_value
from .statistics.maximum import maximum_value
from .statistics.quartiles import quartile_value
from .statistics.mean import mean_value
from .statistics.median import median_value

def run_all(data, precision):
    """
    Generates all eight key regression models (linear, quadratic, cubic, hyperbolic, exponential, logarithmic, logistic, and sinusoidal) for a given data set, in addition to determining the best fit based correlation and providing various statistical measures

    Parameters
    ----------
    data : list or tuple
        List of lists of numbers representing a collection of coordinate pairs
    precision : int
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list or tuple
    TypeError
        Elements nested within first argument must be integers or floats
    ValueError
        First argument must contain at least 10 elements
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    results['models']['linear'] : dict
        See `models.linear`
    results['models']['quadratic'] : dict
        See `models.quadratic`
    results['models']['cubic'] : dict
        See `models.cubic`
    results['models']['hyperbolic'] : dict
        See `models.hyperbolic`
    results['models']['exponential'] : dict
        See `models.exponential`
    results['models']['logarithmic'] : dict
        See `models.logarithmic`
    results['models']['logistic'] : dict
        See `models.logistic`
    results['models']['sinusoidal'] : dict
        See `models.sinusoidal`
    results['statistics']['minimum'] : int or float
        Smallest value of the independent variable from the provided data set
    results['statistics']['maximum'] : int or float
        Largest value of the independent variable from the provided data set
    results['statistics']['q1'] : int or float
        First quartile of the independent variable from the provided data set, below which 25% of the data points lie
    results['statistics']['q3'] : int or float
        Third quartile of the independent variable from the provided data set, above which 25% of the data points lie
    results['statistics']['mean'] : int or float
        Arithmetic mean of the independent variable from the provided data set
    results['statistics']['median'] : int or float
        Median of the independent variable from the provided data set, which splits the data in half
    results['optimal']['option'] : str
        Name of the model with the highest correlation for this particular data set (e.g., 'cubic' if the cubic model has a higher correlation than all other seven models)
    results['optimal']['correlation'] : float
        Value of the correlation for the model with the best fit (i.e., the model listed in ['optimal']['option'])

    Examples
    --------
    Generate all eight regression models for the data set [[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], then print each model's coefficients, the mean of the data set, and the name of the model with the best fit (and round the results to four decimal places, where applicable)
        >>> results = run_all([[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]], 4)
        >>> print(results['models']['linear']['constants'])
        [1.9636, 23.0]
        >>> print(results['models']['quadratic']['constants'])
        [-0.3106, 5.3803, 16.1667]
        >>> print(results['models']['cubic']['constants'])
        [-0.3881, 6.0932, -24.155, 49.4667]
        >>> print(results['models']['hyperbolic']['constants'])
        [-13.5246, 37.7613]
        >>> print(results['models']['exponential']['constants'])
        [22.1049, 1.0692]
        >>> print(results['models']['logarithmic']['constants'])
        [7.4791, 22.5032]
        >>> print(results['models']['logistic']['constants'])
        [43.983, 0.3076, 0.9746]
        >>> print(results['models']['sinusoidal']['constants'])
        [14.0875, 0.7119, -3.7531, 34.2915]
        >>> print(results['statistics']['mean'])
        5.5
        >>> print(results['optimal']['option'])
        'sinusoidal'
    Generate all eight regression models for the data set [[169, 423], [122, 391], [178, 555], [131, 284], [120, 520], [179, 558], [164, 265], [167, 338], [198, 445], [139, 402], [183, 725], [133, 470], [156, 573], [159, 325], [121, 653], [118, 358], [122, 633], [167, 487], [161, 453], [194, 488], [170, 517], [124, 377], [191, 310], [194, 398], [173, 744], [166, 389], [113, 583], [109, 380], [126, 668], [144, 491], [107, 533], [188, 355], [147, 553], [169, 497], [121, 606], [132, 373], [111, 554], [173, 669], [177, 483], [122, 340], [171, 286], [108, 681], [139, 502], [115, 339], [174, 396], [134, 625], [147, 435], [146, 555], [147, 656], [126, 354], [155, 679], [181, 629], [149, 417], [119, 374], [102, 422], [112, 292], [108, 464], [109, 559], [112, 635], [159, 518], [180, 304], [185, 567], [165, 299], [160, 337], [133, 730], [193, 374], [164, 537], [172, 592], [173, 660], [186, 290], [170, 670], [192, 687], [154, 596], [154, 464], [125, 383], [193, 559], [155, 586], [149, 406], [131, 590], [127, 339], [163, 378], [145, 254], [156, 395], [166, 355], [189, 661], [133, 685], [168, 685], [190, 736], [145, 564], [125, 470], [129, 541], [133, 439], [162, 486], [125, 387], [183, 596], [135, 733], [106, 329], [100, 279], [102, 439], [162, 454]], then print each model's coefficients, the mean of the data set, and the name of the model with the best fit (and round the results to four decimal places, where applicable)
        >>> results_large = run_all([[169, 423], [122, 391], [178, 555], [131, 284], [120, 520], [179, 558], [164, 265], [167, 338], [198, 445], [139, 402], [183, 725], [133, 470], [156, 573], [159, 325], [121, 653], [118, 358], [122, 633], [167, 487], [161, 453], [194, 488], [170, 517], [124, 377], [191, 310], [194, 398], [173, 744], [166, 389], [113, 583], [109, 380], [126, 668], [144, 491], [107, 533], [188, 355], [147, 553], [169, 497], [121, 606], [132, 373], [111, 554], [173, 669], [177, 483], [122, 340], [171, 286], [108, 681], [139, 502], [115, 339], [174, 396], [134, 625], [147, 435], [146, 555], [147, 656], [126, 354], [155, 679], [181, 629], [149, 417], [119, 374], [102, 422], [112, 292], [108, 464], [109, 559], [112, 635], [159, 518], [180, 304], [185, 567], [165, 299], [160, 337], [133, 730], [193, 374], [164, 537], [172, 592], [173, 660], [186, 290], [170, 670], [192, 687], [154, 596], [154, 464], [125, 383], [193, 559], [155, 586], [149, 406], [131, 590], [127, 339], [163, 378], [145, 254], [156, 395], [166, 355], [189, 661], [133, 685], [168, 685], [190, 736], [145, 564], [125, 470], [129, 541], [133, 439], [162, 486], [125, 387], [183, 596], [135, 733], [106, 329], [100, 279], [102, 439], [162, 454]], 4)
        >>> print(results_large['models']['linear']['constants'])
        [0.4934, 414.5401]
        >>> print(results_large['models']['quadratic']['constants'])
        [-0.007, 2.5668, 265.4919]
        >>> print(results_large['models']['cubic']['constants'])
        [0.0005, -0.2204, 33.8099, -1226.1397]
        >>> print(results_large['models']['hyperbolic']['constants'])
        [-10786.2465, 563.019]
        >>> print(results_large['models']['exponential']['constants'])
        [407.8094, 1.0009]
        >>> print(results_large['models']['logarithmic']['constants'])
        [74.0076, 118.997]
        >>> print(results_large['models']['logistic']['constants'])
        [488.2, 1.0, 1.0]
        >>> print(results_large['models']['sinusoidal']['constants'])
        [32.3199, 1.0085, 1.8848, 488.9635]
        >>> print(results_large['statistics']['mean'])
        149.29
        >>> print(results_large['optimal']['option'])
        'sinusoidal'
    """
    matrix_of_scalars(data, 'first')
    positive_integer(precision)
    independent_variable = single_dimension(data, 1)
    models = {
        'linear': linear_model(data, precision),
        'quadratic': quadratic_model(data, precision),
        'cubic': cubic_model(data, precision),
        'hyperbolic': hyperbolic_model(data, precision),
        'exponential': exponential_model(data, precision),
        'logarithmic': logarithmic_model(data, precision),
        'logistic': logistic_model(data, precision),
        'sinusoidal': sinusoidal_model(data, precision)
    }
    statistics = {
        'minimum': minimum_value(independent_variable),
        'maximum': maximum_value(independent_variable),
        'q1': quartile_value(independent_variable, 1),
        'q3': quartile_value(independent_variable, 3),
        'mean': mean_value(independent_variable),
        'median': median_value(independent_variable)
    }
    correlations = {
        'linear': models['linear']['correlation'],
        'quadratic': models['quadratic']['correlation'],
        'cubic': models['cubic']['correlation'],
        'hyperbolic': models['hyperbolic']['correlation'],
        'exponential': models['exponential']['correlation'],
        'logarithmic': models['logarithmic']['correlation'],
        'logistic': models['logistic']['correlation'],
        'sinusoidal': models['sinusoidal']['correlation']
    }
    best = max(correlations, key=correlations.get)
    optimal = {
        'option': best,
        'correlation': correlations[best]
    }
    result = {
        'models': models,
        'statistics': statistics,
        'optimal': optimal
    }
    return result