import numpy as np
import matplotlib.pyplot as plt

# normal density function
def normal_density(mean, variance, x):
    f_sub_x = (1/np.sqrt(2*np.pi*variance))*(np.exp((-(x - mean)**2)/(2*variance)))
    return f_sub_x

# Test Case 1: Plotting density function with mean = 20, variance = 3.5^2
x_coords = []
y_coords = []
for n in range(1000):
    x = 0.1*n
    f_sub_x = normal_density(20, 3.5**2, x)
    x_coords.append(x) # appends x values in range of 0 to 100, in increments of 0.1
    y_coords.append(f_sub_x) # appends density function; i.e. f_sub_x of x

plt.plot(x_coords, y_coords)
plt.show()

# Test Case 2: Plotting density function with mean = 40, variance = 5.5^2
x_coords = []
y_coords = []
for n in range(1000):
    x = 0.1*n 
    f_sub_x = normal_density(40, 5.5**2, x)
    x_coords.append(x) # appends x values in range of 0 to 100, in increments of 0.1
    y_coords.append(f_sub_x) # appends density function; i.e. f_sub_x of x

plt.plot(x_coords, y_coords) # plot values
plt.show()

# Test Case 3: Plotting density function with mean = 60, variance = 4.5^2
x_coords = []
y_coords = []
for n in range(1000):
    x = 0.1*n
    f_sub_x = normal_density(60, 4.5**2, x)
    x_coords.append(x) # appends x values in range of 0 to 100, in increments of 0.1
    y_coords.append(f_sub_x) # appends density function; i.e. f_sub_x of x

plt.plot(x_coords, y_coords)
plt.show()


# Function for the integration of density function; finds probability that random value X
# falls between a given x=a and x=b, by finding area under density function plot
def integration(mean, variance, a, b):
    area = 0
    delt_x = (b-a)/10000
    x = a
    for n in range(10000):
        x = a + delt_x*n
        f_X = normal_density(mean, variance, x)
        area += f_X*delt_x # manual integration!
    return area

print(integration(171, 7.1**2, 162, 190)) # Finds probability that height falls between 162cm and 190cm
        
    
    