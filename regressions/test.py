from .run_all import run_all
from .sinusoidal import sinusoidal

agnostic_set = [[1, 3], [2, 147], [3, 286], [4, 352], [5, 423], [6, 510], [7, 591], [8, 451], [9, 689], [10, 862]]
cyclic_set = [[1, 33], [2, 27], [3, 45], [4, 56], [5, 69], [6, 84], [7, 88], [8, 75], [9, 57], [10, 42], [11, 39], [12, 28]]

# all_solutions = run_all(agnostic_set)
cyclic_solution = sinusoidal(cyclic_set)

print(f"Sinusoidal Constants: {cyclic_solution['constants']}") # => [[28.2382], [0.5236], [-1.8948], [53.5833]] // VERSUS WHAT I GOT: [[1126.9119], [1.1709], [-2.1711], [1290.0787]] // NEW VALUES: [[-22022.99146071105], [0.6013015109266755], [0.6276552476317352], [13293.135715281009]] // NEWER VALUES: [[15430.83920235599], [0.6013015109266755], [0.6276552476317352], [-8701.570750628009]] // VALUES AFTER AVERAGING A & B: [[-152.7393206522671], [0.6903501429559035], [0.34884660006533247], [412.3751222003216]]
print(f"Sinusoidal Error: {cyclic_solution['error']}") # => NOT SURE WHAT I SHOULD HAVE EXPECTED, BUT I GOT: 69.6112 // NEW ERROR: 258.3859834434484 // NEWER ERROR: 214.2937082641205 // ERROR AFTER AVERAGING A & B: 34.296893836130046

# print(f"Linear Constants: {all_solutions['options']['linear']['constants']}") # => [[79.7212], [−7.0667]]
# print(f"Linear Error: {all_solutions['options']['linear']['error']}") # => 15.0577

# print(f"Quadratic Constants: {all_solutions['options']['quadratic']['constants']}") # => [[−1.6515], [97.8879], [−43.4000]]
# print(f"Quadratic Error: {all_solutions['options']['quadratic']['error']}") # => 14.9511

# print(f"Cubic Constants: {all_solutions['options']['cubic']['constants']}") # => [[2.7704], [−47.3631], [308.7150], [−281.1000]]
# print(f"Cubic Error: {all_solutions['options']['cubic']['error']}") # => 12.7299

# print(f"Hyperbolic Constants: {all_solutions['options']['hyperbolic']['constants']}") # => [[-766.8421], [656.0056]]
# print(f"Hyperbolic Error: {all_solutions['options']['hyperbolic']['error']}") # => 20.2718

# print(f"Exponential Constants: {all_solutions['options']['exponential']['constants']}") # => [[29.2304], [1.4898]]
# print(f"Exponential Error: {all_solutions['options']['exponential']['error']}") # => 30.7182

# print(f"Logarithmic Constants: {all_solutions['options']['logarithmic']['constants']}") # => [[−58.7194], [324.4875]]
# print(f"Logarithmic Error: {all_solutions['options']['logarithmic']['error']}") # => 16.0616

# print(f"Sinusoidal Constants: {all_solutions['options']['sinusoidal']['constants']}") # => [[29913.7759], [1.5941], [-2.1920], [34287.6855]]
# print(f"Sinusoidal Error: {all_solutions['options']['sinusoidal']['error']}") # => 360.0757

# print(f"Best Choice Function: {all_solutions['optimal']['function']}") # => cubic
# print(f"Best Choice Error: {all_solutions['optimal']['error']}") # => 12.7299