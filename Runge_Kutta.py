#Implementation of Runge-Kutta method
#Caleb Bessit
#25 March 2023

from vpython import *
from math import *

#Declare globals
calc_equation = ""
dt            = 0

#Function evaluation
def f(t,x):
    global calc_equation
    return eval(calc_equation) #Generally unsafe, but useful for our purposes

#3 methods below are the terms in the update formula for the Runge-Kutta method
def k2(t,x,k1):
    global dt
    t +=dt/2
    x += k1/2
    return dt*f(t,x)

def k3(t,x,k_2):
    global dt
    t += dt/2
    x += k_2/2
    return dt*f(t,x)

def k4(t,x,k_3):
    global dt
    t += dt
    x += k_3
    return dt*f(t,x)


def main():
    #Obtain data
    global dt
    global calc_equation
    dt  = float(input("Enter time step (dt): "))
    t   = 0
    T   = float(input("Enter maximum time: "))
    x   = float(input("Enter initial condition, x_0(t_0): "))
    n   = 0
    calc_equation = input("Enter function, f(t,x): ")
    
    #VPython graph which plots numerical solution curve
    figure = graph(color=color.red, title="Trajectory for "+calc_equation, xtitle="t", ytitle="x(t)")
    figure2 = graph(title="Exact solution", xtitle="t", ytitle="x(t)")
    trajectory = gcurve(graph = figure, color=color.green)
    trajectory.plot(t,x)
    
    ##Some additional code to compare a numerical solution to an exact solution, if one is known
    #exact_soln = gcurve(graph=figure, color=color.blue)
    #exact_soln.plot(t, t**2+2*t+1-( (0.5)*exp(t) ) )    
    
    #Iteratively display solution
    while t<T:
        rate(10)  #Animate as points are added to curve
        t += dt
        
        #Evaluate terms at this step, update x
        k1 = dt*f(t,x)
        k_2 = k2(t, x, k1)
        k_3 = k3(t, x, k_2)
        k_4 = k4(t, x, k_3)
        
        x = x + (1/6)*(k1+2*k_2+2*k_3+k_4)
        
        trajectory.plot(t,x)
        
        #exact_soln.plot(t, t**2+2*t+1-( (0.5)*exp(t) ) )        
        
main()