Statistics
==========
These functions are mostly helper functions for the more important, top-level, model-generating functions. For example, the `correlation_coefficient` function is used in all the `models` functions to determine how well the models fit their data. Additionally, the `rounded_value` function is used in multiple functions throughout the library to round values while circumventing possible future errors like division by zero. Even though they aren't the crown jewels of this library, documentation for all of them are provided here in case you want to use them directly (of if you want to better understand how the top-level functions work).

.. toctree::
    :maxdepth: 2

    pages/rounding
    pages/summation
    pages/sort
    pages/halve
    pages/maximum
    pages/minimum
    pages/ranges
    pages/mean
    pages/median
    pages/quartiles
    pages/summary
    pages/residuals
    pages/deviations
    pages/correlation