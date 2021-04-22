Matrices
========
These functions are mostly helper functions for the more important, top-level, model-generating functions. For example, the `system_solution` function is used in all the `models` functions except for `logistic` and `sinusoidal` (since those use machine learning instead of linear algebra). However, documentation for all of them are provided here in case you want to use them directly (of if you want to better understand how the top-level functions work).

.. toctree::
    :maxdepth: 2

    pages/transpose
    pages/addition
    pages/multiplication
    pages/determinant
    pages/cofactors
    pages/minors
    pages/inverse
    pages/solve