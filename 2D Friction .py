# Student ID  : 2555241
# Project Name: Two Dimensional Friction
# Project ID  : S-Friction2D
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
    x_values.append(x) # storing data
    h_values.append(h)

    return


v0 = float(input("V: "))
angle = float(input("Angle: "))
angle = math.radians(angle)  # converting angle to radians


t_values = [0]
x_values = [0] # storing data with initial condition
h_values = [0]


t = 0
x = 0
h = 0
vx = v0 * math.cos(angle)  # x component of velocity
vy = v0 * math.sin(angle)  # y component of velocity




while h >= 0:
    t += dt

    v = math.sqrt(vx**2 + vy**2)  # magnitude of velocity
    F_drag = 0.5 * rho * A * Cd * v**2  # Drag friction data

    ax = - (F_drag/m) * (vx/v)  # x component of acceleration
    ay = -g - (F_drag/m) * (vy/v)  # y component of acceleration

    vx += ax * dt  
    vy += ay * dt  # Updating x and y component of velocity
    x += vx * dt  
    h += vy * dt  # Updating x and y coordinate

    projectile()




# Plotting

plt.figure(figsize=(7, 3))
plt.plot(x_values, h_values, label='Trajectory')
plt.xlabel('x (m)')
plt.ylabel('Height (m)')
plt.title('Two Dimensional Friction')
plt.legend()
plt.grid()
plt.show()




f = open('S-fric2D.dat', 'w')  # opening a file
f.write('x(m)\ty(m)\n') # overwrite data into file


for i in range(len(x_values)):
    f.write(f'{x_values[i]}\t{h_values[i]}\n') # for x values, overwriting height with "tab" space between data
f.close()


