import math
def roots(f,a,b):
    try:
        f(a)
    except ValueError:
        for n in range(1000):
            m = (a+b)/2
            if f(b)*f(m) < 0:
                a = m
            elif f(a+0.000001)*f(m) < 0:
                b = m
            elif f(m)==0:
                return m
        return (a+b)/2
    else:
        if f(a) == 0:
            return a
        elif f(b) == 0:
            return b
        for n in range(1000):
            m = (a+b)/2
            if f(a)*f(m) < 0:
                b = m
            elif f(b)*f(m) < 0:
                a = m
            elif f(m)==0:
                return m
        return (a+b)/2
    
#Test Function 1
print(roots(lambda x: math.exp(x) + math.log(x),0,1))
#Test Function 2
print(roots(lambda x: math.atan(x) - x**2,0,2))
#Test Function 3
print(roots(lambda x: math.sin(x) / math.log(x),3,4))
#Test Function 4
print(roots(lambda x: math.log(math.cos(x)),5,7))

