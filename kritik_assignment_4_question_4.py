import matplotlib.pyplot as plt
import numpy as np

def sussy_descent(f, learning_rate, initial_point):
    
    def deriv(f, base_point):
        return (f(base_point+10**(-5))-f(base_point))/(10**(-5))
    
    x_coords = [initial_point]
    
    y_coords = [f(initial_point)]
    
    x = x_coords[0]
    
    while abs(deriv(f, x)) > 0.00000001:
        x = x - (learning_rate*(deriv(f, x)))
        x_coords.append(x)
        y_coords.append(f(x))
        
    plot_range = np.linspace(min(x_coords) - 0.5,
                             max(x_coords)+0.5, 10000)
    function_range = [f(i) for i in plot_range]
    plt.plot(plot_range, function_range)
    plt.plot(x_coords, y_coords)
    
    return round(x_coords[-1], 3), round(y_coords[-1],3)

print(sussy_descent(lambda x: x**2, 0.1, 2))

print(sussy_descent(lambda x: ((-3*(x**3)) + (10*(x**2)) - (5*x) - 3), 0.1, 0.8))

def funny_function(x):
    if x>0:
        return x**x
    elif x==0:
        return 1
    else:
        return abs(x)**abs(x)
    
print(sussy_descent(lambda x: (funny_function(x)), 0.1, 1))


## make sure to document code before submission
                             