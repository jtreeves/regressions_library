# Regressions

The regressions library is a collection of algorithms for fitting data to different functional models by using linear algebra and machine learning. It can generate the following eight key regression models based on any data set: linear, quadratic, cubic, hyperbolic, exponential, logarithmic, logistic, and sinusoidal. For each model, it outputs the constants of the equation, notable graphical points, and the correlation coefficient, among other useful details. For more information, view the library's full [code base](https://github.com/jtreeves/regressions_library) to understand how it works or its [documentation](https://regressions.readthedocs.io/en/latest/) to master the nuances of its usage.

## Requirements

- Python 3.8 or higher
- NumPy
- SciPy

## Installation

```
pip3 install regressions
```

## Usage

```python
from regressions.execute import run_all # Import function to generate all models

data_set = [[1, 32], [2, 25], [3, 14], [4, 23], [5, 39], [6, 45], [7, 42], [8, 49], [9, 36], [10, 33]] # Create data set to test
results = run_all(data_set) # Generate all models for data set

linear = results['models']['linear'] # Grab specifics for linear model
linear_constants = linear['constants'] # Grab constants of equation for linear model
print(linear_constants) # [1.9636, 23.0]
linear_correlation = linear['correlation'] # Grab correlation coefficient for linear model
print(linear_correlation) # 0.5516

quadratic = results['models']['quadratic'] # Grab specifics for quadratic model
quadratic_constants = quadratic['constants'] # Grab constants of equation for quadratic model
print(quadratic_constants) # [-0.3106, 5.3803, 16.1667]
quadratic_correlation = quadratic['correlation'] # Grab correlation coefficient for quadratic model
print(quadratic_correlation) # 0.5941

cubic = results['models']['cubic'] # Grab specifics for cubic model
cubic_constants = cubic['constants'] # Grab constants of equation for cubic model
print(cubic_constants) # [-0.3881, 6.0932, -24.155, 49.4667]
cubic_correlation = cubic['correlation'] # Grab correlation coefficient for cubic model
print(cubic_correlation) # 0.8933

hyperbolic = results['models']['hyperbolic'] # Grab specifics for hyperbolic model
hyperbolic_constants = hyperbolic['constants'] # Grab constants of equation for hyperbolic model
print(hyperbolic_constants) # [-13.5246, 37.7613]
hyperbolic_correlation = hyperbolic['correlation'] # Grab correlation coefficient for hyperbolic model
print(hyperbolic_correlation) # 0.3479

exponential = results['models']['exponential'] # Grab specifics for exponential model
exponential_constants = exponential['constants'] # Grab constants of equation for exponential model
print(exponential_constants) # [22.1049, 1.0692]
exponential_correlation = exponential['correlation'] # Grab correlation coefficient for exponential model
print(exponential_correlation) # 0.5069

logarithmic = results['models']['logarithmic'] # Grab specifics for logarithmic model
logarithmic_constants = logarithmic['constants'] # Grab constants of equation for logarithmic model
print(logarithmic_constants) # [7.4791, 22.5032]
logarithmic_correlation = logarithmic['correlation'] # Grab correlation coefficient for logarithmic model
print(logarithmic_correlation) # 0.5086

logistic = results['models']['logistic'] # Grab specifics for logistic model
logistic_constants = logistic['constants'] # Grab constants of equation for logistic model
print(logistic_constants) # [43.983, 0.3076, 0.9746]
logistic_correlation = logistic['correlation'] # Grab correlation coefficient for logistic model
print(logistic_correlation) # 0.5875

sinusoidal = results['models']['sinusoidal'] # Grab specifics for sinusoidal model
sinusoidal_constants = sinusoidal['constants'] # Grab constants of equation for sinusoidal model
print(sinusoidal_constants) # [14.0875, 0.7119, -3.7531, 34.2915]
sinusoidal_correlation = sinusoidal['correlation'] # Grab correlation coefficient for sinusoidal model
print(sinusoidal_correlation) # 0.9264

optimal = results['optimal']['option'] # Grab name of model with highest correlation coefficient
print(optimal) # 'sinusoidal'
```

## Testing

There are currently 1276 tests for this library. To run all of them:

1. Clone this repository: `git clone https://github.com/jtreeves/regressions_library.git`
2. Enter the directory: `cd regressons_library`
3. Run tests: `python3 -m unittest`