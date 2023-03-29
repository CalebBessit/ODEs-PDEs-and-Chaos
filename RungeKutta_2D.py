#Attempt at implementing Runge-Kutta on a 2d linear system
#Caleb Bessit
#29 March 2023

import numpy as np
import matplotlib.pyplot as plt
from vpython import *

A = np.array([[1,2],[-2,1]])
X = np.array([[1],[1]])
dt = 0.01
t  = 0
T  = 400


def F(X):
    global A
    return np.dot(A,X)


def main():
    global t
    global dt
    global X    
    #Define some stuff
    
    figure     = graph(title="Solution curve", xlabel="x", ylabel="y")
    trajectory = gcurve(color=color.green, graph = figure)
    
    while t<T:
        
        t += dt
        
        E1 = dt*F(X)
        E2 = dt*F(X + 0.5*E1)
        E3 = dt*F(X + 0.5*E2)
        E4 = dt*F(X + E3)
        
        X  = X + (dt/6) *(E1 + 2*E2 + 2*E3 + E4)
        trajectory.plot(X[0][0],X[1][0])
        
main()
        
        
    