About
-----
The regressions library is a collection of algorithms for fitting data to different functional models by using linear algebra and machine learning. It can generate the following eight key regression models based on any data set: linear, quadratic, cubic, hyperbolic, exponential, logarithmic, logistic, and sinusoidal. For each model, it outputs the constants of the equation, notable graphical points, and the correlation coefficient, among other useful details. To better understand how the library's many functions work, view its full |github| on GitHub.

Purpose
*******
The world is overflowing with data. Almost too much data. So much data that it's often hard to make sense of any of it. Regression modeling is one possible avenue for attempting to wrap your mind around a particular data set. By generating a model to fit a set of data and checking its correlation coefficient to see how strong the fit is, you can possibly come up with a simple way to make sense of your data. Maybe your data periodically oscillates back and forth between two extremes. In which case, a sinusoidal model would probably add some clarity and help you better predict what will happen next. Maybe your data keeps increasing rapidly. In which case, an exponential model would probably help. In all cases, regression models can give you an organizational pattern with some predictive potential—elements beneficial in both business and personal situations.

Features
********

* **Models**: *Regression models for all eight key function types*
    * Linear
    * Quadratic
    * Cubic
    * Hyperbolic
    * Exponential
    * Logarithmic
    * Logistic
    * Sinusoidal
* **Analyses**: *Functions to provide the models with key graphical information*
    * Roots
    * Extrema
    * Inflection points
* **Statistics**: *Functions to provide the models with information about their fit as well as descriptive statistical measures*
    * Correlation
    * Five-number summary
* **Matrices**: *Functions to handle the linear algebra to generate some of the models*
    * Determinant
    * Inverse
    * Solving systems of equations
* **Vectors**: *Functions to assist with other functions higher up the food chain*
    * Dot product
    * Uniting and separating intermediary vectors

Inspiration
***********
Many sites on the web offer free generations of various regression models. However, most do not include sinusoidal or logistic regression models, since they would require using machine learning to generate them. I wanted to build a package for Python that involved all the regression models I saw on a regular basis, plus the two key models of sinusoidal and logistic. I also wanted to include a function that would generate all the models for a specific data set at once (hence, the `run_all` function).

Value
*****
So why should you use this library? If you've ever been overwhelmed by too much data and just want to make sense of it, then this library is for you.

.. |github| raw:: html

    <a href="https://github.com/jtreeves/regressions_library" target="_blank">code base</a>