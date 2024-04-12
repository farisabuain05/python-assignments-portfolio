import numpy as np

def funny(x):
    if x<=-1:
        return 0
    elif x>=1:
        return 0
    else:
        return np.exp(1-(1/(1-x**(10**250))))
    
print(funny(0))

print(funny(0.5))

print(funny(-1))

print(funny(1))

print(funny(-0.99999))

print(funny(-1.00001))

print(funny(0.99999))

print(funny(1.00001))