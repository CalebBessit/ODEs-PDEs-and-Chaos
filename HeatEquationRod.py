#Visualization of Heat equation
#Caleb Bessit
#29 July 2023

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Constants
kappa           = 100          #Diffusivity constant for the material
L               = 20         #Length of the rod
x_0             = 0          #Initial point of the rod
x_L             = x_0 + L    #Terminal point of the rod
t_0             = 0          #Initial condition on time
t_F             = 10         #Ending time
pointsPerLength = 50         #"Resolution" of the plot
n               = 100         #Number of terms to be used in approximation for sum

#Evaluate the equation at this point in space and time
def u(x, t):
    global kappa, L, n

    result = 0
    
    #Approximate the sum
    for i in range(1, n + 1):
        if i % 2 != 0:
            result += (400 / (i * np.pi)) * np.exp(-1 * (i ** 2) * (np.pi ** 2) * kappa * t / L ** 2) * np.sin(i * np.pi * x / L)

    return result

def main():
    global x_0, x_L, t_0, t_F, pointsPerLength

    # Define region of solution
    x_values = np.linspace(x_0, x_L, L * pointsPerLength)
    t_values = np.linspace(t_0, t_F, (t_F - t_0)*pointsPerLength)
    x, t = np.meshgrid(x_values, t_values)


    U = u(x, t)

    #Plot the temperature values over the region(extent) chosen, using the "seismic" color map
    plt.imshow(U, extent=[x_0, x_L, t_0, t_F], aspect='auto', cmap='seismic')

    plt.colorbar(label="Temperatures")
    plt.xlabel('x')
    plt.ylabel('t')
    plt.title('Temperature distribution over time for a rod, with kappa= {}'.format(kappa))
    plt.show()

if __name__ == "__main__":
    main()
