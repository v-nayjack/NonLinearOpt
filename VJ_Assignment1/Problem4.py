# Created by Vinay Jakkali on 11/25/2019

"""
--------------------------------------------------------------------------------------
Problem 4. function takes the following inputs

INPUT:
    X0 - It takes a float value, which acts as an initial guess to Newton-Raphson Method
    (by default x0 = 0.1)

    m - It takes a float value and it represents the slope of the input line
    (by default m = 0.5)

    n - It is the no. of points that are being mapped. It takes an integer value >0
    (by default n = 1000)

    d_range - It is the range defined for the graph
    (by default d_range = (0, 5))

    b - is the y-intercept and takes a float values
    (by default b = 0.0)

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
from NewtonRaphson import newton_raphson as nr
from NewtonRaphson import newtonraphson_plot as nr_plot



def total_least_squares(x0=0.1, m=0.5, n=1000, d_range=(0, 5), b=0.0, eps=1e-2):

    # ri represents Ri from equation y = mx+b+e(Ri-1)
    ri = random.random()

    X = np.linspace(d_range[0], d_range[1], n)
    X = np.array(X)

    y = lambda x: x * m + b + eps * (2 * ri - 1)
    Y = np.array(y(X))

    z = lambda a: (X + a * Y) / (a ** 2 + 1)

    F_a = lambda a: sum((X - z(a)) ** 2 + (Y - a * z(a)) ** 2)

    Minimum, iter_nr = nr(F_a, x0)

    return round(Minimum, 4), X, Y, F_a

""" Function 'prob4_plot' plots the 'actual data' along with the 'best fit line' """

def prob4_plot(rnge, Minimum, X, Y):

    plt.figure()
    plt.scatter(X, Y, color='green', marker='o')
    plt.plot(X, Minimum*X, color='red', Linewidth=2)
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
    X0 = 0.3
    slope = 0.5
    N = 1000
    D_range = (0, 5)
    y_intercept = 0.0
    noise = 1e-3

    # Returned Values
    A, XX, YY, Func_a = total_least_squares(X0, slope, N, D_range, y_intercept, noise)

    # Objective Function Plot
    nr_plot(A, Func_a)

    # Data Minimization Plot
    prob4_plot(D_range, A, XX, YY)

    # Results output printed to the console
    print(" The optimized value of 'a' is = ", A)
    print(" The minimized value of objective function F(a) = ", round(Func_a(A), 4))


