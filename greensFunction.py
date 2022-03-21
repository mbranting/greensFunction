"""
McKenna Branting
CST-305
Green's Function and ODE with IVP

------------------------------------------------------------------------------------------------------------------------
Functions to Solve using ODE and Green's Function
        1. y"+2y'+2 = 2x; t>=0; y(0)=y'(0)=0
        2. y"+y=4; t>=0; y(0)=y'(0)=0
------------------------------------------------------------------------------------------------------------------------

Approach for implementation:
1. First, the Green's function was solved by hand to determine approach for implementation.
2. The functions found in the Green's function obtained by hand were utilized in the code
3. The dU_dx functions were determined based off the equations in the assignment using ODEINT
4. These functions were modified to find the Green's function solution
5. An array for data (x,y) was created
6. Graphs were developed to model the data obtained
"""
import time  # import time to use for performance analysis
import numpy as np  # import numpy for array space
import matplotlib.pyplot as plt  # import matplotlib for graphing functions
from scipy.integrate import odeint  # import scipy to use the ordinary differential equation integral function
import math

# Start the timer to record computational time
start = time.time()


# ODEs where U is a vector (U[0] = y and U[1] = y')
def dy1_dx(Y, x):  # takes inputs U and x
    return [Y[1], -2 * Y[1] + 2 * x - 2]  # returns the array of y' and -2y' + 2x -2


def dy2_dx(Y, x):  # takes inputs U and x
    return [Y[1], 4 - Y[0]]  # returns the array of y' and 4 - y


# lists to hold data for greens function
greenX1 = []
greenX2 = []
greenY1 = []
greenY2 = []

# Equation 1 using Green's Function
print("Equation 1: y'' + 2y' + 2 = 2x; t>=0; y(0) = y'(0) = 0")
"""
------------------------- The function of y(x)=-(((3 * math.expm1(-2 * x)) + (2 * (x ^ 2)) - (6 * x) + 3) / 4)--------
"""

# Equation 2 using Green's Function
print("Equation 2: y'' + y = 4; t>=0; y(0) = y'(0) = 0")
"""
-------------------------- The function of y(x)=-4(np.cos(x)-1)---------------------------------------------------------
"""
# calculates data values for greens function of equations 1 and two from the x values 0 to 50
for x in range(1, 50):
    for y in range(1, 1000):
        equationOne = (((-3 * math.expm1(-2 * x)) + (2 * (x ** 2)) - (6 * x) + 3) / 4)
        equationTwo = 4 - (4 * math.cos(x))
        # adds data values to lists for equation one
        greenX1.append(x)
        greenY1.append(equationOne)
        # adds data values to lists for equation two
        greenX2.append(x)
        greenY2.append(equationTwo)

# vector containing the values of y and y'
U0 = [0, 0]
# x space from 0-10 with 200 steps
xs0 = np.linspace(0, 50, 1000)
# y space using odeint function to solve the formula
ys0 = odeint(dy1_dx, U0, xs0)
ys0 = ys0[:, 0]

# vector containing the values of y and y'
U1 = [0, 0]
# x space from 0-10 with 200 steps
xs1 = np.linspace(0, 50, 1000)

# y space using odeint function to solve the formula
ys1 = odeint(dy2_dx, U1, xs1)
ys1 = ys1[:, 0]

# initialise the subplot with number of rows and columns
figure, axis = plt.subplots(2, 2)

# For ODE of function equation 1
axis[0, 0].plot(xs0, ys0)
axis[0, 0].set_title("ODE Function for Equation 1")

# For ODE of function equation 2
axis[0, 1].plot(xs1, ys1)
axis[0, 1].set_title("ODE Function for Equation 2")

# For Green's function of equation 1
axis[1, 0].plot(greenX1, greenY1)
axis[1, 0].set_title("Green's Function for Equation 1")

# For Green's function of equation 2
axis[1, 1].plot(greenX2, greenY2)
axis[1, 1].set_title("Green's Function for Equation 2")
# shows plots

# Computes the amount of time the program took to execute
end = time.time()
print("Computing Time: ")
print(end - start)

# shows first graph
plt.show()

# shows Greens function and ODEINT graph together for function 1
figure2, axis2 = plt.subplots(1, 2)
# For ODE of function equation 1
axis2[0].plot(xs0, ys0)
# For Green's function of equation 1
axis2[0].plot(greenX1, greenY1)
axis2[0].set_title("ODE Function and Greens Function Equation 1")

# shows Greens function and ODEINT graph together for function 2
# For ODE of function equation 1
axis2[1].plot(xs1, ys1)
# For Green's function of equation 1
axis2[1].plot(greenX2, greenY2)
axis2[1].set_title("ODE Function and Greens Function Equation 1")

# shows second graph
plt.show()

