#Visualization of Heat equation, second version
#Caleb Bessit
#12 August 2023

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.animation import FuncAnimation

# Constants
kappa           = 2                               #Diffusivity constant for the material
L               = 20                              #Length of the rod
x_0             = 0                               #Initial point of the rod
x_L             = x_0 + L                         #Terminal point of the rod
t_0             = 0                               #Initial condition on time
h               = 4                               #Vertical "thickness" of rod
t_F             = 1                               #Ending time
pointsPerLength = 50                              #"Resolution" of the plot
n               = 100                             #Number of terms to be used in approximation for sum
framesPerSecond = 20                              #Delay between frame updates in milliseconds
totalFrames     = int((1000*(t_F-t_0))/framesPerSecond)  #Total frames to be displayed
speed           = 0.5                             #Speed that plot updates at

def u(x, y, t):
    global kappa, L, n

    result = 0
    
    #Approximate the sum
    for i in range(1, n + 1):
        if i % 2 != 0:
            result += (400 / (i * np.pi)) * np.exp( (i ** 2) * (np.pi ** 2) * kappa * -t / L ** 2) * np.sin(i * np.pi * x / L)

    return result



#Points along the rod, at initial time
x_values = np.linspace(x_0, x_L, L * pointsPerLength)
y_values = np.linspace( -(h/2), (h/2), h*pointsPerLength)

X, Y = np.meshgrid(x_values, y_values)

t_init = np.full(len(x_values), t_0)  #Initial condition

U = u(X, Y, t_init)                      #Initial heat distribution

fig, ax = plt.subplots()
pcm = ax.pcolormesh(X, Y, U, cmap='seismic')
plt.colorbar(pcm, ax=ax, label='Magnitude')
ax.set_title('Temperature over rod')
ax.set_xlabel("x: Length")


def update(frame):
    # Update temperatures for the next time step
    newTemps = u(X, Y, frame*speed)
    pcm.set_array(newTemps.ravel())
    return pcm

# Run animation
ani = FuncAnimation(fig, update, frames=range(totalFrames), interval=framesPerSecond)
plt.show()

