# Created by Vinay Jakkali on 11/25/2019

"""
--------------------------------------------------------------------------------------
The bisection function defined here takes following parameters as input

INPUT:
    f : It is defined as an anonymous function

    a : Lower bracketed interval point

    b : Upper bracketed interval point.
    (Values of 'a' and 'b' can be obtained from univariatescan function)

    tol : This is the tolerance accepted for the minimized objective function
    (by default tol = 1e-8)

    maxiter : Maximum iterations to stop the optimization
    (by default maxiter = 1e3)

OUTPUT:
    1. Returns values of minimum 'c' and total number of iterations 'k'

    2. A new window with the plot showing objective function with the minimum point

    3. Print the values of total number of iterations 'k', minimum 'c', minimum 'F(x)' to the console
--------------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, tol=1e-8, maxiter=1e3):

    # initializing 'k' & 'c'

    k = 0
    c = 0.0

    while (np.abs(a - b) >= tol) and k < maxiter:
        # Calculating the mid point 'c' with the given 'a' & 'b'
        c = (a + b) / 2.0
        # Calculating the new value left of point 'c'
        left = (a + c) / 2.0
        # Calculating the new value right of point 'c'
        right = (c + b) / 2.0

        fl = f(left)
        fr = f(right)

        # Determining the direction of search

        if fr > fl:
            b = right

        elif fl > fr:
            a = left

        else:
            a = left
            b = right

        k += 1

    return round(c, 4), k

""" Function 'bisection_plot' plots the objective function along with the minimum """

def bisection_plot(c, f):

    """ Creating points for plotting the objective function """

    m = np.linspace(-10, 10, 1000)
    fv = []

    for i in range(len(m)):
        fv.append(f(m[i]))

    plt.figure()
    plt.plot(m, fv, color="red", linewidth=2)
    plt.scatter(c, f(c), color="b", marker='o')
    plt.title("F(x) minimization using Bisection Method", fontsize=20)
    plt.legend(("F(x)", "Minimum"), fontsize=14)
    plt.xlabel("x", fontsize=16)
    plt.ylabel("F(x)", fontsize=16)
    plt.xlim(-10, 10)
    plt.grid()
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')

    return plt.show()


if __name__ == "__main__":

    # Input Values for the 'bisection' function
    Func = lambda x: x**3 - 3*x**2
    A = 1.23
    B = 2.19
    tolerance = 1e-6
    maxiteration = 1e3

    # Returned Values
    C, K = bisection(Func, A, B, tolerance, maxiteration)

    # Objective Function Plot
    bisection_plot(C, Func)

    # Results output printed to the console
    print(" Total no. of iterations to find the minimum of the Obj func = ", K)
    print(" The minimum point is = ", C)
    print(" The minimum F(x) = ", round(Func(C), 2))
