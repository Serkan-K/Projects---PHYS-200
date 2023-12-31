1# Student ID  : 2555241
# Project Name: One Dimensional Friction
# Project ID  : S-KIN-OneDimFriction
# Description : This code ...

import math
import matplotlib.pyplot as plt


# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
rho = 1.225  # air density (kg/m^3)
A = .1  # cross-sectional area of the object (m^2)
Cd = 0.47  # drag coefficient
m = 1  # mass of the object (kg)
dt = .01  # time step (s)


def projectile():

    t_values.append(t)
    h_values.append(h)
    v_values.append(v)  # storing data
    a_values.append(a)
    #f_values.append(F_drag)

    return



v_0 = float(input("V_0: "))  # getting initial speed from user input
h_0 = float(input("H_0: "))  # getting initial height from user input


t_values = [0]
h_values = [h_0]
v_values = [v_0]
a_values = [g] # storing data with initial condition


t = 0
h = h_0
v = v_0

h_max = h_0 + ((v_0**2) / (2*g)) # maximum height
t_up = v_0 / g
t_down = math.sqrt(2*(h_max) / g)
t_total = t_up + t_down # total projectile motion time




if v > 0:
  while t <= t_up:

    t += dt

    F_drag = 0.5 * rho * A * Cd * (v**2) # Drag friction data
    a = g + (F_drag/m)  # acceleration

    v -= a * dt  # update velocity
    h += v * dt  # update height

    projectile()



# I split it in two part to make sure
while h > 0:
  t += dt
  F_drag = 0.5 * rho * A * Cd * (v**2)
  a = g - (F_drag/m)  # acceleration

  v -= a * dt  # update velocity
  h += v * dt  # update height

  projectile()


#print()
#print("h_max: " + str(h_max))
#print("t_up: " + str(t_up))
#print("t_down: " + str(t_down))
#print("t_total: " + str(t_total))
#print("h_values: " + str(h_values))
#print()
#print("t_values: " + str(t_values))
#print("v_values: " + str(v_values))
#print("a_value: " + str(a_values))
#print("F_drag: " + str(F_drag))
#print("f_values: " + str(f_values))
#print(len(a_values))



# Plotting
plt.figure(figsize=(7, 4))
plt.plot(t_values, h_values, label='Height')
plt.plot(t_values, v_values, label='Velocity')
#plt.plot(t_values, a_values, label='a')
#plt.plot(t_values, f_values, label='f')
plt.xlabel('Time (s)')
plt.ylabel('Height and Velocity')
plt.title('One Dimensional Friction')
plt.legend()
plt.grid()
plt.show()


f = open('S-fric1D.dat', 'w') # opening a file
f.write('Time(s)\tHeight(m)\tVelocity(m/s)\n') # overwrite data into file

for i in range(len(t_values)): 
    f.write(f'{t_values[i]}\t{h_values[i]}\t{v_values[i]}\n') # for t values, overwriting height and speed values with "tab" space between data

f.close()


