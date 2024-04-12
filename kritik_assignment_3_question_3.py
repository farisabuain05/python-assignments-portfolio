import numpy as np
def lin_approx(f,c,E):
    derive_f = ((f(c + (10**-8))) - (f(c - (10**-8)))) / (2*(10**-8))
    g = lambda x: f(c) + ((derive_f)*(x - c))
    for i in range(1000):
        x = (c+(i*0.01))
        if round(abs(g(x) - f(x)),2) == E:
            x2 = x
            break
    for i in range(1000):
        x = (c-(i*0.01))
        if round(abs(g(x) - f(x)),2) == E:
            x1 = x
            break
    try:
        return x1, x2;
    except UnboundLocalError:
        return "There is no such x1 and x2 within E of c"
   
f = lambda x: x**2

print(lin_approx(f,1,0.1))

f = lambda x: np.sin(x)
print(lin_approx(f,np.pi/4,0.05))

f = lambda x: np.exp(x)
print(lin_approx(f,0,0.01)) 
    