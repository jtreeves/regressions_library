from library.execute import run_all

agnostic_set = {
    [1, 32],
    [2, 25],
    [3, 14],
    [4, 23],
    [5, 39],
    [6, 45],
    [7, 42],
    [8, 49],
    [9, 36],
    [10, 33]
}

linear_set = [
    [1, 30],
    [2, 27],
    [3, 24],
    [4, 21],
    [5, 18],
    [6, 15],
    [7, 12],
    [8, 9],
    [9, 6],
    [10, 3]
]

quadratic_set = [
    [1, 10],
    [2, 27],
    [3, 40],
    [4, 49],
    [5, 54],
    [6, 55],
    [7, 52],
    [8, 45],
    [9, 34],
    [10, 19]
]

cubic_set = [
    [1, 42],
    [2, 67],
    [3, 74],
    [4, 69],
    [5, 58],
    [6, 47],
    [7, 42],
    [8, 49],
    [9, 74],
    [10, 123]
]

hyperbolic_set = [
    [1, 2519],
    [2, 1259],
    [3, 839],
    [4, 629],
    [5, 503],
    [6, 419],
    [7, 359],
    [8, 314],
    [9, 279],
    [10, 251]
]

exponential_set = [
    [1, 6],
    [2, 12],
    [3, 24],
    [4, 48],
    [5, 96],
    [6, 192],
    [7, 384],
    [8, 768],
    [9, 1536],
    [10, 3072]
]

logarithmic_set = [
    [1, 2],
    [2, 4.0794],
    [3, 5.2958],
    [4, 6.1589],
    [5, 6.8283],
    [6, 7.3753],
    [7, 7.8377],
    [8, 8.2383],
    [9, 8.5917],
    [10, 8.9078]
]

agnostic_models = run_all(agnostic_set)
linear_models = run_all(linear_set)
quadratic_models = run_all(quadratic_set)
cubic_models = run_all(cubic_set)
hyperbolic_models = run_all(hyperbolic_set)
exponential_models = run_all(exponential_set)
logarithmic_models = run_all(logarithmic_set)

print(f'AGNOSTIC MODELS: {agnostic_models}')
print(f'LINEAR MODELS: {linear_models}')
print(f'QUADRATIC MODELS: {quadratic_models}')
print(f'CUBIC MODELS: {cubic_models}')
print(f'HYPERBOLIC MODELS: {hyperbolic_models}')
print(f'EXPONENTIAL MODELS: {exponential_models}')
print(f'LOGARITHMIC MODELS: {logarithmic_models}')