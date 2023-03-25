#Implementation of Euler's method
#Caleb Bessit
#October 2022
from math import *
from vpython import *

def main():
    #Obtain initial data
    dt  = float(input("Enter time step (dt): "))
    t   = 0
    T   = float(input("Enter maximum time: "))
    x   = float(input("Enter starting x, x_0: "))
    n   = 0
    calc_equation = input("Enter equation, x_dot: ")
    
    x_dot = eval(calc_equation)
    print("Step: " + str(n) + ", x" + str(n) + ": "+ str(round(x,4)) + ", x_dot: "+ str(round(x_dot,4)) + ", t= " + str(t))
    
    gd = graph(color=color.red, title="Trajectory for "+calc_equation, xtitle="Time (s)", ytitle="x(t)")
    trajectory = gcurve(graph=gd, color=color.red)
    trajectory.plot(t,x)
    
    while t<T:
        rate(5)
        n+=1
        t += dt
        #Calculation
        
        
        x = x + dt*x_dot;
        x_dot = eval(calc_equation)
        print("Step: " + str(n) + ", x" + str(n) + ": "+ str(round(x,4)) + ", x_dot: "+ str(round(x_dot,4)) +", t= " + str(t))
        trajectory.plot(t,x)
        
        
        
        
main()
