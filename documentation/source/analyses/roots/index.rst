Roots of Functions
==================
These functions determine the roots (or x-intercepts) of the eight key functions: linear, quadratic, cubic, hyperbolic, exponential, logarithmic, logistic, and sinusoidal. They return arrays containing all the roots of the given function. Some, such as exponential and logistic, never have any roots, so they return an array of `None`. In contrast, sinusoidal functions may either have no roots or an infinite number of roots; in the latter case, initial roots within a four-period interval are provided along with general forms for determining the other roots.

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