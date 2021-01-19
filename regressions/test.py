from .run_all import run_all

agnostic_set = [[1, 3], [2, 147], [3, 286], [4, 352], [5, 423], [6, 510], [7, 591], [8, 451], [9, 689], [10, 862]]

all_solutions = run_all(agnostic_set)

print(f"Linear Constants: {all_solutions['options']['linear']['constants']}") # => [[79.7212], [−7.0667]]
print(f"Linear Error: {all_solutions['options']['linear']['error']}") # => 15.0577

print(f"Quadratic Constants: {all_solutions['options']['quadratic']['constants']}") # => [[−1.6515], [97.8879], [−43.4000]]
print(f"Quadratic Error: {all_solutions['options']['quadratic']['error']}") # => 14.9511

print(f"Cubic Constants: {all_solutions['options']['cubic']['constants']}") # => [[2.7704], [−47.3631], [308.7150], [−281.1000]]
print(f"Cubic Error: {all_solutions['options']['cubic']['error']}") # => 12.7299

print(f"Hyperbolic Constants: {all_solutions['options']['hyperbolic']['constants']}") # => [[-766.8421], [656.0056]]
print(f"Hyperbolic Error: {all_solutions['options']['hyperbolic']['error']}") # => 20.2718

print(f"Exponential Constants: {all_solutions['options']['exponential']['constants']}") # => [[29.2304], [1.4898]]
print(f"Exponential Error: {all_solutions['options']['exponential']['error']}") # => 30.7182

print(f"Logarithmic Constants: {all_solutions['options']['logarithmic']['constants']}") # => [[−58.7194], [324.4875]]
print(f"Logarithmic Error: {all_solutions['options']['logarithmic']['error']}") # => 16.0616

print(f"Sinusoidal Constants: {all_solutions['options']['sinusoidal']['constants']}") # => [[9964.000054521777], [-27758.62987563369], [30908.45155497914], [-18419.33392729645], [6606.09877951361], [-1494.0753819970487], [214.5128404050165], [-18.941550110484073], [0.9366815605039633], [-0.01982197961624288]] // BUT THESE ARE THE POWER EXPANSIONS
print(f"Sinusoidal Error: {all_solutions['options']['sinusoidal']['error']}") # => ???????????????

print(f"Best Choice Function: {all_solutions['optimal']['function']}") # => cubic
print(f"Best Choice Error: {all_solutions['optimal']['error']}") # => 12.7299