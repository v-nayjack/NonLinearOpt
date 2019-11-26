# Created by Vinay Jakkali on 11/25/2019

"""
--------------------------------------------------------------------------------------
The bisection function defined here takes following parameters as input

INPUT:
f : it is defined as an anonymous function

a : lower bracketed interval point

b : upper bracketed interval point.
(Values of 'a' and 'b' can be obtained from univariatescan function)

tol : This is the tolerance accepted for the minimized objective function
(by default tol = 1e-8)

maxiter : Maximum iterations to stop the optimization
(by default maxiter = 1e3)

OUTPUT:
1. Returns values of minimum 'c' and total number of iterations 'k'

2. A new window with the plot showing objective function with the minimum point

3. Print the values of total number of iterations 'k', minimum 'x', minimum 'F(x)' to the console
--------------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, tol=1e-8, maxiter=1e3):

    k = 0
    c = 0.0

    while (np.abs(a - b) >= tol) and k < maxiter:
        c = (a + b) / 2.0
        left = (a + c) / 2.0
        right = (c + b) / 2.0

        fl = f(left)
        fr = f(right)

        if fr > fl:
            b = right

        elif fl > fr:
            a = left

        else:
            a = left
            b = right

        k += 1

    return round(c, 4), k

'''Function 'myplot' plots the objective function along with the minimum'''
def myplot(c, f):
    """Creating points for plotting the objective function"""

    m = np.linspace(-10, 10, 1000)
    fv = []

    for i in range(len(m)):
        fv.append(f(m[i]))

    plt.figure()
    plt.plot(m, fv, color="red", linewidth=2)
    plt.scatter(c, f(c), color="b", marker='o')
    plt.title("F(x) minimization using bisection method", fontsize=24)
    plt.legend(("F(x)", "Minimum"), fontsize=14)
    plt.xlabel("x", fontsize=24)
    plt.ylabel("F(x)", fontsize=24)
    plt.xlim(-10, 10)
    plt.grid()
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')

    return plt.show()


if __name__ == "__main__":

    Func = lambda x: x**3 - 3*x**2
    A = 0.9
    B = 3.0
    tolerance = 1e-6
    maxiteration = 1e3
    C, K = bisection(Func, A, B, tolerance, maxiteration)
    myplot(C, Func)

    print("Total no. of iterations to find the minimum of the Obj func = ", K)
    print("The minimum point is = ", round(C, 4))
    print("The minimum F(x) = ", round(Func(C), 4))
