# Created by Vinay Jakkali on 12/9/2019

"""
--------------------------------------------------------------------------------------
Problem 5. function takes the following inputs

INPUT:
    X0 - It takes an array, which acts as an initial guess to Powell Method

    m - It takes a float value and it represents the slope of the input line
    (by default m = 0.5)

    n - It is the no. of points that are being mapped. It takes an integer value >0
    (by default n = 100)

    d_range - It is the range defined for the graph
    (by default d_range = (0, 5))

    eps - represents the magnitude of the noise in the input data
    (by default eps = 1e-2)

OUTPUT:
    1. Returns the values of minimum 'xn' and total number of iterations 'k'

    2. A new window with the plot showing objective function with the minimum point

    3. Print the values of total number of iterations 'k', minimum 'x', minimum 'F(x)' to the console

--------------------------------------------------------------------------------------
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from Quasi_Newton import quasi_newton
from PowellMethod import powell_method



def total_least_squares(x0, m=0.5, n=100, d_range=(0, 5), eps=1e-2):

    # ri represents Ri from equation y = mx+b+e(Ri-1)
    ri = random.random()

    # Creating a vector of size 'n'
    X = np.linspace(d_range[0], d_range[1], n)
    X = np.array(X)

    # Defining the straight line equation given in the assignment using anonymous function
    y = lambda x: x * m + x0[1] + eps * (2 * ri - 1)

    # Creating a vector containing the y values corresponding to x
    Y = np.array(y(X))

    # Defining the given 'zi' equation
    z = lambda a: (X + a[0] * Y - a[0] * a[1]) / (a[0] ** 2 + 1)

    # Defining the given F(a) equation
    F_a = lambda a: sum((X - z(a)) ** 2 + (Y - (a[0] * z(a) + a[1])) ** 2)

    # Minimizing the function F(a1, a2) using Powell Method
    L = np.array([0.0, 0.0])
    U = np.array([10.0, 10.0])
    Minimum, iter_nr = powell_method(F_a, x0, L, U)

    return Minimum, X, Y, F_a

""" Function 'prob5_plot' plots the 'actual data' along with the 'best fit line' """

def prob5_plot(rnge, Minimum, X, Y):


    v = (Minimum[0] * X) + Minimum[1]

    plt.figure()
    plt.scatter(X, Y, color='green', marker='*')
    plt.plot(X, v, color='red', Linewidth=2)
    plt.title("Least Squares Method", fontsize=20)
    plt.xlabel("x axis", fontsize=16)
    plt.ylabel("y axis", fontsize=16)
    plt.legend(("Best Fit Line", "Actual Data"), fontsize=14)
    plt.xlim(rnge[0], rnge[1])
    plt.ylim(rnge[0], rnge[1])
    plt.grid()
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')

    return plt.show()


if __name__ == "__main__":

    # Input Values for the 'total_least_squares' function
    X0 = np.array([1.0, 1.0])

    slope = 0.5

    N = 100

    D_range = (0, 5)

    noise = 1e-1

    # Returned Values
    A, XX, YY, Func_a = total_least_squares(X0, slope, N, D_range, noise)

    # Objective Function Plot
#    nr_plot(A, Func_a)

    # Data Minimization Plot
    prob5_plot(D_range, A, XX, YY)

    # Results output printed to the console
    print(" The optimized value of 'a' is = ", A)
    print(" The minimized value of objective function F(a) = ", round(Func_a(A), 4))


