from .run_all import run_all

set_20 = [[1, 78], [2, 64], [3, 97], [4, 34], [5, 53], [6, 65], [7, 79], [8, 201], [9, 123], [10, 145], [11, 356], [12, 77], [13, 478], [14, 598], [15, 376], [16, 294], [17, 401], [18, 532], [19, 607], [20, 752]]

all_solutions = run_all(set_20)

print(f"Linear Constants: {all_solutions['options']['linear']['constants']}") # => [[32.98796992481202], [-75.87368421052619]]
print(f"Linear Error: {all_solutions['options']['linear']['error']}") # => 22.312581356511483

print(f"Quadratic Constants: {all_solutions['options']['quadratic']['constants']}") # => [[1.697653223969002], [-2.6627477785371454], [54.84561403508843]]
print(f"Quadratic Error: {all_solutions['options']['quadratic']['error']}") # => 21.07459477444664

print(f"Cubic Constants: {all_solutions['options']['cubic']['constants']}") # => [[-0.040814661624975546], [2.9833150651558444], [-13.727602545073111], [76.53044375644211]]
print(f"Cubic Error: {all_solutions['options']['cubic']['error']}") # => 21.05493315315674

print(f"Hyperbolic Constants: {all_solutions['options']['hyperbolic']['constants']}") # => [[-476.2476028415365], [356.17074436813056]]
print(f"Hyperbolic Error: {all_solutions['options']['hyperbolic']['error']}") # => 29.489660900232142

print(f"Exponential Constants: {all_solutions['options']['exponential']['constants']}") # => [[39.79809056464346], [1.154903969011854]]
print(f"Exponential Error: {all_solutions['options']['exponential']['error']}") # => 21.55169894398324

print(f"Logarithmic Constants: {all_solutions['options']['logarithmic']['constants']}") # => [[-154.60728466072027], [200.8272561968283]]
print(f"Logarithmic Error: {all_solutions['options']['logarithmic']['error']}") # => 26.11858512913022

print(f"Best Choice Function: {all_solutions['optimal']['function']}") # => cubic
print(f"Best Choice Error: {all_solutions['optimal']['error']}") # => 21.05493315315674