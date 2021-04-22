Usage
-----
Whenever you use a new library, it's important to know how to import its functions, what arguments to pass to its functions, and any unusual quirks of the library. Specific usage notes are provided with each individual function in this documentation, but here are some useful overviews to help acquaint you with the library. Plus a few fully worked out examples to show you just what you can achieve by using this library.

General Guidelines
******************

* **Arguments**: Most functions take lists or numbers as their arguments
* **Precision**: Most functions include an optional `precision` parameter to determine the maximum number of digits that will appear after the decimal place; if no value is provided, it will default to 4
* **Coordinate pairs**: List notation is used to indicate the coordinate pairs of points (e.g., [2, 3] for a point with an x-coordinate of 2 and a y-coordinate of 3); a list of lists is used to indicate a set of coordinate pairs (e.g., [[1, 2], [3, 4], [5, 6]] for a set containing three points); the latter nested list notation is necessary for providing arguments for top-level, model-generating functions (e.g., `linear_model`, `quadratic_model`)
* **Sufficient length for data sets**: A set of at least 10 coordinate pairs must be provided to any top-level, model-generating function; otherwise, an error will be raised

If you want to generate a linear model, the following options will fail:

.. code-block:: python

    linear_model([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Argument must be list of lists
    linear_model([1, 2], [3, 4]) # Argument's outer list must contain at least 10 lists

In constast, this will work:

.. code-block:: python

    linear_model([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])

Specific Instructions
*********************
The following are specific examples of how to use the library. They provide examples of what was discussed above.

Import
^^^^^^
In order to use any of the functions in the library, you must first import them.

Here are some imports of the most popular functions:

.. code-block:: python

    from regressions.execute import run_all
    from regressions.models.linear import linear_model
    from regressions.models.quadratic import quadratic_model
    from regressions.models.cubic import cubic_model
    from regressions.models.hyperbolic import hyperbolic_model
    from regressions.models.exponential import exponential_model
    from regressions.models.logarithmic import logarithmic_model
    from regressions.models.logistic import logistic_model
    from regressions.models.sinusoidal import sinusoidal_model

To find out how to import any other function, view its specific page in this documentation. The first example provided within its documentation will explain how to import the specific function.

Create Variables
^^^^^^^^^^^^^^^^
While not strictly necessary, it is often useful to store lists and numbers in variables.

Here are some examples of variables to contain data sets:

.. code-block:: python

    linear_set = [[1, 30], [2, 27], [3, 24], [4, 21], [5, 18], [6, 15], [7, 12], [8, 9], [9, 6], [10, 3]]
    quadratic_set = [[1, 10], [2, 27], [3, 40], [4, 49], [5, 54], [6, 55], [7, 52], [8, 45], [9, 34], [10, 19]]

Use Functions
^^^^^^^^^^^^^
As long as the function has been imported, you are free to use it on any data set.

Here are some examples of using some of the above functions on the above data sets:

.. code-block:: python

    linear_results = linear_model(linear_set)
    quadratic_results = quadratic_model(quadratic_set)

View Results
^^^^^^^^^^^^
Often, you will want to view the results of calling a function on a particular data set. Especiallly since many of the top-level functions (e.g., `linear_model`, `quadratic_model`) provide data-rich dictionaries as their results, it is usually useful to specify which aspect of the dictionary you want to view.

Here are some examples of accessing specific aspects of the above results:

.. code-block:: python

    print(linear_results['constants']) # [-3.0, 33.0]
    print(linear_results['points']['roots']) # [[11.0, 0]]
    print(linear_results['accumulations']['range']) # 148.5
    print(quadratic_results['constants']) # [-2.0, 23.0, -11.0]
    print(quadratic_results['points']['maxima']) # [[5.75, 55.125]]
    print(quadratic_results['averages']['iqr']['mean_values_derivative']) # [5.5]

Complete Tutorial
*****************
The following tutorial walks through all the steps for generating all the regression models for a specific data set.

Import the `run_all` function:

.. code-block:: python

    from regressions.execute import run_all

Create an agnostic data set:

.. code-block:: python

    agnostic_set = [[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]]

Generate all regression models for the agnostic data set:

.. code-block:: python

    all_models = run_all(agnostic_set)

View the constants and the correlation coefficient for the set's linear model:

.. code-block:: python

    linear = all_models['models']['linear']
    linear_constants = linear['constants']
    linear_correlation = linear['correlation']
    print(linear_constants) # [1.9636, 23.0]
    print(linear_correlation) # 0.5516

View the constants and the correlation coefficient for the set's quadratic model:

.. code-block:: python

    quadratic = all_models['models']['quadratic']
    quadratic_constants = quadratic['constants']
    quadratic_correlation = quadratic['correlation']
    print(quadratic_constants) # [-0.3106, 5.3803, 16.1667]
    print(quadratic_correlation) # 0.5941

View the constants and the correlation coefficient for the set's cubic model:

.. code-block:: python

    cubic = all_models['models']['cubic']
    cubic_constants = cubic['constants']
    cubic_correlation = cubic['correlation']
    print(cubic_constants) # [-0.3881, 6.0932, -24.155, 49.4667]
    print(cubic_correlation) # 0.8933

View the constants and the correlation coefficient for the set's hyperbolic model:

.. code-block:: python

    hyperbolic = all_models['models']['hyperbolic']
    hyperbolic_constants = hyperbolic['constants']
    hyperbolic_correlation = hyperbolic['correlation']
    print(hyperbolic_constants) # [-13.5246, 37.7613]
    print(hyperbolic_correlation) # 0.3479

View the constants and the correlation coefficient for the set's exponential model:

.. code-block:: python

    exponential = all_models['models']['exponential']
    exponential_constants = exponential['constants']
    exponential_correlation = exponential['correlation']
    print(exponential_constants) # [22.1049, 1.0692]
    print(exponential_correlation) # 0.5069

View the constants and the correlation coefficient for the set's logarithmic model:

.. code-block:: python

    logarithmic = all_models['models']['logarithmic']
    logarithmic_constants = logarithmic['constants']
    logarithmic_correlation = logarithmic['correlation']
    print(logarithmic_constants) # [7.4791, 22.5032]
    print(logarithmic_correlation) # 0.5086

View the constants and the correlation coefficient for the set's logistic model:

.. code-block:: python

    logistic = all_models['models']['logistic']
    logistic_constants = logistic['constants']
    logistic_correlation = logistic['correlation']
    print(logistic_constants) # [43.983, 0.3076, 0.9746]
    print(logistic_correlation) # 0.5875

View the constants and the correlation coefficient for the set's sinusoidal model:

.. code-block:: python

    sinusoidal = all_models['models']['sinusoidal']
    sinusoidal_constants = sinusoidal['constants']
    sinusoidal_correlation = sinusoidal['correlation']
    print(sinusoidal_constants) # [14.0875, 0.7119, -3.7531, 34.2915]
    print(sinusoidal_correlation) # 0.9264

View the name of the model with the best fit (by virtue of having the highest correlation coefficient):

.. code-block:: python

    optimal = all_models['optimal']['option']
    print(optimal) # 'sinusoidal'

Determine the equations for all of the models based on the above results:

    * **Linear equation**: :math:`lin(x) = 1.9636\cdot{x} + 23.0`
    * **Quadratic equation**: :math:`quad(x) = -0.3106\cdot{x^2} + 5.3803\cdot{x} + 16.1667`
    * **Cubic equation**: :math:`cub(x) = -0.3881\cdot{x^3} + 6.0932\cdot{x^2} - 24.155\cdot{x} + 49.4667`
    * **Hyperbolic equation**: :math:`hyp(x) = -13.5246\cdot{\frac{1}{x}} + 37.7613`
    * **Exponential equation**: :math:`exp(x) = 22.1049\cdot{1.0692^x}`
    * **Logarithmic equation**: :math:`log(x) = 7.4791\cdot{\ln{x}} + 22.5032`
    * **Logistic equation**: :math:`lst(x) = \frac{43.983}{1 + \text{e}^{-0.3076\cdot(x - 0.9746)}}`
    * **Sinusoidal equation**: :math:`sin(x) = 14.0875\cdot{\sin(0.7119\cdot(x + 3.7531))} + 34.2915`

Predict what the output will be when the input is 20 for each of the models based on the above equations:

    * **Linear prediction**: :math:`lin(20) = 62.272`
    * **Quadratic prediction**: :math:`quad(20) = -0.4673`
    * **Cubic prediction**: :math:`cub(20) = -1101.1533`
    * **Hyperbolic prediction**: :math:`hyp(20) = 37.0851`
    * **Exponential prediction**: :math:`exp(20) = 84.2689`
    * **Logarithmic prediction**: :math:`log(20) = 44.9086`
    * **Logistic prediction**: :math:`lst(20) = 43.857`
    * **Sinusoidal prediction**: :math:`sin(20) = 21.1519`

Interpret the above results:

    The sinusoidal model provides the best fit for the data set because it has the highest correlation coefficient of the group (0.9264). In contrast, the hyperbolic model provides the worst fit for the data set because it has the lowest correlation coefficient of the group (0.3479). The linear, exponential, and logarithmic models all predict the data set will continue increasing (albeit at different notably different rates, with exponential predicting the fastest rate and logarithmic predicting the slowest rate); whereas both the quadratic and cubic models predict the data set will decrease rapidly. The hyperbolic model and the logistic model both predict the data set will approach their horizontal asymptotes (37.7613 and 43.983, respectively); whereas the sinusoidal model predicts the data will continue oscillating between a low of 20.204 and a high of 48.379. While the sinusoidal model happens to be the best fit for the provided data set, it would be interesting to see if it remained the best if the data set were augmented with more values. In other words, maybe the hyperbolic or logistic models are correct and the data eventually do approach a single value. Or maybe the quadratic or cubic models are correct and the data do begin to decrease rapidly after this brief interlude. Or maybe the linear, exponential, or logarithmic models are correct and the data continue to increase. Without more data, it is impossible to know for sure.

More Examples
*************
The following are some real-world examples of how regression modeling can be used to better make sense of all the data at our disposal.

Weather
^^^^^^^
Use a sinusoidal model to analyze average monthly temperature highs in Atlanta. Temperatures rise and fall on a fairly predictable basis every year, so a sinusoidal model makes the most sense.

========= ===========
Month     Temperature
========= ===========
January   53
February  58
March     66
April     73
May       80
June      87
July      89
August    88
September 83
October   74
November  64
December  55
========= ===========

*Source*: |noaa|

Import the sinusoidal model:

.. code-block:: python

    from regressions.models.sinusoidal import sinusoidal_model

Create a list of coordinate pairs from the data in the table:

.. code-block:: python

    monthly_highs = [[1, 53], [2, 58], [3, 66], [4, 73], [5, 80], [6, 87], [7, 89], [8, 88], [9, 83], [10, 74], [11, 64], [12, 55]]

Generate a sinusoidal model to fit the data:

.. code-block:: python

    sinusoidal_best_fit = sinusoidal_model(monthly_highs)

View the constants of the resultant sinusoidal equation and the correlation coefficient of the model:

.. code-block:: python

    sinusoidal_constants = sinusoidal_best_fit['constants']
    sinusoidal_correlation = sinusoidal_best_fit['correlation']
    print(sinusoidal_constants) # [16.722, -0.6093, -11.0, 74.6609]
    print(sinusoidal_correlation) # 0.9689

Determine the sinusoidal equation that best fits the data by using the above results:

.. math::
    
    w(m) = 16.722\cdot{\sin(-0.6093\cdot(m + 11.0))} + 74.6609

Determine the correlation coefficient for the sinusoidal model by using the above results:

.. math::

    0.9689

Make inferences from the equation:

    * **Average high temperature**: :math:`74.6609^{\circ}F`
    * **Maximum high temperature**: :math:`91.3829^{\circ}F`
    * **Minimum high temperature**: :math:`57.9389^{\circ}F`
    * **Predicted high temperature in July 2021**: :math:`83.6925^{\circ}F`

Draw conclusions from the results:

    The monthly high temperatures in Atlanta follow a strong sinusoidal pattern, since the correlation coefficient of its sinusoidal model is so close to 1. However, this model implies that the length of a period for Atlanta's weather is closer to 10 months than it is to 12 months (which it should be, since the period should be 1 year).

Disease
^^^^^^^
Use a logistic model to analyze total deaths in the US from COVID-19, based on total deaths by the end of each month in 2020. As with all diseases, total deaths will increase slowly, then quickly, then slowly again, until finally leveling off. (This is an oversimplication of the process, and it doesn't take into account fluctuations based on other variables, but it's a useful simplication for the purposes of this example.) As a result, total deaths should fit to a sigmoid graph (a.k.a., an S-shaped curve), so a logistic model makes the most sense.

========= ============
Month     Total Deaths
========= ============
January   4
February  20
March     7117
April     72390
May       110593
June      128525
July      159539
August    189293
September 208337
October   232942
November  285620
December  382580
========= ============

*Source*: |cdc|

Import the logistic model:

.. code-block:: python

    from regressions.models.logistic import logistic_model

Create a list of coordinate pairs from the data in the table:

.. code-block:: python

    monthly_deaths = [[1, 4], [2, 20], [3, 7117], [4, 72390], [5, 110593], [6, 128525], [7, 159539], [8, 189293], [9, 208337], [10, 232942], [11, 285620], [12, 382580]]

Generate a logistic model to fit the data:

.. code-block:: python

    logistic_best_fit = logistic_model(monthly_deaths)

View the constants of the resultant logistic equation and the correlation coefficient of the model:

.. code-block:: python

    logistic_constants = logistic_best_fit['constants']
    logistic_correlation = logistic_best_fit['correlation']
    print(logistic_constants) # [564205.3166, 0.3277, 10.4152]
    print(logistic_correlation) # 0.9756

Determine the logistic equation that best fits the data by using the above results:

.. math::
    
    d(m) = \frac{564205.3166}{1 + \text{e}^{-0.3277\cdot(m - 10.4152)}}

Determine the correlation coefficient for the logistic model by using the above results:

.. math::

    0.9756

Make inferences from the equation:

    * **Total deaths**: 564,205 people
    * **Turning point**: October 2020
    * **Predicted total deaths by July 2021**: 532,264 people

Draw conclusions from the results:

    The total deaths from COVID-19 in the US follow a strong logistic pattern, since the correlation coefficient of its logistic model is so close to 1. However, this model implies that October 2020 was a turning point, which would mean that monthly deaths should have been decreasing in November and December (in fact, December experienced the most deaths out of any of the months in the table).

Profits
^^^^^^^
Use a quadratic model to analyze the total annual profits of a fictional company, based on how many units of a product it produces per year. While this is a fictional case study, it deals with something fairly common in business analysis: profit maximization based on some criteria. In this case, it appears that profit will be maximized when a certain number of units are produced. Since profits appear to initially increase as units increase only to later decrease, a quadratic model makes sense.

===== ========
Units Profit
===== ========
152   17892.35
167   18672.32
178   21321.67
193   24178.92
201   25761.21   
214   23111.43
229   21245.87
236   19678.25
247   18721.17
258   16239.55
===== ========

Import the quadratic model:

.. code-block:: python

    from regressions.models.quadratic import quadratic_model

Create a list of coordinate pairs from the data in the table:

.. code-block:: python

    annual_profits = [[152, 17892.35], [167, 18672.32], [178, 21321.67], [193, 24178.92], [201, 25761.21], [214, 23111.43], [229, 21245.87], [236, 19678.25], [247, 18721.17], [258, 16239.55]]

Generate a quadratic model to fit the data:

.. code-block:: python

    quadratic_best_fit = quadratic_model(annual_profits)

View the constants of the resultant quadratic equation, the correlation coefficient of the model, and the model's maximum point:

.. code-block:: python

    quadratic_constants = quadratic_best_fit['constants']
    quadratic_correlation = quadratic_best_fit['correlation']
    quadratic_maximum = quadratic_best_fit['points']['maxima']
    print(quadratic_constants) # [-2.6043, 1055.9536, -83362.0271]
    print(quadratic_correlation) # 0.9285
    print(quadratic_maximum) # [[202.7327, 23676.1411]]

Determine the quadratic equation that best fits the data by using the above results:

.. math::
    
    p(u) = -2.6043\cdot{u^2} + 1055.9536\cdot{u} - 83362.0271

Determine the correlation coefficient for the quadratic model by using the above results:

.. math::

    0.9285

Determine the coordinates of the absolute maximum for the quadratic model by using the above results:

.. math::

    (202.7327, 23676.1411)

Make inferences from the above information:

    * **Highest possible profits**: $23,676.14
    * **Units to produce to maximize profits**: 203 units
    * **Predicted profits if 275 units produced**: $10,075.03

Draw conclusions from the results:

    The relationship between units produced and profits earned follows a strong quadratic pattern, since the correlation coefficient of its quadratic model is so close to 1. However, this model implies that the company can never achieve profits higher than $23,676.14 (even though it earned $25,761.21 when it previously sold 201 units, as seen in the table).

.. |noaa| raw:: html

    <a href="https://www.ncdc.noaa.gov" target="_blank">NOAA</a>

.. |cdc| raw:: html

    <a href="https://www.cdc.gov/nchs/nvss/vsrr/covid19/index.htm" target="_blank">CDC</a>