Usage
-----
Notes on general usage of the library.

Import
******

.. code-block:: python

    from regressions.models.linear import linear_model
    from regressions.vectors.multiplication import dot_product

Create Variables
****************

.. code-block:: python

    data_set = [[1, 2], [3, 4]]
    vector_one = [1, 2, 3]
    vector_two = [4, 5, 6]

Use Functions
*************

.. code-block:: python

    vector_product = dot_product(vector_one, vector_two)

View Results
************

.. code-block:: python

    print(vector_product) # 32

Specific Examples
*****************
Some specific examples of using the library.

Weather
^^^^^^^
Average monthly highs in Atlanta

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

Create a list of coordinate pairs from the data in the table:

.. code-block:: python

    monthly_highs = [[1, 53], [2, 58], [3, 66], [4, 73], [5, 80], [6, 87], [7, 89], [8, 88], [9, 83], [10, 74], [11, 64], [12, 55]]

Generate a sinusoidal model to fit the data:

.. code-block:: python

    from regressions.models.sinusoidal import sinusoidal_model
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

    * **Average high temperature:** :math:`74.6609^{\circ}F`
    * **Maximum high temperature:** :math:`91.3829^{\circ}F`
    * **Minimum high temperature:** :math:`57.9389^{\circ}F`
    * **Predicted high temperature in July 2021:** :math:`83.6925^{\circ}F`

Draw conclusions from the results:

    The monthly high temperatures in Atlanta follow a strong sinusoidal pattern, since the correlation coefficient of its sinusoidal model is so close to 1. However, this model implies that the length of a period for Atlanta's weather is closer to 10 months than it is to 12 months (which it should be, since the period should be 1 year).

Disease
^^^^^^^
Total deaths in the US from COVID-19 by month in 2020

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

Create a list of coordinate pairs from the data in the table:

.. code-block:: python

    monthly_deaths = [[1, 4], [2, 20], [3, 7117], [4, 72390], [5, 110593], [6, 128525], [7, 159539], [8, 189293], [9, 208337], [10, 232942], [11, 285620], [12, 382580]]

Generate a logistic model to fit the data:

.. code-block:: python

    from regressions.models.logistic import logistic_model
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

    * **Total deaths:** 564,205 people
    * **Turning point:** October 2020
    * **Predicted total deaths by July 2021:** 532,264 people

Draw conclusions from the results:

    The total deaths from COVID-19 in the US follow a strong logistic pattern, since the correlation coefficient of its logistic model is so close to 1. However, this model implies that October 2020 was a turning point, which would mean that monthly deaths should have been decreasing in November and December (in fact, December experienced the most deaths out of any of the months in the table).

Profits
^^^^^^^
Total annual profits of a fictional company based on how many units of a product it produces per year

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

Create a list of coordinate pairs from the data in the table:

.. code-block:: python

    annual_profits = [[152, 17892.35], [167, 18672.32], [178, 21321.67], [193, 24178.92], [201, 25761.21], [214, 23111.43], [229, 21245.87], [236, 19678.25], [247, 18721.17], [258, 16239.55]]

Generate a quadratic model to fit the data:

.. code-block:: python

    from regressions.models.quadratic import quadratic_model
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

    * **Highest possible profits:** $23,676.14
    * **Units to produce to maximize profits:** 203 units
    * **Predicted profits if 275 units produced:** $10,075.03

Draw conclusions from the results:

    The relationship between units produced and profits earned follows a strong quadratic pattern, since the correlation coefficient of its quadratic model is so close to 1. However, this model implies that the company can never achieve profits higher than $23,676.14 (even though it earned $25,761.21 when it previously sold 201 units, as seen in the table).

.. |noaa| raw:: html

    <a href="https://www.ncdc.noaa.gov" target="_blank">NOAA</a>

.. |cdc| raw:: html

    <a href="https://www.cdc.gov/nchs/nvss/vsrr/covid19/index.htm" target="_blank">CDC</a>