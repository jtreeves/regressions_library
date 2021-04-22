Vectors
=======
These functions are mostly helper functions for the more important, top-level, model-generating functions. For example, the `single_dimension` function is used in all the `models` functions to separate the data for the independent and dependent variables. Additionally, the `dot_product` function is used in the `matrix_product` function, which in turn is used in the `system_solution` function, which in turn shows up repeatedly in the `models` functions. Even though they aren't the crown jewels of this library, documentation for all of them are provided here in case you want to use them directly (of if you want to better understand how the top-level functions work).

.. toctree::
    :maxdepth: 2

    pages/generate
    pages/separate
    pages/unify
    pages/dimension
    pages/column
    pages/components
    pages/addition
    pages/multiplication
    pages/magnitude
    pages/direction
    pages/unit