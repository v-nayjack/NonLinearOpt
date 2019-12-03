# Created by Vinay Jakkali on 11/25/2019

"""
--------------------------------------------------------------------------------------
The univariatescan function defined here takes following parameters as input

INPUT:
    f : It is defined as an anonymous function

    x0 : It is initial guess required for Univariate Scan method
    (by default x0 = 0.0)

    tol : This is the tolerance accepted for the minimized objective function
    (by default tol = 1e-8)

    alp : This is the step size
    (by default alp = 1e-2)

    maxiter : Maximum iterations to stop the optimization
    (by default maxiter = 1e3)

OUTPUT:
    1. Returns values of lower bracketed point 'a', upper bracketed point 'b' and total number of iterations 'k'

    2. A new window with the plot showing objective function with the bracketed interval

    3. Print the values of total number of iterations 'k', 'a' and 'b' to the console
--------------------------------------------------------------------------------------
"""

import matplotlib.pyplot as plt
import numpy as np


def univariatescan(F, x0=0.0, tol=1e-8, alp=1e-2, maxiter=1e3):

    fp = (F(x0 + tol) - F(x0)) / tol
    fpp = (F(x0 + tol) - 2 * F(x0) + F(x0 - tol)) / (tol ** 2)

    """ The following code block is used to check if the initial guess is a maxima or a point of inflection.
    If the given point is a maxima or a point of inflection, the function takes small steps left and right
    of the given point to decide appropriate stepping direction to evaluate the bracketed interval """

    if abs(fpp) <= tol:

        print(" Initial guess is a maxima or a point of inflection ")

        xr = x0 + 1.0
        xl = x0 - 1.0

        fpp_xr = (F(xr + tol) - 2 * F(xr) + F(xr - tol)) / (tol ** 2)
        fpp_xl = (F(xl + tol) - 2 * F(xl) + F(xl - tol)) / (tol ** 2)

        if fpp_xr > fpp_xl:
            x0 = xr

        else:
            x0 = xl

    """ Checking to see if the user guessed the minima """

    if fp == 0 and fpp > 0:

        print(" The initial guess is the minima ")

        a = x0 + 2
        b = x0 - 2
        k = 0

        return [a, b, k]

    """ Actual calculation to find the bracketed values begins here.
     Determining the sign of the delta based on the first derivative of the objective function """

    if fp > 0:
        delta = -alp

    else:
        delta = alp

    xk = x0
    xk_f = xk + delta

    f_xk_f = round(F(xk_f), 4)
    f_xk = round(F(xk), 4)

    k = 0
    a = min(xk, xk_f)
    b = max(xk, xk_f)

    """ After calculating initial values, the function iterates to update the values of Xn and Xn_1.
    The stopping criteria used --> Checking conditions {F(Xn_1) > F(Xn)} and maximum iterations {k < maxiter} """

    while (f_xk > f_xk_f) and k < maxiter:

        delta = 2 * delta

        xk_b = xk
        xk = xk_f
        xk_f = xk + delta

        f_xk_f = F(xk_f)
        f_xk = F(xk)

        a = min(xk_b, xk_f)
        b = max(xk_b, xk_f)

        """ The following conditions check whether 'a' & 'b' have negative values, 
        if yes, it kicks them back to +ve side """

        if a < 0 and b < 0:
            xk = 10 * x0

        elif a < 0:
            xk = 10 * x0

            delta = -1 * delta

            f_xk = F(b)
            f_xk_f = F(a)

        k += 1

    return [round(a, 4), round(b, 4), k]


""" Function 'univariate_plot' plots the objective function along with the bracketed values """

def univariate_plot(a, b, f):

    """ Creating points for plotting the objective function """

    m = np.linspace(-10, 10, 1000)
    fv = []

    for i in range(len(m)):
        fv.append(f(m[i]))

    plt.figure()
    plt.plot(m, fv, color="red", linewidth=2)
    plt.plot([a, b], [f(a), f(b)], color="blue", linestyle='--')
    plt.scatter(a, f(a), color="green", marker='*')
    plt.scatter(b, f(b), color="green", marker='*')
    plt.legend(("F(x)", "Bracketed Interval"), fontsize=14)
    plt.title("Bracketed Interval", fontsize=20)
    plt.xlabel("x", fontsize=16)
    plt.ylabel("F(x)", fontsize=16)
    plt.grid()
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')

    return plt.show()


if __name__ == "__main__":

    # Input Values for the 'univariatescan' function
    Func = lambda x: x**3 - 3*x**2
    X0 = 2.5

    # Returned Values
    A, B, K = univariatescan(Func, X0)

    # Objective Function Plot
    univariate_plot(A, B, Func)

    # Results output printed to the console
    print(" The total number of iterations to find the bracket = ", K)
    print(" The Bracket values: a =", A, "b = ", B)
