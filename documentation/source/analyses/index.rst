Analyses
========
Although these functions are mostly helper functions for the more important, top-level, model-generating functions, there are more functions in this section than all the other sections combined. Incidentally, all the functions within the `equations`, `derivatives`, `integrals`, and `roots` subsections of this section constitute almost a third of all the functions in this documentation. As a result, this is probably the most important section after the all-important `models` section. Furthermore, many of these functions have direct applications outside of regression analysis. For example, if you already know the coefficients of a cubic equation you want to analyze, then you can directly use functions like `extrema_points` to determine the maxima and minima of your function. Additionally, `evaluations` is an important dictionary returned by all `models` functions, and all of them come directly from the functions detailed in the above subsections—making understanding their functions that much more important.

.. toctree::
    :maxdepth: 2

    equations/index
    derivatives/index
    integrals/index
    roots/index
    pages/criticals
    pages/intervals
    pages/intercepts
    pages/maxima
    pages/minima
    pages/extrema
    pages/inflections
    pages/points
    pages/accumulation
    pages/mean_values