# Student ID  : 2555241
# Project Name: Newton Root
# Project ID  : S-NewtonRoot
# Description : This code ...


import matplotlib.pyplot as plt
import random
import math


#a, b, c, d = .93, -.59, -.9, .16

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: ")) # getting coefficients from user input



max_coeff = max(abs(a), abs(b), abs(c), abs(d))  # calculating the maximum absolute coefficient for graph limit, so it can show properly


range_size = int(max_coeff) + 4  # calculating the range and step size based on the maximum coefficient,  4 to include the maximum coefficient in the range for graph



def func(x):
    return a*(x**3) + b*(x**2) + c*x + d # polynomial funtion


def der_func(x):
    return 3*a*(x**2) + 2*b*x + c # derivative of funtion


x = [i/100 for i in range(-1000, 1000)] # x values

y = [func(i) for i in x] # f(x) values




# Plotting
plt.plot(x, y, label=r'f(x) = {:.2f}$x^3$ {:+.2f}$x^2$ {:+.2f}x {:+.2f}'.format(a, b, c, d))
plt.title(r'Plot of the $3^{rd}$ degree polynomial')
plt.axvline(x=0, color='k', linewidth=1)  # Vertical line at x=0
plt.axhline(y=0, color='k', linewidth=1)  # Horizontal line at y=0
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.ylim([-range_size, range_size])  
plt.xlim([-range_size, range_size])  # setting x and y-axis limits due to graph scale
plt.xticks([i for i in range(-range_size, range_size, 1)])
plt.yticks([i for i in range(-range_size, range_size, 1)]) # graph axis scale

plt.show()






# Newton's method

roots = []


for _ in range(100):  # number of initial guesses
    x_n = random.uniform(-range_size, range_size)


    for i in range(10000):  # maximum repetitions
        x_n1 = x_n - func(x_n) / der_func(x_n)


        if abs(x_n - x_n1) < 1e-6:  # convergence criteria
            break

        x_n = x_n1



    if all(abs(x_n - root) > 1e-6 for root in roots):      # checking whether root is already in the list
        roots.append(x_n)

print(f'Approximately roots {roots}')
