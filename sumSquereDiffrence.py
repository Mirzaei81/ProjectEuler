import numpy as np
SquereOfSums = 0
n = np.sum(np.arange(100))
SumsOfSqueres = np.sum(np.square(n))
for i in range(100):
    SquereOfSums+=i**2
print(SquereOfSums)
print(SumsOfSqueres)
print(SquereOfSums-SumsOfSqueres)
    
