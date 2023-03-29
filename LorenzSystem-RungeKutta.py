#Attempt at implementing Runge-Kutta to plot a solution curve of the Lorenz system
#Caleb Bessit
#29 March 2023

import numpy as np
import matplotlib.pyplot as plt
from vpython import *

#Elements of system

X = np.array([[4],[1],[3]]) #Initial position
dt = 0.01                   #Time step
t  = 0                      #Running time
T  = 300                   #Final time

#Function which evaluates the derivatives in the Lorenz system at a particular point
def F(X):
    #System parameters
    sigma = 10
    rho   = 28
    beta  = 8/3
    
    #A is the coeffiecient matrix corresponding to the parameters in the Lorenz system
    A = np.array([[-1*sigma, sigma, 0],[rho, -1, -1*X[0][0]],[0,X[0][0],-1*beta]])
    return np.dot(A,X)


def main():
    global t
    global dt
    global X    
    
    #Figures which will display information about solution curve
    
    figure_x  = graph(title="Trajectory for x", xtitle="t", ytitle="x(t)")
    figure_y  = graph(title="Trajectory for y", xtitle="t", ytitle="y(t)")
    figure_z  = graph(title="Trajectory for z", xtitle="t", ytitle="z(t)")

    #Defining trajectory curves
    trajectory_x = gcurve(graph=figure_x, color= color.green)
    trajectory_y = gcurve(graph=figure_y, color= color.blue)
    trajectory_z = gcurve(graph=figure_z, color= color.red)

    #Plotting initial point
    trajectory_x.plot(t,X[0][0])
    trajectory_y.plot(t,X[1][0])
    trajectory_z.plot(t,X[2][0])
 
    #Modelling a "particle" in the region of the attractor
    trail = curve(color=color.green, radius=0.5)
    
    #Implementation of Runge-Kutta method to solve system numerically
    while t<T:
        
        t += dt
        
        #Runge-Kutta terms
        E1 = dt*F(X)
        E2 = dt*F(X + 0.5*E1)
        E3 = dt*F(X + 0.5*E2)
        E4 = dt*F(X + E3)
        
        X  = X + (dt/6) *(E1 + 2*E2 + 2*E3 + E4)
        
        #Plotting points
        trajectory_x.plot(t,X[0][0])
        trajectory_y.plot(t,X[1][0])
        trajectory_z.plot(t,X[2][0])  
        
        trail.append(vector(X[0][0],X[1][0],X[2][0]))
        
        
main()
        
        
