Models
======
These are the top-level, model-generating functions. As a result, they're the most popular functions in the library—with the most detailed documentation. All of them provide data-rich dictionaries as their results, and all of them call multiple helper functions found elsewhere in the library. For example, all of the functions in this section use the `correlation_coefficient` function from the `statistics` section, the `single_dimension` function from the `vectors` section, and the `key_coordinates` function from the `analyses` section, among other helper functions. To better understand how these top-level functions work, it is recommended that you also view the documentation in the other sections.

.. toctree::
    :maxdepth: 2

    pages/linear
    pages/quadratic
    pages/cubic
    pages/hyperbolic
    pages/exponential
    pages/logarithmic
    pages/logistic
    pages/sinusoidal