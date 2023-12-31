# Student ID  : 2555241
# Project Name: Taylor Expansion
# Project ID  : S-Taylor
# Description : This code ...


import math
import random
import matplotlib.pyplot as plt




def taylor(x, N): #Taylor expansion
    T = 0
    for i in range(N+1):
        T += (x**i) / math.factorial(i)
    return T

def p_error(t, a): #percentage error calculation
    return abs((t - a) / a) * 100






x_ = random.randint(3, 7) # x values for exponential function values
N = int(input("N: ")) # N input value for Taylor expansion terms


k = 10  #for float x values

x_values = [i/k for i in range((x_)*k)] 
y_actual = [math.exp(m) for m in x_values] # for exponential values
y_taylor = [taylor(x, N) for x in x_values] # for Taylor calculations







fig, axs = plt.subplots(1, 2, figsize=(12, 4))  # for 1 row, 2 columns plot graph, and figure size obviously


# First subplot
axs[0].plot(x_values, y_actual, "c-", label='$e^x$')
axs[0].plot(x_values, y_taylor, "r." , label="Taylor")
axs[0].set_xlabel("x")
axs[0].set_ylabel("f(x)")
axs[0].set_title(r'f(x) = $e^x$ and Taylor Series Approximation')
axs[0].legend(['$e^x$ (x = {})'.format(x_), 'Taylor (N = {})'.format(N)])
axs[0].grid()




N_values = [i for i in range(N+1)]  # N values from 0 to N
p_errors = [p_error(taylor(x_, n), math.exp(x_)) for n in N_values]  # calculating error for each N


# Second subplot
axs[1].plot(N_values, p_errors, "g-" , label='Percentage Error')
axs[1].set_xlabel("N")
axs[1].set_ylabel(r'$\%_{error}$')
axs[1].set_title('Percentage Error between $e^x$ and Taylor Series Approximation')
axs[1].legend(['Percentage Error (N = {})'.format(N)])
axs[1].grid()

plt.show()
