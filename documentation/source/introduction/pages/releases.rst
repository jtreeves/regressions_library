Release Notes
-------------
To understand what updates have happened for what versions, peruse the below lists.

**TERMS**

* **Added**: Feature that did not exist in a previous version
* **Removed**: Feature that existed in a previous version but not in the current version
* **Deprecated**: Feature that existed in a previous version and still exists in the current version but whose usage is discouraged
* **Improved**: Feature that existed in a previous version and with no bugs, but which has been notably improved in the current version
* **Fixed**: Feature that existed in a previous version but with bugs, and which has been fixed to ensure no bugs in the current version

Versions above 2.0
******************
The most recent versions of the library involve both logistic and sinusoidal models, and many of the function names and file structures have changed.

Version 2.1.1
^^^^^^^^^^^^^
*10/03/21*

**FIXED**

* Change syntax in error handling functions to avoid throwing errors with large data sets; library now comfortably handles data sets containing as many as 1,000 coordinate pairs

Version 2.1.0
^^^^^^^^^^^^^
*05/16/21*

**IMPROVED**

* :func:`~regressions.models.logistic.logistic_model` now produces models with higher correlation coefficients on average, allowing it to better provide models for less logistically inclined data sets

**FIXED**

* :func:`~regressions.vectors.generate.generate_elements` now converts negative periodic units to their positive counterparts, allowing general forms of sinusoidal points to always include only a plus sign before the periodic unit as opposed to both plus and minus signs in some cases

Version 2.0.8
^^^^^^^^^^^^^
*04/24/21*

**FIXED**

* Add error handling to block program from attempting to evaluate the logarithm of zero

Version 2.0.7
^^^^^^^^^^^^^
*04/22/21*

**FIXED**

* Change folder name to ensure installed library will appear as `regressions` on user's computer

Version 2.0.6
^^^^^^^^^^^^^
*04/22/21*

**ADDED**

* Sinusoidal models
* Logistic models
* Graphical analysis
* Correlation coefficient

**REMOVED**

* Error calculation (since correlation coefficient can replace it)

Versions above 1.0
******************
The initial versions of the library involved models for the core six functions: linear, quadratic, cubic, hyperbolic, exponential, and logarithmic. All of them were generated using linear algebra techniques.

Version 1.0.1
^^^^^^^^^^^^^
*01/24/21*

**ADDED**

* Linear models
* Quadratic models
* Cubic models
* Hyperbolic models
* Exponential models
* Logarithmic models
* Matrix manipulations to solve systems of equations
* Error calculation to determine how well a model fits a data set